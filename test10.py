# if
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
  if 'bmw'==car:
    print(car.upper())
  else:
    print(car)

age = 16
if age > 18:
  print('you are old enough to vote!')
else: 
  print('you are not old enough!')

# 4 岁以下免费;
# 4~18 岁收费 5 美元;
# 18 岁(含)以上收费 10 美元
age = 21
cost = 0
if age <4:
  cost = 0
elif age >=4 and age <18:
  cost = 5
elif age >=18:
  cost = 10
print(cost)





