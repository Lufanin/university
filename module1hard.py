students_sort = sorted(students)
grades_m =[sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),
           sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])]
a=dict(zip(students_sort,grades_m))
print(a)
