print('hello' * 5)  # hellohellohellohellohello
print([7] * 10)  # [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
# 可以向上面这样乘以一个想要得到的序列，从而得到想要的重复序列


# 想得到占用10个元素的空列表，但里面却不包括任何内容，怎么做呢？
sq = [None] * 5  # None是Python的内建值，确切含义是“这里什么也没有”
print(sq)  # [None, None, None, None, None]
