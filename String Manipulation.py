#To print the alphabets from Z to A using for loop
x = ord("A")
y = ord("Z")
for i in range (y,x-1,-1):
     print(chr(i),end=' ')



#To print the alphabets from A to Z using for loop
x = ord("A")
y = ord("Z")
for i in range (x,y+1):
     print(chr(i),end=' ')



#Programme to enter a string and print the character with the highest ascii value
x = input("enter the string")
y = len(x)
high = x[0]
for i in range(0, len(x)-1):
    if ord(x[i]) > ord(x[i+1]):   #ord A = 64
        high = x[i]
    else:
        high = x[i+1]
print("The character with the highest ascii value is:",high)



#Return the most frequent character and its count. If tie, return the earliest.
#Find the unique characters and add them to a dictionary
#Take first character in the dictonary and check its frequency in the string
#Do the same for all the items in the dictionary
#Compare the frequency of each character and return the one with the highest frequency
#If there is a tie, return the earliest character
x = input("enter the string")
y = len(x)
sStr = list(set(x))
#print(sStr)
for i in range(0,len(sStr)):
    freq = x.count(sStr[i])
    print(sStr[i],"=",freq)


'''to print the pattern ****
                        ****
                        ****
                        ****'''
n = int(input("enter the number of rows"))
o = int(input("Enter the number of columns"))
l = (input("Enter the character to be printed "))
for i in range(0,n):
    i+=1
    print(" ")
    for j in range(0,o):
        j+=1
        print(l,end = '')



#to take input of a string and find out the largest string with ascii value
x = input("enter the string")
y = input   