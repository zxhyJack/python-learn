# 10-6 加法运算
while True:
    str1 = input('请输入数字: ')
    str2 = input('请输入数字: ')
    try:
        print(int(str1)+int(str2))
    except ValueError:
        # print(TypeError)
        pass
        # print('请输入数字！')

line = "Row, row, row your boat"
line.count('row')
line.lower().count('row')
