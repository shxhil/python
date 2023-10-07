#print years from 1800 to 2025

years=[y for y in range(1800,2026)] 
# print(years)

#print century years

century=[y for y in years if y%100==0 ]
# print(century)

non_century=[y for y in years if y%100!=0 ]
print(non_century)