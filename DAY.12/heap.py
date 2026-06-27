"""#min Heap:
import heapq
nums=[7,1,4,3]
heapq.heapify(nums)
print(nums)
"""
"""import heapq
nums=[-7,-1,-4,-3]
heapq.heapify(nums)
print(nums)"""

"""import heapq
nums=[8,1,2,3,6,7]
min_heap=[]
for i in nums:
    heapq.heappush(min_heap,i)
print(min_heap)"""

"""import heapq
nums=[8,1,2,3,6,7]
min_heap=[]
for i in nums:
    heapq.heappush(min_heap,i)
for i in nums:
    heapq.heappop(min_heap)
    print(min_heap)"""

"""#maxheap
import heapq
nums=[10,8,20,7,6,15]
nums=[-num for num in nums]
heapq.heapify(nums)
print(nums)
nums=[-num for num in nums]
print(nums)
"""

"""#heappush:
import heapq
nums=[10,8,20,7,6,15]
max_heap=[]
nums=[-num for num in nums]
for i in nums:
    heapq.heappush(max_heap,i)
    print(max_heap)
"""

"""import heapq
nums=[10,8,20,7,6,15]
max_heap=[]
nums=[-num for num in nums]
for i in nums:
    heapq.heappush(max_heap,i)
for i in nums:
    print(max_heap)
    heapq.heappop(max_heap)
"""
