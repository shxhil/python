f=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\fileinput\\year.txt","w")
for i in range(1800,2025):
    f.write(str(i)+"\n")
f=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\fileinput\\year.txt","r")
leap=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\fileinput\\leap.txt","w")
for i in f:
    if (int(i)%4==0 and int(i)%100!=0)or (int(i)%400==0):
        leap.write(i)
