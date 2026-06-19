'''
#linear serch
list1=[]
for i in range (1,1000000):
  list1.append(i)
target=9900
list2=list(range(1,100000))
print(target in list2)
'''

'''
list1=[]
for i in range (1,1000000):
  list1.append(i)
target=9900
seen=False
list2=list(range(1,100000))
for i in list2:
  if i == target:
    seen=true
    break
'''

'''
#find the min and max
nums=input().split()
print(nums)
for i in range(len(nums)):
  nums[i]=int(nums[i])
print(nums)
'''

'''
#square 
nums=input().split()
print(nums)
for i in range(len(nums)):
  nums[i]=int(nums[i])**2
print(nums)
'''

'''
#minimum
nums=list(map(int,input().split()))
curr_min=nums[0]
for i in range(len(nums)):
  if curr_min>nums[i]:
    curr_min=nums[i]
print(curr_min)
'''

'''
#maximum
nums=list(map(int,input().split()))
curr_max=nums[0]
for i in range(len(nums)):
  if curr_max<nums[i]:
    curr_max=nums[i]
print(curr_max)
'''

'''
#even or add
num=3
if num%2==0:
  if num>1:
    print("even positive")
  else:
    print("even negative")
else:
  if num>=0:
    print("odd positive")
  else:
    print("odd negative")
'''
'''
num=2
if num%2==0 and num>1:
  print("even positive")
  if 100%num==0:
    print("super number")
elif num%2==0 and num<0:
  print("even negative")
elif num%2==1 and num>1:
  print("odd ppositive")
elif num%2==1 and num<0:
  print("odd negative")
'''
