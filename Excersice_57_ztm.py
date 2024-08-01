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

def checkmatching(array1, array2):
    for j in array2:    
        for i in array1:  
            if i == j: 
                return True
    else:
        return False

# Calling the function with the example arrays
result = checkmatching(array1=array1, array2=array2)
print(result)