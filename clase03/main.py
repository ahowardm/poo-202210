from student import Student
from course import Course

my_course = Course('POO')
new_student = Student('Andres', 'Howard', 45)
other_student = Student('Vicente', 'Cuevas', 20)

my_course.add_student(new_student)
my_course.add_student(other_student)

my_course.list_students()

my_course.remove_student(other_student)

my_course.list_students()

# print(new_student.greet())
