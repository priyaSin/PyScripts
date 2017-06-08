""" You have a record of N students. Each record contains the student's name,
and their percent marks in Maths, Physics and Chemistry. The marks can be
floating values. The user enters some integer N followed by the names and marks
for N students. You are required to save the record in a dictionary data type.
The user then enters a student's name. Output the average percentage marks
obtained by that student, correct to two decimal places.

****Input Format****  

The first line contains the integer N , the number of
students. The next N lines contains the name and marks obtained by that
student separated by a space. The final line contains the name of a particular
student previously listed.

****Output Format**** 

Print one line: The average of the marks obtained by the
particular student correct to 2 decimal places.


****Constraints****

1. 2<=N<=10
2. 0<=Marks<=100
"""

#Input the number of students
print ("Enter the number of students in a class:")
n = int(input())
#Creating an empty dictionary
student_marks = {}
for i in range(n):
#Spliting input as name and list of marks
    print ("Input Name and marks of the student separated by space")
    name, *line = input().split()
    scores = list(map(float, line))
#Adding a key-value pair to the dictionary student_marks
    student_marks[name] = scores
print ("Input name of the student whose average marks is to be found")
query_name = input()
#Searching for a key and printing average 
for key in student_marks:
    if key==query_name:
        sum=0
        for marks in student_marks[key]:
            sum+=marks
        avg=sum/len(student_marks[key])
        print ("Average Marks of %s %.2f" %(key,avg))
        break
else:
    print ("Student Name Not Found.")



