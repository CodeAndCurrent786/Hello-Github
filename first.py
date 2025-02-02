"""Objects and Data structures ()"""
import math
a = "Hello World"
mylist = [1, 6, 2, 3, 4, 5]
nums = [-1, -2,-3]
mydict = {'key1' : 'Hello','key2' : 'value1', 'key3' : 'good'}
tupple = (1, 'list', 2, 3, 4, 5)        # immutable
myfile = open(r"C:\Users\Computer\Desktop\python\python\Complete-Python-3-Bootcamp-master\00-Python Object and Data Structure Basics\test.txt")
st = 'Print only the words that start with s in this sentence'

class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first = first_name
        self.last = last_name
        self.email = f"{self.first}.{self.last}@company.com"
        self.pay = pay
    def greet(self):
        greeting = f"My full name is {self.first+' '+self.last}. My email address is {self.email} and I earn {self.pay} per month."
        return greeting


