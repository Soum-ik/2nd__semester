#list operation in python 

dataValue = ["soumik",676095,"computer", True]
print(dataValue)

#tuple operation in python 
dataValue1 = ("soumik","soumik",676095,'soumik')
print(dataValue1)
#amar qestion ta hoita sa ja amra to jane ja tuple duplicate value accetep kora na tahol oi khana to mam "soumik"  ami 3 bar print korse  [oi khano mamm bolban]

#set operation in python 
dataValue2 = {"soumik",676095,"computer", True,"computer","soumik",676095,}
print(dataValue2)
#tuple r ja rqeqirment gula asa oi gula accepte korta sana but set a kaj korta sa

#dictonar operation in python 
dataValue3 = {"Name":"soumik","Roll":676095, "Department": "Computer", "Subject":"Python"}
print(dataValue3)



#Functions of list
Cursh = ['Soumik',"M.khalifa","D.Danial","Sunny leone","Dimond jakcson"]
print(len(Cursh))
print(type(Cursh))
print(Cursh[1])
print(Cursh[:1])

Cursh[1] = "Soumik"
Cursh[0:1] = ["Shakira"]

Cursh.append("lisa_blackpink")
print(Cursh)

Cursh.insert(1,"Dua_lipa")
print(Cursh)

Cursh.remove("Soumik")
print(Cursh)

Cursh.pop(3)
print(Cursh)

Cursh.sort()
print(Cursh)

Cursh.reverse()
print(Cursh)

Cursh.clear()
print(Cursh)

