"""
eval()函数十分强大 -- 将字符串当成有效的表达式来求值并返回计算记过
"""

print(eval("1+1"))  # 2
print(eval("'*'*10"))  # **********
print(type(eval("[1,2,3,4]")))  # <class 'list'>
print(type(eval("{'卢本伟','无情哈拉少','带篮子'}")))  # <class 'set'>
