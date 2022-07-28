f=open('m_table.txt','w')
for i in range(1,10):
    for j in range(1,i+1):
        print('%d × %d = %d'%(j,i,i*j),end='\t')
        print('%d × %d = %d'%(j,i,i*j),end='\t',file=f)
    print('\n')
    print('\n',file=f)
f.close()