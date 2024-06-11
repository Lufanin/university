grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
x=len(grades[0])
a = grades[0]
b = a[0] + a[1] + a[2] + a[3] +a[4]
c = b/x # средний бал Aaron

z=len(grades[1])
d = grades[1]
e = d[0] + d[1] + d[2] + d[3]
f = e/z # средний бал Bilbo

y = len(grades[2])
g = grades[2]
h = g[0] + g[1] + g[2] + g[3]
i=h/y # средний бал Johnny

w =len(grades[3])
j= grades[3]
k = j[0] + j[1] + j[2]
l=k/w # средний бал Khendrik

v = len(grades[4])
m = grades[4]
n = m[0]+m[1]+m[2]+m[3]+m[4]
o = n/v # средний бал для Steve

students = list(students)
students[0]= 'Johnny', i
students[1]= 'Bilbo', f
students[2]= 'Steve', o
students[3]= 'Khendrik', l
students[4]= 'Aaron', c
students = set(students)
print(students)