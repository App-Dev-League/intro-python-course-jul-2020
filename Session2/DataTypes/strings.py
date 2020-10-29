#Strings
name = "Krish"
print(name)
print(type(name))

#Indexing and Slicing
print(name[0])  
print(name[4])
print(name[2:4]) #get characters from 2 to 4 (not included)
print(name[-1]) #gets last index
print(name[-2]) #gets second to last index
print(name[:]) #gets whole string

#Length
print(len(name))

#Common String methods
print(name.index("K"))
print(name.replace("Krish", "Bob")) #these give copies and does not modify name
print(name.lower()) 
print(name.upper())
