#If statements
is_raining = True
if is_raining: # can be rewritten as just is_raining
    print("It is raining today.")

age_threshold = 20
age = 13
if age < age_threshold:
    print("You are a very young programmer!")

#And, or, not operations
is_tall = True
is_handsome = False

if is_tall and is_handsome:
    print("You are tall and handsome")
if is_tall or is_handsome:
    print("You are either tall or handsome")
if not is_tall:
    print("You are not tall")


