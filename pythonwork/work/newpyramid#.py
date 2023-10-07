# for row in range(4,1,-1):
#     for col in range(row,1,-1):
#         print("#",end="\t")
#     print()


for row in range(1,4):
    for col in range(4-row):
        print("#",end="\t")
    print()