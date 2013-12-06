'''
Created on 25 Nov 2013

@author: Oskar
'''
import unittest
from oskar.room import Room


class Test(unittest.TestCase):


    def setUp(self):
        self.room = Room('foo')
        self.room.add_connection(Room('bar'))


    def testGetRoomByName(self):
        door = self.room.exits[0]
        bar = door.i_go(self.room)
        self.assertEquals(bar.name,'bar')
        self.assertEquals(self.room.get_exit_by_name('bar'),door)
        self.assertEquals(bar.get_exit_by_name('foo'),door)
        self.assertIsNone(self.room.get_exit_by_name('foo bar'), 'should not have found room')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()