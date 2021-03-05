# This is code will find some text in an access file
# Author: Andrew Beatty

import re

regex ="(?<=T)(.*)(?=.HTTP)"

filename = "smallsample.log"
result = []
foundTextList =[]
with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        #result.append(foundTextList)
        if (len(foundTextList)!= 0):
            #print(foundTextList)
            result.append(foundTextList)
            #foundText = foundTextList[0]
            #foundTextList.append(line)
            #print(foundText.strip())
            # if I did not want the [] at the beginning and end
            #print(foundText[1:-1])
#for i in result:
   # print(i)

print(result, end='')