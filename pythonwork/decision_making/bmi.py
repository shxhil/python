height_incm=165
weight_inkg=68

height_inm=height_incm/100
bmi=weight_inkg//height_inm**2
print(bmi)

if(bmi<19):
    print("underweight")
elif(bmi<=25):
    print("normal weight")
elif(bmi<=30):
    print("over weight")
else:# lessthan 30
    print("obisity")
    