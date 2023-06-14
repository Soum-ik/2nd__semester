""" This program is creat for the value of result""" 
        Bangla = int(input("value of bangla result"))
        English = int(input("value of bangla result"))
        Math = int(input("value of bangla result"))
        Chemistry = int(input("value of bangla result"))
        Python = int(input("value of bangla result"))

        Total_value = ((Bangla+English+Math+Chemistry+Python) / 5)
        if(Total_value >= 80):
            print("1st semester you got A+")
        elif(Total_value >= 75):
            print("1st semester you got A")
        elif(Total_value >= 60):
            print("1st semester you got B")
        elif(Total_value >= 50):
            print("1st semester you got C")
        elif(Total_value >= 40):
            print("1st semester you got D")
        else:
            print("Sorry you are not continue to the 2nd semester")