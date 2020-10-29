numbers = [1, 2, 3, 4, 5]
names = ["Bob", "Jill", "Jack", "Jim"]

#Append
names.append("Jack")
print(names)

#Insert
names.insert(2, "Jeff")
print(names)

#Remove
names.remove("Jeff")
print(names)

#Counting occurences
print(names.count("Jack"))

#Sort
numbers.sort()
names.sort()

print(numbers)
print(names)

#Reverse
numbers.reverse()
print(numbers)

#Clear
names.clear()
print(names)