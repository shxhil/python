from json import load
path="C:\\Users\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\modules\\read_fromjson\\countries\\countries.json"
with open(path,encoding="utf-8") as f:
    country=load(f)

# print(len(country))

starts_withc=[c.get("name") for c in country if c.get("name").startswith("C")]
# print(starts_withc)

#same border sharing countries


#county and capital

name_capital=[[c.get("name"),c.get("capital")] for c in country]
# print(name_capital)

#maximum border sharing countries

# max_border=max(country,key=lambda c:len(c.get("borders")))
c_with_borders=[c for c in country if "borders" in c] #sort country whoes have borders
# print(c_with_borders)
max_border=max(c_with_borders,key=lambda c:len(c.get("borders")))
# print(max_border.get("name"),max_border)

#country names whoes border sharing with india,afghanisthan

#india borders only
# india_bord=[c.get("borders") for c in country if c.get("name")=="India"]
# print(india_bord)
# print(india_bord[0])#index[of]

india_bord=[c.get("borders") for c in country if c.get("name")=="Afghanistan"][0]
indiaborder_names=[c.get("name") for c in country if c.get("alpha3Code") in india_bord]
# print(indiaborder_names)

#regions of all country

all_region={c.get("region") for c in country}
# print(all_region)

#dependent countrys

depemdent=[c.get("name") for c in country if c.get("independent")==False]
# print(depemdent)

#population under 4lakh

population=[c.get("name") for c in country if c.get("population")<400000]
# print(population)


#regionwise