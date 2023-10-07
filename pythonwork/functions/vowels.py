#vowels and consonents


def text(a):
    v_count=0
    c_count=0
    for i in range(len(a)):
        if a[i] in ["a","e","i","0","u"]:
            v_count+=1
        else:
            c_count+=1
    print(v_count)
    print(c_count)
a=input("enter the namer=")
text(a)