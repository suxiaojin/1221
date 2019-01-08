#匿名函数
# def add(x,y):
#     return x+y
# f=add(1,2)
# print(f)
#
# f1=lambda x,y:x+y
# print(f1(1,2))

# 三元表达式     r=x if x>y else y
#print(r)

# x=2
# y=5
# r=x if x>y else y
# print(r)

#map
# list_x=[1,2,3,4,5,6,7]
# def square(x):
#     return x*x
# # for x in list_x:
# #     square(x)
# r=map(square,list_x)
# print(list(r))

#reduce
from functools import reduce
list_x=[1,2,3,4,5,6,7]
r=reduce(lambda x,y:x+y,list_x)
print(r)