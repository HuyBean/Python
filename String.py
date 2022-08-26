# str = 'Hello World'
# print(str)
# print(type(str))
# strstr = "I'm Beginner"
# print(type(strstr))

# strA = "Hello World "
# strB = "I'm Huy Bean"
# strC = strA +  "\n" + strB
# print(strC)
# print(strA*5)
# strH = "H"
# print(strH in strB)
# strT = "t"
# strTemp= strT in strB
# print(strTemp)

# #cut string
# stra = "HuyBean"
# strb = stra[1:len(stra)]# get element 1 to the end
# strc = stra[:] # get whole string
# strd = stra[3:None] # None to get the ending string element
# print(strb)
# print(strc)
# print(strd)

# #cut by step
# stre = stra[None:5:2] #get element from the beginning to the 5th elementh with step 2 
# print(stre)

#from string to int
# strA = int("69") + 5
# print(strA)

#change value
# strA = "Hello world"
# strA = strA[None:4] + "0" + strA[5:None]
# print(strA)

# a = 'My name is %s' %('HuyBean')
# b = "I'm %d years old and %s days" %(19, "50")
# print(a)
# print(b)

# s = '%s %s'
# result = s % ('1', '2')
# print(result)

# r = '1: {hello}, 2: {HuyBean}'.format(hello = 123, HuyBean = 1000)
# print(r)

# t = '{:$^11}'.format('HuyBean') # align center
# print(t)
# t = '{:$<11}'.format('HuyBean') # align left
# print(t)
# t = '{:$>11}'.format('HuyBean') # align right
# print(t)

a = 'mot hai ba bon nam'
b = a.capitalize() # capital first letter
c = a.upper()# capital whole string
d = a.title() # capital each first letter
e = a.center(30, '-') # align center
f = a.rjust(20, '-') 
g = a.ljust(20, '-') 
h = a.count('a', 0, None)
i = a.startswith('mot', 8, None ) # also a.endswith('n')
k = a.find('a') # find the first position appear
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(k)