#!/usr/bin/env node
'use strict';

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var _commandLineArgs = require('command-line-args');

var _commandLineArgs2 = _interopRequireDefault(_commandLineArgs);

var _nativeDns = require('native-dns');

var _nativeDns2 = _interopRequireDefault(_nativeDns);

var _socks5HttpsClientLibAgent = require('socks5-https-client/lib/Agent');

var _socks5HttpsClientLibAgent2 = _interopRequireDefault(_socks5HttpsClientLibAgent);

var _request = require('request');

var _request2 = _interopRequireDefault(_request);

var _memoryCache = require('memory-cache');

var _memoryCache2 = _interopRequireDefault(_memoryCache);

var _isRoot = require('is-root');

var _isRoot2 = _interopRequireDefault(_isRoot);

var _fs = require('fs');

var _fs2 = _interopRequireDefault(_fs);

var _micromatch = require('micromatch');

var _micromatch2 = _interopRequireDefault(_micromatch);

var _process = require('process');

var _process2 = _interopRequireDefault(_process);

var _winston = require('winston');

var _winston2 = _interopRequireDefault(_winston);

var _utils = require('./utils');

var GOOGLE_DNS = 'dns.google.com';

var cli = (0, _commandLineArgs2['default'])([{ name: 'socks_host', alias: 's', type: String,
  description: 'Host of socks proxy(optional)', defaultValue: null }, { name: 'socks_port', alias: 'p', type: Number,
  description: 'Port of socks proxy(default 1080)', defaultValue: 1080 }, { name: 'fallback', alias: 'f', type: String,
  description: 'DNS to resolve Google DNS address once and whitelist(Default 8.8.8.8)', defaultValue: '8.8.8.8' }, { name: 'cache_time', alias: 't', type: Number,
  description: 'Cache time(ms, Default 300000)', defaultValue: 300000 }, { name: 'whitelist_file', alias: 'w', type: String,
  description: 'Whitelist file contains domains to resolve by fallback directly', defaultValue: null }]);

var app = {
  title: 'dns-proxy-https',
  description: 'DNS proxy server over Google HTTPS DNS Service with socks supported',
  synopsis: ['$ sudo dns-proxy-https -s 127.0.0.1 -p 1081', '$ sudo dns-proxy-https -s 127.0.0.1 -p 1081 -f 114.114.114.114 -t 500000', '$ sudo dns-proxy-https -s 127.0.0.1 -p 1081 -w whitelist.txt'],
  footer: 'Project home: [dns-proxy-https]{https://github.com/CodeFalling/dns-proxy-https}'
};

var option = cli.parse();

console.log(cli.getUsage(app));

// help end

// check sudo
if (!(0, _isRoot2['default'])()) {
  throw new Error('Please run dns-proxy-https with sudo!');
}

// read whitelist if existed
var whitelist = [];
if (option.whitelist_file) {
  _fs2['default'].readFile(option.whitelist_file, 'utf8', function (err, data) {
    if (err) {
      _winston2['default'].info(err);
      return;
    }
    whitelist = data.split('\n').filter(function (line) {
      return line[0] !== '#'; // ignore comment
    });
  });
}

function requestOverHTTPS(name) {
  return new Promise(function (resolve, reject) {
    (0, _request2['default'])({
      url: 'https://1.1.1.1/dns-query?ct=application/dns-json&name=' + name + '&type=A',
      agentClass: option.socks_host ? _socks5HttpsClientLibAgent2['default'] : null,
      agentOptions: {
        socksHost: option.socks_host,
        socksPort: option.socks_port
      }
    }, function (err, res) {
      if (err) {
        reject(err);
      } else {
        resolve(res);
      }
    });
  });
}

function handleRequest(req, response) {
  _winston2['default'].info('Request ' + req.question[0].name + '       ' + Date().toString());
  var question = req.question[0];

  // cache check
  var cacheValue = _memoryCache2['default'].get(question.name);
  if (cacheValue) {
    _winston2['default'].info(question.name + ' hit cache');
    response.answer.push(cacheValue);
    response.send();
    return;
  }

  // whitelist check
  if (_micromatch2['default'].any(question.name, whitelist)) {
    // query on fallback DNS
    _winston2['default'].info(req.question[0].name + ' hit whitelist');
    var dnsReq = new _nativeDns2['default'].Request({
      question: (0, _utils.makeQuestion)(question),
      server: option.fallback,
      timeout: 6000
    });

    dnsReq.on('message', function (err, answer) {
      if (!err) {
        response.answer.push((0, _utils.makeAnswer)(answer.answer[0]));
      } else {
        _winston2['default'].info(err);
      }
      response.send();
    });

    dnsReq.send();
    return;
  }

  // query over https
  requestOverHTTPS(question.name, option).then(function (res) {
    if (res.statusCode === 200) {
      var json = JSON.parse(res.body);
      var a = json.Answer[0];
      var record = {
        name: a.name,
        type: a.type,
        ttl: a.TTL
      };
      switch (a.type) {
        case 1:case 28:
          // A & AAAA
          record.address = a.data;
          break;
        case 5:
          // CNAME
          record.data = a.data;
          break;
        case 15:
          // MX
          // For example "5 hotmail.com" is a response by the API in case of an MX type.
          record.priority = a.data.charAt(0);
          record.exchange = a.data.substring(2);
          break;
      }
      var answer = (0, _utils.makeAnswer)(record);
      response.answer.push(answer);
      _memoryCache2['default'].put(question.name, answer, option.cache_time);
    }
    response.send();
  })['catch'](function (err) {
    _winston2['default'].info(err);
    response.send();
  });
}

var server = _nativeDns2['default'].createServer();
server.on('listening', function () {
  return _winston2['default'].info('server listening', server.address());
});
server.on('close', function () {
  return _winston2['default'].info('server closed', server.address());
});
server.on('error', function (err) {
  return console.error(err.stack);
});
server.on('socketError', function (err) {
  return console.error(err);
});

// init
// Resolve GOOGLE_DNS then Start
_winston2['default'].info('Resolving Google DNS Service using ' + option.fallback + '...');

_nativeDns2['default'].resolve(GOOGLE_DNS, 'A', option.fallback, function (err) {
  if (err) {
    _winston2['default'].info(err);
  } else {
    _winston2['default'].info('Now start server');
    server.on('request', handleRequest);
    server.serve(8888);
  }
});

// catch all exception
_process2['default'].on('uncaughtException', function (err) {
  _winston2['default'].info('Caught exception: ' + err);
});