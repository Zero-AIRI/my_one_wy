# 定义装饰器
def print_hello(func):
    def wrapper():
        print("Hello")  
        func()          
    return wrapper

# 使用 @ 装饰器
@print_hello
def greet():
    print("World!")

# 调用 greet() 会自动先打印 "Hello"，再执行原函数
greet()

# 定义原函数
def greet():
    print("World!")
# 手动装饰：把 greet 替换成装饰后的版本
greet = print_hello(greet)
# 调用 greet() 效果和 @ 版本一样
greet()
