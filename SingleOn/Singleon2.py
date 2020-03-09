#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
通过共享属性创建单例
"""


class SingleOn(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(SingleOn, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._state
        return obj


if __name__ == '__main__':
    a = SingleOn()
    b = SingleOn()
    print(id(a) == id(b))
    print(a.__dict__ == b.__dict__)
