# 7.3  使用 while 循环来处理列表和字典
unconfirmed_users = ['Jack', 'Bob', 'Bill']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    # print(current_user)
    confirmed_users.append(current_user)

print('the following users are confirmed:')
for user in confirmed_users:
    print(user)

# 7.3.2  删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'dog' in pets:
    pets.remove('dog')
print(pets)

# 7.3.3  使用用户输入来填充字典
user = {}

flag = True
while flag:
    name = input('please input you name: ')
    age = input('please input you age: ')
    user[name] = age
    if input('would you like to add another person?') == 'no':
        flag = False

print(user)
for k, v in user.items():
    print(k)
    print(v)

# 7-8 熟食店
sandwich_orders = ['a', 'b', 'c']
finished_sandwiches = []
while sandwich_orders:
    current = sandwich_orders.pop()
    print(current + 'I made your tuna sandwich')
    finished_sandwiches.insert(0, current)

for finished in finished_sandwiches:
    print(finished)

# 7-9 五香烟熏牛肉( pastrami )卖完了
sandwich_orders = ['a', 'pastrami', 'b', 'pastrami', 'c', 'pastrami']
print('pastrami has sold out')
while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')
print(sandwich_orders)

# 7-10 梦想的度假胜地
user = {}
flag = True
while flag:
  name = input('what is you name? ')
  place = input('If you could visit one place in the world, where would you go? ')
  user[name] = place
  if input('would you like to let another person respond?').lower() == 'no':
    flag = False

print(user)



