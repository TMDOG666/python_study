# ============================================
#   第一部分：异常处理的核心机制 try...except
# ============================================

# 1. 基本语法
print("--- 1. try...except 基本用法 ---")
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator # 这行会引发 ZeroDivisionError
    print(result) # 这行代码不会被执行
except ZeroDivisionError as e:
    # 捕捉到 ZeroDivisionError 后，执行这里的代码
    print(f"错误：除数不能为零！错误详情 : {e}")

print("程序并没有崩溃，而是继续执行到了这里。")
print("-" * 30)

#### **2. 捕捉多种特定异常**

# 一个 `try` 块中可能发生多种不同类型的错误。你可以设置多个 `except` 块来分别处理它们，就像汽车仪表盘上有不同的警示灯（机油灯、电瓶灯等）。
print("--- 2. 捕捉多种特定异常 ---")

try:
    user_input = input("请输入一个数字来计算 100 除以它：")
    number = int(user_input)
    result = 100 / number
    print(f"结果是 {result}.")
except ValueError as e:
    print(f"错误: 输入的不是一个数字. 错误详情: {e}")
except ZeroDivisionError as e:
    print(f"错误: 除数不能为零. 错误详情: {e}")

print("程序并没有崩溃，而是继续执行到了这里")
print("-" * 30)


#### **3. 获取异常对象信息**

# 有时候，你不仅想知道发生了什么类型的错误，还想看到 Python 提供的具体错误信息。你可以使用 `as` 关键字来捕获异常对象。
# 
# **语法：** `except ExceptionType as e:`

print("--- 3. 获取异常对象信息 ---")
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print("文件操作失败！")
    print(f"具体的错误信息是: {e}")
    print(f"错误的类型是: {type(e)}")
print("-" * 30)

#### **4. 捕捉所有异常 (通用 `except`)**

# 你可以使用 `except Exception:` 来捕捉几乎所有类型的异常。这通常放在所有特定 `except` 块的最后，作为一个“终极保险”。
#
# **⚠️ 警告：** 避免使用一个光秃秃的 `except:`。它会捕捉包括系统退出 (`SystemExit`) 在内的所有东西，可能会隐藏严重的问题，让调试变得极其困难。`except Exception:` 是更规范、更安全的做法。

print("--- 4. 捕捉所有异常 ---")
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print("文件操作失败！")
    print(f"具体的错误信息是: {e}")
    print(f"错误的类型是: {type(e)}")
except Exception as e:
    print("出现了一个未知错误")
    print(f"具体的错误信息是: {e}")
    print(f"错误的类型是: {type(e)}")

print("-" * 30)

# ============================================
#        第二部分：完整的异常处理结构
# ============================================
# `try...except...else...finally`
# **为什么需要 `else` 和 `finally`？**
# * **`else` 的意义**：它能让你的“成功路径”代码与“风险代码”分离，使 `try` 块更简洁，逻辑更清晰。
# * **`finally` 的意义**：它主要用于**资源清理**。无论程序是成功还是失败，有些操作（如关闭文件、关闭数据库连接）都必须执行，以防资源泄露。

print("--- 4. 完整的 try...except...else...finally ---")
file_path = "A07_Exception/data.txt"
try:
    print(f"尝试打开文件 '{file_path}' 进行写入...")
    f = open(file_path, 'w')
    f.write("Hello, finally!")
    # 如果在这里插入一行 10/0，会触发异常
except IOError as e:
    print(f"写入文件时发生 I/O 错误: {e}")
else:
    # 只有在 try 块完全成功时才会执行
    print("文件写入成功，没有发生任何异常。")
finally:
    # 无论 try 成功还是 except 被触发，这里都会执行
    print("进入 finally 块：执行清理工作。")
    if 'f' in locals() and not f.closed:
        f.close()
        print("文件已关闭。")
    else:
        print("文件未能成功打开，无需关闭。")
print("-" * 30)

# ============================================
#       第三部分：主动抛出异常 `raise`
# ============================================

print("--- 5. 主动抛出异常 raise ---")
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数。")
    if age < 0 or age > 120:
        raise ValueError("年龄必须在 0 到 120 之间。")
    print(f"年龄设置为: {age}")

try:
    set_age(25)     # 成功
    set_age(-5)     # 将会引发 ValueError
except (ValueError, TypeError) as e:
    print(f"设置年龄失败: {e}")

try:
    set_age('abc')
except (ValueError, TypeError) as e:
    print(f"设置年龄失败: {e}")


print("-" * 30)


# ============================================
#    第四部分：自定义异常 (Custom Exceptions)
# ============================================
print("--- 6. 自定义异常 ---")

# 1. 定义自己的异常类
class MyAppError(Exception):
    """应用程序的基准错误类"""
    pass

class ValidationError(MyAppError):
    """数据验证相关的错误"""
    pass

# 2. 在代码中使用自定义异常
def register_user(username):
    if len(username) < 3:
        raise ValidationError("用户名长度不能少于3个字符！")
    print(f"用户 '{username}' 注册成功！")

# 3. 捕捉自定义异常
try:
    register_user("Al")
except ValidationError as e:
    print(f"注册失败: {e}")
except MyAppError as e:
    print(f"发生应用错误: {e}")
print("-" * 30)



