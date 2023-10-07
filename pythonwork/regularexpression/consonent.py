from re import*
# text="abAcdefgKhij*&^5"
# pattern="[^aeiou]"

# word=finditer(pattern,text)

# for m in word:
#     if m.group().isalpha():
#         print(f"location={m.start()} consonents={m.group()}")

text="hellowthere@12"
pattern="[^aeiou\W\d]"
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())