'''
#merge sort: split 
nums = [1, 2, 0, 4, 3]
def split(nums):
    L = len(nums)
    return nums[:L//2], nums[L//2:]
print(split(nums)) 
'''
'''
nums=[1,2,0,4,3]
def s(nums):
  if len(nums)<=1:
   return nums
  L=len(nums)
  Left=nums[:L//2]
  Right=nums[L//2:]
  print(s(Left),s(Right))
  return(nums)
(s(nums))
'''

'''
#merge sort:
def merge_lists(L1,L2):
  i,j=0,0
  res=[]
  while i<len(L1) and j<len(L2):
    if L1[i]<=L2[j]:#i=0,j=0:L1[0]<L2[0],1
      res.append(L1[i])
      i+=1
    else:
      res.append(L2[j])
      j+=1
  res.extend(L1[i:])
  res.extend(L2[j:])
  return res
ans=merge_lists([1,5,6],[2,3,5,7,8])
print(ans)
'''
