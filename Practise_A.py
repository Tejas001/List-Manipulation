# Program to find minimum value
# l = [4,3,1,5,3,6]
# mini = idx =0
# for i,j in enumerate(l):
#     if i == 0:
#         mini = l[i]

#     if l[i] < mini:
#         mini = l[i]
#         idx = i
# print('Minimum value',mini, 'and its index value is ',idx)

# Program to print mean of given list
# l = eval(input('Enter a list in []: '))
# sum = mean = 0
# for i in l:
#     sum += i
# mean = sum/len(l)
# print(f'Mean of list is : {mean}')

# Program to search for an element in list
# l = eval(input('Enter a list: '))
# num = int(input('Enter a number to be searched: ')) 

# for i in range(len(l)-1):
#     if num == l[i]:
#         print(f'Element {num} found at index {i} in list {l}')
#         break

# Program to count frequency of a given element in list
# l = eval(input('Enter a list: '))
# cnt = 0
# d = {}
# for i in l:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(f'For Original list {l} its element frequency is count: {d}')

# a = [1,2,3]
# print(a*3)
# print(a+a+a)
# a[1:2] = [9] 
# a[1:1] = [4]
# print(a)

L = ["These", ["are", "a", "few", "words"], "that", "we", "will", "use"]
print(L[1][0::2])
print("a" in L[1][0])
print(L[:1] + L[1])
print(L[2::2])
print(L[2][2] in L[1])