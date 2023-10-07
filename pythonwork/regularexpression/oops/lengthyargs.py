max_word=("hello","goodmorning","evening")
max_word=("hello","evening")

def max_word(*args):
    length_word=max(args,key= lambda w: len(w))
    return length_word

print(max_word("hello","goodmorning","evening"))