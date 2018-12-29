import json
from country_code import get_country_code
from pygal_maps_world.maps import World

filename = 'data_version/population_data.json'
with open(filename) as f:
    data = json.load(f)
    # print(isinstance(data, list))

result = []
for item in data:
    if item['Year'] == '2010':
        country_name = item['Country Name']
        population = int(float(item['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ': '+str(population))
        else:
            print('ERROR - ' + country_name)

wm = World()
wm.title = 'North, Central, and South America'
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')