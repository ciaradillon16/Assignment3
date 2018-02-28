import requests
import re

pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 

r1 = requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
r2 = requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt")
r3 = requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt")
r4 = requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt")
r5 = requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt")

file1 = r1.text.split('\n')
file2 = r2.text.split('\n')
file3 = r3.text.split('\n')
file4 = r4.text.split('\n')
file5 = r5.text.split('\n')

for line in file1:
    print(line)
