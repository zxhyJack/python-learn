# 读取文件 

filename = '悯农.txt'
with open(filename) as file_object:
    print(file_object)
    lines = file_object.read()
    # print(lines)
    # print(file_object.read())
    # for line in file_object:
    #   print(line.rstrip())
poem = ''
for line in lines:
    # print(line.rstrip())
    poem += line.rstrip()

print(poem)
poem.replace('辛苦','hard')
print(poem.replace('辛苦','hard'))
