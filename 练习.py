import time

def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator
def f1(func_name1,func_name2,**kw):
    print("this is a function 666" + func_name1 +func_name2)
    print(kw)

f1("suxiaojin","zhangsan",a=1,b=2,c='123')