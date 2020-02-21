"""
1. To create a csv file
2. Append records
3. Display the file and the number of records
4. Calculate max, min and average ttot
5. Details of student with grade A1 or A2
"""

import csv

def create():
    with open('student.csv', 'x') as f:
        pass
    print()
    print('File created')
    print()
    
    
def append():
    with open('student.csv', 'a') as f:
        obj = csv.writer(f, lineterminator='\n')
        for i in range(4):
            roll = int(input('Enter roll no: '))
            name = input('Enter name: ')
            theo = float(input('Enter theory marks: '))
            prac = float(input('Enter practical marks: '))
            ttot = float(input('Enter total marks: '))
            grade = input('Enter grade: ')
            rec = [roll, name, theo, prac, ttot, grade]
            obj.writerow(rec)
    print()
    print('Records appended')
    print()


def display():
    with open('student.csv', 'r') as f:
        read = csv.reader(f)
        count = -1
        for i in read:
            print(i[0], i[1], i[2], i[3], i[4], i[5], sep='\t')
            count += 1
        print()
        print(count, 'records')
        print()


def ttot():
    with open('student.csv') as f:
        read = csv.reader(f)
        sum = count = max = 0
        min = 100
        for i in read:
            if i[0] != 'ROLL':
                sum += int(i[4])
                if int(i[4]) > max:
                    max = int(i[4])
                elif int(i[4]) < min:
                    min = int(i[4])
                count += 1
        print('Maximum and minimum ttot is ', max, ' and ', min)
        print('Average ttot is', sum / count)
        print()


def grade():
    with open('student.csv') as f:
        read = csv.reader(f)
        count = 0
        for i in read:
            if i[5] in ('A1', 'A2'):
                print(i[0], i[1], i[2], i[3], i[4], i[5], sep='\t')
                count += 1
        print('There were ', count, ' students')
        print()


print('''
1. To create a csv file
2. Append records
3. Display the file and the number of records
4. Calculate max, min and average ttot
5. Details of student with grade A1 or A2
6. Exit the menu
''')
opt = 0
while opt != 6:
    opt = int(input('Enter your option: '))
    if opt == 1:
        create()
    elif opt == 2:
        append()
    elif opt == 3:
        display()
    elif opt == 4:
        ttot()
    elif opt == 5:
        grade()
