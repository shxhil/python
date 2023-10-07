f=open("C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\fileinput\\data.txt","r")
 #  // 2nnam od \ one in path
# lst=[] 
# for line in f:
#     # print(line)
#     lst.append(line.rstrip("\n"))
# # print(lst)
# longest_word=max(lst,key=lambda w:len(w))
# print(longest_word)


#list combrihention method(another method)

words=[line.rstrip("\n") for line in f]
longest_word=max(words,key= lambda w :len(w))
print(longest_word)