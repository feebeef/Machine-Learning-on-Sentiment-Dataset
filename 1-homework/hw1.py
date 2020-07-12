file  = open("starwars.txt", "r") 
x = file.read()

#https://www.debuggex.com/cheatsheet/regex/python
#https://pythex.org/
import re
words = re.findall("(\w+-*\w*'*\w*)",x)
print('total: ' + str(len(words)))

