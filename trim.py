def trim(s):
    m=0
    n=-1
    while s[m]==' ':
          m+=1
    if m==len(s)-1:
        return ''
    else:
        if s[-1]==' ':
            return s[m:]
        else:
            while s[n]==' ':
              n-=1
        return s[m:n]



