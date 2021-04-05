import os
import sys


#UI

dir = input("Where are the files? ")



     


nameList = os.listdir(dir)
length = len(nameList)
nameList2 = nameList
extensionList = []

## Preprocessing

#Remove the extensions from files to add back later
for name in nameList2:
    name = name.split(".")
    extensionList.append("."+name[-1])
for i in range(length):
    nameList[i]= nameList[i].replace(extensionList[i], "")
    print(nameList[i])
    
#Find the minimum length of strings 
lengthList =[]
for name in nameList:
    lengthList.append(len(name))
minLen = min(lengthList)

#Find the minimum length of lists
def findMinLen():
    lengthListx = []
    for name in nameList:
        lengthListx.append(len(name))
    minLen = min(lengthListx)
    return minLen


##Chars

#Replace a string (1)
def replaceString():
    toRemove = input("What should be replaced? ")
    toReplace =input("Should be replaced with? (Enter if you want to remove the above string) ")
    for i in range(0, length):
        nameList[i] = nameList[i].replace(toRemove, toReplace)
        print(nameList[i]+extensionList[i]) #Print a preview of the file names

#Remove first n characters (2)
def removeFirstNChar():
    
    ask = True
    while ask == True:
        index = int(input("How many characters should be remove from the beginning? Between 0 and "+ str(minLen)+ " "))
        if (index < minLen) & (index>=0):
            ask = False
    for i in range (0, length):
        nameList[i] = nameList[i][index :]
        print(nameList[i]+extensionList[i]) #Print a preview of the file names


#Remove last n characters (3)
def removeLastNChar():

    ask = True
    while ask == True:
        index = int(input("How many characters should be remove from the beginning? Between 0 and "+ str(minLen)+ " "))
        if (index < minLen) & (index>=0):
            ask = False
        index = index*-1
    for i in range (0, length):
        nameList[i] = nameList[i][: index]
        print(nameList[i]+extensionList[i]) #Print a preview of the file names

#Add a String to index (4)
def addStringToIndex():
    ask = True
    while ask == True:
        index = int(input("Where should the string be added? Between 0 and "+ str(minLen)+ " "))
        if (index < minLen) & (index>=0):
            ask = False
    add = input("What should be added?")
    for i in range (0, length):
        nameList[i] = nameList[i][: index] + add + nameList[i][index :]
        print(nameList[i]+extensionList[i]) #Print a preview of the file names

#Add a String to to the end 
def addStringToEnd():
    add = input("What should be added?")
    for i in range (0, length):
        nameList[i] = nameList[i]+add
        print(nameList[i]+extensionList[i]) #Print a preview of the file names


##Strings

#Split the file names 
def splitNames():
    split = input("What are the strings separated by? ")
    for i in range (0, length):
        nameList[i] = nameList[i].split(split)

#Append the lists to Strings
def appendNames():
    for i in range (0, length):
        name = ""
        for ele in nameList[i]:
            name += ele+" "
        name = name[: len(name)-1]
        nameList[i] = name   

    
#Remove string at index ()
def removeNthString():
    splitNames()
    x = findMinLen()
    print(x)
    for names in nameList:
        print(names)
    ask = True
    while ask == True:
        index = int(input("Where is the string you want to remove? Between 0 and " +str(x-1) + ": "))
        if (index < x-1) & (index>=0):
            ask = False
    for names in nameList:
        names.pop(index)
    appendNames()
    for i in range (0, length):
        print(nameList[i]+extensionList[i]) #Print a preview of the file names

#Remove first n strings ()
def removeFirstNString():
    splitNames()
    x = findMinLen()
    print(x)
    for names in nameList:
        print(names)
    ask = True
    while ask == True:
        index = int(input("Where is the string you want to remove up to? Between 0 and " +str(x-1) + ": "))
        if (index < x-1) & (index>=0):
            ask = False
        index = index*-1
    for i in range (0, length):
        name = []
        name = nameList[i][index:]
        nameList[i] = name


    appendNames()
    for i in range (0, length):
        print(nameList[i]+extensionList[i]) #Print a preview of the file names

#Remove last n Strings ()

def removeLastNString():
    splitNames()
    x = findMinLen()
    print(x)
    for names in nameList:
        print(names)
    ask = True
    while ask == True:
        index = int(input("Where is the string you want to remove up to from last? Between 0 and " +str(x-1) + ": "))
        if (index < x-1) & (index>=0):
            ask = False
        
    for i in range (0, length):
        name = []
        name = nameList[i][ : (len(nameList[i]) - index - 1)]
        nameList[i] = name


    appendNames()
    for i in range (0, length):
        print(nameList[i]+extensionList[i]) #Print a preview of the file names



while True:

    command = int(input("What do you want to do? "))
    if command == 0:
        break
    if command == 1:
        replaceString()
    if command == 2:
        removeFirstNChar()
    if command == 3:
        removeLastNChar()
    if command == 4:
        addStringToIndex()
    if command == 5:
        removeFirstNString()#
    if command == 6:
        removeLastNString()

#Change the names of the files
oldNames = os.listdir(dir)
os.chdir(dir)
print(oldNames)
print(nameList)
for i in range (0, length):
    nameList[i] = nameList[i]+extensionList[i]

print(nameList)
for i in range (0, length):
    os.rename(oldNames[i], nameList[i])
    