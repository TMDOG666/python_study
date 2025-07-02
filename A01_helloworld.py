# ====================================================================
# Python 学习笔记 Day 1 - 基础语法完整示例代码
# ====================================================================

### 1. 输出与注释 ###
print("--- 1. 输出与注释 ---")
# 使用 print() 输出，并添加注释
print("Hello, World!")  # 输出一行字符串
print(1 + 1)           # 也可以直接输出计算结果
print("-" * 20)        # 打印20个'-'作为分隔线，这是个小技巧


### 2. 变量与命名规则 ###
print("--- 2. 变量与命名规则 ---")
# 定义和使用变量
message = "学 Python 很有趣！"
print(message)

# 变量的值可以被改变
my_age = 18
student_name = "小王"
print(f"初次定义：我叫 {student_name}，今年 {my_age} 岁。")

my_age = 19 # 更新变量的值
print(f"更新之后：我叫 {student_name}，现在 {my_age} 岁了。")
print("-" * 20)

### 3. 核心数据类型 ###
print("--- 3. 核心数据类型 ---")
# 我们可以用 type() 函数来查看一个变量的类型
my_name_str = 'tmdog'     # 字符串 (str)
my_age_int = 18           # 整数 (int)
my_height_float = 1.75    # 浮点数 (float)

print(f"变量 my_name_str 的值是 '{my_name_str}', 类型是 {type(my_name_str)}")
print(f"变量 my_age_int 的值是 {my_age_int}, 类型是 {type(my_age_int)}")
print(f"变量 my_height_float 的值是 {my_height_float}, 类型是 {type(my_height_float)}")
print("-" * 20)


### 4. 字符串处理 ###
print("--- 4. 字符串处理 ---")

# a. 传统拼接 (+)
greeting = "大家好，我叫" + my_name_str
print(f"传统拼接: {greeting}")

# b. 格式化字符串 (f-string) - 这是目前最推荐的方式
personal_info = f"f-string: 我叫 {student_name}，今年 {my_age} 岁了。"
print(personal_info)
print("-" * 20)


### 5. 用户输入与类型转换 ###
print("--- 5. 用户输入与类型转换 ---")
print("接下来，程序将需要你输入一些信息...")

# 使用 input() 获取用户输入
user_name = input("请输入你的名字: ")
user_age_str = input("请输入你的年龄: ") # input() 返回的是字符串

# ⭐ 关键：使用 int() 函数将字符串转换为整数
try:
    user_age_int = int(user_age_str)
    age_next_year = user_age_int + 1
    
    # 现在可以愉快地输出结果了
    print(f"\n太好了！处理结果如下：") # \n 是换行的意思
    print(f"你好, {user_name}！你今年 {user_age_int} 岁。")
    print(f"到明年，你就 {age_next_year} 岁啦！")

except ValueError:
    # 如果用户输入的年龄不是一个有效的数字，int()会报错，我们可以处理这个错误
    print(f"\n出错了！'{user_age_str}' 不是一个有效的年龄数字。请重新运行程序并输入数字。")

print("-" * 20)
print("所有代码已执行完毕！")