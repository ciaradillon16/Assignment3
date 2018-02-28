import re
import webbrowser
import urllib2

#pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 

for line in urllib2.urlopen('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'):
    print(line)
