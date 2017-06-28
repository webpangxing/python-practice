grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(grades):
    sum = 0
    for i in grades:
        sum += i
    return sum

def grades_average(grades):
    grade = grades_sum(grades)
    average = int(grade / len(grades))
    return average
print (grades_average(grades))