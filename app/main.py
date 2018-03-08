import requests
import re
import sys
import os
        
class lightTester:
    
    lights = None
   
    def __init__(self, N):
        self.N = N
        self.lights = [[False]*N for _ in range(N)]
        
    def size(self, number):
        if number < 0:
            return 0
        if number > self.N:
            return self.N-1
        else:
            return number
                         
    def apply(self, array):
        self.array = array
        cmd = array[0]
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
        count = 0
        for i in range (self.N):
            for j in range (self.N): 
                if self.lights[i][j]:
                    count += 1         
        return count
    
def parse_file():
    command = sys.argv[1]
    instructions = sys.argv[2]

    if instructions.startswith("http://"):
        r = requests.get(instructions)
        file = r.text.split('\n')
        N = file[0]
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        mylight = lightTester(int(N))
    
        for line in file:  
            m = pat.match(line)
            if m:
                array = [m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)]
                mylight.apply(array)
        print(mylight.count())
                
    else: 
        file = open(instructions, 'r')
        file = file.readlines()
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        
        for line in file[:1]:
            N = line[0]
        
        for line in file:
            mylight = lightTester(N)
            m = pat.match(line)
            if m:
                array = [m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)]
                mylight.apply(array)
        print(mylight.count())
    
if __name__ == '__main__':
    parse_file()
    
