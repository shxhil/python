text=input("enter the word=")
v_count=0
c_count=0
for ch in text:
    if ch in ["a","e","i","o","u"]:
        v_count+=1
    elif ch not in[" ",".","/","!"]:
        c_count+=1

print("vowels count",v_count)
print("consonent count",c_count)