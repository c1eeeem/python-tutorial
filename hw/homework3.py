# # string = " 32,Пр и вет  , ка8 к дела?"

# # result = []
# # i = 0
# # while not string[i].isalpha():
# #     result.append(string[i])
# #     i += 1

# # result.append(string[i].upper())
# # to_upper = True


# # for char in string[i+1:]:
# #     if char.isalpha():
# #         if to_upper:
# #             result.append(char.lower())
# #         else:
# #             result.append(char.upper())
# #         to_upper = not to_upper
# #     else:
# #         result.append(char)

# # print(''.join(result))

# # string = "дождливЫЙ, вечеР??"

# # result = ""
# # to_upper = True
# # first_char = True

# # for char in string:
# #     if char.isalpha():
# #         if first_char:
# #             result += char.upper()
# #             first_char = False
# #             continue
        
# #         if to_upper:
# #             result += char.lower()
# #         else:
# #             result += char.upper()
# #         to_upper = not to_upper
# #     else:
# #         result += char

# # print(result)





# # text = "hello worldx"
# # key = 3
# # result = ""

# # for char in text:
# #     if char.isalpha():
# #         if char.isupper():
# #             ascii_shift = ord("A")
# #         else:
# #             ascii_shift = ord("a")

# #         character_code = ord(char)
# #         shifted_code = (character_code - ascii_shift + key) % 26 + ascii_shift # доделай новый чартер
# #         new_character = chr(shifted_code)

# #         result = result + new_character
# #     else:
# #         result += char

# # print(result)

# # H 72 - character_code
# # A 65 - ascii_shift

# # 72 - 65 + 1 = 8

# text = "hello worldxyz%,"
# key = 4
# result = ""

# for char in text.lower():
#     if char.isalpha():
#         character_code = ord(char)
#         shifted_code = character_code + key
#         if shifted_code > 122:
#             shifted_code -= 26

#         new_character = chr(shifted_code)
#         result += new_character
#     else:
#         result += char

# print(result)



# text = "lipps asvphbcd%,"
# key = 4
# result = ""

# for char in text.lower():
#     if char.isalpha():
#         character_code = ord(char)
#         shifted_code = character_code - key
#         if shifted_code < 97:
#             shifted_code += 26

#         new_character = chr(shifted_code)
#         result += new_character
#     else:
#         result += char

# print(result)


# import homework4

# result = homework4.get_discounts([5, 9, 10, 4], 0.4)
# print('result', result)