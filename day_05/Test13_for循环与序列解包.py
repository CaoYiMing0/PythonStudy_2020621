# for循环的一大好处是可以在循环中使用序列解包
tups = {'卢本伟': '1001', '五五开': '1002', 'white': '1003'}
for key, value in tups.items():
    print('%s:%s' % (key, value))
"""
卢本伟:1001
五五开:1002
white:1003
"""