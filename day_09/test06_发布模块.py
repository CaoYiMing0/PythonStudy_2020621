"""
发布模块
    如果希望自己开发的模块，分享给其他人，可以按照以下步骤操作



1.制作发布压缩包的步骤

1) 创建setup.py文件
from distutils.core import setup
setup(name="message",  # 包名
      version="1.0",  # 版本
      description="发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="cym",  # 作者
      author_email="cym@qq.com",  # 作者邮箱
      url="www.hpu.edu.cn",  # 主页
      py_modules=["message.send_message",
                  "message.receive_message"])

2) 构建模块（命令中）
    $ python3 setup.py build

3) 生成发布压缩包
    $ python3 setup.py sdist


2.安装模块
    $ tar -zxvf message-1.0.tar.gz
    $ sudo python3 setup.py install

3.卸载模块
    $ cd /usr/local/lib/python3.5/dist-packages/
    $ sudo rm -r message*
"""
