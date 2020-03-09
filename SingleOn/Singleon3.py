#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
通过装饰器创建单例
"""


def singleon(cls, *args, **kwargs):
    instance = {}

    def get_instance():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
    return get_instance


@singleon
class MyClass:
    pass


if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print(id(a) == id(b))
