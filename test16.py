# 第 8 章 函数

# 8-1 消息


def display_message():
    print('第八章 函数')


display_message()

# 8-2 喜欢的图书


def favorite_books(title):
    '''喜欢的图书'''
    """喜欢的图书"""
    print('one of my favorite books is ' + title)


favorite_books('artist of love')

# 8-3 T 恤


def make_shirt(size, typeface):
    print('size:' + size)
    print('typeface:' + typeface)


make_shirt('M', 'python')
make_shirt(size='L', typeface='hello world')
make_shirt(typeface='nodejs', size='XL')

# 8-4 大号T恤


def make_shirt1(size='L', typeface='I Love Python'):
    print('size:' + size)
    print('typeface:' + typeface)


make_shirt1()
make_shirt1(size='M')
make_shirt1(typeface='Hello World')

# 8-5 city


def describe_city(city, country='China'):
    print(city + 'is in ' + country)


describe_city('Beijing')
describe_city('Shanghai')
describe_city('London', 'England')

# 8-6 城市名


def city_country(city, country):
    print((city+', '+country).title())


city_country('beijing', 'china')
city_country(city='london', country='england')

# 8-7 专辑


def make_album(singer, album_name, amount=''):
    album = {'singer': singer.title(), 'album_name': album_name.title()}
    if amount:
        album['amount'] = amount
    return album


make_album('Jay', 'qinghuaci')
make_album('Eason', 'ten years', 3)


# 8-8 用户的专辑
while True:
    album = ''
    print('q 退出')
    singer = input('singer: ')
    if singer == 'q':
        break
    album_name = input('album_name: ')
    if album_name == 'q':
        break
    haveAmount = input('是否输入数量?(yes/no)')
    if haveAmount == 'q':
        break
    if haveAmount == 'yes':
        amount = input('amount: ')
        if amount == 'q':
            break
        album = make_album(singer, album_name, amount)
    else:
        album = make_album(singer, album_name)
    print(album)

# 8-9 魔术师


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ['a', 'b', 'c']
show_magicians(magicians)

# 了不起的魔术师


def make_great(magicians):
    result = []
    for magician in magicians:
        result.append('the Great ' + magician)
    return result


show_magicians(make_great(magicians))
show_magicians(magicians)

# 8-12 三明治


def make_sanwiches(*toppings):
    for topping in toppings:
        print('食材有：' + topping)


make_sanwiches('mushrooms', 'green peppers', 'extra cheese')


# 8-13 用户简介
def build_profile(name, **user_info):
    user = {'name': name}
    for k, v in user_info.items():
        user[k] = v
    return user
 
user = build_profile('Jack', phone = 110, location = 'China', hobby = 'basketball')

print(user)


