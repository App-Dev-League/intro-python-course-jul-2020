#Tuples (explain - immutable)
friend_birth = (2004, 2003, 2001, 2005, 2006)

#Indexing
print(friend_birth[0]) 
print(friend_birth[-1])
print(friend_birth[1:])
print(friend_birth[1:3])

#Immutable
friend_birth[0] = 2009 #(doesn't work)

#There is a way to perform these operations, but it is not recommended 
friend_birth = list(friend_birth)
friend_birth[2] = 2000
friend_birth = tuple(friend_birth)
print(friend_birth)

#When would you use tuples over lists? -- Data that won't be changed
