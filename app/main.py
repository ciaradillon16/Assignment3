# Importing all required packages to run this code
import requests
import re
import sys
import os 
        
class lightTester:
    """ This class applies the commands 'turn on', 'turn off' and 'switch' to an LED lightboard
    of any size. It turns on the lights in coordinate pairs. The count function then counts how many
    lights are on and returns that value""" 
    
    lights = None
   
    
    def __init__(self, N):
        """Constructor - initializing lights and the size of the board and setting all lights to off"""
        self.N = N
        self.lights = [[False]*N for _ in range(N)]
     
  
    def size(self, number):
        """Function to account for coordinates outside the range of N""" 
        if number < 0:
            return 0
        if number > self.N:
            return self.N-1
        else:
            return number
                         
    def apply(self, array):
        """Applies one of the three commands to a selection of lights as read in by the program""" 
        self.array = array
        cmd = array[0]
        
        #Below I extract the necessary data and store them in variables to be used
        x = self.size(int(array[1])) 
        y = self.size(int(array[2]))
        x1 = self.size(int(array[3]))
        y1 = self.size(int(array[4]))
    
        for i in range(min(y, y1), max(y, y1)+1):
            for j in range(min(x, x1), max(x, x1)+1):
                    
                if cmd == 'turn off' or cmd == 'turn off ':
                    self.lights[i][j] = False           
            
                elif cmd == 'turn on' or cmd == 'turn on ':
                    self.lights[i][j] = True  
            
                elif cmd == 'switch' or cmd == 'switch ':
                    self.lights[i][j] = not self.lights[i][j]
                else:
                    continue
            
        return self.lights
                 
    def count(self):
        """This function counts the number of files that are turned on once the apply function has been
        carried out""" 
        count = 0
        for i in range (self.N):
            for j in range (self.N): 
                if self.lights[i][j]:
                    count += 1         
        return count
    
def parse_file():
    """This function reads in a web address and parse the text from it to be used by the lightTester
    class""" 
    #Setting up console script
    command = sys.argv[1] #Required for console script '--input' 
    instructions = sys.argv[2]
    
    #Regex to pull appropriate data from the files
    pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")

    # Case for parsing URLs 
    if instructions.startswith("http://"):
        r = requests.get(instructions)
        file = r.text.split('\n')
        N = file[0]
        mylight = lightTester(int(N))
        
        for line in file:  
            m = pat.match(line)
            if m:
                array = [m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)]
                mylight.apply(array)
        print(mylight.count())
     
    # Case for parsing local files 
    else: 
        fh1= open(instructions, 'r').readlines()       
        if os.path.isfile(instructions):
            for line in fh1[:1]:
                N = int(line)
                mylight = lightTester(N)
        
        for line in fh1:
            m = pat.match(line)
            if m:
                array = [m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)]
                mylight.apply(array)
        print(mylight.count())
    
if __name__ == '__main__':
    parse_file()
    
