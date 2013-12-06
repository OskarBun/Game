'''
Created on 26 Nov 2013

@author: Oskar
'''
import unittest

class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self._age = 0
        self.age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 15:
            raise Exception('too young')
        self._age = value
    
    def get_name(self):
        return "poo:{}".format(self.__name)


    def set_name(self, value):
        self.__name = value


    def del_name(self):
        del self.__name

    name = property(get_name, set_name, del_name, "name's docstring")
    

class Test(unittest.TestCase):


    def testName(self):
        o = Foo("oskar", 19)
        o.age = 14
        print(o.name, o.age)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()