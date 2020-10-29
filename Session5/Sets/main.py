#Sets
ages_in_class = {15, 16, 12, 13, 11, 18} 
print(ages_in_class)
print(len(ages_in_class))

#Accessing items (can't through indexing because it's random)
for x in ages_in_class:
  print(x)

if 20 in ages_in_class:
    print("There is a 15 year old in the class")
else:
    print("Your specified age is not in the class")

#Adding items
ages_in_class.add(14)
print(ages_in_class)

#Keep in mind, for adding duplicates are not allowed
ages_in_class.add(15)
print(ages_in_class)

#Removing items
ages_in_class.remove(16)
print(ages_in_class)

