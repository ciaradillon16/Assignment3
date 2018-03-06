import requests
import re

#def main(filename, N): #files provided and first line of that file = N  
    
    #lights = lightTester(N)


    #instructions = parse_file(filename)
    #for cmd in instructions:
        #lights.apply(cmd)
class lightTester:
 
    lights = None
    N = 10 
     
    def __init__(self, N):
        self.lights = [[False]*N for i in range(N)]
                 
    #def apply(self, cmd):
        #if (cmd =='turn on'):
    def apply(self):
        for i in range(len(self.lights)):
            for j in range(len(self.lights[i])):
                self.lights[i][j] = False               
        return self.lights
             
        #elif (cmd == 'turn off'):
            #pass
        #elif (cmd == 'switch'):
            #pass
        
    def count(self,lights):
        count = 0
        for i in range(len(self.lights)):
            for j in range(len(self.lights[i])):
                if lights[i][j] == True:
                    count += 1 
        return count
    
    def parse_file(self, filename):
        self.link = input("Enter the list of inputs: ")
        self.r = requests.get(self.link)
        self.file = self.r.text.split('\n')
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")

        for line in self.file[1:-1]:  
            m = pat.match(line)
            if m: 
                array = [m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)]
                cmd = array[0]
                x1 = array[1]
                x2 = array[2]
                y1 = array[3]
                y2 = array[4]
            print(cmd, x1, x2, y1, y2)




#lights = [[0 for x in range(10)] for y in range(10)]
#x = lightTester(10)
#print(lightTester.apply(x))
#print(lightTester.count(x, lights))      
