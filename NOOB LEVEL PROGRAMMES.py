
#1
print("executing noob level programme 1")
x = str(input(" what is your name "))
if x==('devadathan'):
    print("welcome back")
else:
    print("you are an intruder")


#this is the path of this file just paste it if not available "C:\Users\thund\Desktop\DEVS PROGRAMMS\NOOB LEVEL PROGRAMMES.py"


#2
import time
print("executing noob level programme 2")
time.sleep(2)
print("i know you are going to die of cringe from this programme but trust me i am a begginer")
time.sleep(2)
print("programme is to add 2 numbers basically an addition calculator")
time.sleep(2)
a = int(input("ENTER THE FIRST NUMBER"))
b = int(input("ENTER THE SECOND NUMBER"))
print("calculation going on")
time.sleep(2)
print("receiving file from google server")
time.sleep(1)
print("sum of these numbers is ",   a+b)

#3
#ALL PROGRAMMES

#chapter 1 programs



#Program to enter name and age and print it
name = input("Enter your name")
age = int(input("Enter your age"))
print("Your name is",name,"and your age is",age)



#Program to enter 3 numbers and find average
a =int(input("Enter the first number"))
b =int(input("Enter the second number"))
c = int(input("Enter the third number"))
average = a+b+c/3
print("Your average is",average)



#Program to enter age of a person and print age after 5 years
age = int(input("Enter your age"))
age_after_five_years = age+5
print("Age after 5 years will be",age_after_five_years)



#Enter number and find cube
a = int(input("Enter number to be cubed"))
print("Cube of the number is",a**3)



#enter length and breadth and fuind area
length = int(input("Enter the length of the rectangle"))
breadth = int(input("Enter the breadth of the rectangle"))
area = (length*breadth)
print("Area of the rectangle is",area)



#enter numbers and swap their value
a = int(input("Enter the number"))
b = int(input("Enter the second number"))
a,b = b,a
print("The new value of first number is",a,"and new value of second number is",b)
#swap values using 3rd variable



#enter 2 int and perform all arithmetic operations
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
operator = input("Enter operator")
if operator == ("+"):
    print("The sunm of these number is",a+b)
elif operator == ("-"):
    print("The difference of these numbers is",a-b)
elif operator == ("*"):
    print("The product of these two numbers are",a*b)
elif operator == ("/"):
    print("The quotient of these two number are",a/b)
else:
    print("Invalid operator given")



#repeat string n times
a = input("Enter the word you want to repeat")
n = int(input("Enter the number of times you want to repeat the string"))
print("After repeating the string n times we get",n*a)
      


#find volume of the sphere with radius r
radius = int(input("Enter the radius of the sphere"))
volume = (4/3*22/7*radius**3)



#temp in celcius and convert into farenheit
tempcelsius = int(input("Enter the temperature in celsius"))
tempfarenheit = (9/5*tempcelsius + 32)
print("The temperature in farenheit is",tempfarenheit)



#Simple Interest prgramme
principle = int(input("enter the principle amount"))
intrest = int(input("enter the rate of intrest "))
time = int(input("enter the time period of the simple intrest"))
simple_intrest = (principle*intrest*time/100)
print("The simple intrest after",time,"years is",simple_intrest)



#to find if no is even or odd
a = int(input("Enter the number"))
if a%2 == 0:
        print("The number entered is even")
else:
    print("The number is odd")



#Eligibilty to vote
x = int(input("Input voter age"))
if x>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")



#Smallest number printing
print("Programme to print the smallest of 2 numbers")
j = int(input("Enter the first number"))
k = int(input("Enter the second number"))
if j>k:
        print("First number is greater than the second number")
else :
    print("Second number is greater than the first number")



#If no is + or -
print("Programme to check if numberis positive negative or 0")
g = int(input("Enter the number"))
if g>0:
    print("The number you have entered is Positive")
elif g==0:
    print("The number you have entered is 0 which is neither positive nor negative")
else:
    print("The number you have entered is Negative")


  
#enter marks and display grades
print("Programme to check marks of 3 subjects and print the grafe accordingly")
Math = int(input("Enter your math marks"))
Science = int(input("Enter your science marks"))
Computer = int(input("Enter your computer marks"))
Total_Marks = int(input("What is the total marks you can get for each subject"))
Average_percent = (Math+Science+Computer/3*Total_Marks)*100
if Average_percent < 50:
    print("You have failed and you have got an F")
elif 60<=Average_percent<70:
    print("You have got a D in your exams")
elif 70<=Average_percent<80:
    print("You have got a C in your exams")
elif 80<=Average_percent<85:
    print("You have got a B in your exams ")
elif 90<=Average_percent<100:
    print("You have got an A in your exams")
else:
    print("Congrats you have got an A+ in your exams")

    

#Programme to find the greatest of the 3 numbers
print("Programme to find greatest of 3 numbers")
a =int(input("Enter the first number"))
b =int(input("Enter the second number"))
c = int(input("Enter the third number"))
if a>b>c:
    print("The first number",a,"is the largest number")
elif a<b<c:
    print("The last number",c,"is the largest number")
elif a==b>c:
    print("The first and second number",a,b,"are the largest numbers")
elif a>b==c:
    print("The first number",a,"is the largest number")

    

#Calculating area and perimiter of a circle
print("Programme to find perimeter and area of a circle")
Radius = int(input("Enter the radius of the circle"))
Area = (22/7*Radius**2)
Perimeter = 2*22/7*Radius
print("The area of the circle is",Area,"The perimeter of the circle is",Perimeter)



#To find if entered character is vowel or string
print("Programme to check if entered character is vowel or string")
a = input("Enter the vowel or the string")
if a == ('a',"e","i","o","u","A","E","I","O","U"):
        print("The charcter you have entered is ",a,"and it is a vowel")
else:
         print("The charcter you have entered is ",a,"and it is a consonant")


#if statement related programmes

#to find if no is even or odd
print("Program to check if number is even or odd")
a = int(input("Enter the number"))
if a%2 == 0:
        print("The number entered is even")
else:
    print("The number is odd")



#Eligibilty to vote
print("Programme to check if person is eligible to vote")
x = int(input("Input voter age"))
if x>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")



#Multiple of 5
print("Programme to find if number entered is a multiple of 5")
o = int(input("Enter the number"))
if o%5==0:
    print("yes the number is divisible by 5")
else:
    print("N0 the number you have entered is not divisible by 5")



#write prog to obtain temp of 7 days and display avg temp of the week
day1 = int(input("Enter the weather for day 1"))
day2 = int(input("Enter the weather for day 2"))
day3 = int(input("Enter the weather for day 3"))
day4 = int(input("Enter the weather for day 4"))
day5 = int(input("Enter the weather for day 5"))
day6 = int(input("Enter the weather for day 6"))
day7 = int(input("Enter the weather for day 7"))
average_weather = day1+day2+day3+day4+day5+day6+day7/7
print("Average Weather for 7 days is",average_weather )

#printing this using while 
'''i = 1
days = int(input("Enter the average weather"))
while i<=7:
     sum = 
'''


#to promp user to enter the price and then give discounts accordingly
price = int(input("Enter the BILLED amount"))
if price>= 10000:
     print("The amount you have paid is",price,"The discount you get is 10% and the final amount to be paid is",price*10/100)
elif 5000<= price <=9999:
     print("The amount you have paid is",price,"The discount you get is 5% and the final amount to be paid is",price*5/100)
else:
     print("The amount you have paid is",price,"The discount you get is 3% and the final amount to be paid is",price*3/100)


                  
#To check the type of triangle by prompting user to enter the sides
side1 = int(input("Enter the length of the first side of the triangle"))
side2 = int(input("Enter the length of the second side of the triangle"))
side3 = int(input("Enter the length of the third side of the triangle"))
if side1==side2==side3:
     print("Since all sides are equal the triangle is equilateral")
elif side1!=side2!=side3:
     print("None of the sides of your triangle are equal so it is a scalene triangle")
else:
     print("Your triangle is isoscles")



#To check roots of a quadratic equation is real,imaginary or 0
print("Equation must be in the form ax^2+bx+c=0")
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c - int(input("Enter the value of c"))
print("Your quadraticc equation is",a,"x^2 +",b,"x +",c)
print("Finding the  type of roots")
root_type = (b^2-4*a*c)/ (2*a)  
if root_type == 0:
     print("Both the roots are equal")
elif root_type > 0:
     print("Your roots are imaginary")
else:
     print("The roots are positive and the are distinct")



#For and While loop programms



#To find sum of n natural numbers and print their sum
i = 1
s = 0
n = int(input("Enter the number till which addittion should occur"))
while i>=n:
     i += 1
     s += i
print(s)     



#To find sum of n odd natural numbers and print their sum
i = 1
s = 0
n = int(input("Enter the number till which addition should occur"))
while i>=n:
     i = i+2
     s += i
print(s)



#to print multiples of the given number uptil 10 using while
n = int(input("Enter the number uptil which the multiplication table of 10 should occur"))
i = 1
s = 1
while i<=10:
    print(s*i)
    i = i+1



#redoing some shit 
#to print hello 5 times 
i = 1
while i <= 5:
     print("Hello")
     i = i+1



i = 1
n = int(input("Enter the number"))
while i <= n:
    if i%2==0:
        print(i,end = '@')
    i += 1



i = 1
while i <= 5:
     print("Square of",i,"is",i**2)
     i = i+1



#STRING MANIPULATION
x = "A"
print(ord(x))



x = 65
print(chr(x))



#To print ABCD......
x = ord("A")
for i in range(x,ord("Z")+1):
     print(chr(i),end = " ")



#To print the alphabeets backwards
x = ord("Z")
for i in range (x,ord("A"),-1):
     print(chr(i),end = " ")



#Traversing a string
x = "Hello world"
for i in x:
     print(i,end = " ")



#To Print Number Of Characters
y = "Hello Everyone"
print(len(y))



z = "Devadathan is here"
for i in range (0,len(z)):
     print(i,end = "$")



#To Print The String In Reverse Order
h = "Laptop"
for i in range (-1,-len(h)-1,-1):
     print(chr(i),end = " ")



#to print the smallest of 3 number entered
x = int(input("Enter the first number"))
y = int(input( "Enter the second number"))
z = int(input("Enter the third number"))
if x<y and x<z:
     print("The smallest number is",x)
if y<x and y<z:
     print("The smallest number is",y)
if z<y and z<x:
        print("The smallest number is",z)
else:
    print("All numbers are equal")
     


#To print the alphabets from A to Z using for loop
x = ord("A")
y = ord("Z")
for i in range (x,y+1):
     print(chr(i),end=' ')


'''switch to advanced programmes to continue with menu driven prorgammes and some looping and list related question'''


    
     




     
        