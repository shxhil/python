text=input("enter 1 st word= ") #"bread"
word1=sorted(text)
out=input("enter 2 nd word= ") #"beard"
word2=sorted(out)
if word1==word2:
    print(" is anagram")
else:
    print("not anagram")