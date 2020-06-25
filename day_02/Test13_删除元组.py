# 元组中的元素值不允许删除，但可以使用del语句删除整个元组
field = ('hello', 'world')
del field
print(field)  # 错误：NameError: name 'field' is not defined
