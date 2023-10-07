from json import load
from builtins import print#(eg)
path="C:\\Users\\kamoh\\Desktop\\pythonwork\\decision_making\\list_works\\modules\\read_fromjson\\data.json"
with open(path,encoding="utf-8")as f:
#to avoid close(with)    
    records=load(f)
    

# print(records)
f_names=[f.get("name") for f in records ]
# print(f_names)

#high rating

top_rating=max(records,key=lambda d: d.get("rating"))
# print(top_rating)