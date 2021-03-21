import pytest
from common.basecase import basecase
import allure


class Calculator:
    """计算机"""

    def add(self, a, b):
        return a + b


cal = Calculator()
def setup_function():
    print('这是setup_function')
def teardown_function():
    print('这是teardown_funct')


@allure.feature('add测试用例')
@pytest.mark.parametrize('a,b,c', basecase.get_data()[0], ids=basecase.get_data()[1])
def test_add(a, b, c):
    result = cal.add(a, b)
    assert result == c


@allure.story('读取数据')
def test_get_data():
    print(basecase.get_data()[0])
    print(basecase.get_data()[1])
