import json
from country_code import get_country_code
from pygal_maps_world.maps import World

filename = 'data_version/population_data.json'
with open(filename) as f:
    data = json.load(f)
    # print(isinstance(data, list))

cc_population = {}
for item in data:
    if item['Year'] == '2010':
        country_name = item['Country Name']
        population = int(float(item['Value']))
        code = get_country_code(country_name)
        if code:
           cc_population[code] = population
        

wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010',cc_population)

wm.render_to_file('world_population.svg')