'''welcome to some advanced programms written by dev (python ide # 2)
some menu driven programms

#,Category,Program Description
1,Basic I/O,Write a program that asks the user for their name and then prints a greeting.

2,Arithmetic,Calculate and print the area of a rectangle given its length and width.

3,Conditional,"Check if a number entered by the user is positive, negative, or zero."

4,Loops,Print the first 10 natural numbers using a for loop.

5,Loops,Calculate the sum of all numbers from 1 to 100 using a for loop.

6,String,"Count the number of vowels (a, e, i, o, u) in a given string."

7,Conditional,"Determine if a year entered by the user is a leap year (divisible by 4, but not by 100 unless also by 400)."

8,Loops,Print a right-angled triangle pattern of asterisks * with 5 rows.

9,Loops,"Print the multiplication table for a number (e.g., up to 10 times) entered by the user."

10,List,Find the largest number in a predefined list of integers.

11,List,Count how many times a specific element appears in a list.

12,String,"Reverse a given string (e.g., ""hello"" becomes ""olleh"")."

13,Loops,"Calculate the factorial of a number (e.g., 5!=5×4×3×2×1)."

14,Loops,Check if a number is a prime number (only divisible by 1 and itself).

15,Conditional,"Create a simple calculator that can perform addition, subtraction, multiplication, and division based on user input for the operation."'''


#,Category,Program Description
'''16,Function,Write a function that converts Celsius to Fahrenheit.

17,List,"Sort a list of numbers in ascending order without using the built-in sort() method (e.g., using a simple bubble sort or selection sort)."

18,String,"Check if a given string is a palindrome (reads the same forward and backward, like ""madam"")."

19,List,Remove duplicate elements from a list.

20,Function,Generate the Fibonacci sequence up to N terms.

21,Loops,Print an inverted pyramid pattern of numbers or symbols.

22,List,Merge two sorted lists into a single sorted list.

23,Dictionary,Count the frequency of each character in a string and store it in a dictionary.

24,Loops,Find the GCD (Greatest Common Divisor) of two numbers.

25,Loops,Find the LCM (Least Common Multiple) of two numbers.

26,List,Rotate the elements of a list to the left by one position.

27,List,Find the second largest number in a list.

28,Dictionary,"Create a simple inventory dictionary where keys are product names and values are their stock counts. Allow the user to ""add"" or ""remove"" stock."

29,String,Check if a string contains all unique characters.

30,List/Tuple,Transpose a given matrix (a list of lists).

31,Function,Implement a function to calculate power xy without using the built-in ** operator or math.pow().

32,String,"Check if one string is an anagram of another (e.g., ""listen"" and ""silent"")."

33,Conditional,"Implement the 'FizzBuzz' game: print ""Fizz"" for multiples of 3, ""Buzz"" for multiples of 5, and ""FizzBuzz"" for multiples of both."

34,List,Find the intersection (common elements) of two lists.

35,Dictionary,"Given a dictionary of student names and scores, find the student with the highest score."

36,String,Title case a given sentence (capitalize the first letter of every word).

37,List,Implement a linear search function to find an element's index in a list.

38,Loops,"Check if a number is an Armstrong number (e.g., 153=13+53+33)."

39,Function,Calculate the Hypotenuse of a right-angled triangle given the other two sides (c=a2+b2​).

40,String,Remove all punctuation from a string.'''


#,Category,Program Description
'''41,Algorithm,Implement the Binary Search algorithm on a sorted list.

42,Recursion,Write a recursive function to calculate the factorial of a number.

43,Algorithm,"Write a function to convert an integer to its Roman Numeral representation (e.g., 1994 → MCMXCIV)."

44,Algorithm,"Implement a simple Guessing Game where the computer selects a random number, and the user has a limited number of attempts to guess it."

45,List/Algorithm,Find the maximum subarray sum (Kadane's algorithm).

46,Algorithm,Write a program to generate all permutations of a given string or list.

47,String/List,"Write a function that implements Run-Length Encoding (RLE) (e.g., ""WWWWAAABBC"" → ""W4A3B2C1"")."

48,Algorithm,Solve the Towers of Hanoi puzzle using recursion.

49,OOP,Create a simple Car class with properties like color and speed and a method accelerate().

50,Algorithm,Implement a function that converts a decimal number to its binary representation.'''

# "16,Function,Write a function that converts Celsius to Fahrenheit."
print("16,Function,Write a function that converts Celsius to Fahrenheit.")
x = input("Are you entering the temperature in celcius or farenheit press c for celsius and f for farenheit")
if x=="c":
    print("Converting from celsius to farenheit")
    c = float(input("Enter the temperature in degree celsius"))
    f = 9/5*c +32
    print("The temperature in degree farenheit is",f)
    exit
if x=="f":
    print("Converting from farenheit to celsius")
    f = float(input("Enter the temperature in degree farenheit"))
    c = f-32*5/9
    print("The temperature in degree cesius is",c)



'''#to find the lcm of two numbers entered by the user
x1 = int(input("Enter the 1st whole number"))
x2 = int(input("Enter the 2nd whole number"))
list_of_fact1 = []
list_of_fact2 = []
#now we have to find the factors of the number
for i in range (1,x1+1):
    if x1%i==0:
        list_of_fact1.append(i)#later we can convert this into a set
for j in range (1,x2+1):
    if x2%j==0:
        list_of_fact2.append(j)#later we can convert this into a set
factors_of_number1 = set(list_of_fact1)
factors_of_number2 = set(list_of_fact2)
if factors_of_number1.issubset(factors_of_number2):
    o = set(factors_of_number2)-set(factors_of_number1)
    for number in o:
        h = 1
        h *= 1
print("LCM of the numbers are",x1*h)
if :
    factors_of_number2.issubset(factors_of_number1)
    o = set(factors_of_number1)-set(factors_of_number2)
    for number in o:
        h = 1
        h *= 1
print("LCM of the numbers are",x2*h)
if:
    o = x1*x2
    print("LCM IS",o)'''



'''checking if a string has all uniques characters'''
v = input("Enter the string")
list = []
for i in v:
    c = v[i]
    list.append(c)
x = list
y = Counter(list)
print(y)






#Check palindrome string
x = input("Enter the string")
count = 0
for i in range(0,len(x)+1):
    if x[i]==x[len(x)-i]:
        count+=1
    if count==len(x):
        print("Palindrome")
    else:
        print("Not a Palindrome")
print("Programme Exited")


