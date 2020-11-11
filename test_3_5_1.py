try:
    s = input()
    a = [int(x) for x in s.split()]
    print(a)
    print(sum(a))
except:
    print('повтор')
#
str = input('Ввéдите строку чисел, через пробел или q - чтобы выйти: ').split()
print(str)

#
s = input()
print(s)
b = s.split()
print(b)
print(list(map(int, s.split())))
a = list(map(int, s.split()))
print(sum(a))


