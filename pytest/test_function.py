# 测试指令：pytest -vv test_function.py (-vv：打印详细信息)
# pytest：则会执行全部test开头的文件
# def add(x,y):
#     return x+y
# def test0():
#     assert 2 == add(1,1)
# def test1():
#     assert 1 != add(1,1)

# 测试计算时间


# 测试异常
# import pytest
# def function(x):
#     if x == 0:
#         raise ValueError('value error')
#     else:
#         pass
# def test_0():
#     with pytest.raises(ValueError):
#         function(0)
# def test_1():
#     assert function(1) == None

# 测试函数
# import pytest
# def add(x,y):
#     return x + y
#
# @pytest.mark.parametrize('x,y,result',[(1,1,2),(2,6,8),(5,1,6)])
# def test_add(x,y,result):
#     assert result == add(x,y)

# 函数分组测试
import pytest

@pytest.mark.g1
def test_a():
    pass

@pytest.mark.g2
def test_b():
    pass

@pytest.mark.g1
def test_c():
    pass

