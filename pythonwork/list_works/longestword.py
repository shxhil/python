#longest word

text="hello good hello goodmorning"
word=text.split(" ") #['hello', 'good', 'hello', 'goodmorning']
# print(word)
longest_word=max(word,key=lambda w: len(w))     #key=(for make change in default setup here ascicode,to convert it to length)
print(longest_word)


