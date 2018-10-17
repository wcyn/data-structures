from array import array

arr = array('i', [12, 34, 56, 34])

print("The new created array is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")

arr.append(3)


print("After appending : ", end="")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

arr.insert(2, 89)

print("After inserting : ", end="")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

print("\r")

print("Pop: ", arr.pop(2))
print("Array after popping: ", arr)

print("Remove: ", arr.remove(34))
print("Array after removing: ", arr)

print("Index of 34? ", arr.index(34))

print("Reversing: ", arr.reverse())
print("Array after reverse: ", arr)