'''
Created on 29 Nov 2013

@author: Oskar
'''
import unittest

template = """
xp:{xp}
hp:{hp}
name:{name}
"""
expected = """
xp:3
hp:10
name:foo
"""
class Test(unittest.TestCase):


    def testName(self):
        values = {
                  "name":"foo",
                  "xp": 3,
                  "hp": 10
                  }
        self.assertEqual(expected, template.format(**values))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()