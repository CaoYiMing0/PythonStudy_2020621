"""
readline方法可以一次读取一行内容
方法执行后，会把文件指针移动到下一行，准备再次读取
"""

file = open("readme")
text = file.readline()
print(text)
file.close()

# 改造一下
file = open("readme")
while True:
    text = file.readline()

    # 判断是否读取到内容
    if not text:
        break
    print(text)
file.close()
