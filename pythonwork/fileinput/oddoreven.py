f=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\fileinput\\oddeven.txt","w")
for i in range(1,600):
    f.write(str(i)+"\n")#int aayt idkkan pattula
#read(call)
f=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\fileinput\\oddeven.txt","r")

odd_num=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\fileinput\\odd.txt","w")
even_num=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\fileinput\\even.txt","w")





for i in f:
    if (int(i)%2==0):
        even_num.write(i)
    else:
        odd_num.write(i)
