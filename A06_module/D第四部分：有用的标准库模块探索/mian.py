# Python “自带电池”的精髓就在于其强大的标准库。这里介绍几个你几乎肯定会用到的：
# 
# * **`os`**: 与操作系统交互。
  
import os
print(os.getcwd()) # 获取当前工作目录
if not os.path.exists("my_folder"):
    os.makedirs("A06_module/my_folder") # 创建文件夹

# * **`sys`**: 与 Python 解释器交互。

import sys
print(sys.argv) # 获取命令行参数

# * **`datetime`**: 处理日期和时间。

from datetime import datetime, timedelta
now = datetime.now()
print(f"现在: {now}")
yesterday = now - timedelta(days=1)
print(f"昨天: {yesterday}")
print(f"格式化输出: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# * **`json`**: 编码和解码 JSON 数据。

import json
# 字典 -> JSON 字符串
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data, indent=4) # indent 用于美化输出
print(json_string)
# JSON 字符串 -> 字典
parsed_data = json.loads(json_string)
print(parsed_data['name'])
