all_users=["sachin","dhoni","kohli","rohit","sanju","padikkal"]

sanju_following=["padikkal","sachin"]
# suggestion=all_users.pop(sanju_following)
# all=set(all_users)
# sanju=set(sanju_following)
suggestion=set(all_users).difference(set(sanju_following))
new=list(suggestion)
sanju_possition=new.index("sanju")
new.pop(sanju_possition)

print(new)