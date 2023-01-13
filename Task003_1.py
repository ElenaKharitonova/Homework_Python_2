# Задача 3. Даны две строки. Посчитайте сколько раз каждый 
# символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
phrase=input('Введите первую строку: ')
text=input('Введите вторую строку: ')
used=[]
for el in phrase:
    if el not in used:
        used.append(el)
        count = 0
        for letter in text:
            if letter == el:
                count += 1
    print(f'символ "{el}" встречается во второй строке {count} раз(а)') 