### DH-demo
基于 Diffie-Hellman 的三方密钥交换算法演示

#### 实验环境：
方法1：为了统一依赖，我们采用 Pyenv 来管理 Python 的版本，Pipenv 来管理依赖的版本。

+ [Windows 10 下安装 Pyenv](https://www.cnblogs.com/baowang/p/12499279.html)
+ [Pipenv 的安装](https://www.return520.com/posts/18616/)
+ [简明操作指南](https://blog.csdn.net/c13232906050/article/details/100039727)

方法2：实验环境为python3.7及django3.0.6，可以自行下载

#### 算法流程：
* 随机生成大素数p
* 生成大素数p的一个原根g
* Alice,Bob,Carol随机产生小于p的私钥
* 密钥的二轮分发及产生共享密钥。
	* Alice选取一个大的随机整数x,并且发送给Bob X=g^x mod n
      Bob选取一个大的随机整数y,并且发送给Carol Y=g^y mod n
      Carol选取一个大的随机整数z,并且发送给Alice Z=g^x mod n
    * Alice发送给Bob Z’=Z^x mod n
             Bob发送给Carol X’=X^y mod n
             Carol发送给Alice Y’=Y^z mod n
     * 产生共享密钥：
     	* Alice计算k=Y’^x mod n
        * Bob计算k=Z’^y mod n
         * Carol计算k=X’^z mod n
* 加解密的验证：利用python的pydes库进行DES加解密的验证。

#### 演示界面
![DH1](https://img-blog.csdnimg.cn/20200810150259930.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NMYXJhbGkw,size_16,color_FFFFFF,t_70)

![DH2](https://img-blog.csdnimg.cn/20200810150341450.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NMYXJhbGkw,size_16,color_FFFFFF,t_70)
#### 遇到的问题
1. javascript中大数溢出问题。
解决办法：利用BigInt对象，但是要注意这里BigInt对象的除法运算的结果自动向下取整，和普通的javascript语法有所区别。

2. 环境依赖
解决办法：利用pipenv管理小组成员的python,django版本和pydes函数库
3. 密钥交换之后不知该如何加解密的验证。
解决办法：通过截取调用DES的库完成验证。同时，由于pydes 中PAD_PKCS5填充规定DES为8位，于是我们采用密钥小于8位前面补0，大于8位截取前8位的方法。 

4. 如何提升生成随机大素数原根的效率
	因为要求时大素数，所以暴力的解法并不是一个比较好的选择，所以我们深入了解原根的相关原理。进行程序的优化，首先通过埃氏筛得出1~p-1范围内的所有质数，然后求p-1的所有质因子，然后验证是否为原根。 若a^((p-1)/p1), a^((p-1)/p2)…中不存在一个模p 等于 1，则a是模p的一个原根。
	
5. 前端布局混乱
学习 flex 布局，使用横向容器和纵向容器的布局理念，使块级元素合理分布在嵌套的容器中、界面更加美观。

6. 选择器不会用
区分 id、class、tag 等元素选择器的用法。

#### 总结
**经验** 通过这次实验，更加熟练掌握的Django创建一个项目基本流程。接触了jQuery-AJAX加载后端数据的方法。通过这个项目，更加明确了项目中应该进行各个模块的测试。python中可以直接运行某个函数。javascript可以将生成的值console.log()输出到控制台来查看。

**个人感悟**  这次实验中其实有现成的DH算法python库可以调用，但是我们选择了自己来实现其中各个方法。无论是生成随机大素数，还是生成原根，二次分发，共享密钥都尝试自己实现。从最开始的只能生成3位数的素数，到现在可以生成8位数的素数，我们进行了不断的尝试，虽然还是跟实际生活中100+位的素数有所差别。但是我们也掌握了一些效率更高算法的方法，比如说Miller-Rabin素性测试，欧拉筛等等。

**不足** 在生成随机素数的原根的过程中，我们使用的算法有一定不足，其不适用于更大位数的素数，因为“求1~sqrt(n)范围内的所有质数”即使时间复杂度为O(n)，但是对于n大于1e8时生成时间依旧会比较长。这个算法是用于求“最小的原根”的问题，但是实验中其实只需要求“其中一个原根”就可以了。根据这个性质，其实我们可以：
1.  生成一个大素数 q，直接p是素数，其中 p = 2q + 1
```
do{
    q = gen_prime();
    p = q * 2 + 1;
}while( ! is_prime(p) );
```
2.  生成一个随机数 g，1 < g < p - 1，直到g^2 mod p 和 g^q mod p 都不等于 1
```
do{
    g = random(2, p - 1); 
}while( (pow(g, 2) % p == 1) || (pow(q, 2) % p == 1) );
```
3.  得到g是p的本元根
```
print("p的本元根g是:" + g);
```
