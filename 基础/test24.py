# unit test Employee
import unittest


class Employee():
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def give_raise(self, salary=5000):
        self.salary += salary


class EmployeeUnitTest(unittest.TestCase):
    '''unit test Employee'''

    def setUp(self):
        self.employee = Employee('Jack', 'Smith', 10000)

    def test_get_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 15000)

    def test_get_custom_raise(self):
        self.employee.give_raise(8000)

        self.assertEqual(self.employee.salary, 18000)

unittest.main()