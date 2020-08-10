import math

import random
import time

import base64
from pyDes import *

# 用辗转相除求最大公因子
def gcd(a,b):
	r=a%b
	while(r!=0):
		a=b
		b=r
		r=a%b
	return b

# 判断是否为素数
def judgeprime(a):
	count=0
	if gcd(a,1)!=1:
		count+=1
	if gcd(a,2)!=1:
		count+=1
	for i in range(3,int(a**0.5)+1):
		if i%2!=0 and gcd(a,i)!=1:
			count+=1
	return count

#生成伪素数
def pseudoprime(prime):
	while(True):
		pseudo=random.randint(5000000,50000000)*2+1
		for i in prime:
			temp=pseudo%i
			if(temp==0):
				break
		if(i==prime[len(prime)-1]):
			break
	return pseudo

#判断一定范围内的素数，生成素数列表
def primelist():
	prime=[]
	prime.append(2)
	for i in range(3,10008):
		#print("求素数",i)
		if i%2==1 and judgeprime(i)==0:
			prime.append(i)
	return prime



"""
求1~na所有的质数：
Eratosthenes
筛选2~(p-1)的质数
剔除已知素数的倍数
10^8
"""
def primes(n):
	f = []
	p = []
	for i in range(n+1):
		if (i > 2 and i % 2 == 0):
			f.append(1)
		else :
			f.append(0)
	
	i = 3
	j = i * i
	while (j <= n):
		f[j] = 1
		l = j + 2 * i
		while l <= n:
			f[l] = 1
			l = l + 2 * i #步长为2 * i。因为:奇数+偶数=奇数
		i = i + 2
		j = i * i
		
	p.append(2)
	for i in range(3,n + 1,2):
		if (f[i] == 0):
			p.append(i)
	
	return p
	
"""
求n的所有质因子:
问题：如何快速求解2*(大素数)的质因子
"""
def prime_factor(n):
	p = primes(int (math.sqrt(n)))
	r = []
	for i in p:
		if (n % i == 0):
			r.append(i)
		while (n % i == 0):
			n = n // i
	if (n > 1):
		r.append(n)
	return r

	
"""
模p快速幂:x^y%p
ll pow_m(ll a, ll n, ll m){
    ll t = a % m;
    ll r = 1;
    while(n > 0){
        if(n & 1)
            r = r * t % m;
        t = t * t % m;
        n >>= 1;
    }
    return r;
}
"""
def quick_pow_mod(x,y,p):
	x = x % p
	ret = 1
	while (y != 0):
		if (y % 2 == 1):
			ret = ret * x % p
		x = x * x % p
		y //= 2 ###
	return ret
	
"""
test if a ^ ((p-1)/ri) == 1 (mod p)
ri是(p-1)的质因子
"""
def test_a(a, p):
	r = prime_factor(p-1)
	for ri in r:
		t = (p - 1) // ri
		ret = quick_pow_mod(a, t, p)
		if ret == 1:
			return 0
	return 1
	
"""
求素数p的原根
"""
def primitive_root(p):
	rootlist=[]
	for a in range(2,p,1):
		test = test_a(a,p)
		if test == 1 and a > 10:
			rootlist.append(a)
			if len(rootlist)==20:
				a=random.choice(rootlist)
				return a

		
#产生一个随机素数p
def gen_p():
    bigprime=pseudoprime(primelist())
    return bigprime

#产生p的一个随机的原根
def gen_a(p):
    ret = primitive_root(p)
    return ret

#des加密
def show_encode(m, k):
	if len(str(k)) > 8:
		k = str(k)[0:8]
	if len(str(k)) < 8:
		k = str(k).zfill(8)
	Key = bytes(str(k),"utf-8") # Key
	Des_IV = b"\x22\x33\x35\x81\xBC\x38\x5A\xE7" # 自定IV向量
	ke = des(Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
	EncryptM = ke.encrypt(str(m))
	return base64.b64encode(EncryptM)

#des解密
def show_decode(m, k):
	if len(str(k)) > 8:
		k = str(k)[0:8]
	if len(str(k)) < 8:
		k = str(k).zfill(8)
	Key = bytes(str(k),"utf-8") # Key
	Des_IV = b"\x22\x33\x35\x81\xBC\x38\x5A\xE7" # 自定IV向量
	ke = des(Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
	return ke.decrypt(base64.b64decode(str(m)))





