num=[2,5,9,1]
print(num)
num[2]=3
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} valores')
num.insert(2,4)
print(num)
num.pop(3)
print(num)
if 4 in num:
    num.remove(4)
    print(num)
else:
    print('Não tem numero 4')
