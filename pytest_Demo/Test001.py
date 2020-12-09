# -*- coding: utf-8 -*-
#-------------------------------
# @Time: 20-12-8  下午2:39
# @Author: tina
# @File: Test001.py
#-------------------------------

import pytest
import yaml

def test_add():
    result = 1 + 2
    print result
    assert result == 3

def test_add2():
    result = 1 + 3
    print result
    assert result == 3
