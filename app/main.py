import requests
import re

#def main(filename, N): #files provided and first line of that file = N  
    
    #lights = lightTester(N)
#     instructions = lights.parse_file(filename)
#     
#     for cmd in instructions:
#         lights.apply(cmd)

        
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
    
        if cmd == 'turn off' or cmd == 'turn off ':
            for i in range(y, y1+1):
                for j in range(x, x1+1):
                    self.lights[i][j] = False                
            #return self.lights
        
        elif cmd == 'turn on' or cmd == 'turn on ':
            for i in range(y, y1+1):
                for j in range(x, x1+1):
                    self.lights[i][j] = True  
            #return self.lights
        
        elif cmd == 'switch' or cmd == 'switch ':
            for i in range(y, y1+1):
                for j in range(x, x1+1):
                    self.lights[i][j] = not self.lights[i][j]
#                     if (self.lights[i][j] == False):
#                         self.lights[i][j] = True
#                     elif self.lights[i][j] == True:
#                        self.lights = False
        return self.lights
                 
    def count(self):
        count = 0
        for i in range (self.N):
            for j in range (self.N): 
                if self.lights[i][j]:
                    count += 1 
        return count
    
def parse_file():
#self.link = input("Enter the list of inputs: ")

    r = requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
    file = r.text.split('\n')
    N = file[0]
    print(N)
    pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    
    for line in file:  
        m = pat.match(line)
        print
        if m: 
            array = [m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)]
            print(array)
        
    mylight = lightTester(int(N))
    mylight.apply(array)
    print(mylight.count())
    
if __name__ == '__main__':
    parse_file()
    
