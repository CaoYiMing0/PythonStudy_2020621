file_read = open("readme")
file_write = open("readme复件2", "w")

while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)
file_read.close()
file_write.close()
