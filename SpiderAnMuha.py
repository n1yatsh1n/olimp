f = open('test.txt')
p = f.readline().split(' ')
s = f.readline().split(' ')
m = f.readline().split(' ')
r = ((int(s[0])-int(m[0]))**2 + (int(s[1])-int(m[1]))**2 + (int(s[2])-int(m[2]))**2) ** 0.5
