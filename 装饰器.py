#装饰器
import time
# def f1():
#     print("this is a function")
#
# def print_current_time(func):
#     print(time.time())
#     func()
#
# print_current_time(f1)

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorator
def f1():
    print("this is a function")

f1()
# f=decorator(f1)
# f()
