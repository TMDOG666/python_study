# pip install requests
# pip install pandas

import requests

try:
    response = requests.get("https://www.python.org")
    response.raise_for_status() # 如果请求失败 (如404), 会抛出异常
    print("成功获取 Python 官网内容！")
    print(f"内容的前150个字符: {response.text[:150]}")
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")