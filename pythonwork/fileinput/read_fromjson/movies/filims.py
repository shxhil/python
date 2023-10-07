from json import load
path="C:\\Users\\kamoh\\Desktop\\pythonwork\\fileinput\\read_fromjson\\movies\\mdb.json"
with open(path,encoding="utf-8") as f:
    movies=load(f)

#total number of movies
# print(len(movies))

#name of movies

movie_names=[m.get("title") for m in movies]
# print(movie_names) #how to split and print names in list

#print movie title released in 2005

movie_title=[m.get("title") for m in movies if m.get("year")=="2005"]
# print(movie_title)

#print movie title whoes genre="comedy"

# for m in movies:
    # for g in m:
        # if g.get("generes")=="Comedy":
            # print(m.get("title"))   error ahn


fun_movies=[m.get("title") for m in movies if "Comedy" in m.get("genres")]
# print(fun_movies )              #list ayoond in movies n nookkum

#lengthy title

lengthy=max(movies,key=lambda m: int(m.get("runtime")))
# print(lengthy)

#print all geners
geners={g for m in movies for g in m.get("genres")}
# print(geners)
# for m in movies:
    # for g in m.get("geners"):
        # print(m.get("ge"))

#comedy movies released in 2015

movie=[m.get("title") for m in movies  if m.get("year")=="2015" and "Comedy" in m.get("genres")]
# print(movie)


#heighest movie released year
wc={}
for m in movies:
    year=m.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1 

# print(wc)

maximum=max(wc,key=lambda k:wc[k])
                    #k=key(illussion)
for i in movies:
   if maximum :
    print(wc)