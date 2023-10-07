f=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\fileinput\\numbers.txt","r")
numbers=[i.rstrip("\n") for i in f]
tn_numbers=[num for num in numbers if num.startswith("tn")]
print(tn_numbers)                               #tn registration only
