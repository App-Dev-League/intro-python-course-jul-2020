patients = {
    "Jane": [14, 23, 19],
    "John": [13, 14, 2],
    "Jackie": [18, 3, 10],
    "Brian": [6, 11, 5],
    "David": [12, 4, 9]
}

def max_visits_month(visits):
    max = -1
    for i in visits:
        for j in visits[i]:
            if j > max:
                max = j
    return max

def most_freq_visitor(visits):
    most_freq = ""
    max_visits_sum = -1
    for key, val in visits.items():
        sum = 0
        for i in val:
            sum = sum + i 
        if sum > max_visits_sum:
            max_visits_sum = sum
            most_freq = key
    return most_freq
            
print(f"The maximum number of visits from all patients in a single month is {max_visits_month(patients)}")
print(f"Most frequent visitor is {most_freq_visitor(patients)}")