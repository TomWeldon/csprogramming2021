# This is code will find some text in an access file
# Author: Andrew Beatty

import re

regex ="(?<=T)(.*)(?=.HTTP)"

filename = "smallsample.log"
result = []
with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        
        if (len(foundTextList)!= 0):
            
            foundText = foundTextList[0]
            result.append(foundText.strip())
           
print(result)
print(type(result))
for i in result:
    print(i)