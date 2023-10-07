all_users=["mohanlal","fahad","unny","mamooty","nivin"]

nivin_friend=["mohanlal","unny","fahad"]
req=0
suggestion_list=[]
for u in all_users:
    if u not in nivin_friend:
        suggestion_list.append(u)
suggestion_list.pop(suggestion_list.index("nivin"))
#suggestion_list.remove("nivin)"
print(suggestion_list)