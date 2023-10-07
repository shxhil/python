foods=[
    {"id":1,"name":"ghee-roast","price":70,"category":"veg","avl":12},
    {"id":2,"name":"chicken-roast","price":170,"category":"non-veg","avl":0},
    {"id":3,"name":"cb","price":170,"category":"non-veg","avl":10},
    {"id":4,"name":"bb","price":190,"category":"non-veg","avl":13},
    {"id":5,"name":"fried-rice","price":140,"category":"veg","avl":0},
    {"id":6,"name":"chicken-friedrice","price":170,"category":"non-veg","avl":15},
    {"id":7,"name":"nan","price":70,"category":"veg","avl":15},
    {"id":8,"name":"alfham","price":370,"category":"non-veg","avl":0},
     
]
# print non veg items in stock
stock=[ f for f in foods if f.get("category")=="non-veg"]
avl=[i.get("name")  for i in stock if i.get("avl")>0]
# print(avl)
# for f in  avl:
    # print(f["name"],f["price"])
                    

# total number of items
# print name whose category = veg
# food names available under rs 100
# costly item
# costly non-veg food

# length=len(foods)
# # print(length)


# category=[f.get("name") for f in foods if f.get("category")=="veg" ]
# # print(category)

# rupees=[f.get("name") for f in foods if f.get("price")<100]
# # print(rupees)

# costly=max(foods,key= lambda i:i.get("price"))
# # print(costly)

# costly_non=[f for f in foods if f.get("category")=="non-veg"]
# cost=max(costly_non,key= lambda i: i.get("price"))
# print(cost)

# veg=[i for i in foods if i.get("category")=="veg"]
# costly=min(veg,key=lambda i:i.get("price"))
# print(costly)



#print all category

catogries={f.get("category") for f in foods}
print(catogries)