""" Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names
alphabetically and print each name on a new line."""

arr=[]
lowest=100
seclowest=100
for i in range(int(input("Enter the number of students in Physics class: "))):
    print ("Enter the name of student number"+str(i))
    name = input()
    print ("Enter the score of "+name)
    score = float(input())
    if score<lowest:
        lowest,seclowest=score,lowest
    elif score>lowest and score<seclowest:
        seclowest=score
    arr.append([name,score])
    arr.sort()
print ("The following students have the second lowest scores:")
for row in arr:
    if row[1]==seclowest:
        print (row[0])
