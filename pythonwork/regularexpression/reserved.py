from re import*
text="abcd123KABC@#"
pattern="\D"#[]^0-9exceppt digit
# pattern="\d"#[0-9]digit only
# pattern="\w"#[a-zA-Z0-9]alpha numeric
# pattern="\W"#special character
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
