from re import*
# text="abababcdab"

# matcher=finditer("ab",text)
# count=0
# for m in matcher:
#     print(m.start(),m.group())
#     count+=1
# print(count)


# text="abcdABCD7e9fk"
# pattern="[0-9]"
# #       0123456789
# matcher=finditer(pattern,text)

# for m in matcher:
#     print(f"location ={m.start()} pattern matched={m.group()}")

#lowercase only

text="abcdABCD7e9fk"
pattern="[a-z]"
#       0123456789
matcher=finditer(pattern,text)

for m in matcher:
    print(f"location ={m.start()} pattern matched={m.group()}")
