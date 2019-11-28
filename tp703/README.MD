2019年1.7


2015-01-28 12:35:22  买tp  信号不好

2016-2017 玩传奇霸业 掉线 刷 openwrt 固件用的 (http://bbs.eeworld.com.cn/thread-457709-1-1.html)  还是掉线 


2018 op 不支持ipv6  刷   https://openwrt.org/zh/toh/tp-link/tl-wr703n  变砖 

电络铁 焊上ttl 串口线 救活  固件用的   http://bbs.eeworld.com.cn/thread-457709-1-1.html

步骤按照
https://blog.csdn.net/u011582412/article/details/19492983


setenv serverip 192.168.1.169

setenv ipaddr 192.168.1.1

 tftp 0x80000000 abcd.bin
 erase 0x9f020000 +0x3c0000
 cp.b 0x80000000 0x9f020000 0x3c0000

救活


救活后  固件版本
当前软件版本：	
3.14.4 Build 121204 Rel.41020n
当前硬件版本：	
WR703N v1 00000000


官方有   tplink  固件  是2017/7/3年的 
http://service.tp-link.com.cn/download/20177/TL-WR703N%20V1.0%E5%8D%87%E7%BA%A7%E8%BD%AF%E4%BB%B620140120.rar


问题1.tp 官方固件的 ttl 登录密码是多少
问题2   何谓不死 uboot?  https://www.v2ex.com/t/160078
问题3  ipv6 问题 

有机会试试  老毛子Padavan  DD


想想以前 openwrt 的玩法  1.旋转图片  （找找那家伙的csdn博客 ）

接入点模式 （Access Point） 中继模式 （Repeater） 桥接模式 （Bridge with AP） 客户端模式 （Cl
https://blog.csdn.net/bytxl/article/details/50418842


有空看看 路由器固件反编译  binwalk  有机会查查资料 。。

有空 去 cnbeta 查查 智能路由的玩法 


freebuf   cnblogs cnbeta  csdn  改天全查了吧 

https://www.cnblogs.com/beer/p/4938427.html   路由器抓包 

实在不行 动手自己写 。。操作系统



2019.1.8
login: root
password: 5up 

break cd continue eval exec exit export help login newgrp
        read readonly set shift times trap umask wait
		
		
		
		
703  tpl 命令  

hornet> help
?       - alias for 'help'
bootm   - boot application image from memory
cp      - memory copy
erase   - erase FLASH memory
help    - print online help
md      - memory display
mm      - memory modify (auto-incrementing)
mtest   - simple RAM test
mw      - memory write (fill)
nm      - memory modify (constant address)
printenv- print environment variables
progmac - Set ethernet MAC addresses
reset   - Perform RESET of the CPU
setenv  - set environment variables
tftpboot- boot image via network using TFTP protocol
version - print monitor version



2019.1.9
http://www.anywlan.com/  这论坛 路由 无线资料 貌似比较多 以后看看



2019.1.10
ESMT  貌似是 闪存  能吹下来  上编程器

ATHEROS  是处理器 mips 指令


2019.2.13

路由器  在设置向导里面修改   

ap 模式   改个ip 192.168.1.111  相当于交换机

repeater   模式    改个  ip  192.168.1.111      wifi连接管理器里面 同ssid 不同 mac

Bridge 这个是先接收信号 然后  发射   新固件 没成功  改天再试把 



1.所有路由器分布 
2.房间表   mac表   路由器表  ssid表  故障表    会议表   电脑配置表 （摄像头）



升级了  官方 固件后  	
3.17.1 Build 140120 Rel.56593n  登录密码 tplink
https://service.tp-link.com.cn/detail_article_1351.html


2.19
把 703  弄成 192.168.55.1 用手机 跟路由器 可以替代笔记本测网络
