# Program that reverses array of integer
# l = eval(input('Enter a list: '))
# print(f'Original list is {l}')
# rev_l = []
# for i in range(len(l)-1,0-1,-1):
#     rev_l.append(l[i])

# print(f'Reverse list is {rev_l}')

# Program to create a third list
# l1 = eval(input('Enter a first list: '))
# l2 = eval(input('Enter a second list: '))
# l3 = l1+l2
# print('First list',l1,'Second list',l2,'Third list',l3)

# Program to replace elements greater than 10 with 10
# l = eval(input('Enter a list between 1 and 12: '))
# for i in range(len(l)-1):
#     if l[i] >=10:
#         l[i] = 10 

# print('List after replacing list ',l)

# Program to enter string and create new list by removing first char
# s = eval(input('Enter a string: '))
# s1 = []
# for i in range(len(s)):
#     s1.append(s[i][1:])
# print('New List: ',s1)

# Program to create list using for loop
# l1 = []
# for i in range(0,50):
#     l1.append(i)
# print(l1)

# l2 = []
# for i in range(1,51):
#     l2.append(i*i)
# print(l2)

# l3 = []
# for i in range(1,27):
#     l3.append(chr(i+96)*i)
# print(l3)

# Program that takes 2 lists and adds the element them and store O/P in another list
# l = eval(input('Enter a list1: '))
# m = eval(input('Enter a list2: '))
# n = []
# for i,j in zip(l,m):
#     n.append(i+j)
# print(f'New list with addition: {n}')

# Program to rotate elements of list
# l = eval(input('Enter a list: '))
# print(f'Original list {l}')
# l = l[-1:] + l[:-1]
# print(f'Rotated same list: {l}')

# Program to print fibonacci series
# n = int(input("Enter n: "))

# if (n > 20):
#     print("n should be less than or equal to 20")
# else :
#     a = 0
#     b = 1
#     c = a + b
#     for i in range(3, n + 1):
#         a = b
#         b = c
#         c = a + b

#     print(n, "term of Fibonacci series =", c)

# n = int(input('Enter a number for fib series: '))
# a = 0
# b = 1

# if n ==0:
#     print(a)
# elif n == 1:
#     print(a,b)
# else:    
#         print(a,end=' ')
#         print(b,end=' ')
# for i in range(n):
#     c = a+b
#     a = b
#     b = c
#     print(b,end=' ')

# Program as per following specifications:

'''L is a list of numbers. Print a new list where each element is the corresponding element of list L summed with number num.'''
l = eval(input('Enter a list: '))
num = int(input('Enter a number to be summed: '))
nl = []
for i in l:
    nl.append(i+num)
print('Original list',l,' and summed list ',nl)