
### 第四部分：更专门化的原生类型

#### 9. 字节序列 (bytes)

`bytes` 类型用来表示**二进制数据**，比如图片文件、视频文件或网络传输的原始数据。它和字符串很像，但是它包含的是字节（0-255之间的整数），而不是 Unicode 字符。

* **核心特性：**
  * **有序 (Ordered):** 和字符串一样，有索引。
  * **不可变 (Immutable):** 一旦创建，就不能修改。
  * **创建:** 通常通过对字符串进行编码 (`.encode()`) 或在字符串前加 `b` 前缀来创建。
* **主要用途：**
  * 处理二进制文件（以 'rb' 或 'wb' 模式读写）。
  * 网络编程中的数据传输。
  * 处理任何需要原始字节流的场景。

**详细代码示例：**

```python
print("--- 9. 字节序列 (bytes) ---")

# 通过编码字符串创建 bytes
str_data = "你好, Python"
bytes_data = str_data.encode('utf-8') # 使用 utf-8 编码
print(f"字符串: {str_data}")
print(f"编码后的 bytes: {bytes_data}")
print(f"bytes 的类型是: {type(bytes_data)}")

# 通过 b'' 前缀创建 (只能包含 ASCII 字符)
ascii_bytes = b'Hello, World'
print(f"ASCII bytes: {ascii_bytes}")

# 索引 bytes 对象返回的是整数 (0-255)
first_byte_value = ascii_bytes[0]
print(f"第一个字节的整数值: {first_byte_value}") # H 的 ASCII 值是 72

# 解码: 将 bytes 变回字符串
decoded_string = bytes_data.decode('utf-8')
print(f"解码后的字符串: {decoded_string}")

# 同样不可变
try:
    bytes_data[0] = 97 # 尝试修改
except TypeError as e:
    print(f"\n试图修改 bytes 会报错: {e}")

print("-" * 30)
```

---

#### 10. 字节数组 (bytearray)

`bytearray` 是 `bytes` 的**可变版本**。你可以把它想象成“字节列表”，可以随时修改、添加或删除其中的字节。

* **核心特性：**
  * **有序 (Ordered):** 同 `bytes`。
  * **可变 (Mutable):** 这是与 `bytes` 的核心区别。
* **主要用途：**
  * 需要对二进制数据进行原地修改的场景，例如在接收网络数据时构建一个缓冲区。

**详细代码示例：**

```python
print("--- 10. 字节数组 (bytearray) ---")

# 从 bytes 创建 bytearray
mutable_bytes = bytearray(b'hello')
print(f"初始 bytearray: {mutable_bytes}")

# 修改 (in-place modification)
mutable_bytes[0] = 72 # 72 是 'H' 的 ASCII 值
print(f"修改后: {mutable_bytes}")

# 添加字节
mutable_bytes.append(33) # 33 是 '!' 的 ASCII 值
print(f"添加 '!' 后: {mutable_bytes}")

# 可以像列表一样操作
print(f"现在的 bytearray: {mutable_bytes.decode('ascii')}") # 'Hello!'
print("-" * 30)
```

---

#### 11. 内存视图 (memoryview)

`memoryview` 是一种更高级的类型，它允许你在不复制内容的情况下，访问支持缓冲区协议的对象（如 `bytes` 和 `bytearray`）的内存。

* **核心特性：**
  * **零拷贝 (Zero-copy):** 创建一个 `memoryview` 不会复制底层数据，非常高效。
  * **切片:** 可以创建指向原始数据一部分的“视图”。
* **主要用途：**
  * 处理非常大的数据集时，避免因切片而产生不必要的内存拷贝，提升性能。

**详细代码示例：**

```python
print("--- 11. 内存视图 (memoryview) ---")

# 创建一个大的 bytearray
data = bytearray(b'This is a large piece of data')
print(f"原始数据: {data}")

# 创建一个指向 data 的 memoryview
view = memoryview(data)

# 创建一个指向 data 一部分的视图 (零拷贝)
part_view = view[10:15] # 指向 'large'
print(f"视图的一部分: {part_view.tobytes()}") # b'large'

# 修改视图会影响原始数据！
part_view[0] = ord('S') # ord() 获取字符的整数表示
print(f"修改视图后，原始数据变为: {data}") # 'This is a Sarge piece of data'
print("-" * 30)
```

---

#### 12. 不可变集合 (frozenset)

`frozenset` 是 `set` 类型的**不可变版本**。一旦创建，就不能再添加或删除元素。

* **核心特性：**
  * **无序 (Unordered):** 同 `set`。
  * **唯一 (Unique):** 同 `set`。
  * **不可变 (Immutable):** 这是与 `set` 的核心区别。
* **为什么需要它？**
  * 因为 `frozenset` 是不可变的，所以它可以作为**字典的键**或**集合中的元素**，而可变的 `set` 不行。

**详细代码示例：**

```python
print("--- 12. 不可变集合 (frozenset) ---")

# 创建 frozenset
frozen = frozenset([1, 2, 3, 2, 1])
print(f"不可变集合: {frozen}")

# 主要用途：作为字典的键
student_courses = {
    frozenset(["Math", "Physics"]): "Science Stream",
    frozenset(["History", "Literature"]): "Arts Stream"
}
my_courses = frozenset(["Physics", "Math"])
print(f"我的课程组合属于: {student_courses[my_courses]}")

# 尝试修改会报错
try:
    frozen.add(4)
except AttributeError as e:
    print(f"\n试图修改 frozenset 会报错: {e}")
print("-" * 30)
```

---

#### 13. 范围 (range)

`range` 类型表示一个不可变的**算术级数序列**。它非常节省内存，因为无论范围多大，它都只存储起始值、结束值和步长。

* **核心特性：**
  * **不可变 (Immutable):** 创建后无法修改。
  * **惰性求值 (Lazy):** 只有在需要时才生成序列中的数字。
* **主要用途：**
  * 在 `for` 循环中迭代指定的次数。

**详细代码示例：**

```python
print("--- 13. 范围 (range) ---")

# 创建 range 对象
my_range = range(0, 10, 2) # 从0开始，到10结束(不含10)，步长为2
print(f"range 对象: {my_range}")
print(f"range 的类型是: {type(my_range)}")

# range 对象非常节省内存
import sys
big_range = range(1000000)
big_list = list(big_range)
print(f"range 对象的内存大小: {sys.getsizeof(big_range)} 字节")
print(f"等效列表的内存大小: {sys.getsizeof(big_list)} 字节")

# 在 for 循环中使用
print("遍历 range 对象:")
for i in my_range:
    print(i, end=" ") # 输出: 0 2 4 6 8 
print("\n" + "-" * 30)
```

---

### 总结：Python 原生数据类型一览表

| 分类             | 类型           | 可变性         | 描述                   |
| :--------------- | :------------- | :------------- | :--------------------- |
| **文本**   | `str`        | 不可变         | Unicode 字符序列       |
| **数字**   | `int`        | 不可变         | 任意大小的整数         |
|                  | `float`      | 不可变         | 浮点数                 |
|                  | `complex`    | 不可变         | 复数                   |
|                  | `bool`       | 不可变         | `True` 或 `False`  |
| **序列**   | `list`       | **可变** | 有序、异构的元素列表   |
|                  | `tuple`      | 不可变         | 有序、异构的元素列表   |
|                  | `range`      | 不可变         | 算术级数序列           |
| **二进制** | `bytes`      | 不可变         | 字节序列               |
|                  | `bytearray`  | **可变** | 字节数组               |
|                  | `memoryview` | -              | 内存视图（零拷贝）     |
| **集合**   | `set`        | **可变** | 无序、不重复的元素集合 |
|                  | `frozenset`  | 不可变         | 无序、不重复的元素集合 |
| **映射**   | `dict`       | **可变** | 键值对集合             |
| **特殊**   | `NoneType`   | 不可变         | 代表空值 `None`      |

除此之外，像函数、类、模块等在 Python 中也都是对象，拥有自己的类型 (`function`, `type`, `module`)，这体现了 Python “一切皆对象” 的设计哲学。
