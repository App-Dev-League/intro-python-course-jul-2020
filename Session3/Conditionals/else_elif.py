#else statements
is_raining = True

if is_raining:
    print("It is raining")
else:
    print("It is not raining")

#elif statements

letter_a = 90
letter_b = 80
letter_c = 70
cur_grade = 87

if cur_grade > letter_a:
    print("You have an A in the class! Great job!")
elif cur_grade > letter_b: 
    print("You have a B in the class!")
elif cur_grade > letter_c: 
    print("You have a C in the class.")
else:
    print("You are not passing the class unfortunately... :(")