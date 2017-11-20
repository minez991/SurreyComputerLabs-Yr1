lst = [1,2.2,"Why am I doing this",1+2j]
print(lst)
for x in range(0,len(lst)):  #Or the EVIL EVIL ISINSTANCE
    if type(lst[x]) == float:
        print("FLOAT HERE")
    
dic = {"A" : 90,
       "B" : 45,
       "C" : 22.5
       }

print(dic)
print(dic["A"])
