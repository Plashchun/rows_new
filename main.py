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
text = input("Введіть рядок: ")
if text.startswith("abc"):
  text = text.replace("abc", "www")#else:
  text += "qqq"
print(text)

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
