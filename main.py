import random
a1 = random.randint(0, 3)
a2 = random.randint(0, 3)
b1 = random.randint(0, 3)
b2 = random.randint(0, 3)
print('Good luck!')
dict1 = {0: ['.', '.', '.', '.'],
         1: ['.', '.', '.', '.'],
         2: ['.', '.', '.', '.'],
         3: ['.', '.', '.', '.']}
dict1[a1].pop(a2)
dict1[a1].insert(a2, 2)
dict1[b1].pop(b2)
dict1[b1].insert(b2, 2)

for m in dict1.values():
    for k in m:
        print(k, end='  ')
    print('')
loop = True
score = 0

while loop:
    k = int(input('Insert something: '))
    score = score
    score1 = score
    if k == 1:
        for y, x in dict1.items():
            k = 0
            kl = x.copy()
            for m in kl:
                if m == '.':
                    x.remove('.')
                    k = k + 1
            for m in range(k):
                x.append('.')
            if x[3] == x[2] and x[1] == x[0] and type(x[3]) == int and type(x[1]) == int:
                score = score + int(x[1])*2 + int(x[2])*2
                x.insert(0, 2 * x[1])
                x.insert(1, 2 * x[3])
                x.insert(2, '.')
                x.insert(3, '.')
                x = x[:4]
            elif x[3] == x[2] and type(x[3]) == int:
                score = x[3]*2 + score
                x.insert(2, 2 * x[3])
                x.insert(3, '.')
                x = x[:4]
            elif x[2] == x[1] and type(x[2]) == int:
                score = score + x[2] * 2
                x.insert(1, x[2] * 2)
                x.pop(2)
                x.pop(2)
                x.append('.')
            elif x[1] == x[0] and type(x[1]) == int:
                score = score + x[1] * 2
                x.insert(0, x[1] * 2)
                x.pop(1)
                x.pop(1)
                x.append('.')
            k = 0
            dict1[y] = x
    if k == 2:
        for y, x in dict1.items():
            k = 0
            kl = x.copy()
            for m in kl:
                if m == '.':
                    x.remove('.')
                    k = k + 1
            for m in range(k):
                x.insert(0, '.')
            if x[3] == x[2] and x[1] == x[0] and type(x[3]) == int and type(x[1]) == int:
                score = score + x[3] * 2 + x[1] * 2
                v = x.pop(0)
                x.pop(1)
                d = x.pop(2)
                x.pop(3)
                x.append('.')
                x.append('.')
                x.append(v*2)
                x.append(d*2)

            elif x[1] == x[0] and type(x[1]) == int:
                score = score + x[1] * 2
                x.insert(1, 2 * x[1])
                x.insert(0, '.')
                x = x[:4]
            elif x[2] == x[1] and type(x[2]) == int:
                score = score + x[2] * 2
                x.insert(2, x[2] * 2)
                x.pop(3)
                x.pop(1)
                x.insert(0, '.')
            elif x[3] == x[2] and type(x[3]) == int:
                score = score + x[3] * 2
                x.insert(3, x[3] * 2)
                x.pop(4)
                x.pop(2)
                x.insert(0, '.')
            k = 0
            dict1[y] = x
    if k == 3:
        dict2 = {}
        for x, y in dict1.items():
            dict2[0] = dict2.get(0, []) + [y[0]]
            dict2[1] = dict2.get(1, []) + [y[1]]
            dict2[2] = dict2.get(2, []) + [y[2]]
            dict2[3] = dict2.get(3, []) + [y[3]]
        for y, x in dict2.items():
            k = 0
            kl = x.copy()
            for m in kl:
                if m == '.':
                    x.remove('.')
                    k = k + 1
            for m in range(k):
                x.append('.')
            if x[3] == x[2] and x[1] == x[0] and type(x[3]) == int and type(x[1]) == int:
                score = score + x[3] * 2 + x[1] * 2
                x.insert(0, 2 * x[1])
                x.insert(1, 2 * x[3])
                x.insert(2, '.')
                x.insert(3, '.')
                x = x[:4]
            elif x[3] == x[2] and type(x[3]) == int:
                score = score + x[3] * 2
                x.insert(2, 2 * x[3])
                x.insert(3, '.')
                x = x[:4]
            elif x[2] == x[1] and type(x[2]) == int:
                score = score + x[2] * 2
                x.insert(1, x[2] * 2)
                x.pop(2)
                x.pop(2)
                x.append('.')
            elif x[1] == x[0] and type(x[1]) == int:
                score = score + x[1] * 2
                x.insert(0, x[1] * 2)
                x.pop(1)
                x.pop(1)
                x.append('.')
            k = 0
            dict2[y] = x
        dict1 = {}
        for x, y in dict2.items():
            dict1[0] = dict1.get(0, []) + [y[0]]
            dict1[1] = dict1.get(1, []) + [y[1]]
            dict1[2] = dict1.get(2, []) + [y[2]]
            dict1[3] = dict1.get(3, []) + [y[3]]
    if k == 4:
        dict2 = {}
        for x, y in dict1.items():
            dict2[0] = dict2.get(0, []) + [y[0]]
            dict2[1] = dict2.get(1, []) + [y[1]]
            dict2[2] = dict2.get(2, []) + [y[2]]
            dict2[3] = dict2.get(3, []) + [y[3]]
        for y, x in dict2.items():
            k = 0
            kl = x.copy()
            for m in kl:
                if m == '.':
                    x.remove('.')
                    k = k + 1
            for m in range(k):
                x.insert(0, '.')
            if x[3] == x[2] and x[1] == x[0] and type(x[3]) == int and type(x[1]) == int:
                k = []
                score = score + x[3] * 2 + x[1] * 2
                k.insert(3, 2 * x[3])
                k.insert(2, 2 * x[1])
                k.insert(1, '.')
                k.insert(0, '.')
                x = k.copy()
            elif x[1] == x[0] and type(x[1]) == int:
                score = score + x[1] * 2
                x.insert(1, 2 * x[1])
                x.insert(0, '.')
                x = x[:4]
            elif x[2] == x[1] and type(x[2]) == int:
                score = score + x[2] * 2
                x.insert(2, x[2] * 2)
                x.pop(3)
                x.pop(1)
                x.insert(0, '.')
            elif x[3] == x[2] and type(x[3]) == int:
                score = score + x[3] * 2
                x.insert(3, x[3] * 2)
                x.pop(4)
                x.pop(2)
                x.insert(0, '.')
            k = 0
            dict2[y] = x
        dict1 = {}
        for x, y in dict2.items():
            dict1[0] = dict1.get(0, []) + [y[0]]
            dict1[1] = dict1.get(1, []) + [y[1]]

    dict1[2] = dict1.get(2, []) + [y[2]]
    dict1[3] = dict1.get(3, []) + [y[3]]
    list1 = []
    for d, l in dict1.items():
        for m in range(4):
            if l[m] == '.':
                list1.append((d, m))
    if len(list1) == 0:
        v = int(input(f'Game over! If you wanna play again press "Enter", if not press anything else! Your score is {score}'))
        if v == '':
            print('Good luck!')
            continue
        else:
            loop = False
            print('Thanks for playing!')
    a1 = random.randint(0, len(list1)-1)
    v = dict1[list1[a1][0]]
    v.pop(list1[a1][1])
    v.insert(list1[a1][1], 2)
    dict1[list1[a1][0]] = v
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    for m in dict1.values():
        list4.append(len(str(m[0])))
        list5.append(len(str(m[1])))
        list6.append(len(str(m[2])))
        list7.append(len(str(m[3])))

    v = max(list4)
    d = max(list5)
    c = max(list6)
    f = max(list7)
    for m in dict1.values():
        for k in range(4):
            if k == 0:
                print(str(m[k])+' '*(v - len(str(m[k]))), end='  ')
            if k == 1:
                print(' ' * (d - len(str(m[k]))) + str(m[k]), end='  ')
            if k == 2:
                print(' ' * (c - len(str(m[k]))) + str(m[k]), end='  ')
            if k == 3:
                print(' ' * (f - len(str(m[k]))) + str(m[k]), end='  ')
        print('')

    print('')
    print('')
    print(score)