import requests
import re

link = input("Enter the list of inputs: ")
r = requests.get(link)
file = r.text.split('\n')
pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")

for line in file[1:-1]:  
    m = pat.match(line)
    if m: 
        array = [m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)]
        cmd = array[0]
        x1 = array[1]
        x2 = array[2]
        y1 = array[3]
        y2 = array[4]
    print(cmd, x1, x2, y1, y2)

    

