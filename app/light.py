lights = [[0 for x in range(10)] for y in range(10)] 
counter = 0
total = 1000

for i in range(len(lights)):
    for j in range(len(lights[i])):
        lights[i][j] = False #False - off   
print(lights)

lights[0][9] = True
lights[1][8] = True

for i in range(len(lights)):
    for j in range(len(lights[i])):
        if lights[i][j] == True:
            counter += 1
print (lights)
            
print ('The number of lights off: ', total - counter)
print('The number of lights on: ', counter)
          
          
        
        
