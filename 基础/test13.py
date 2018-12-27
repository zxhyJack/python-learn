# input
message = input('Tell me something, and I will repeat it back to you:')
print(message)

name = input('what is you firstname?')
print('\nhello ' + name)

# int()
age = input('How old are you?\n')
age = int(age)

if age >= 18:
    print('you are old enough')
else:
    print('you are young')

# 7-1 汽车租赁
input('Let me see if I can find you a Subaru')

# 7-2 餐馆订位
count = input('请问有几人用餐?')
count = int(count)

if count > 8:
    print('sorry, 没有空桌')
else:
    print('有空桌')

# 7-3 10 的整数倍
num = input('请输入数字:')
num = int(num)
if num % 10 == 0:
    print('yes')
else:
    print('no')
