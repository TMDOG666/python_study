# ===================================================
# ### **第一部分：条件判断 - 在分岔路口做选择**
# ===================================================


# 条件判断让你的程序能够根据不同的条件，执行不同的代码块。
# 
# #### **1. 最简单的结构: `if`**
# 
# `if` 就像一个只有一个选项的岔路口。如果满足某个条件，就执行一件事；如果不满足，就直接跳过，什么也不做。

print("--- 1. if 结构 ---")
weather = "sunny"
temperature = 28

# 条件1: 天气是晴天吗？
if weather == "sunny":
    print("天气真好，是晴天！")
    print("很适合出门散步。")

# 条件2: 温度超过25度吗？
if temperature > 25:
    print("今天有点热，记得穿短袖。")

# 条件3: 一个不满足的条件
if temperature < 0:
    # 这个条件是 False, 所以下面这行代码不会被执行
    print("天哪，结冰了！")

print("程序继续执行...")
print("-" * 30)

#### **2. 二选一结构: `if...else`**

# `if...else` 提供了一个“非此即彼”的选择，像一个有两个出口的岔路口。
print("--- 2. if...else 结构 ---")
score = 55

# 判断考试是否及格 (及格线为60分)
if score >= 60:
    print(f"你的分数是 {score}，恭喜你，及格了！")
else:
    print(f"你的分数是 {score}，很遗憾，没及格，下次加油！")

# 检查一个数字是奇数还是偶数
number = 10
if number % 2 == 0: # % 2 == 0 表示能被2整除，是偶数
    print(f"{number} 是一个偶数。")
else:
    print(f"{number} 是一个奇数。")

age = 17

if age >= 18:
    print("可以进入成人区.")
else:
    print("不能进入成人区.")

print("-" * 30)


#### **3. 多选一结构: `if...elif...else`**

# `elif` 是 "else if" 的缩写。当你有多个互斥的条件需要判断时，这个结构非常有用，就像一个有多个出口的环岛。

print("--- 3. if...elif...else 结构 ---")
score = 85

if score >= 90:
    grade = "A (优秀)"
elif score >= 80: # 能执行到这里，说明 score 肯定小于 90
    grade = "B (良好)"
elif score >= 70:
    grade = "C (中等)"
elif score >= 60:
    grade = "D (及格)"
else: # 能执行到这里，说明 score 肯定小于 60
    grade = "F (不及格)"

print(f"你的分数是 {score}，对应的等级是 {grade}。")
print("-" * 30)


# ===================================================
#           第二部分：循环 - 让重复工作自动化
# ===================================================

#### **1. `for` 循环：遍历所有元素**

# `for` 循环的核心思想是“**对一个集合中的每一个成员，都做同样一件事**”。它非常适合用来处理列表、元组、字符串等任何**可迭代 (iterable)** 的对象。

print("--- 4. for 循环 ---")

# a. 遍历列表 (list)
fruits = ["apple", "banana", "cherry", 3333]
print("遍历水果列表:")
for fruit in fruits:
    print(f"  我正在吃 {fruit}")

# b. 遍历字符串 (string)
message = "Python"
print("\n遍历字符串 'Python':")
for char in message:
    print(f"  字符: {char}")

# c. 遍历 range() 函数 (最常见的用法之一)
# range(5) 会生成一个从 0 到 4 的数字序列 [0, 1, 2, 3, 4]
print("\n使用 range(5) 循环5次:")
for i in range(5):
    print(f"  这是第 {i+1} 次循环。")

# range(start, stop, step)
print("\n使用 range(2, 11, 2) 打印偶数:")
for num in range(2, 11, 2): # 从2开始, 到11前结束, 每次加2
    print(f"  偶数: {num}")

# d. 遍历字典 (dict)
student_scores = {"Alice": 92, "Bob": 78, "Charlie": 85}
print("\n遍历字典的键:")
for name in student_scores:
    print(f"  学生: {name}")

for name in student_scores.keys():
    print(f"  学生: {name}")

print("\n遍历字典的值:")
for score in student_scores.values():
    print(f"  分数: {score}")

print("\n遍历字典的项 (键和值):")
for name, score in student_scores.items(): # .items() 返回 (键, 值) 对
    print(f"  学生 {name} 的分数是 {score}")


print("-" * 30)


#### **2. `while` 循环：直到条件不满足**

# `while` 循环的思想是“**只要这个条件还成立，就一直重复做这件事**”。它适用于你不知道具体要循环多少次，但知道循环的停止条件。
print("--- 5. while 循环 ---")

# a. 简单的计数器
count = 1
print("从1数到5:")
while count <= 5:
    print(f"  当前数字: {count}")
    count = count + 1 # 关键！让 count 增长，最终使条件不满足
print("数完了！")

# b. 模拟一个需要用户确认的场景
command = ""
print("\n输入 'quit' 退出程序:")
while command.lower() != "quit":
    command = input("> ") # 用户的输入会改变 command 的值
    print(f"  你输入了: {command}")
print("程序已退出。")
print("-" * 30)


# ===================================================
#        第三部分：循环控制 - 精准操控循环的节奏
# ===================================================

#### **1. `break`: 立即终止循环**

# `break` 语句会**立即、完全地**终止它所在的**最内层**循环，程序会跳到循环后面的代码继续执行。
# 
# **使用场景：** 通常用于“找到了就收工”的搜索场景。

print("--- 6. break 控制 ---")
numbers = [1, 5, 8, 13, 20, 25, 30]
print(f"在列表 {numbers} 中寻找第一个大于10的数。")

for num in numbers:
    print(f"  正在检查: {num}")
    if num > 10:
        print(f"  找到了！{num} 大于 10。")
        break # 找到后立即退出循环
print("搜索结束。")
print("-" * 30)






