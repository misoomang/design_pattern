#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
运用new方法创建单例
"""


class SingleOn(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingleOn, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Myclass(SingleOn):
    pass


if __name__ == '__main__':
    a = Myclass()
    b = Myclass()
    print(id(a) == id(b))

