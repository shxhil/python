
# def add(*args):      tupple aaayt idkm
#         return sum(args)

# print(add(10,20,30))    


def product(*args):
    res=1
    for n in args:
        res*=n
    return res
    

print(product(5,2,3,4,5))