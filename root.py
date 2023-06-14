# This is how to find root of quadatie




# import math

# a = int(input("Enter the value of a:" ));
# b = int(input("Enter the value of b:" ));
# c = int(input("Enter the value of c:" ));

# d = b*b - 4*a*c

# if(d>0):
#     print("this is root value num");
#     x =(-b +math.sqrt(d) / 2*a);
#     y =(-b -math.sqrt(d) / 2*a);
#     print(x,y);          

# elif(d ==0 ):
#     print("this is root value");
#     z = (-b / 2*a)
#     print(z)

# else:
#     print("this way to not possible to root");
    


import math
a= int(input("enter number"))
b= int(input("enter number"))
c= int(input("enter number"))
d = (b*b - 4*a*c)
if(d>0):
    print("this is a root number")
    x = (-b +math.sqrt(d)/2*a)
    y = (-b -math.sqrt(d)/2*a)
    print(x,y)
elif(d<0):
    print("this is a root a value")
    z= (-b/2*a);
    print(z)
else:
    print("this is a not a root a number")