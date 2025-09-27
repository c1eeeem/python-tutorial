# str1 = "abc83cde7 1 b 24 4566"
# str2 = 'порог порох порок солнце вода поро'
# phone = "+380987685639 ukraine +380567941253 greece +486789809 poland"

# result = []
# number = ""

# for char in str1:
#     if char.isdigit():
#         number += char
#     else:
#         if number:
#             result.append(int(number))
#             number = ""

# if number:
#     result.append(int(number))

# print(result)


# import re

# # result = re.findall("c{\d+}", str1)
# # print(result)

# # result = re.findall("поро[а-я]", str2)
# # print(result)

# result = re.findall("\+380\d{9}", phone)
# print(result)
# re.split()

# str.split()


# str2 = '---порог порох порок солнце вода поро------'
# # print(str2.title())
# print(str2.find('вода', 0, 10))
# if str2.find('вода') == -1:



# str2 = str2.strip('-')
# words: list[str] = str2.split()
# words.reverse()
# result = " ".join(words)

# count = 0
# for word in words:
#     if word.startswith('поро'):
#         count += 1
# result = " ".join(words)

# print(count)

# print(str2.split("о",3))
# print(str2.lstrip('-'))

# words = ["Порох","Порок","Солнце","ВОДА"]

# result = "=".join(words)
# print(result)


# n = int(input("Введите число: "))
# print('-' * n)



# print("".join([str(_) for _ in range(n)]))


# str2 = '24234234fggfh'
# print(str2.title())
# a = 'hello'
# a += 't'

# print(str2. count('поро'))
# print(str2.replace("п", 'р'))

# if not str2.isdigit():
#     print('+')

# if str2:
#     print('+2')

# str1 = " a   hello   world656people,word "
# in_word = False

# count_words = 0
# for char in str1:
#     if char.isalpha() and not in_word:
#         count_words +=1
#         in_word = True
#     elif not char.isalpha():
#         in_word = False



# print(count_words)
