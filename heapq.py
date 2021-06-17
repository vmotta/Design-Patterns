import heapq

# prioridade máxima ou mínima
idades = [15,10,20,18,25,8,19]
print(idades)

# os três menores números na lista
print(heapq.nsmallest(3, idades))

# os três maiores números na lista
print(heapq.nlargest(3, idades))

# ordenando com heapq
heapq.heapify(idades)
print(idades)

# usando o heappop
print(heapq.heappop(idades))
print(idades)

# usando heappush
print(heapq.heappush(idades, 5))
print(idades)