"""
translate()方法根据参数table给出的表（包含256个字符）转换字符串的字符，将要过滤
掉的字符放到del参数中。
语法如下：
    str.translate(table[,deletechars])
str代表要检索的字符串；table代表翻译表，翻译表通过maketrans方法转换而来；deletechars代表
字符串中要过滤的字符列表。返回结果为翻译后的字符串。
"""

intab = 'adfas'
outtab = '12345'
trantab = str.maketrans(intab, outtab)
st = 'just do it'
print(st.translate(trantab))  # ju5t 2o it
