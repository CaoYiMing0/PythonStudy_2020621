"""
在 终端/文件浏览器 中可以执行常规的 文件/目录 管理操作，例如：
    创建、重命名、删除、改变路径、查看目录内容......
在Python中，如果希望通过程序实现上述功能，需要导入os模块


文件操作
rename 重命名文件 os.rename(源文件名, 目标文件名)
remove 删除文件   os.remove(文件名)

目录操作
listdir 目录列表  os.listdir(目录名)
mkdir   创建目录  os.mkdir(目录名)
rmdir   删除目录  os.rmdir(目录名)
getcwd  获取当前目录  os.getcwd()
chdir   修改工作目录  os.chdir(目标目录)
path.isdir  判断是否是文件  os.path.isdir(文件路径)
"""
