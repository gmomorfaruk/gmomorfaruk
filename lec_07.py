# -*- coding: utf-8 -*-
"""Lec-07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AR-wOu2J7ly3R2GaYnyObuEyvMJr2UeL
"""

fruits = 'bananas'
index = 0
while index < len(fruits):
  letter = fruits[index]
  print(index, letter)
  index+=1



fruits = 'bananas'
for letter in fruits:
  print(letter)

for letters in fruits:
  if letters == 'a':
    print(f"The letter {letters} is mathced.")
  else:
    print(f"The letter {letters} is not matched. ")

# fruits[1] = 'B'
print(fruits)
# it will show string cant assign a value

str1 = '222'
str2 = int(str1) + 1
print(str2)

str3 = str1 + str(1)
print(str3)

fruits = 'banana'
a = lambda fruits: [print(x) for x in fruits]
a(fruits)

str_ = 'Monty Python'
print(str_[::-1])

str_ = 'Monty Python'
print(str_[:-1])

str_ = 'Monty Python'
print(str_[-1])

def is_palindrome():
  n = input("Enter a number to check palindrome: ")
  if n == n[::-1]:
    print("It is  palindrome")
  else:
    print("Not palindrome")
is_palindrome()

word = 'Cipher'
key = 3
ceaser = ''
for i in word:
  ceaser += chr(ord(i)+3)
print(ceaser)

'n' in fruits

word = input("Enter a sentence: ")
if word>'Banana':
  print(word)
elif word<'Banana':
  print(word)
else:
  print("Alright  Banana")

str_ = 'aBc'
print(str_.lower())

dir(list)

dir(int)

dir(str)

dir(dict)

str_ = 'A brown fox jumps over the lazy dog'
print(str_.split())

str_ = 'A brown fox jumps over the lazy dog'
print(str_.split( ))
str1 = ''.join(str_)
print(str1)

str_ = 'A brown fox jumps over the lazy dog'
print(str_.split())
str1 = ' '.join(str_)
print(str1)



str_ = 'A brown fox jumps over the lazy dog'
print(str_.split('j'))

str_ = 'A brown fox jumps over the lazy dog'
print(str_.split('j')[0])

str_ = 'A brown fox jumps over the lazy dog'
print(str_.split())

dir(str)

fruits = 'he is a good boy.and i am not good'
print(fruits.capitalize())
# casefold
print(fruits.casefold())

#center
x = fruits.count('e')
print(x)

name = 'A good man'
list_ = name.split()
print(list_)
str_ = ' '.join(list_)
print(str_)

text = 'Apple Apple Apple is a fruit'
result = text.replace('Apple',"banana")
print(result)
result2 = text.replace('Apple',"banana",2)
print(result2)
result3 = text.replace('Apple','')
print(result3)
result4 = text.replace(" ","")
print(result4,len(result4))

text = "name=John;age=25;city=New York"
result = text.partition(';')
print(result)

#problem 1
sentence_ = 'i love my country'
without_space = sentence_.replace(" ","")
length = len(without_space)
print(length)
print(sentence_.capitalize())

while True:
    inp = input("Enter a number: ")
    if inp.isnumeric():
        print("Valid number entered!")
        break  # Exit the loop
    else:
        print("Try again")

str_ = 'sdkfjlks2323dddfd232j'
nst = ''.join(list(filter(lambda x: x.isdigit(),str_)))
print(nst)

Name = input("Enter a name with 'a': ")

if Name.startswith('a'):
  print("valid")
else:
  print("Not valid")

Name = input("Enter a name with 'a': ")

if Name.endswith('a'):
  print("valid")
else:
  print("Not valid")

from ast import Index
word = 'Lets go for a tour. '
i = 0
while i < len(word):
  if i % 2 != 0:
     print(word[i])
  i+=1

sen = input("Enter a sentence")
for index ,word in enumerate(sen):
  if index % 2:
    print(index, word)

sen = input("Enter a sentence")
sl =sen.split()
for index, word in enumerate(sl):
  if index % 2:
    print(index,word)
for index ,word in enumerate(sen):
  if index % 2:
    print(index, word)

sl = [word for index, word in enumerate(sen.spilt()) if index % 2]

colors = ["yellow", 'red','gray']
nl = list(filter(lambda x: x.startswith('g'),colors))
print(nl)