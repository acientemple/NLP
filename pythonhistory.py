f=open('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\python.txt')
line=f.readline()
while line:
    print(line,end=' ')
    line=f.readline()
f.close()
