from re import*
p=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\regularexpression\\phone.txt","w")
e=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\regularexpression\\email.txt","w")
path="C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\regularexpression\\emailphnno.txt"
with open(path,encoding="utf-8") as f:
    text=f.read()
# print(type(text))
data=text.split()
rule1="\d{10}"
rule2="\w+@(gmail.com)"
for w in data:
    # print(w)
    if fullmatch(rule1,w):
        p.write(w+"\n")
    elif fullmatch(rule2,w):
        e.write(w+"\n")