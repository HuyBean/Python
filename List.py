# Giới hạn bởi cặp ngoặc vuông
# Các phần tử của list cách nhau bởi dấu,
# List có khả năng chứa mọi giá trị đối tượng của Python.
# Và bao gồm chính nó
a = [1, 2, 5, "Hello"]
b = [[[1, 2 , 3], [3, 5, 6]], ['a', 'b','c'], ["HuyBean 2003"]]
#list rỗng
c = []
print(a)
print(b)

#List conprehension
d = [i for i in range(30)]# tao ra 30 phtu bat dau tu 0
print(d)

e = [[n,n*1,n*2,n*5] for n in range(1,4)]
print(e)
# List string's element
f = list("Huy Bean")
print(f)
g = [1,2]
g+= ['one', 'two']
print(g)
h = g*2
print(h)
i = 'one' in h
print(i)
A = [[1, 2, 3], [4, 5, 6]]
B = list(A)
print(A)
print(B)
B[0] = 'Hello'
print(A)
print(B)
