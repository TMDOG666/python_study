# #### **2. `import` 语句的四种形态**
# 
# `import` 是你使用模块的钥匙。它有几种不同的用法，适用于不同的场景。
# #### **2. `import` 语句的四种形态**
# 
# `import` 是你使用模块的钥匙。它有几种不同的用法，适用于不同的场景。

"""
**形态一：`import module_name` (最常用)**

* **作用：** 导入整个模块。
* **使用方式：** `module_name.function_name` 或 `module_name.variable_name`。
* **优点：** 来源清晰，代码可读性强。你知道 `add` 函数是来自 `my_math` 模块的。
"""
import random
random_number = random.randint(1, 10)
print(f"调用了random模块，生成随机数{random_number}")

print("-" * 30)


"""
**形态二：`from module_name import name1, name2, ...`**

* **作用：** 只从模块中导入指定的变量、函数或类。
* **使用方式：** 直接使用 `name1`, `name2`。
* **优点：** 调用时更简洁，无需写模块名前缀。
* **缺点：** 如果导入了多个模块的同名函数，后导入的会覆盖先导入的，可能引起混淆。
"""
from my_math import add, PI
from datetime import datetime

sum_result = add(10, 20) # 直接调用 add
print(f"PI 的值是: {PI}")
print(f"现在的时间是: {datetime.now()}")

print("-" * 30)


"""
**形态三：`from module_name import *` (不推荐)**

* **作用：** 导入模块中所有不以下划线 `_` 开头的名称。
* **使用方式：** 直接使用所有导入的名称。
* **为什么不推荐？**

  1. **污染命名空间：** 你不知道到底导入了哪些东西，很容易与你自己定义的变量或函数产生冲突。
  2. **可读性差：** 看到一个函数调用时，你无法直观地判断它来自哪里。

  * **唯一例外：** 在一些设计为如此使用的库（如 `tkinter`）或在交互式解释器中为了方便可以偶尔使用。
*
"""
from math import *
print(sqrt(16)) # sqrt 来自哪里？不明确
print(pi)       # pi 来自哪里？不明确

print("-" * 30)

"""
**形态四：`import module_name as alias`**

* **作用：** 导入模块并给它起一个**别名 (alias)**。
* **使用方式：** `alias.function_name`。
* **优点：**
  1. 当模块名很长时，可以简化代码。
  2. 当不同模块有相同名称时，可以避免冲突。
  3. 遵循社区约定，提高代码可读性（例如数据科学领域）。
*
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 这是数据科学领域几乎雷打不动的标准别名
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})




