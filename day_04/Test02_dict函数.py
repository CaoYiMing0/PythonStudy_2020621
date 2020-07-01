# 可以使用dict函数，通过其他映射（如其他字典）或键/值序列对建立字典

student = [('name', '卢本伟'), ('number', '1001')]
detail = dict(student)
print(detail)  # {'name': '卢本伟', 'number': '1001'}
print(detail['name'])  # 卢本伟
print(detail['number'])  # 1001

# dict函数还可以通过关键字参数创建字典
detail = dict(name='卢本伟', number='1002')
print(detail)  # {'name': '卢本伟', 'number': '1002'}
