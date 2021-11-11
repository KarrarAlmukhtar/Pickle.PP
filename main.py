import pickle
names = []
grades = []
numStudents = int(input('How many students do you have? '))
for k in range(0, numStudents, 1):
    name = input('Please inter students name: ')
    names.append(name)
    prompt = 'Please inter ' + name + "'s grade: "
    grade = float(input('Please inter grade: '))
    grade = float(input(prompt))
    grades.append(grade)
with open('StudentData.pkl', 'wb') as dataK:
    pickle.dump(numStudents, dataK)
    pickle.dump(names, dataK)
    pickle.dump(grades, dataK)
with open('studentData.pkl', 'rb') as readF:
    a = pickle.load(readF)
    b = pickle.load(readF)
    c = pickle.load(readF)
print(a)
print(b)
print(c)
