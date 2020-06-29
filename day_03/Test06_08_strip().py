"""
strip()方法用于移除字符串头尾指定的字符（默认为空格）。
方法如下：
    str.strip([chars])
str代表指定检索的字符串，chars代表移除字符串头尾指定的字符。返回结果为移
除字符串头尾指定的字符生成的新字符串
"""

field = '----do it now----'
print(field.strip('-'))  # do it now
st = '----do--it--now----'
print(st.strip('-'))  # do--it--now
