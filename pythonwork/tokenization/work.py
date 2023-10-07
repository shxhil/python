f_news=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\tokenization\\news")
f_stop=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\tokenization\\stopword")

stop_words={line.rstrip("\n") for line in f_stop }

news_set=set()

for line in f_news:#news line by line aayt idkkan
    word=line.split() #words aayt split cheyyan
    for w in word:
        news_set.add(w)

print(news_set.difference(stop_words))
