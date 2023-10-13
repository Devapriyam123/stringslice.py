#string slicing

name = "devapriyam"
print(name[0:4])
print(name[1:5])
print(name[ : ])
print(name[1:])

#reverse a string

name = "safari"
str = (name[::-1])
print(str)

# reverse a string without slicing

name = "devapriyam"
str = "".join(reversed(name))
print(str)

# reverse a list items

names = list(("deva","priyam","prasad"))
print(names[::-1])