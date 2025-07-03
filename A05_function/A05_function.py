# ============================================
#      第一部分：函数的基础 - 定义与调用
# ============================================


#### **1. 定义一个最简单的函数**

# **语法结构：**

# ```python
# def function_name():
#     # 函数体 (indented block of code)
#     # 这里是函数要执行的代码
# ```
# 
# * `def`：关键字，告诉 Python 你正在定义一个函数。
# * `function_name`：你给函数起的名字。命名规则和变量一样（小写字母和下划线），并且名字要有意义。
# * `()`：圆括号，即使没有信息要传递，它也是必需的。
# * `:`：冒号，表示函数定义的开始。
# * **缩进的代码块**：所有属于这个函数的代码都必须缩进。
print("--- 1. 定义与调用最简单的函数 ---")

# 定义一个名为 greet 的函数
def grteet():
    print("Hello,函数")
    print("这是一个简单的问候。")

# 第一次调用 greet 函数
print("\n第一次调用 greet 函数")
grteet()

# 第二次调用 greet 函数
print("\n第二次调用 greet 函数")
grteet()

print("-" * 30)


# ============================================
#   第二部分：让函数更强大 - 参数 (Parameters)
# ============================================

# 2. 带有一个参数的函数
print("--- 2. 带参数的函数 ---")

# 'name' 是一个参数，它将在函数内部作为变量使用
def greet_person(name):
    print(f"你好, {name}!")
    print("很高兴认识你。")

# 调用函数，并传入具体的“参数”
greet_person("Alice") # "Alice" 是传递给 name 参数的参数

print() # 打印一个空行

greet_person("Bob") # "Bob" 是传递给 name 参数的参数
print("-" * 30)

# 3. 带有多个参数的函数
print("--- 3. 带有多个参数的函数 ---")

# 定义一个函数，接收姓和名，以及年龄
def describe_person(first_name, last_name, age):
    full_name = f"{first_name} {last_name}"
    print(f"这位是 {full_name}。")
    print(f"他/她今年 {age} 岁。")

# 调用时，必须按顺序提供所有参数
describe_person("三", "张", 25) 
print("-" * 30)


# ============================================
#   第三部分：从函数获取结果 - `return` 语句
# ============================================
# 4. 使用 `return` 返回值

print("--- 4. 使用 return 返回值 ---")

# 定义一个加法函数
def add(a, b):
    result = a + b
    return result
    # return 下方的任何代码都不会被执行！
    print("这行代码永远不会运行") #变成暗色

# 调用函数，并将返回的结果存储在一个变量中
sum_result = add(5, 3)
print(f"5 + 3 的计算结果是: {sum_result}")

# 你也可以直接在其他表达式中使用函数的返回值
another_result = add(10, 20) * 2
print(f"(10 + 20) * 2 的结果是: {another_result}")
print("-" * 30)


# ============================================
#   第四部分：参数的高级用法 (细节中的魔鬼)
# ============================================
# ### **5. 默认参数 (Default Arguments)**
# 
# 你可以为参数提供一个默认值。如果调用函数时没有提供该参数，它就会使用这个默认值。
# 
# *语法：** `def function_name(param1, param2=default_value):`
# *规则：** 默认参数必须放在所有非默认参数的**后面**。

print("--- 5. 默认参数 ---")

def greet_with_title(name, title="同学"): # title 有一个默认值
    print(f"你好, {name} {title}!")

greet_with_title("小明") # 不提供 title，使用默认值 "同学"
greet_with_title("王", "老师") # 提供 title，覆盖默认值
print("-" * 30)

#### **6. 关键字参数 (Keyword Arguments)**
# 调用函数时，你可以通过 `参数名=值` 的形式来指定参数，这样就不必关心参数的顺序了。


print("--- 6. 关键字参数 ---")

def greet_with_title(name, title="同学"):
    print(f"你好, {name} {title}!\n")

greet_with_title("小明")
greet_with_title("王", "老师")

greet_with_title(title="同学", name="小明")
greet_with_title(name="王", title="老师")
print("-" * 30)


#### **7. 任意数量的参数 (`*args` 和 `**kwargs`)**

# 有时候，你无法预知函数会被传入多少个参数。
# 
# * `*args` (任意位置参数): 将所有多余的**位置参数**收集到一个**元组 (tuple)** 中。
# * `**kwargs` (任意关键字参数): 将所有多余的**关键字参数**收集到一个**字典 (dict)** 中。

print("--- 7. 任意数量的参数 ---")

# a. 使用 *args 计算任意数字的和
def sum_all(*numbers):
    print(f"接收到的参数元组: {numbers}")
    total = 0
    for num in numbers:
        total += num
    return total

print(f"1, 2, 3 的和是: {sum_all(1, 2, 3)}")
print(f"10, 20, 30, 40 的和是: {sum_all(10, 20, 30, 40)}")

# b. 使用 **kwargs 构建一个用户资料
def build_profile(name, **user_info):
    profile = {'name': name}
    print(f"接收到的关键字参数字典: {user_info}")
    for key, value in user_info.items():
        profile[key] = value
    return profile

user1 = build_profile("Alice", age=28, city="New York", occupation="Developer", hobby="编程")
print(f"构建的用户资料: {user1}")
print("-" * 30)


# ============================================
#       第五部分：变量的作用域 (Scope)
# ============================================
# 一个变量并不是在程序的任何地方都可以被访问的，它有自己的“生命周期”和“作用范围”，这就是作用域。
# 
# **局部作用域 (Local Scope):** 在函数**内部**定义的变量，只在该函数内部有效。函数执行结束，它就消失了。
# **全局作用域 (Global Scope):** 在所有函数**外部**定义的变量，在整个程序中都有效。
print("--- 8. 变量作用域 ---")

x = 100 # 全局变量
def my_function():
    y = 20 # 局部变量
    print(f"函数内部的局部变量 y 的值: {y}")
    print(f"函数内部的全局变量 x 的值: {x}")

my_function()

try:
    print(f"函数外的全局变量 x 的值: {x}")
    print(f"函数外的局部变量 y 的值: {y}")
except NameError:
    print("变量 y 不在当前作用域内")


# **⚠️ 忠告：** 尽量避免在函数内部修改全局变量。这会让程序逻辑变得混乱，难以调试。最佳实践是，让函数通过 `return` 返回值来与外部世界通信，而不是直接修改外部的变量。

print("-" * 30)

# ============================================
#       第六部分：文档字符串 (Docstrings)
# ============================================
# Python 提供了一种标准方式——文档字符串。它就是函数定义下方的第一个字符串，用三引号 `"""..."""` 包围。

print("--- 9. 文档字符串 ---")

def power(base, exponent):
    f"""
    计算一个数的幂。

    Args:
        base (int or float): 基数。
        exponent (int or float): 指数。
        {base ** exponent}
    Returns:
        int or float: base 的 exponent 次幂的结果。
    """
    return base ** exponent

# 使用 help() 函数可以查看一个函数的文档字符串,是静态的如果向上面这样打印不出来
help(power)
print(f"\n2的3次方是: {power(2, 3)}")

