import test010
import test011

test010.say_hello()  # 我是 模块1
test011.say_hello()  # 我是 模块2
dog = test010.Dog()
print(dog)  # <test010.Dog object at 0x0000019DEDA52E08>

cat = test011.Cat()
print(cat)  # <test011.Cat object at 0x0000019DEDA52F08>
