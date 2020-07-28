# 打开文件
file = open("readme")
# 读取文件
text = file.read()
print(text)  # hello
print('*' * 50)  # **************************************************
text = file.read()  # 没有任何输出，此时文件指针到达文件内容末尾
print(text)
# 关闭文件
file.close()
