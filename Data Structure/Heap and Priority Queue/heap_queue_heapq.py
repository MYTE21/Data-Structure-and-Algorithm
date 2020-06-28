import heapq

li = [5, 7, 9, 1, 3]

heapq.heapify(li)
print(li)

heapq.heappush(li, 4)
print(li)
a = heapq.heappop(li)
print(li)
print(a)

li1 = [5, 7, 9, 4, 3]
li2 = [5, 7, 9, 4, 3]
heapq.heapify(li1)
heapq.heapify(li2)
print(li1)
heapq.heappushpop(li1, 2)
print(li1)
print(li2)
heapq.heapreplace(li2, 2)
print(li2)

li3 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
print(heapq.nlargest(2, li3))
print(heapq.nsmallest(2, li3))
