from day_09 import Test010
from day_09 import Test011

Test010.say_hello()  # 我是 模块1
Test011.say_hello()  # 我是 模块2

dog = Test010.Dog()
print(dog)

cat = Test011.Cat()
print(cat)
