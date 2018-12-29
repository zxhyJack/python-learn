from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        # print(code, name)
        if name == country_name:
            return code
        # 如果没有找到指定的国家,就返回 None
    return None