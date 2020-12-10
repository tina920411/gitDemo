# -*- coding: utf-8 -*-
#-------------------------------
# @Time: 20-12-10  下午3:10
# @Author: tina
# @File: test_calc.py
#-------------------------------
import pytest
import yaml
from Function_code.Calculator import Calculator

def setup_module():
    """
    这是一个module级别的setup，它会在module(xxx.py)里
    所有test执行之前，被调用一次。
    注意，它是直接定义为一个module里的函数
    """
    print()
    print("-------------- setup before module --------------")

def teardown_module():
    """
    这是一个module级别的teardown，它会在module(xxx.py)里
    所有test执行之后，被调用一次。
    注意，它是直接定义为一个module里的函数
    """
    print()
    print("-------------- teardown after module --------------")

class TestCalc:
    """
    生成加减乘除四种方法，以及他们的setup和tesrdown
    """
    def setup_class(self):
        print("setup_class: 所有用例开始前执行")
        self.calc = Calculator()
        print("测试前先加载Calculator Function")
        print()

    def teardown_class(self):
        print()
        print("teardown_class: 所有用例测试结束")

    def setup_method(self):
        print("setup_method: 开始计算")

    def teardown_method(self):
        print("teardown_method:计算结束")
        print()

    @pytest.mark.parametrize("a,b,expect",
                             yaml.safe_load(open("./data_add.yaml")),
                             ids = ["add_int", "add_minus", "add_bigint"])
    def test_add(self,a,b,expect):
        print("正在执行 add 运算：%s + %s = %s" % (a,b,expect))
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             yaml.safe_load(open("./data_sub.yaml")),
                             ids=["sub_int", "sub_minus", "sub_bigint"])
    def test_sub(self,a,b,expect):
        print("正在执行 sub 运算：%s - %s = %s" % (a, b, expect))
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             yaml.safe_load(open("./data_mul.yaml")),
                             ids=["mul_int", "mul_minus", "mul_bigint"])
    def test_mul(self, a, b, expect):
        print("正在执行 mul 运算：%s * %s = %s" % (a, b, expect))
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data_div.yaml")),
                             ids=["div_int", "div_minus", "div_bigint", "ZeroDivisionError"])
    def test_div(self, a, b, expect):
        print("正在执行 div 运算：%s / %s = %s" % (a, b, expect))
        try:
            assert expect == self.calc.div(a, b)
        except ZeroDivisionError as e:
            print(e)
            print("警告：除数不能为0")

if __name__ == '__main__':
    pytest.main(['test_calc.py', '-sv'])







