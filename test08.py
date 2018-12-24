# 使用列表中的一部分——切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# 遍历前三名运动员
for player in players[0:3]:
  print(player)

# 复制切片
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods.append('jiaozi')
friend_foods.insert(0, 'hotpot')
print(my_foods)
print(friend_foods)

# 4-10 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('The first three items in the list are:')
print(players[0:3])
print('Three items from the middle of the list are:')
print(players[1:4])
print('The last three items in the list are:')
print(players[-3:])
