guests = ['Jack','Rose','Lucy']

print(guests)
# 有嘉宾无法赴约，另外邀请以为
print('Lucy can not attend the party')
guests.remove('Lucy')
guests.append('Judy')
print(guests)

# 3-6 更大的餐桌
guests.insert(0,'James')
guests.insert(2,'Bill')
guests.append('Kobe')
print(guests)

# 3-7 缩减名单
while(len(guests)>2):
  
  print(guests.pop() + ', sorry')

print(guests)

del guests[0]
del guests[0]
print(guests)
