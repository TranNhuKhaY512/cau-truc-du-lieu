# Linked_List
from collections import deque
deque()
deque([{'data': 'a'}, {'data': 'b'}])
llist = deque('abcd')
print(llist)
llist.append('h')
print(llist)
llist.pop()
print(llist)

from collections import deque
d= deque ([1,2,3,4,5,6])
print(d)
for i in d:
    print(i)
print(d.pop(),d)