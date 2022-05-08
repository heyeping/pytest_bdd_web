"""
@Time ： 2022/5/5 21:29
@Auth ： heyeping
@File ：public.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import signal,os

class Signal(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        pass

def get_pathfile():
    path = "/".join(os.path.realpath(__file__).split("/")[:-2])
    return path