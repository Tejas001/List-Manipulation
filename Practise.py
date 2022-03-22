# l = list('Hello')
# print(l)

# t = (1,2,3,4)
# print(list(t))

# l = list(input('Enter anything without space: ' ))
# print(l)

# l = eval(input('Enter a array of values within [ ] if you want to create int list: '))
# print(l)

# l = [1,2,3,4]
# print(l[0:2])
# print(l[-1])
# print(l[::-1])
# l[3] = 5
# print(l)

# l = ['p','y','t','h','o','n']
# for i in range(len(l)-1,-1,-1):
#     print(l[i])

# for i in range(len(l)):
#     print(f'Positive Index {i} , negative index {i-(len(l))} and its value {l[i]}')

# a = [1,2,3] * 2
# b = [4,5,6]
# c=a+b
# print(c)

# a = [1,2,3,4,5,6]
# print(a[2:-2])
# a[0]=0
# print(a)

# a = [1,2,3,4,5,6]
# print(a[3:10])
# print(a[-6:3])
# print(a[0:len(a)-1:2])
# print(a[::2])
# print(a[2::2])
# print(a[::-1])


# main_list = [i for i in range(1,20+1)]
# lst1 = main_list[5:15:2]
# lst2 = main_list[::4]
# print(lst2)
# sum = avg = 0
# for i in lst1:
#     sum += i
# print(f'For list {lst1} sum is {sum}')

# sum1 = 0
# for i in lst2:
#     sum1 += i
# avg = sum1/len(lst2)
# print(f'For list {lst2} avg is {avg}')

# a = ['1','2','3']
# a[0:2] = [1,2]
# print(a)


a = [1,1,2,3,4]
# a.append(5)
# del a[2:]
# print(a)
b = a
c = list(a)
# a[4:] = [1,2,3,4]
# print(a,b,c)
z=[5,6,7]
print(a.index(4))
a.extend(z)
a.insert(2,'3')
a.pop()
a.remove('3')
print(a.count(1))
a.reverse()
print(a)
a.sort()
print(a)