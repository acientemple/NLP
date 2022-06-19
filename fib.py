def fib(n):
    f,a,b=0,0,1
    while b<n:
      print(f+1,':',b)
      a,b=b,a+b
      f=f+1