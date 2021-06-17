import heapq

class FilaPrioridade:

    def __init__(self) -> None:
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index +=1 

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def __str__(self) -> str:
        return str(self._queue) + ' -> ' + str(self._index)

class Person:
    def __init__(self, name) -> None:
        self._name = name

    def __repr__(self) -> str:
        return self._name    

fp = FilaPrioridade()
fp.push(Person('Naiara'), 29)
print(fp)
fp.push(Person('Carlos'), 33)
print(fp)
fp.push(Person('Vinícius'), 40)
print(fp)
fp.push(Person('Marco'), 45)
print(fp)
fp.push(Person('Eduarda'), 3)
print(fp)
print(fp.pop())