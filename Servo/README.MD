，我们先给LPT端口发送0xff（1 1 1 1 1 1 1 1），然后1.5ms后发送0x00（0 0 0 0 0 0 0 0），如此往复。这样每个端口所连接的舵机就会接收到1.5ms的高电平信号，根据舵机角度与高电平时间的关系，所有连接的舵机都会指向90度的位置。


https://www.cnblogs.com/manors/archive/2011/03/27/LPT-Servo-Control-2.html

以前写过一个C#的 


25楼    盒子（洞）  细线   舵机  纸板  鸡蛋  木板  下落2次  精准下落？ 遥控鸡蛋 😀


https://baike.baidu.com/item/%E8%83%B6%E5%9B%8A%E5%86%85%E9%95%9C%E6%9C%BA%E5%99%A8%E4%BA%BA/15841693  磁铁 ？ 不知道旋转怎么控制？


有空查查这个资料 


https://blog.csdn.net/kucoffee12/article/details/78982958
