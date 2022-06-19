import math
print('每人按一个键，准备开始！')
letter1=input()
letter2=input()
num1,num2,num3=0,0,1
while num3:
    key_letter=input()
    if ke_letter==letter1:
        num1+=1
    else:
        num2+=1
    if math.abs(num1-num2)>=10 and num1-num2>0:
        print('%s胜出！'%letter1)
        num3=0
    if math.abs(num1-num2)>=10 and num1-num2<0:
        print('%s胜出！'%letter2)
        num3=0

        
    
      
