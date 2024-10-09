# deque -> double ended queue
# A list like sequence optimized for data accesses near its end points

from collections import deque

d = deque([1,2,3])
print(d)
d.append(4)
print(d)
d.appendleft(0)
print(d)

d.append(5) # This method just adds an element to the list
d.extend([9,10,11]) # This method adds list or multiple elements to the dequeue
print(d)

d.pop()
d.popleft()
print(d)

d.reverse()
print(d)
