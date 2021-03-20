# This is code will find some text in an access file
# Author: Andrew Beatty

import re

regex ="(?<=T)(.*)(?=.HTTP)"

filename = "smallsample.log"
<<<<<<< HEAD
result = []
=======
#result = []
foundTextList =[]
>>>>>>> 5dea942fdf5e6eb3100fc44d4c9fad9e9801585c
with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        
        if (len(foundTextList)!= 0):
<<<<<<< HEAD
            
            foundText = foundTextList[0]
            result.append(foundText.strip())
           
print(result)
print(type(result))
for i in result:
    print(i)
=======
            #print(foundTextList)
            #result.append(foundTextList)
            foundText = foundTextList
            foundTextList.append(foundText)
            #foundTextList.append(line)
            print(foundText)
            # if I did not want the [] at the beginning and end
            #print(foundText[1:-1])
#for i in result:
   # print(i)

#print(foundTextList, end='')
>>>>>>> 5dea942fdf5e6eb3100fc44d4c9fad9e9801585c
