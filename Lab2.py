# fragmenty dotyczące rozwiązania poszczególnych zadań proszę oddzielić odpowiednimi komentarzami
import itertools
from array import *
import random
import numpy as np

# zadanie 2



def zad2():
  znaki = array('u')
  x = input("Podaj ilość znaków, które chcesz wpisać")
  for i in range(int(x)):
    a = input("Podaj kolejny znak, który chcesz dołączyć")
    znaki.append(a)

  print("Odwrócona tablica")
  znaki.reverse()
  print(znaki)


# zad2()

# zadanie 3

def zad3():
  liczby = array('f')
  a = int(-5)
  b = int(5)
  for i in range(5):
    liczby.append(random.uniform(a,b))
  file = open("result.txt", "w")
  file.write(str(liczby))
  file.close()

#zad3()

# zadanie 4

def zad4():
  x = np.array([2,3,4,5,6])
  for j in range(2,6):
    for i in range(5):
      x[j,i] = x[j,i]*x[j,i]
  print(x)

#zad4()

# zadanie 5

def zad5():
  nazwa = input("Podaj nazwe pliku:")
  plik = open(nazwa + ".txt")
  histogram = {}
  while 1:
    char = plik.read(1)
    if not char:
      break
    if(char in histogram):
      w=histogram.get(char)
      histogram[char] = w+1
    else:
      histogram[char]= 1
  plik.close()
  print(histogram)

#zad5()

# zadanie 6
def deck():
  deck = [('2','c'),('2','d'),('2','h'),('2','s'),('3','c'),('3','d'),('3','h'),('3','s'),('4','c'),('4','d'),('4','h'),('4','s'),('5','c'),('5','d'),('5','h'),('5','s'),('6','c'),('6','d'),('6','h'),('6','s'),('7','c'),('7','d'),('7','h'),('7','s'),('8','c'),('8','d'),('8','h'),('8','s'),('9','c'),('9','d'),('9','h'),('9','s'),('10','c'),('10','d'),('10','h'),('10','s'),('J','c'),('J','d'),('J','h'),('J','s'),('D','c'),('D','d'),('D','h'),('D','s'),('K','c'),('K','d'),('K','h'),('K','s'),('A','c'),('A','d'),('A','h'),('A','s')]
  return deck


def shuffle_deck(deck):
  random.shuffle(deck)
  return tuple(deck)

def deal(deck,n):
  lista =[]
  newdeck = shuffle_deck(deck)
  x=0
  for i in range(n):
    for j in range(5):
      lista.append(newdeck[x])
      x=x+1
  print(lista)

deal(deck(),2)
