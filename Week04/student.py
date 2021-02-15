# Program to take in first and second names and append to student list 
# when finished entering names the student list is printed


students = []

# Enter firstname
firstName = input('Enter firstname (blank to Quit) : ').strip()

# while firstname is not blank, append to list
# enter bklank to exit the loop
while firstName != '':
    student = {}
    student['firstname'] = firstName
    lastName = input('enter lastname: ').strip()
    student['lastname'] = lastName
    students.append(student)
    firstName = input('Enter firstname of next (blank to quit): ').strip()

# Print the list of students in format firstname and lastname
print('Here are the students')
for currentStudent in students:
    print('{} {}'.format(currentStudent['firstname'], currentStudent['lastname']))
