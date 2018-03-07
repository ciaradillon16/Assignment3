import unittest
import sys 

sys.path.append('../src') 

from app.main import *

class Test(unittest.TestCase):

    def turnOn(self):
        myObject = lightTester(5)
        myObject.apply(['switch', '296', '687', '906', '775'])
        self.assertEqual(myObject.count(), -4, 'Failed: Count incorrect')


