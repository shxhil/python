text="hi is am hello good hello goodmorning"
word=text.split(" ") #['hello', 'good', 'hello', 'goodmorning']
srt_word=sorted(word,key=lambda w:len(w),reverse=True)
                                         #to print in descenting order(reverse=true)
print(srt_word)                                         