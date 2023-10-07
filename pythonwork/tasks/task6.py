# Write a program to check whether the character is vowel or no



char=str(input("enter=")).casefold()
vowels="a","e","o","i","u"
# w=sorted(vowels)
if char in vowels:
    print("vowel")
else:
    print("not vowel")