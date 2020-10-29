#Functions
def test():
    print("Hello World")

test()

#Parameters
def introduction(name, age):
    print(f"This is {name} who is {age} years old")

introduction("Jeff", 15)

#Return 
value = pow(4, 2) #4 squared which is 16
print(value)

def exponent(base, exp):
    finalAnswer = 1
    for i in range(exp):
        finalAnswer *= base
    return finalAnswer

exp = exponent(4, 2)
print(exp)