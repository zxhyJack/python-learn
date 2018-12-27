# 字典、列表嵌套
aliens = []
for alien_num in range(30):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)
print(aliens)
print('total number of aliens is: ' + str(len(aliens)))

# 存储所点比萨的信息
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

print(pizza['crust'])

for topping in pizza['toppings']:
  print(topping)

# 在字典中存储字典
users = {
  'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
  },
  'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
  },
}

for username, user_info in users.items():
  print('username: ' + username)
  print('\tfullname: ' + user_info['first'] + ' ' +user_info['last'])
  print('\tlocation: ' + user_info['location'] + '\n')

# 6-8 宠物
pet1 = {'name':'dog', 'host': 'zhangsan'}
pet2 = {'name':'cat', 'host': 'lisi'}

pets = [pet1, pet2]
for pet in pets:
  print(pet)

pets = [{'name':'dog', 'host': 'zhangsan'},{'name':'cat', 'host': 'lisi'}]
print(pets)

# 6-9 喜欢的地方
favorite_places = {
  'Jack': ['Beijing', 'Nanjing', 'Xian'],
  'Rose': ['New York', 'Tokyo'],
  'Judy': ['Paris']
}

for name, places in favorite_places.items():
  print('\n' + name + '喜欢的城市有: ')
  for place in places:
    print(place)

# 6-11 城市
cities = {
  'Beijing':{
    'country': 'China',
    'population': 23000000,
    'fact': ''
  },
  'Nanjing':{
    'country': 'China',
    'population': 10000000,
    'fact': ''
  },
  'Jinan':{
    'country': 'China',
    'population': 7000000,
    'fact': ''
  },
}

for city,infos in cities.items():
  print(city)
  print('\tcountry: '+ infos['country'] )
  print('\tpopulation: ' + str(infos['population']))
  print('\tfact: '+infos['fact'] )
  # for name, info in infos.items():
  #   print(name)
  #   print(info)

dic = {
  'name': 'Jack',
  'age': 21
}

print(dic)
del dic['age']
print(dic)


nums = [1,2,3,4,5]
for num in nums:
  print(num)

# 九九乘法表
for i in range(1,10):
  for j in range(1,i+1):
    print(str(i) + '*' + str(j) + '=' + str(i*j) + '\t', end='')
  print()

