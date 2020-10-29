#Nested Loops
for i in range(5):
    for j in range(5):
        print(f"The value of i is {i} and the value of j is {j}")

#Nested lists and loops
table = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

print(table)

for row in table:  
    print(row)
    for col in row:
        print(col)