# 
for i in range(1,101):
    count  = 0  
    for n in range(1, i + 1):
        if( i% n == 0):
            count = count + n
    if(count== 2):
            print(i)
    

# n = int(input("s"))
# count = 0
# for i in range(1, n + 1 ,7):
#     count = count + 1
#     print("1+3+5+...",n,'=',count)

# n = int(input("enter "))
# for num in range(1,n):
#     if(n % num) == 0:
#         break
#     else:
#         print(num)?>
                    #   n?>  