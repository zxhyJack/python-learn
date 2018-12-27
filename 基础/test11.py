# 字典

# 6-1 人 :使用一个字典来存储一个熟人的信息,包括名、姓、年龄和居住的城市。该字典应包含键 first_name 、 last_name 、 age 和 city 。
# 将存储在该字典中的每项信息都打印出来
user = {
  'first_name': 'Jack',
  'last_name': 'Smith',
  'age':21,
  'city':'Beijing',
}

print(user['first_name'])
print(user['last_name'])
print(user['age'])
print(user['city'])

# 6-2 喜欢的数字
favorite_nums = {
  'Jack':3,
  'Rose':5,
  'Lucy':4,
  'Judy':4,
  'Array':4,
}

# print(favorite_nums['Jack'])
# print(favorite_nums['Lucy'])
# print(favorite_nums['Rose'])

# 遍历所有的键 — 值对
for key, value in favorite_nums.items():
  print('\nkey:' + key)
  print('value:' + str(value))

# 遍历字典中的所有键
for name in favorite_nums.keys():
  print(name)

# 按顺序遍历字典中的所有键
for name in sorted(favorite_nums.keys()):
  print(name)

# 遍历字典中的所有值
for value in favorite_nums.values():
  print(value)

# 遍历字典中的所有值
for value in set(favorite_nums.values()):
  print(value)

# 6-5 河流
rivers = {
  'changjiang': 'China',
  'huanghe':'China',
  'yinduhe': 'India',
}

for river, country in rivers.items():
  print(river + ' runs through ' + country)
  print('river ' + river)
  print('country ' + country)
