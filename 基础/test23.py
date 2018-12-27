# unit test
import unittest


def city_country(city, country, population=''):
    '''format city country'''
    format_info = (city+', '+country).title()
    if population:
        format_info += ' - population ' + str(population)
    print(format_info)
    return format_info


class NameUnitTest(unittest.TestCase):
    '''test city_country()'''

    def test_city_country(self):
        new_name = city_country('beijing', 'china', 2300)
        # print(new_name)
        self.assertEqual(new_name, 'Beijing, China')


unittest.main()
