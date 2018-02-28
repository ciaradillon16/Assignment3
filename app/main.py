import requests
import re

pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 

r = requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
file = r.text.split('\n')

for line in file:
    print(line)
  
