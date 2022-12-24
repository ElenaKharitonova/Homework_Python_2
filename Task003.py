# Задача 3. Даны две строки. Посчитайте сколько раз каждый 
# символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
def zadacha3():
    phrase=input('Введите первую строку: ')
    text=input('Введите вторую строку: ')
    for i in range(0,len(phrase)): 
        print(f'символ "{phrase[i]}" встречается во второй строке {text.count(phrase[i])} раз(а)')
zadacha3()  