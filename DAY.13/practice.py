"""#Take a character as input and print its ASCII value.
ch = input("enter a charachter:")
ascii_value = ord(ch)
print(ascii_value)"""

"""num = int(input("enter a number:"))
ascii_value = chr(num)
print(ascii_value)"""


"""ch = input("enter a character:")
ascii_value = ord(ch)
next_ascii = ascii_value+1
next_char = chr(next_ascii)
print(next_char)"""

"""a=2
b=3
temp=a
a=b
b=temp
print("after swaping")
print("a",a)
print("b",b)"""

"""num=4
fact=1
for i in range(1,num+1):
    fact=fact*i
print('factorial',fact)
"""
"""a=3
b=4
c=5
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)"""

"""num=2
if num % 2 == 0:
    print("even")
else:
    print("odd")"""

"""num=2
if num >0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")
"""
"""

#print prime numbers from 1 to N 
n=int(input("enter a number:"))
for num in range(2,n+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)
"""
    
s=input("enter a string:")
rev = s[::-1]
if s == rev:
    print("palindrome")
else:
    print("not palindrome")