
#common friend list
nivin_friends=["mohanlal","unny","fahad"]
fahad_friends=["mohanlal","mamooty","unny"]
common=[]
norepeat=[]
for i in nivin_friends:
    for i in fahad_friends:
        if i in nivin_friends and fahad_friends:
            common.append(i)
            # common.remove("mohanlal","unny")
print(common)