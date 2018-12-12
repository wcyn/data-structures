import heapq
heap = []
data = [1, 3, 6, 5, 7, 9, 2, 7, 4, 6, 8, 0]
data2 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for item in data:
    heapq.heappush(heap, item)

# print(heap)
# heapq.heapify(data2)
# print('Heapify: ', data2)
# print(heapq.heappop(data2))
# print('Pop:" ',data2)
# print(heapq.heappush(data2, -2))
# print('After push:" ', data2)

# print(heapq.heappush(data2, 7))
# print('Another push:" ', data2)

# print(heapq.heappushpop(data2, -7))
# print('Push pop:" ', data2)

# print(heapq.heapreplace(data2, -7))
# print('Push pop:" ', data2)

heap2 = []
data3 = [(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')]
data4 = [('J', 1, 3, 4), ('N', 4, 43, 35), ('H', 3, 534342,233,23,3,32,3), ('O', 2, 423,23,'fs', '56',3,2,1,5,6,7,8)]
for item in data3:
    heapq.heappush(heap2, item)

# print(heap2)
print(heapq.nlargest(4, heap))
print(heapq.nsmallest(3, heap))