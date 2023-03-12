# introduce lists
list = [20, 30, 40];
print(list[1])

# +- indexes, OutOfBound error
print(list[1], list[-1], list[len(list) - 1])

# list slices
print(list[0:2])

# changing list
list[0] = 100
print(list)

list.append(123)
print(list)

list.append([1,2,3])
print(list)
list.pop()

list.extend([1,2,3])
print(list)

val = list.pop()
print(list, val)

list.insert(2, 32)
print(list)

# copy list
list1 = list.copy()

# some other function
sum(list)
(list)

# iterating list in loop
for val in list:
    print(val)
    
for val in range(0, len(list)-1):
    print(val)
    
for ix, val in enumerate(list):
    print(ix)
    
# multidimentional arrays

matrix = [
    [1,2], 
    [3,4]
    ]
print(matrix[0][0])
