# Program to check below expression
# l = [1,2,3,4]
# print(l * 3) # Prints the same output
# l *= 3 # Prints the same output
# print(l)

# Program to find out error
# L1 = ["this", 'is', 'a', 'List']
# L2 = ["this", ["is", "another"], "List"]

# print(L1 == L2) #False
# print(L1.upper( )) # AttributeError: 'list' object has no attribute 'upper'
# print(L1[3].upper( )) # LIST
# print(L2.upper( )) # AttributeError: 'list' object has no attribute 'upper'
# print(L2[1].upper( )) # AttributeError: 'list' object has no attribute 'upper'
# print(L2[1][1].upper( )) # ANOTHER

# To check output
# L1 = [3, 4.5, 12, 25.7, [2, 1, 0, 5], 88]
# print(L1[2:len(L1)-1])
# print(L1[-2])
# print(L1[4:5])
# print(L1[1::2])

# To check using list function
# L1 = [3, 4.5, 12, 25.7, [2, 1, 0, 5], 88]
# print(L1.pop(4))
# print(L1.remove([2, 1, 0, 5]))
# del L1[4]
# print(L1[4:])

# Program to check o/p
# l = [1,3,5,7,9]
# print(l == l.reverse())
# print(l)

# Program to check o/p
# my_list= [ 'p', 'r', 'o', 'b', 'l' , 'e', 'm']
# my_list[2:3] = []
# print(my_list)
# my_list[2:5] = []
# print(my_list)

# Predict the o/p
# List1 = [13, 18, 11, 16, 13, 18, 13]
# print(List1.index(18)) 
# print(List1.count(18)) 
# List1.append(List1.count(13))
# print(List1)

# Predict the o/p
# Odd = [1,3,5]
# print( (Odd +[2, 4, 6])[4] ) # [1,3,5,2,4,6][4] = 4
# print( (Odd +[12, 14, 16])[4] - (Odd +[2, 4, 6])[4] ) # [1,3,5,12,14,16][4] - [1,3,5,2,4,6][4] = 14-4=10

# Predict O/p
# a, b, c = [1,2], [1, 2], [1, 2]
# print(a == b)
# print (a is b) 

# find out diff
# L1, L2 = [2, 4] , [2, 4]
# L3 = L2                 
# L2[1] = 5               
# print(L3) #[2,5]

# L1, L2 = [2, 4] , [2, 4]
# L3 = list(L2)
# L2[1] = 5
# print(L3) #[2,4]

#Find the errors:
# L1 = [1, 11, 21, 31]
# L2 = L1 + 2  # TypeError: can only concatenate list (not "int") to list
# L3 = L1 * 2
# Idx = L1.index(45)  # ValueError: 45 is not in list

# Predict O/P
# L1 = [3, 3, 8, 1, 3, 0, '1', '0', '2', 'e', 'w', 'e', 'r']
# print(L1[: :-1])
# print(L1[-1:-2:-3])
# print(L1[-1:-2:-3:-4]) # SyntaxError: invalid syntax

# Predict O/P
x = ['3', '2', '5']
y = ''
while x:
    y = y + x[-1]
    x = x[:len(x) - 1]
print(y)
print(x)
print(type(x), type(y))