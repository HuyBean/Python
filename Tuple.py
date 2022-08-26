# được giới hạn bởi cặp ngoặc ()
# các phần tử của tuple đc phân cách nhau bởi dấu, 
# tuple có khả năng chứa mọi giá trị 
# tốc độ truy xuất tuple nhanh hơn list 
# dung lượng chiếm trong bộ nhớ nhỏ hơn list
# bảo vệ dữ liệu của bạn sẽ không bị thay đổi
# có thể dùng làm key của dictionary

# tup = (1, 1, 2, 5, 6, 77, 7, 7)
# arrtup = (2)
# arr = [2]
# tupl = (i for i in range(10) if i % 2 == 0)
# a = tuple(tupl)

# print(tup)
# print(arrtup)
# print(arr)
# print(a)
tup = (1,5,9)
tup+=(2,4,6)
print(tup)
tup*=2
print(tup)
a = 1 in tup
print(a)
b = tup[0]
print(b)
c = len(tup)
print(c)
d = tup[-1]
print(d)
e = tup[::-1]
print(e)
f = tup[3: 7]
print(f)
a = tup.count(1)
print(a)

#Tuple không cho phép sửa chữa nội dung, List thì có