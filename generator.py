def count(n):
    x=0
    while x<n:
        yield x
        x+=1
sum=0
for i in count(6):
    sum=sum+i
    print(sum)