#1+2+3+ ... + 100  START
sum = 0
for i in range(1,100+1,1):
    sum = sum + i
    print(sum)


# END




#1+3+5+ ... + 100   START
sum = 0
for i in range(1,100+1,2):
    sum = sum + i
    print(sum)

# END




#2+4+6+ ... + 100  START 
sum = 0
for i in range(2,100+1,2):
    sum = sum + i
    print(sum)


# END

# 1*1+2*2+3*3+ ... + 100  START
sum = 0
for i in range(1,100+1,1):
    sum = sum + i*i
    print(sum)


# END
    
    

import math
sum = 0
for i in range(1,100+1,1):
    sum = sum + pow(i*i)
    print(sum)
    


n = int(input("enter the value"))
sum = 0
for i in range(1,n+1,1):
    sum = sum+i
    print("1+2+3+....+",n,"=",sum );
    
    
n = int(input("enter the value"))
sum = 0 
for i in range(1, n+1,2):
    sum = sum+i
    print("1+2+3+....+",n,"=",sum )