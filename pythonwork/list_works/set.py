# set() if it is empty
#set{10,20,30} if there is object
#mutable
#not preserved insertion order
# no duplication

# lst=[10,20,10,30,40,50,30]
# st=set(lst)
# print(st)
st={10,20,30}
st.add(100)
# print(st)
st.add("hello")
print(st)