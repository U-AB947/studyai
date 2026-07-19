

# Part A: Variables & Data Types
# Store the student's name as a string
name='Usman Abdulazeez'
# Store the student's age as an integer
age=20
# Store the student's CGPA as a float
cgpa=3.00
# Store whether the student is a Python student as a Boolean
is_python_student=True
# Print the type of each variable
print(type(name));print(type(age));print(type(cgpa));print(type(is_python_student))

# Part B: Lists
# Create a list of five gadgets
gadgets=['Laptop','Smartphone','Tablet','Smartwatch','Headphones']
# Print first and last gadgets
print(gadgets[0]);print(gadgets[-1])
# Add two gadgets
gadgets.append('Power Bank');gadgets.append('Bluetooth Speaker')
# Remove a middle gadget
gadgets.remove('Tablet')
# Print list length
print(len(gadgets))

# Part C: Tuples
# Create a tuple
coordinates=(10,20,30)
# coordinates[1]=99
# TypeError: tuple object does not support item assignment because tuples are immutable.
# Print last item
print(coordinates[-1])

# Part D: Dictionaries
# Create a student dictionary
student={'name':'Usman Abdulazeez','matric_no':'FCP/CIT/23/1041','department':'Information Technology','age':20}
# Print name and department
print(student['name']);print(student['department'])
# Add cgpa
student['cgpa']=3.00
# Update age
student['age']=21
# Print keys and values
print(student.keys());print(student.values())

# Part E: Mixed Practice
# Create a list of student dictionaries
class_list=[{'name':'Ali','score':80},{'name':'Amina','score':92},{'name':'Musa','score':88}]
# Print second student's name
print(class_list[1]['name'])
# Print last student's score
print(class_list[-1]['score'])