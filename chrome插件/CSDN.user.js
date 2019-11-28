// ==UserScript==
// @name       CSDN自动展开阅读更多及界面简化
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description		如果有阅读更多按钮，将自动点击，去除一些无用元素
// @author       You
// @iconURL			https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3856144780,3450407977&fm=58
// @match        https://*/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';




console.log("点开折叠");
fff();

setInterval(fff, 5000);




})();





function fff()
{
		var d = document;
		if(d.getElementById('btn-readmore')!=null)
		{
			d.getElementById('btn-readmore').click();								//auto click readmore button if exist
		}

		if(d.querySelector(".tbl-read-more-btn")!=null)
		{
			d.querySelector(".tbl-read-more-btn").click();
		}	
}