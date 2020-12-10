# -*- coding: utf-8 -*-
#-------------------------------
# @Time: 20-12-10  下午3:07
# @Author: tina
# @File: test.py
#-------------------------------

def div(a, b):
    """
    关于除法的函数，注意，如果除数为0 则返回error
    :param a: 被除数
    :param b: 除数
    :return: 商
    """
    result = 0
    try:
        return a / b
    except ZeroDivisionError as e:
        raise e


print(div(1, 2))
