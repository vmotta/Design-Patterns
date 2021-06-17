from collections import deque

'''
fila = deque(maxlen=4)
fila.append(1)
fila.append(2)
fila.append(3)
fila.append(4)
fila.append(5)
print(fila)
'''

f = deque()
f.append(1)
f.append(2)
f.append(3)
f.appendleft(4)
print(f)
f.pop()
f.popleft()
print(f)