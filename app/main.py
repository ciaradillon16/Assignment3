#def main(filename, N): #files provided and first line of that file = N  
    
    #lights = lightTester(N)

    #instructions = parse_file(filename)
    
    #for cmd in instructions:
        #lights.apply(cmd)


#class lightTester:
    
lights = [[0 for x in range(10)] for y in range(10)]
    
    #def __init__(self, N):
        #self.lights = ""
        
    #def apply(self, cmd):
        #if (cmd =='turn on'):
            #pass
        #elif (cmd == 'turn off'):
            #pass
        #elif (cmd == 'switch'):
            #pass
      
        
def count(lights):
    count = 0
    for i in range(len(lights)):
        for j in range(len(lights[i])):
            if lights[i][j] == True:
                count += 1 
        return count

for i in range(len(lights)):
    for j in range(len(lights[i])):
        lights[i][j] = False #False - off 

lights[0][4] = True  
print(count(lights))    
            
