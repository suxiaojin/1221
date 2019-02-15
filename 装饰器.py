#装饰器
import time
def f1():
    print("this is a function")
def f2():
    print("this is function2")

def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)

# def decorator(func):
#     def wrapper(*args,**kw):
#         print(time.time())
#         func(*args,**kw)
#     return wrapper

# @decorator
# def f1(func_nmae):
#     print("this is a function" + func_nmae)
#
# @decorator
# def f2(func_name1,func_name2):
#     print("this is a function" + func_name1)
#     print("this is a function" + func_name2)
#
# @decorator
# def f3(func_name1,func_name2,**kw):
#     print("this is a function" + func_name1)
#     print("this is a function" + func_name2)
#     print(kw)
#
# ub
# f1('suxiaojin')
# f2('test1','test2')
# f3('hah1','haha2',a=1,b=2,d=1111)
# # f=decorator(f1)
# # f()
