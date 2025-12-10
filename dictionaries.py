#Create a dictionary student with keys: "name", "age", "grade" and print the value of "name"
student = {'name' : 'sidhu', 'grade' : 'A+', 'age' :'21'}
print(student['name'])
#Add a new key "city" with value "Delhi" to the dictionary student.
#Update the "grade" of student to "A+".
student = {'name' : 'sidhu', 'grade' : 'B', 'age' :'21'}
student['city']= 'delhi'
student['grade'] = 'A+'
print(student['grade'])
#Remove the key "age" from the dictionary.
#Remove the last inserted item using a dictionary method.
student = {'name' : 'sidhu', 'grade' : 'B', 'age' :'21'}
student['city']= 'delhi'
student['grade'] = 'A+'
student.pop('age')
student.popitem()
print(student)
#Create a dictionary students containing two students, each represented as a dictionary with keys "name" and "age".
#Access the name of the second student.
students = {
    1:{ 'name' : 'sidhu', 'grade' : 'A+', 'age' :'21'} ,
    2:{ 'name' : 'shelin', 'grade' : 'C' , 'age' : '23'}
    }
print(students[2])
#Create a dictionary where keys are numbers from 5 to 7 and values are their squares.
squares = {}
for i in range(5, 7 + 1):
    squares[i] = i * i

print(squares)
