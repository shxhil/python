text="hi is am hello good hello goodmorning"
word=text.split(" ") #['hello', 'good', 'hello', 'goodmorning']
# print(word)
mini_word=min(word,key=lambda w: len(w))  
print(mini_word)


#to overcom length issue sorted word
#smallest_sorted.py
