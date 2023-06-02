a = 'input_s1_01.txt'
f = open(a)
stuff = dict()
struct = dict()
was = []
line = f.readline().split()
while line[0] != 'END':
    struct[line[0]] = ''
    b = line[0]
    if b not in was:
        stuff[b] = ''
        was.append(b)
    if line[0] != ''.join(line):
        del line[0]
        stuff[b] = ' '.join(line)
        line.insert(0, b)
    else:
        if (stuff[b] == ''):
            stuff[b] = 'Unknown name'
    line = f.readline().split()
del was
del line
#####
f = open(a)
line1 = f.readline().split()[0]
line2 = f.readline().split()
while line1 != 'END':
    struct[line1] += line2[0] + ' '
    for key, value in struct.items():
        if line1 in value:
            struct[key] += line2[0] + ' '
    line1 = f.readline().split()[0]
    line2 = f.readline().split()
for key, value in struct.items():
    struct[key] = value.split()
    struct[key].sort()
    if struct[key] == []:
        struct[key] = 'NO'
b =' '.join(line2)
del line1
del line2

for key, value in stuff.items():
    if key == b or value == b:
        if struct[key] == 'NO':
            print('NO')
        else:
            for j in range(len(struct[key])):
                print(struct[key][j] + ' ' + stuff[struct[key][j]])
print()