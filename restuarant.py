class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name + ' 是 ' + self.type)

    def open_reataurant(self):
        print('the restaurant is opening')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, num):
        self.number_served += num
