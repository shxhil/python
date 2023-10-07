def swap(fn):
    def wrapp(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapp

@swap
def sub(n1,n2):
    return n1-n2

def div(n1,n2):
    return n1/n2

print(sub(5,10))