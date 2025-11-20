'''write code to execute it here'''
#Check palindrome string
x = input("Enter the string")
count = 0
for i in range(0,len(x)+1):
    if x[i]==x[len(x)-1-i]:
        count+=1
    if count==len(x):
        print("Palindrome")
    else:
        print("Not a Palindrome")
print("Programme Exited")