春节在家没事做？不如来打牌....

<img src="./img/1.jpg" alt="规则" style="zoom: 50%;" />

不能三带一，只能一张张出，在程序模拟100次的情况下可以得出下家赢的概率极大

上家a

下家b

牌面转化为数字，放入列表

选择下一个谁出，进入对应的function

首先判断对方手里只有一张牌的情况，且知道对方的牌

------

如轮到b出牌，

在对方只有1张牌的时候判断一下

​	a只有一张4，b有小王,J,9;   b从大往小出，b必赢

​	a只有一张Q，b有小王,K,J;   b从大往小出，b必赢

​	a只有一张Q，b有小王,J,9;   b从大往小出，a必赢

可得，判断标准为时候b里面比a小的牌是否大于1

再根据上一张牌面算出b手里可以出的牌

​		如果没有，直接b不能出

​		如果有，随机数种子决定要不要出

b随机出牌后，下一个跳到a出牌的function里面

b不出牌，则a在剩余的牌里面再随机出一张，下一次跳到b出牌的function里面

-----------------------------

轮到a出牌时同理

不要再问斗地主啦！技术有限，写不出三带一！╥﹏╥...

2020武汉加油！中国加油！💪

