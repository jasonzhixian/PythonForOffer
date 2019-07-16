#using the __new__ method
class SingleTon(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
        
#using the decorator
def singleton(cls):
    _instance = {}
    def wrap_func():
        if cls not in _instance:
            _instance[cls] = cls() #使用不可变的类地址作为键，其实例作为值
        return _instance[cls]
    return wrap_func

@singleton
class Cls(object):
    def __init__(self):
        pass

#test_case_1
if __name__ == '__main__':
    a = SingleTon()
    b = SingleTon()
    print(id(a) == id(b))

#test_case_2
if __name__ == '__main__':
    a = Cls()
    b = Cls()
    print(id(a) == id(b))