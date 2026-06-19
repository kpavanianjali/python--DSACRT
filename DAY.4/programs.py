'''
def h():
  for i in range(3):
    print(i)
result=(h())
print(result)
'''
'''
#sorting:
#arranging elements of a collection in a particular order according to a specified criterion.
#bubble sort :
# repeatedly compares adjacent elements and swaps them if they are in the wrong order until the entire list is sorted.
'''
'''
#bubble sorted desending order
def BubbleSort(nums):
  L=len(nums)
  c=0
  for j in range(L):
    swapped=False
    for i in range(L-1-j):
      c+=1
      if nums[i]<nums[i+1]:
        nums[i],nums[i+1] = nums[i+1],nums[i]
        swapped=True
      print(c,j,i,nums)
    if not swapped:
      break
  return nums
nums = [5,4,3,1,2]
print(BubbleSort(nums))
'''
'''
#bubble sorted ascending order
def BubbleSort(nums):
  L=len(nums)
  c=0
  for j in range(L):
    swapped=False
    for i in range(L-1-j):
      c+=1
      if nums[i]<nums[i+1]:
        nums[i],nums[i+1] = nums[i+1],nums[i]
        swapped=True
      print(c,j,i,nums)
    if not swapped:
      break
  return nums
nums = [5,4,3,1,2]
print(BubbleSort(nums))
'''
#SelectionSort:
#repeatedly finds the smallest element from the unsorted part of the array and places it at the correct position.

'''
#selectioon sorted
def SelectionSort(arr):
  n=len(arr)
  for i in range(n):
    min_index = i
    for j in range(i + 1,n):
      if arr[j] < arr[min_index]:
        min_index = j 
    arr[i], arr[min_index] = arr[min_index],arr[i]
  return arr
nums = [3,5,1,2,4]
print(SelectionSort(nums))
'''
#insertion_sort:
#that builds the sorted array one element at a time by inserting each element into its correct position.
'''
#insertion sort(cards)
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1 
        while j >=0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1 
        arr[j + 1] = key
    return arr
nums = [5,2,4,1,3]
print(insertion_sort(nums))
'''

#recursion:
#it is a function solves a problem by calling itself on a smaller version of the same problem until a stopping condition (base case) is reached.

'''
#recursionusing for loop 
for i in range(1,11):
  print(i)
  '''
'''
#recursionusing while loop
i = 1
while i<11:
  print(i)
  i+=1
  '''
'''
i=11
while i>10:
  print(10)
  print(9)
  print(8)
  print(7)
  print(6)
  print(5)
  print(4)
  print(3)
  print(2)
  print(1)
  break
  '''
'''
def hello():
  for i in range(5):
    print(i)
    if i==1:
      break
print('hello')
'''
'''
def count(n):
  if n==0:
    return
  print(n)
  count(n-1 )
count(10)
'''

'''
def sum_n(n):
  if n<+0:
    return 0
  return n + sum_n(n-1)
'''
'''
#factorial of a number
def sum_n(n):
  if n <= 0:
    return 0
  return n + sum_n(n-1)
print(sum_n)
'''
'''
def factorial(n):
  if n==0:
    return 1
  return n* factorial(n-1)
print(factorial(5))
'''
