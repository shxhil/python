
# for row in range(1,5):
#     for i in range(5,0,-1):
#         print("#")
#         for col in range(row):# row number= #number
#          print("#",end=" ")
#     print()
for row in range(1,7):
    for space in range(7-row,1,-1):#space reduce while moving downwords
        print(end=" ")
    for st in range(row):#number of rows=no of cols
        print("*",end=" ") 
    print()