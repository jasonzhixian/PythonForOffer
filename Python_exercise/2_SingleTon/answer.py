#using the __new__ method
# class SingleTon(object):

#     __instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls, *args, **kwargs)
#         return cls.__instance
        
#using the decorator
def singleton(cls):
    instance = {}
    def wrap_func():
        if cls not in instance:
            instance[cls] = cls()
        return instance[cls]
    return wrap_func

@singleton
class Cls(object):
    def __init__(self):
        pass
#test_case_1
# if __name__ == '__main__':
#     a = SingleTon()
#     b = SingleTon()
#     print(id(a) == id(b))

#test_case_2
if __name__ == '__main__':
    a = Cls()
    b = Cls()
    print(id(a) == id(b))