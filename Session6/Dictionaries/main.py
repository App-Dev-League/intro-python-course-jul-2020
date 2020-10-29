#Dictionaries (like a list except the indices are what you choose)

age_translator = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

#Access items, keys, values
print(f"These are the items of the ageTranslator dictionary: {age_translator.items()}")
print(f"These are the keys of the ageTranslator dictionary: {age_translator.keys()}")
print(f"These are the values of the ageTranslator dictionary: {age_translator.values()}")

print()

#Only way to iterate over a dictionary
for key in age_translator:
    print(f"The value of {key} is {age_translator[key]}")
print(age_translator[:])
print()


