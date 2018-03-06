import requests
import re
import urllib.request
import urllib.parse

pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
r1 = urllib.request.urlopen("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt").read().decode('utf-8')
file = r1.split('\n')

for line in file: 
    m = pat.findall(line[:-1])[0]
    print(m)
    




