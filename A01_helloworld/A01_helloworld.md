# Python 学习笔记：Day 1 - 基础语法入门

### 核心目标

1. **输出 (Output):** 使用 `print()` 函数在屏幕上显示信息。
2. **注释 (Comment):** 使用 `#` 添加代码说明，让代码更易读。
3. **变量 (Variable):** 学会创建和使用变量来存储数据。
4. **数据类型 (Data Type):** 理解最基本的类型：字符串(`str`)、整数(`int`)、浮点数(`float`)。
5. **字符串格式化 (String Formatting):** 掌握现代、高效的 `f-string` 用法。
6. **用户输入 (Input):** 使用 `input()` 函数与用户交互，并处理输入的数据。

---

### 1. 输出与注释

`print()` 函数用于输出信息，`#` 用于注释，解释器会忽略注释。

```python
# 目标[1] & [2]: 使用 print() 输出，并添加注释
print("Hello, World!")  # 输出一行字符串

print(1 + 1)           # 也可以直接输出计算结果
```

### 2. 变量与命名规则

变量是给数据贴的“标签”，方便我们引用。

**命名规则：**

* 只能包含 **字母、数字和下划线 `_`**。
* 不能以 **数字** 开头。
* 大小写敏感 (`age` 和 `Age` 是两个不同的变量)。
* 推荐使用有意义的英文单词，多个单词用下划线连接（称为蛇形命名法, e.g., `big_apple`）。

```python
# 目标[3]: 定义和使用变量
message = "学 Python 很有趣！"
print(message)

my_age = 18
student_name = "小王"

# 变量的值可以被改变
my_age = 19 
print(my_age)
```

### 3. 核心数据类型

Python 会自动识别数据类型。我们可以用 `type()` 函数来查看一个变量的类型。

```python
# 目标[4]: 认识基本数据类型
my_name = 'tmdog'     # 字符串 (str), 单双引号通用
my_age = 18           # 整数 (int)
my_height = 1.75      # 浮点数 (float)

print(f"变量 my_name 的值是 '{my_name}', 类型是 {type(my_name)}")
print(f"变量 my_age 的值是 {my_age}, 类型是 {type(my_age)}")
print(f"变量 my_height 的值是 {my_height}, 类型是 {type(my_height)}")
```

**输出结果:**

```
变量 my_name 的值是 'tmdog', 类型是 <class 'str'>
变量 my_age 的值是 18, 类型是 <class 'int'>
变量 my_height 的值是 1.75, 类型是 <class 'float'>
```

### 4. 字符串处理

#### a. 传统拼接 (`+`)

可以用 `+` 号连接字符串，但不推荐在复杂场景下使用。

```python
greeting = "大家好，我叫" + my_name
print(greeting) # 输出: 大家好，我叫tmdog
```

#### b. 格式化字符串 (f-string)

在字符串前加 `f`，用 `{}` 直接嵌入变量。**这是目前最推荐的方式，代码更简洁易读。**

```python
# 目标[5]: 使用 f-string
personal_info = f"我叫 {student_name}，今年 {my_age} 岁了。"
print(personal_info) # 输出: 我叫 小王，今年 19 岁了。
```

### 5. 用户输入与类型转换

`input()` 函数用于获取用户在键盘上的输入。

**⭐ 关键知识点：**
`input()` 函数返回的**所有内容**，都会被 Python 当作**字符串（str）类型**处理。如果需要进行数学计算，必须先进行**类型转换**。

```python
# 目标[6]: 使用 input() 并处理数据
user_name = input("请输入你的名字: ")
user_age_str = input("请输入你的年龄: ") # 此时 user_age_str 是一个字符串

# 错误的做法：字符串和数字不能直接相加
# print(user_age_str + 1) # 这行代码会报错 TypeError!

# 正确的做法：使用 int() 函数将字符串转换为整数
user_age_int = int(user_age_str)
age_next_year = user_age_int + 1

# 现在可以愉快地输出结果了
print(f"你好, {user_name}！你今年 {user_age_int} 岁。")
print(f"到明年，你就 {age_next_year} 岁啦！")
```

---

### 本节总结与最佳实践

* `print()` 用于输出，是调试代码的好帮手。
* 变量命名要规范，养成好习惯。
* 优先使用 `f-string` 进行字符串格式化。
* **牢记：`input()` 返回的是字符串，需要计算时务必用 `int()` 或 `float()` 进行类型转换！** 这是初学者最常犯的错误之一。
