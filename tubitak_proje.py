import math
import re
from decimal import Decimal
import numpy as np

kul=input("lütfen şifreleme istediğiniz metni giriniz")

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
n=input("kaçıncı fibonaci satisonı şstiyorsunuz")
n=int(n)
m=int(n+1)
o=int(n+2)
k=int(n+3)
a=fibonacci(n)
b=fibonacci(m)
c=fibonacci(o)
d=fibonacci(k)
print((2*a-b)/(2*a+b))
print((2*c-d)/(2*c+d))
e=Decimal(math.degrees(math.acos((2*a-b)/(2*a+b))))
f=Decimal(math.degrees(math.acos((2*c-d)/(2*c+d))))
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
    if esitsizlik:
        j+=g[i]
        j+=h[i]
        de=int(j)
		#p=de%40
		#print(de)
        sayi.append(de)
		#print(len(sayi))
        sayi2.append(sayi[::-1])
    elif  g[i]!=h[i]:
        j+=g[i]
        j+=h[i]
        de=int(j)
		#p=de%40
		#print(de)
        sayi.append(de)
		#print(len(sayi))
        sayi2.append(sayi[::-1])
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
