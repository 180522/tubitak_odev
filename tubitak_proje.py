import math
import re
from decimal import Decimal
import numpy as np

kul=input("Lütfen şifreleme istediğiniz metni giriniz= ").lower()

FibArray = [1,1]

def fibonacci(n):
    if n<0 :
        print("Yanlış Sayı Girdiniz")
    elif n<=len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib
def rotate(l, n):
    return l[n:] + l[:n]
n=input("Kaçıncı fibonaci sayısını istiyorsunuz= ")
n=int(n)
m=int(n+1)
o=int(n+2)
a=fibonacci(n)
b=fibonacci(m)
c=fibonacci(o)
k=(2*b-a)/(2*b+a)
l=(1-k**2)**(1/2)
p=k/l
r=1/p
x=(2*c-b)/(2*c+b)
y=(1-x**2)**(1/2)
z=x/y
t=1/z
xc=n%16
if xc==0:
    e=Decimal(k)
    f=Decimal(x)
    print(e)
    print(f)
elif xc==1:
    
    e=Decimal(k)
    f=Decimal(y)
    print(e)
    print(f)
elif xc==2:
    e=Decimal(k)
    f=Decimal(z)
    print(e)
    print(f)
elif xc==3:
    e=Decimal(k)
    f=Decimal(t)
    print(e)
    print(f)
elif xc==4:
    e=Decimal(l)
    f=Decimal(x)
    print(e)
    print(f)
elif xc==5:
    e=Decimal(l)
    f=Decimal(y)
    print(e)
    print(f)
elif xc==6:
    e=Decimal(l)
    f=Decimal(z)
    print(e)
    print(f)
elif xc==7:
    e=Decimal(l)
    f=Decimal(t)
    print(e)
    print(f)
elif xc==8:
    e=Decimal(p)
    f=Decimal(x)
    print(e)
    print(f)
elif xc==9:
    e=Decimal(p)
    f=Decimal(y)
    print(e)
    print(f)
elif xc==10:
    e=Decimal(p)
    f=Decimal(z)
    print(e)
    print(f)
elif xc==11:
    e=Decimal(p)
    f=Decimal(t)
    print(e)
    print(f)
elif xc==12:
    e=Decimal(r)
    f=Decimal(x)
    print(e)
    print(f)
elif xc==13:
    e=Decimal(r)
    f=Decimal(y)
    print(e)
    print(f)
elif xc==14:
    e=Decimal(r)
    f=Decimal(z)
    print(e)
    print(f)
elif xc==15:
    e=Decimal(r)
    f=Decimal(t)
    print(e)
    print(f)

e=str(e)
f=str(f)
g=e
h=f
j=""

alfabe=[
  "a",
  "b",
  "c",
  "ç",
  "d",
  "e",
  "f",
  "g",
  "ğ",
  "h",
  "ı",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "ö",
  "p",
  "r",
  "s",
  "ş",
  "t",
  "u",
  "ü",
  "v",
  "y",
  "z",
  " ",
  "0",
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9"
]

avb=[]
tablo = [alfabe,[]]
for i in range (len(alfabe)):
    tablo[0][i] = alfabe[i]
    av=rotate(alfabe,i)
    avb.append(av)
print(avb)

son3=[]
sayi=[]
sayi2=[]
esitsizlik=False
for i in range(len(e)):
    if i<=42 and esitsizlik and i>0:
        j+=g[i]
        j+=h[i]
        de=int(j)
		#p=de%40
		#print(de)
        sayi.append(de)
		#print(len(sayi))
        sayi2.append(sayi[:1:-1])
    elif i<=42 and g[i]!=h[i] and i>0:
        j+=g[i]
        j+=h[i]
        de=int(j)
		#p=de%40
		#print(de)
        sayi.append(de)
		#print(len(sayi))
        sayi2.append(sayi[:1:-1])
        esitsizlik=True
son=sayi2[len(sayi)-1][0]
print(son)
son=str(son)
son1=re.findall('..',son)
print(re.findall('..',son))
#print(sayi2)
#print(sayi)
for i in range(int(len(son)/2-2)):
    son2=son1[i]
    print(son2)
    son2=int(son2)
    son4=son2%40
    son3.append(son4)
print(son3)
kar=[*kul]
print(kar)
sonuc=""
for x in range(len(kul)):
    z=alfabe.index(kul[x])
    print("son3x:",son3[x]," z:",z, " sonuç:",avb[son3[x]][z])
    sonuc+=avb[son3[x]][z]
print(sonuc)
