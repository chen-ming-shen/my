#关于装饰品的训练
#利用闭包返回函数完成不对对象函数的修改添加一些日志调试功能





#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start=time.time()
        call=fn(*args, **kw)
        print(f"当前函数 {fn.__name__} 执行了{time.time()-start:.3f}秒")
        return call
    return wrapper
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;
@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;
f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print(f'f测试失败!{f}')
elif s != 7986:
    print(f's测试失败!{s}')
print(f"结束\nf={f}\ns={s}")
#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
#再思考一下能否写出一个@log的decorator，使它既支持：
def log(text=None):
    if callable(text):#装饰器不带参数
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print(" \nbegin call")
            before_use=text(*args, **kw)
            print('\n函数%s\n没有文本的%s ():\nend call\n ' % (text.__name__,text.__name__))
            return before_use
        return wrapper
    else:#装饰器带参数
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print(" \nbegin call")
                before_use=func(*args, **kw)
                print('\n函数%s\n%s %s ():\nend call\n ' % (func.__name__,text,func.__name__))
                return before_use
            return wrapper
    return decorator
@log
def f_0():
    return 0
#又支持：
@log('execute')
def f_1():
    return 0
a,b=f_1(),f_0()
