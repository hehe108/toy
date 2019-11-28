#!/usr/bin/env node
'use strict';

Object.defineProperty(exports, '__esModule', {
  value: true
});
exports.makeAnswer = makeAnswer;
exports.makeQuestion = makeQuestion;

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var _nativeDns = require('native-dns');

var _nativeDns2 = _interopRequireDefault(_nativeDns);

// Simple DNS RR type to string conversion to use with native-dns.
// Look here for a comprehensive list of RR types: http://www.zytrax.com/books/dns/ch8/
// copy from https://github.com/OmniscientJV/dns-proxy-for-google-dns-over-https-api/blob/master/app.js
function dnsRRTypeToString(type) {
  // Default value.
  var t = 'A';
  switch (type) {
    case 1:
      t = 'A';
      break;
    case 28:
      t = 'AAAA';
      break;
    case 5:
      t = 'CNAME';
      break;
    case 15:
      t = 'MX';
      break;
    case 6:
      t = 'SOA';
      break;
  }

  return t;
}

function makeAnswer(record) {
  return _nativeDns2['default'][dnsRRTypeToString(record.type)](record);
}

function makeQuestion(question) {
  return new _nativeDns2['default'].Question({
    name: question.name,
    type: dnsRRTypeToString(question.type)
  });
}