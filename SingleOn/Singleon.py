#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
运用metaclass创建单例模式
"""


class SingleOn(type):
    def __init__(cls, name, bases, dict_1):
        super(SingleOn, cls).__init__(name, bases, dict_1)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingleOn, cls).__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=SingleOn):
    pass


if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print(id(a) == id(b))
