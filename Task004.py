# Задача 4. Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции 
# вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
import random

def shift_array(massif, n):   
   i=0
   j=0
   new_massif=[]
   while i<n:
      factor=massif[-(n-i)]
      new_massif.append(factor)
      i=i+1
   while i<len(massif):
      factor=massif[j]
      new_massif.append(factor)
      i=i+1
      j=j+1
   return new_massif

def zadacha4():
   number=int(input('Задайте количество элементов списка '))
   shift=int(input('Введите кол-во позиций на сколько должен список сместится вправо  '))
   array= random.sample(range(-number, number+1), number)
   print(f'Первоначальный массив: {array}')
   print(f'Со сдвигом на {shift} позиции(-ий): {shift_array(array, shift)}')    

zadacha4()
