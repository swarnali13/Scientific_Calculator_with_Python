from math import log as logarithm
from math import sqrt as square_root        #Importing the necessary packages for our program

info="""
Hello, I am an online calculator. I can perform the following operations:
a)Addition
b)Subtraction
c)Division
d)Multiplication 
e)Logarithm 
f)Square root
g)Unit conversion(Binary to Decimal and vice versa)
"""
'''
instructions="""
For addition press 'a',
for subtraction press 'b',
for division press 'c',
for multiplication press 'd',                                           
for logarithm press 'e',
for square root press 'f',
for unit conversion press 'g'
Also in order to quit anytime you want, enter 'quit'.
"""
'''
print(info)             #Dispaying the information and instructions
#print(instructions)

while True:            #Creating a while loop in order to maintain the continuity 
    try: 
        choice=input('Enter your choice:').lower()

        if choice=='a':
            num1=float(input('Enter first number:'))
            num2=float(input('Second number:'))
            result=num1+num2
            print('Result:',result)
        
        elif choice=='b':   #Creating conditions for various operations to be performed
            num1=float(input('Enter first number:'))
            num2=float(input('Second number:'))
            result=num1-num2
            print('Result:',result)

        elif choice=='c':
            num1=float(input('Enter first number:'))
            num2=float(input('Second number:'))

            if num2==0:      #In order to avoid exceptions we display a warning message
                print('Cannot Divide by zero! Enter a valid denominator!')
            
            else:
                result=num1/num2
                print('Result:',round(result,2))    #Here we are rounding of the decimal to two decimal places for simplicity and easy readability of the program
        
        elif choice=='d':
            num1=float(input('Enter the first no:'))
            num2=float(input('Enter second no:'))
            result=num1*num2
            print('Result:',result)

        elif choice=='e':
            num1=float(input('Enter the number:'))
            base1=float(input('Enter the base:'))

            if num1<=0 or base1<=1:
                print('Please enter a number > 0 or a base greater than 1')

            else:
                result=logarithm(num1,base1)
                print('Result:',round(result,2))    #Rounding off to 2 decimal places using in-built round() function

        elif choice=='f':
            num1=float(input('Enter a number:'))

            if num1<0:
                print('Cannot compute the square root of a negative no! Please enter a nom negative number.')

            else:
                result=square_root(num1)
                print('Result:',round(result,2))    #Using round() function rounding off to two decimal places

        elif choice=='g':

            preference=input('Enter your conversion prference(binary/decimal):').lower()

            if preference=='binary':
                num1=int(input('Enter the decimal no:'))
                result=bin(num1)
                print('Result:',result[2:])

            elif preference=='decimal':
                num1=input('Enter the binary no:')
                result=int(num1,2)
                print('Result:',result)
            
            elif preference=='quit':
                break
            
            else:
                print('Enter a valid preference!')
        
        elif choice=='quit':
            break

        else:
            raise ValueError
    except ValueError: #Handling ValueError
        print('Please enter a valid value!')

print('Thank you for using the calculator. ')       #Finally completing the program!
