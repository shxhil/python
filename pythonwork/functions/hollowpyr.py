for row in range(1, 7):                  #1
    for sp in range(7 - row, 1, -1):       #7-1,1,-1 =6,1(0),-1  #7-2,1,-1=5,1,-1
        print(end=" ")
    for st in range(row):
        if st == 0 or st == row - 1 or row == 6:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()

    # if row+col=7 or col-row=5 or row==6