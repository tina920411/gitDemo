# -*- coding: utf-8 -*-
#-------------------------------
# @Time: 20-12-10  下午2:51
# @Author: tina
# @File: Calculator.py
#-------------------------------

class Calculator():

    def add(self,a,b):
        """
        关于加法的函数
        :param a: 加法中的第一个变量
        :param b: 加法中的第二个变量
        :return: 返回sum
        """
        return a + b

    def sub(self,a,b):
        """
        关于减法的函数
        :param a: 被减数
        :param b: 减数
        :return: 返回差值
        """
        return a - b

    def mul(self,a,b):
        """
        关于乘法的函数
        :param a: 乘法中的第一个变量
        :param b: 乘法中的第二个变量
        :return: 返回乘积
        """
        return a * b

    def div(self,a,b):
        """
        关于除法的函数，注意，如果除数为0 则返回error
        :param a: 被除数
        :param b: 除数
        :return: 商
        """
        result = 0
        return a / b
        # try:
        #     return a / b
        # except ZeroDivisionError as e:
        #     return e



