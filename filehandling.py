row = [[]]
crimefile = open("students.csv", 'r')
for line in crimefile.readlines():
    tmp = []
    for element in line[:].split(','):
        tmp.append(element)
        row.append(tmp)
    print(tmp)