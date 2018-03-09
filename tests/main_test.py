import unittest
import sys 

sys.path.append('../src') 
from app.main import *
class Test(unittest.TestCase):
     
    def test_apply_function(self):
        #testing to see if the correct lights turn on when told to switch
        test1 = lightTester(5)
        test1.apply(["switch", 0, 0, 1, 1])
        self.assertTrue(test1.lights[0][1] == 1)
        
        #testing to see if the correct lights are left on when a range of lights is told to turn off
        test2 = lightTester(3)
        test2.apply(['turn off', 0, 2, 0 ,2])
        self.assertTrue(test2.lights[0][2] == 0)
        
        #testing to see if the correct lights are turned on when a range of lights is told to turn on
        test3 = lightTester(9)
        test3.apply(["turn on", 0, 0, 2, 2])
        self.assertTrue(test3.lights[0][1] == 1)

    def test_count_functions(self):
        #testing that the count is correct for a specified number of lights
        test4 = lightTester(2)
        test4.apply(['turn on', 0, 0, 1, 1])
        self.assertTrue(test4.count() == 4)
        
        #testing that the count is correct for a specified number of lights 
        test5 = lightTester(3)
        test5.apply(['switch', 0, 0, 2, 2])
        self.assertTrue(test5.count() == 9)
        
        #testing that the count is correct for a specified number of lights 
        test6 = lightTester(5)
        test6.apply(['turn off', 0, 0, 4, 4])
        self.assertTrue(test6.count() == 0)
        
if __name__== '__main__':
    unittest.main()
    
