# my_tupple = (1,2,3)
# for item in my_tupple:
#     print(item)
# print(my_tupple.index(3))

# tupple_with_const = tuple(("apple","dsfsd"))
# print(tupple_with_const)
# a,b,c = (1,2,3)
# print(a,b,c)

## Set
my_set = {1,2,3}
# set2 = {[3,5,6]}
s3 = set(("hello",4))
# print(s3)

# for item in s3:
#     print(item)
# s3.add(5)

# s3.update([5,6])
# s3.remove(4)
# s3.discard(5)
# s3.pop()
# s3.clear()
# print(s3)

# a = {1,2,3}
# b = {2,4,5}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(b.difference(a))
# print(a.symmetric_difference(b))

a= {1,2}
b= {1,2,3}

print(a.issubset(b))
print(b.issubset(a))
print(a.isdisjoint({4,5}))