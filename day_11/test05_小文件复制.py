file_read = open("readme")
file_write = open("readme复件", "w")

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()
