"""
replace()方法把字符串中的old（旧字符串）替换成new（新字符串），
如果指定第3个参数max，替换次数就不超过max次
用法如下：
    str.replace(old,new[,max]
str代表指定检索的字符串；old代表将被替换的子字符串；new代表新字符串，用于替换old子字符串;
max代表替换次数不超过max次
"""

field = 'do it now,do right now'
print(field.replace('do', 'Just do'))  # Just do it now,Just do right now
print(field.replace('o', 'Just', 1))  # dJust it now,do right now
print(field.replace('o', 'Just', 2))  # dJust it nJustw,do right now
print(field.replace('o', 'Just', 3))  # dJust it nJustw,dJust right now
