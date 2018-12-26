# 10-11 喜欢的数字
import json


def get_stored_number():
    filename = 'favoritenumber.json'
    try:
      with open(filename) as obj:
        favorite_number = json.load(obj)
    except FileNotFoundError:
      return None
    else:
      return favorite_number

def get_new_number():
    filename = 'favoritenumber.json'
    try:
      new_number = int(input('请输入你喜欢的数字：'))
    except ValueError:
      print('输入有误！')
    else:
      with open(filename, 'w') as file_obj:
          json.dump(new_number, file_obj)

favorite_num = get_stored_number()
if favorite_num:
  print('I know your favorite number,it is ' + str(favorite_num))
else:
  get_new_number()


