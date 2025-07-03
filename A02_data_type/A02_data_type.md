
### 第一部分：基本类型

这些是构成程序信息的最基本单位。

#### 1. 字符串 (String, `str`)

字符串就是文本。所有用单引号 `' '`、双引号 `" "` 或三引号 `''' '''` 包围起来的内容都是字符串。

* **核心特性：**
  * **有序 (Ordered):** 字符串中的每个字符都有一个固定的位置（索引），从 `0` 开始。
  * **不可变 (Immutable):** 一旦创建，字符串的内容就不能被修改。任何对字符串的修改操作（如替换）都会创建一个*新*的字符串。
* **常用操作：**
  * **索引和切片：** 访问单个或部分字符。
  * **拼接和重复：** 使用 `+` 和 `*`。
  * **常用方法：** `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.find()` 等。
  * **长度：** 使用 `len()` 函数。

**详细代码示例：**

```python
print("--- 1. 字符串 (str) ---")

# 创建字符串
my_string = "  Hello, Python!  "
another_string = '学习Python很有趣'
print(f"原始字符串: '{my_string}'")

# 1. 索引 (Indexing) - 访问单个字符 (从0开始)
first_char = my_string[2] # 第一个非空格字符是 'H'
last_char = another_string[-1] # -1 代表最后一个字符
print(f"索引[2]的字符是: '{first_char}'")
print(f"最后一个字符是: '{last_char}'")

# 2. 切片 (Slicing) - 截取一部分字符串
# 格式: [start:stop:step], stop位置的字符不被包含
substring = my_string[2:7] # 从索引2到6 (Hello)
print(f"切片[2:7]的结果: '{substring}'")

# 3. 拼接与重复
full_sentence = another_string + " Let's go!"
repeated_word = "Go! " * 3
print(f"拼接后的句子: {full_sentence}")
print(f"重复3次的结果: {repeated_word}")

# 4. 常用方法 (方法不会改变原始字符串, 而是返回新的)
upper_case = my_string.upper() # 全部转为大写
lower_case = my_string.lower() # 全部转为小写
stripped_string = my_string.strip() # 去掉两边的空格
replaced_string = my_string.strip().replace("Python", "World") # 替换
word_list = replaced_string.split(", ") # 按 ", " 分割成列表

print(f"转为大写: '{upper_case}'")
print(f"转为小写: '{lower_case}'")
print(f"去掉两边空格后: '{stripped_string}'")
print(f"替换'Python'后: '{replaced_string}'")
print(f"分割后的列表: {word_list}")

# 5. 长度
length = len(stripped_string)
print(f"'{stripped_string}' 的长度是: {length}")

# 6. 检查不可变性
try:
    my_string[2] = 'h' # 尝试修改第一个字符
except TypeError as e:
    print(f"\n试图修改字符串会报错: {e}")

print("-" * 30)
```

---

#### 2. 数字 (Number): 整数 (`int`) 和 浮点数 (`float`)

* **整数 (`int`):** 就是没有小数点的数字，可以是正数、负数或零。
* **浮点数 (`float`):** 就是带小数点的数字。
* **核心特性：**

  * **可变 (Mutable):** 严格来说数字本身不可变，但赋予变量新值看起来就像是可变的。
  * **运算：** 支持所有标准的数学运算。
* **常用操作：**

  * 加 `+`, 减 `-`, 乘 `*`, 除 `/`
  * 整除 `//` (结果向下取整)
  * 取余 `%` (模运算)
  * 乘方 `**`

**详细代码示例：**

```python
print("--- 2. 数字 (int, float) ---")

# 整数 (int)
a = 10
b = 3

# 浮点数 (float)
pi = 3.14
c = 10.0 # 只要带小数点就是浮点数

print(f"a = {a}, b = {b}, pi = {pi}")

# 数学运算
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}") # 除法结果总是浮点数
print(f"a // b = {a // b}") # 整除，结果是3
print(f"a % b = {a % b}") # 取余，10除以3余1
print(f"b ** 2 = {b ** 2}") # 3的2次方

# 类型转换
num_str = "123"
num_int = int(num_str) # 字符串转整数
print(f"从字符串'{num_str}'转换来的整数: {num_int}")

float_from_int = float(a) # 整数转浮点数
print(f"从整数{a}转换来的浮点数: {float_from_int}")
print("-" * 30)
```

---

#### 3. 布尔值 (Boolean, `bool`)

布尔值是用来表示“真”或“假”的。它只有两个值：`True` 和 `False`。

* **核心特性：**
  * 是所有逻辑判断的基础。
  * 通常是比较运算 (`==`, `!=`, `>`, `<`) 的结果。
* **常用操作：**
  * 逻辑与 `and`: 两者都为 `True` 时，结果才为 `True`。
  * 逻辑或 `or`: 只要有一个为 `True`，结果就为 `True`。
  * 逻辑非 `not`:颠倒布尔值 (`not True` 结果是 `False`)。

**详细代码示例：**

```python
print("--- 3. 布尔值 (bool) ---")

is_learning = True
is_tired = False

print(f"我在学习吗? {is_learning}")
print(f"我累了吗? {is_tired}")

# 比较运算产生布尔值
age = 20
print(f"年龄 > 18 吗? {age > 18}") # True
print(f"年龄 == 20 吗? {age == 20}") # True

# 逻辑运算
# 场景: 只有在学习并且不累的时候，才会感到快乐
is_happy = is_learning and not is_tired
print(f"我快乐吗? {is_happy}")

# 场景: 只要在学习，或者没在睡觉，我就醒着
is_sleeping = False
is_awake = is_learning or not is_sleeping
print(f"我醒着吗? {is_awake}")

# 在 if 语句中的应用 (预告)
if is_happy:
    print("太棒了，继续保持！")
else:
    print("需要休息一下吗？")
print("-" * 30)
```

---

### 第二部分：容器类型

容器用来存放多个数据项。

#### 4. 列表 (List, `list`)

列表是最常用、最灵活的容器，像一个可以随时增删物品的购物清单。

* **核心特性：**
  * **有序 (Ordered):** 元素按插入顺序排列，有索引。
  * **可变 (Mutable):** 可以随时添加、删除或修改其中的元素。
  * **可重复:** 可以包含重复的元素。
  * **异构性:** 可以包含不同数据类型的元素。
* **常用操作：**
  * **增:** `.append()`, `.insert()`
  * **删:** `.remove()`, `.pop()`, `del`
  * **改:** 通过索引赋值 `my_list[i] = new_value`
  * **查:** 索引、切片、`in` 关键字

**详细代码示例：**

```python
print("--- 4. 列表 (list) ---")

# 创建列表
fruits = ["apple", "banana", "cherry"]
print(f"初始列表: {fruits}")

# 1. 查 (Access)
first_fruit = fruits[0]
print(f"第一个水果是: {first_fruit}")

# 2. 改 (Modify)
fruits[1] = "blackberry"
print(f"修改后: {fruits}")

# 3. 增 (Add)
fruits.append("orange") # 在末尾添加
print(f"append 'orange' 后: {fruits}")
fruits.insert(1, "grape") # 在索引1的位置插入
print(f"insert 'grape' 后: {fruits}")

# 4. 删 (Delete)
fruits.remove("apple") # 删除指定的第一个元素
print(f"remove 'apple' 后: {fruits}")
popped_fruit = fruits.pop(2) # 删除索引2的元素并返回它
print(f"pop 索引2的元素 '{popped_fruit}' 后: {fruits}")
del fruits[0] # 使用del删除索引0的元素
print(f"del 索引0的元素后: {fruits}")

# 5. 其他
print(f"列表长度: {len(fruits)}")
print(f"'orange' 在列表中吗? {'orange' in fruits}")
print("-" * 30)
```

---

#### 5. 元组 (Tuple, `tuple`)

元组可以看作是“不可变的列表”。一旦创建，就不能再修改。

* **核心特性：**
  * **有序 (Ordered):** 同列表。
  * **不可变 (Immutable):** 创建后不能增、删、改。这是与列表最核心的区别。
* **为什么需要元组？**
  * **安全:** 传递的数据不希望被修改时使用。
  * **性能:** 通常比列表稍快。
  * **作为字典的键:** 因为不可变，元组可以作为字典的键，而列表不行。

**详细代码示例：**

```python
print("--- 5. 元组 (tuple) ---")

# 创建元组 (使用圆括号)
coordinates = (10.0, 20.5)
# 注意: 创建只含一个元素的元组，必须加逗号
single_tuple = (1,) 

print(f"坐标元组: {coordinates}")
print(f"单个元素的元组: {single_tuple}")

# 1. 查 (Access) - 和列表一样
x = coordinates[0]
y = coordinates[1]
print(f"X坐标: {x}, Y坐标: {y}")

# 2. 检查不可变性
try:
    coordinates[0] = 15.0 # 尝试修改
except TypeError as e:
    print(f"\n试图修改元组会报错: {e}")

# 元组可以包含不同类型
person_info = ("John", 25, "Engineer")
print(f"个人信息元组: {person_info}")
print("-" * 30)
```

---

#### 6. 字典 (Dictionary, `dict`)

字典是无序的键值对 (`key: value`) 集合，非常适合用来存储结构化信息。就像一本真正的字典，通过“词”（key）来查找“释义”（value）。

* **核心特性：**
  * **键值对:** 以 `key: value` 形式存储。
  * **键唯一且不可变:** `key` 必须是唯一的，且必须是不可变类型（如字符串、数字、元组）。
  * **值任意:** `value` 可以是任何数据类型，也可以重复。
  * **可变 (Mutable):** 可以随时增、删、改键值对。
  * **有序 (Python 3.7+):** 在较新版本的 Python 中，字典会保持插入顺序，但最好不要依赖此特性来编写逻辑。

**详细代码示例：**

```python
print("--- 6. 字典 (dict) ---")

# 创建字典
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science",
    "courses": ["Math", "Programming", "History"]
}
print(f"初始字典: {student}")

# 1. 查 (Access)
student_name = student["name"]
print(f"学生姓名: {student_name}")
# 更安全的访问方式: .get()，如果键不存在不会报错，而是返回None
student_grade = student.get("grade") 
print(f"学生的年级: {student_grade}") # 输出 None

# 2. 改/增 (Modify/Add)
student["age"] = 22 # 修改已存在的键
student["grade"] = "Senior" # 添加新的键值对
print(f"修改年龄、添加年级后: {student}")

# 3. 删 (Delete)
del student["major"]
print(f"删除专业后: {student}")

# 4. 常用方法
keys = student.keys()
values = student.values()
items = student.items() # 获取所有键值对
print(f"所有键: {keys}")
print(f"所有值: {values}")
print(f"所有项: {items}")
print("-" * 30)
```

---

#### 7. 集合 (Set, `set`)

集合是一个无序且不含重复元素的容器。主要用于去重和数学中的集合运算。

* **核心特性：**
  * **无序 (Unordered):** 没有索引，不能通过位置访问。
  * **唯一 (Unique):** 自动去除重复元素。
  * **可变 (Mutable):** 可以添加或删除元素。
* **常用操作：**
  * **去重**
  * **集合运算:** 交集 (`&`)、并集 (`|`)、差集 (`-`)、对称差集 (`^`)。

**详细代码示例：**

```python
print("--- 7. 集合 (set) ---")

# 创建集合
numbers = {1, 2, 3, 4, 4, 5, 5} # 重复的元素会被自动去掉
print(f"初始集合 (自动去重): {numbers}")

# 1. 增/删
numbers.add(6)
print(f"添加6后: {numbers}")
numbers.remove(3) # 如果元素不存在会报错
numbers.discard(10) # 如果元素不存在不会报错
print(f"删除3后: {numbers}")

# 2. 集合运算
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"\n集合A: {set_a}")
print(f"集合B: {set_b}")

# 并集 (Union): 所有出现在A或B中的元素
print(f"并集 (A | B): {set_a | set_b}")
# 交集 (Intersection): 同时出现在A和B中的元素
print(f"交集 (A & B): {set_a & set_b}")
# 差集 (Difference): 出现在A中但不在B中的元素
print(f"差集 (A - B): {set_a - set_b}")
# 对称差集 (Symmetric Difference): 只出现在A或B中，但不同时在两者中的元素
print(f"对称差集 (A ^ B): {set_a ^ set_b}")
print("-" * 30)
```

---

### 第三部分：特殊类型

#### 8. 空值 (NoneType, `None`)

`None` 是一个特殊的值，代表“什么都没有”或“空”。

* **核心特性：**
  * 它是一种独立的类型 `NoneType`。
  * 全宇宙只有一个 `None`。
  * 常用于函数默认返回值或作为变量的初始占位符。

**详细代码示例：**

```python
print("--- 8. 空值 (None) ---")

# 定义一个没有初始值的变量
winner = None
print(f"获胜者是: {winner}, 类型是: {type(winner)}")

# 函数如果没有明确的 return 语句，默认返回 None
def do_nothing():
    pass

result = do_nothing()
print(f"do_nothing() 函数的返回值是: {result}")

# 检查一个变量是否是 None
if winner is None:
    print("比赛尚未决出胜负。")
print("-" * 30)
```

希望这份超级详细的讲解和示例能帮你彻底搞懂 Python 的数据类型！建议你把这些代码都亲手敲一遍，试着修改它们，看看会发生什么，这样印象会更深刻。
