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
  
lights = [[0 for x in range(10)] for y in range(10)]
x = lightTester(10)
print(lightTester.apply(x))
print(lightTester.count(x, lights))      
