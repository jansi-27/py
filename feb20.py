# a - section
'''Write a program to check if a given number is positive,negative, or zero.'''

number = int(input("enter a number"))
if number>0:
    print("positive")
elif number==0:
    print("zero")
else:
    print("negative")
    
'''Determine if a number is odd or even.'''

number = int(input("enter a number :"))
if number%2==0:
    print("even")
else:
    print("odd")

'''Check if a person is eligible to vote (age >= 18).'''

age = int(input("enter a number :"))
if age>=18:
    print("your eligible for  vote")
else:
    print("your not eligible for vote")
    
'''Write a program to find the greatest of two numbers.'''

num1 = int(input("enter a number :"))
num2 = int(input("enter a number :"))
if num1>num2:
    print("num1 is greater than num2",num1)
else:
    print("num2 is greater than num1 :",num2)
    
'''Print "Pass" if a student scores more than 40 marks;
otherwise, print "Fail."'''

score = int(input("enter a number :"))
if score>=40:
    print("pass")
else:
    print("fail")
    
'''Write a program to display the day of the week based on a
number input (1 for Monday, 2 for Tuesday, etc.).'''

day = int(input("enter a number :"))
if day==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday")
elif day==4:
    print("thrusday")
elif day==5:
    print("friday")
elif day==6:
    print("saturday")
elif day==7:
    print("sunday")
else:
    print("enter a valid number")
    
'''Implement a simple calculator to perform addition,
subtraction, multiplication, and division.'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    print( num1 + num2)
elif operation == "-":
    print( num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error!")
else:
    print("Invalid operation")

'''Write a program to display the name of a month based on
the month number (1 for January, 2 for February, etc.).'''

month = int(input("Enter a number:"))
if month == 1:
    print("january")
elif month == 2:
    print("february")
elif month == 3:
    print("march")
elif month == 4:
    print("april")
elif month == 5:
    print("may")
elif month == 6:
    print("june")
elif month == 7:
    print("july")
elif month== 8:
    print("august")
elif month == 9:
    print("september")
elif month == 10:
    print("october")
elif month == 11:
    print("november")
elif month == 12:
    print("december")
else:
    print("Invalid month")
    
'''b.Write a program to find the greatest of three numbers.'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if num1 >= num2 and num1 >= num3:
    print("The greatest number is num1", num1)
elif num2 >= num1 and num2 >= num3:
    print("The greatest number is num2", num2)
else:
    print("The greatest number is num3", num3)

'''Check if a year is a leap year.'''

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

'''Write a program to classify a character entered by the user
as a vowel, consonant, or neither.'''

char = input("Enter a character: ")  
if char in 'aeiouAEIOU':  
    print("Vowel")
elif char.isalpha():
    print("Consonant")
else:
    print("Neither a vowel nor a consonant")

'''Calculate the grade of a student based on the marks they
score:
1. 90-100: Grade A
2. 80-89: Grade B
3. 70-79: Grade C
4. <70: Fail.'''

marks = int(input("Enter your marks:"))
if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks <= 89:
    print("Grade B")
elif 70 <= marks <= 79:
    print("Grade C")
elif marks < 70:
    print("Fail")
else:
    print("Invalid marks")
    
'''Write a program to check if three sides length form a valid
triangle.'''

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))
if (a + b > c )and (a + c > b) and (b + c > a):
    print("valid triangle")
else:
    print("Invalid triangle")