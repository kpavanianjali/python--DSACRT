'''
#sum of numbers

nums=input()
s=0
for i in nums:
  if i.isdigit():
    s+=int(i)
print(s)
'''

'''
#product of numbers
nums=input()
s=1
for i in nums:
  if i.isdigit():
    s*=int(i)
print(s)
'''

'''
#count of target amoung all numbers
nums=input()
t=int(input())
c=0
for i in nums:
  if i.isdigit() and int(i)==t:
    c+=1
print(c)
'''

'''
# square of all numbers
nums=input()
s=0
for i in nums:
  if i.isdigit():
    print(int(i) *int(i))
'''

'''
#reverse method
nums=input().split()
L=len(nums)
nums=nums[::-1] #nums.reverse()
print(nums)
'''

'''
#anagram  
s1 = "silent"
s2 = "listen"
if sorted(s1) == sorted(s2):
    print("anagram")
else:
    print("not anagram")
'''

'''
# not anagram
s1 = "dad"
s2 = "mom"
if sorted(s1) == sorted(s2):
    print("anagram")
else:
    print("not anagram")
'''

'''
#time complexity of prime numbers
n=int(input())
c = 0
for i in range(1,n//2+1):
  if n % i ==0:
    c += 1
    print(c,i)
print(c+1,n)
'''

