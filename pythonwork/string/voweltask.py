name="A headline is the title of a newspaper story, printed in large letters at the top of the story, especially on the front page"
word=name.split(" ")
vowels="a","e","i","o","u"

for w in word:
#    if w.casefold().startswith(vowels):
      if w[0].casefold() in vowels:
         print(w)
