# 在while循环中使用else子句
num = 0
while num < 3:
    print(num, '小于3')
    num = num + 1
else:
    print(num, '大于或等于3')
print("结束循环")
"""
1 小于3
2 小于3
3 大于或等于3
结束循环
"""

# 在for循环中使用else语句
names = ['小鸟伏特加', '猫灯伏特加']
for name in names:
    if name == "俄罗果":
        print("名称：", name)
        break
    print("循环名称列表" + name)
else:
    print("没有循环数据！")
print("结束循环！")
"""
循环名称列表猫灯伏特加
没有循环数据！
结束循环！
"""