#Given 2 arrays, create a function that lets a user know(true/false) whether
#these two arrays contain any common items
#For Example
# array1 = ['a','b','c','x']
# array2 = ['z','y','i']
#should return false
array1 = ['a','b','c','x']
array2 = ['z','y','x']
#should return true

#2 parameters - array1 and array2    -inputs
#return true or false   -output
# array1 = [1, 2, 3, 4, 5]
# array2 = [5, 6, 7, 8, 9]


#Answer -1 
#Naive Bruteforce method - Nested Loop
def checkMatchingValues(array1, array2):
    for j in array2:    #O(n)
        for i in array1:  #O(n)
            if i == j: 
                return True
    else:
        return False

# Calling the function with the example arrays
result = checkMatchingValues(array1=array1, array2=array2)
print(result)

#O(n*n) = O(n^2)  TC
#O(1)  SC
#code is not efficient 

#Answer -2
def checkMatchingValues2(array1, array2):
    for j in array2:    #O(n) 
            if j in array1: #O(1) per lookup so it will be O(m) 
                      return True
    else:
        return False
#O(n+m) = O(n) TC


# Calling the function with the example arrays
result = checkMatchingValues2(array1=array1, array2=array2)
print(result)


#Answer 3 
#can we assume always two arrays

def matchvalue(arr1, arr2):
    item_map = {}
    for j in arr1:  #O(a)
        if j not in item_map: 
            item_map[j] = True

    for i in arr2:
        if i in item_map: #O(b)
                return True

    return False

result = matchvalue(array1, array2)
print(result)

# time complexity = o(n)
# space complexity= O(n)