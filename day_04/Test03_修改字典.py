dict = {'卢本伟': '1001', '五五开': '1002', 'white': '1003'}
dict['white'] = '1005'
print(dict['white'])  # 1005
print('%(white)s' % dict)  # 1005
# 添加一个
dict['赌怪'] = '5000000'
print('%(赌怪)s' % dict)  # 5000000
