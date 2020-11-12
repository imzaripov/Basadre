nt_func = lambda word: word.title() if word and ascii(word)[1:-1].isalpha() else ''
print(' _ '.join(map(nt_func, input("Enter phrase: ").split())))
