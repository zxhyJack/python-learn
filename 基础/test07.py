# range()函数生成一系列数字
for value in range(1,5):
  print(value)

# list()函数将range()生成的数字转化为list
nums = list(range(1,5))
print(nums)

# 创建一个列表,其中包含前 10 个整数(即 1~10 )的平方
squares = []
for value in range(1,11):
  squares.append(value**2)
print(squares)

# list中的最大值、最小值和总和
nums = list(range(1,11))
print(max(nums))
print(min(nums))
print(sum(nums))

# 列表解析
squares = [value ** 2 for value in range(1,11)]
print(squares)

# 4-3 数到 20 :使用一个 for 循环打印数字 1~20 (含)
for value in range(1,21):
  print(value)

# 4-4 一百万
for value in range(1,1000001):
  print(value)
  
# 4-5 计算 1~1 000 000 的总和
nums = list(range(1,1000001))
print(max(nums))
print(min(nums))
print(sum(nums))

# 4-6 奇数
even_nums = list(range(1,21,2))
print(even_nums)

# 4-7 3 的倍数
three_nums = list(range(3,31,3))
for value in three_nums:
  print(value)

# 4-8 立方
cubes = []
for value in list(range(1,11)):
  cubes.append(value**3)
for cube in cubes:
  print(cube)

# 4-9 立方解析
cubes = [value ** 3 for value in list(range(1,11))]
for cube in cubes:
  print(cube)
