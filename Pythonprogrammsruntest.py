x = input("enter the string")
for i in range (len(x)):
    if x[i]==x[len(x)-1-i]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")
        break