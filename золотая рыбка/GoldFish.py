a = 'input_s1_01.txt'
f = open(a)
n = int(f.readline())
words = []
for i in range(n):
    words.append(f.readline().replace('\n', ''))
n = int(f.readline())
beg = {'0': 0}
del beg['0']
for i in range(n):
    line = f.readline().split()
    beg[line[0]] = int(line[1])
n = int(f.readline())
end = {'0': 0}
del end['0']
for i in range(n):
    line = f.readline().split()
    end[line[0]] = int(line[1])
k = 0
s = 0
beglet = ''
endlet = ''
for i in range(len(words)):
    for j in range(len(beg)):
        if words[i][0] == list(beg.keys())[j] and beg[list(beg.keys())[j]] > 0:
            k += 1
            beglet = words[i][0]
    for j in range(len(end)):
        if words[i][-1] == list(end.keys())[j] and end[list(end.keys())[j]] > 0:
            k += 1
            endlet = words[i][-1]
    if k == 2:
        s += 1
        beg[beglet] -= 1
        end[endlet] -= 1
    k = 0
print(s)