# Выведите таблицу истинности 
# для выражения ¬(X ∧ Y) ∨ Z
def zadacha2():
    print(f'x|y|¬(X ∧ Y) ∨ Z')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                a = not(x and y) or z
                print(f'{x}| {y}| {z}|{int(a)}')
zadacha2()