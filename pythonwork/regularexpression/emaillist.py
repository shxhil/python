from re import*
f=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\regularexpression\\emailphnno.txt")
phone_rule="\d{10}"
mail_rule="\w+@gmail.com"
phone_num=[]
mail_ids=[]
for line in f:
    word=line.rstrip("\n").split()
    for w in word:
        matcher=fullmatch(phone_rule,w)
        email_matcher=fullmatch(mail_rule,w)
        if matcher!=None:
            phone_num.append(w)

        elif email_matcher!=None:
            mail_ids.append(w)

print(phone_num)
print(mail_ids)
        