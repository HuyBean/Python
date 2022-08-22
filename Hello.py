#note
print("Hello World")
L = 99999999999999
A = 2000
B = 804
S = A + B

#maximum approximate 15 number after .
C = 3.14159265312345678910111213
H = "Hello Word"
print(C)
print(S)

#type 
print(type(S))
print(type(H))
print(type(C))
print(type(L))

# get whole content of decimal library
from decimal import*

# get maximum 30 number in decimal
getcontext().prec = 30 #prec mean pecision

print(Decimal(10)/Decimal(3))
print((10)/Decimal(3))
print(Decimal(10)/(3))
f = 10/3
print(f)

# Fraction lib
from fractions import*
frac1 = Fraction(6, 9)
frac2 = Fraction(5, 10)
frac3 = frac1 + frac2
print(frac1)
print(frac2)
print(frac3)
print(type(frac1))

#complex number
c = complex(1, 2)
print(c)
print(type(c))