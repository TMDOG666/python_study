# main.py

# 方式一：导入具体函数
from my_app.utils.string_helper import to_upper_case
from my_app.math.calculators import add

print(to_upper_case("hello world"))
print(add(100, 200))

# 方式二：导入模块
from my_app.math import calculators
print(calculators.add(5, 5))