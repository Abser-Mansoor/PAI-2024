import numpy as np

student_dtype = np.dtype([
    ('name', 'U10'),    
    ('height', 'f4'),   
    ('class', 'U10')     
])

students = np.array([
    ('Abser', 5.5, '10A'),
    ('Bilal', 5.7, '10B'),
    ('Uneeb', 5.5, '10A')
], dtype=student_dtype)

sorted_students = np.sort(students, order=['class', 'height'])

print(sorted_students)
