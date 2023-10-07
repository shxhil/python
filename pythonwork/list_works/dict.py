employ={"name":"hari","age":25,"experence":" 3 years","gender":"male","salary":25000}
# print(employ["salary"])
# print(employ)

if("salary" in employ):
    # print("present")
# else:
    # print("not present")
    employ["salary"]=200000
    employ["salary"]+=5000
    print(employ["salary"])