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

#O(n*n) = O(n^2)
#code is not efficient 

#Answer -2
def checkMatchingValues2(array1, array2):
    for j in array2:    #O(n) 
            if j in array1: #O(1) per lookup os it will be O(m) 
                      return True
    else:
        return False
#O(n*m) = O(n^2)

# Calling the function with the example arrays
result = checkMatchingValues2(array1=array1, array2=array2)
print(result)


#Answer 3 
def contains_common_item(arr1, arr2):
    # Create a dictionary to store items from the first array
    item_map = {}
    
    # Loop through the first array and add items to the dictionary
    for item in arr1:
        if item not in item_map:
            item_map[item] = True   #O(n)
    
    # Loop through the second array and check if any item exists in the dictionary
    for item in arr2:
        if item in item_map:
            return True         #O(N)

    return False



#can we assume always to arrays
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