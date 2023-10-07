from re import*
text="abcdABCD7e9fk".casefold()
pattern="[aeiou]"
#       
matcher=finditer(pattern,text)

for m in matcher:
    # print(f"location ={m.start()} pattern matched={m.group()}")
    print(m)