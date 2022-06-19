# encoding: utf-8
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
def fact_display(n):
    i=0
    if n==1:
            print('fact(1)=1')
    else:
        print('fact(%d)='%n,end='')
        while((n-i)>1):
            print('%d*'%(n-i),end='')
            i+=1
        print('1=%d'%fact(n))

