# print("'hello world'")
'''
name = "anjali"
print(name)
'''
'''
num = int(input("Enter an integer:"))
print("you enterd", num)
'''
'''
a = 3
b = 4
print(a+b)
'''
'''
num = int(input("Enter a number:"))
if num >1:
    for i in range(2,num):
      if  num % i == 0:
        print("not prime")
        break
      else:
        print("prime")
'''

'''
a = 3.5
b = 4.8
print(a*b)
'''
'''
#Take a character as input and print its ASCII value.
ch = input("Enter a character: ")
ascii_value = ord(ch)
print(ascii_value)
'''
'''
#Print the Next Character Using ASCII Values
ch = input("Enter a character: ")

ascii_value = ord(ch)
next_ascii = ascii_value + 1
next_char = chr(next_ascii)

print(next_char)
'''
'''
#Print the Previous Character Using ASCII Values
ch = input("Enter a character: ")

ascii_value = ord(ch)
prev_ascii = ascii_value - 1
prev_char = chr(prev_ascii)

print(prev_char)
'''
'''
#Take an ASCII Value and Print the Corresponding Character
num= int(input("Enter an ASCII value: "))
ch = chr(num)
print(ch)
'''
'''
#Check Whether a Character is Uppercase or Not
#HINT:ASCII values of uppercase letters are from 65 to 90.
ch = input("Enter a character: ")
ascii_value = ord(ch)
if ascii_value >= 65 and ascii_value <= 90:
    print("Uppercase")
else:
    print("Not Uppercase")
'''
'''
#swaoing without temp(temoarary variable)
a=2
b=3
a,b= b,a 
print("after swaping")
print("a",a)
print("b",b)
'''
'''
#swaping with using temperary variable(temp)
a=2
b=3
temp = a 
a = b 
b = temp
print("after swaping")
print("a",a)
print("b",b)
'''
'''
#Swap three numbers in a circular way 
a = 10
b = 20
c = 30
a,b,c =c,a,b
print("after swaping")
print("a",a)
print("b",b)
print("c",c)
'''
'''
#to calculate farenheit to celsius python program
#To convert Fahrenheit to Celsius, use the formula:
#C=(F-32)*5/9
f=float(input("enter a number:"))
print((f-32)*5/9)
'''
'''
# find the size of int,float,char,double
import sys
a = 3
b = 1.2
c = "a"
d = 7
print(sys.getsizeof(a)) #sys is a built in python module
print(sys.getsizeof(b)) #getsizeof is a function inside the sys module
print(sys.getsizeof(c))
print(sys.getsizeof(d))
'''
'''
# add two complex numbers
a = (3 +2j)
b = (2 +5j)
print(a+b)
'''
'''
#print prime numbers from 1 to N 
n = int(input("enter a number:"))
for num in range(2,n+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)
 '''   
'''
# to find the simple interest
# fromula = p*r*t/100
p = float(input("enter principal amount:"))
r = float(input("enter rate of interest:"))
t = float(input("enter time:"))
si  = (p * r * t)/100
print("simple interest:",si)
'''
'''
# compound interest
#formula : 𝐴 = P (1+R/100)^T
p = float(input("enter principal amount:"))
r = float(input("enter rate of interest(%): "))
t = float(input("enter time:"))
amount = p*(1+r/100)**t 
ci = amount -  p 
print("compound interest ",ci)
print("total amount",amount)
'''
'''
# Area And Perimeter of Rectangle
length = 10
breadth = 3
area = length * breadth
Perimeter = 2*(length + breadth)
print("area",area)
print("Perimeter",Perimeter)
'''
'''
#Check Whether a Number is Positive or Negative or Zero
num = 10
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("zero")
'''
'''
#Check for Odd or Even Number
num = 2
if num % 2 == 0:
    print("even")
else:
    print('odd')
'''
'''
#Check Vowel or Consonant
ch = input("enter a character:")
if ch in "aeiouAEIOU":
    print("vowels")
else:
    print("Consonant")
'''
'''
#Find the Largest Number Among Three Numbers
a = 2
b = 3
c = 1
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)
'''
'''
#Calculate Sum of Natural Numbers
# formula: Sum= n(n+1)​/2
n = int(input("enter a number:"))
sum_n = n*(n+1)/2
print("sum of natural number:",sum_n)
'''
'''
#Print Alphabets From A to Z Using Loop
for i in range(ord('A'),ord('Z') + 1):
  print(chr(i))
'''
'''
#The 400 rule exists because the Earth's orbit around
#the Sun is not exactly 365.25 days.
#Leap Year Rules:
#Every year divisible by 4 → Leap Year
#But years divisible by 100 → Not a Leap Year
#But years divisible by 400 → Leap Year again
# to check Leap Year
year = 2024
if year % 400 == 0:
  print("leap year")
else:
  print("not a leap year")
'''
'''
# factorial of a number
num = 5
fact = 1
for i in range(1,num+1):
  fact = fact*i
print("factoriai:",fact)
'''



