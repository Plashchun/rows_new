#1
print ("Введіть слово")
slovo = input('')
i = slovo[:: -1]
if i == slovo:
    print('+')
else:
   print('-')
#2
print("Введіть текст і слово")
text = input(" ")
slovo = input(" ")
if slovo in text:
      print('Yes')
else:
      print('No')

#3
print("Користувач вводить рядок")
string = 'abcqwrrtt'
place = string.replace('abc', 'www')
just = (string + 'qqq')
if place in string:
    print(string)
else:
    print(just)
#3
string = 'abcbcrewer'
def f(string):
    if string[:3] == 'abc':
     string = 'www' + string[3:]
    else:
     string += 'qqq'
    return string
print(f(string))


#4
print("Користувач вводить текст")
text = 'eewrgr4654gfhj'
for i in text:
    if i.isalpha():
        print(i)

#5
print("Користувач вводить пошту")
email = input(" ")
if "@" in email and "." in email:
    print('YES')
else:
    print('NO')