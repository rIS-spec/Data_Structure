s ={1,3,5,5,5,7,"amex"}
e = set()  # dont use s = {} as it will creat an enpthy dictionary
print(s)
print(s, type(s))
s.add(999)
print(s, type(s))
s.remove(7)
print(s, type(s))
# s.clear(s)
# print(s, type(s))  # have a doubt this type
print(s.pop())

 
# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# set_difference = s1 - s2
# print(set_difference)


# s1 = {1,3,5,9}
# s2 = {2,4,5,8,9,1,6}
# print(s1.union(s1))

# print(s1.intersection(s2))
