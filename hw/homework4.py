# def get_discounts(prices: list[int], discount_percent: float):
#     result = []
#     for char in prices:
#         result.append(char * discount_percent)
#     # return result
    


# get_discounts([2, 4, 6, 11], 0.5)
# get_discounts([10, 20, 40, 80], 0.75)
# get_discounts([100], 0.45)

# def count_vowels(string: str):
#     if not isinstance(string, str):
#         raise ValueError("Параметр функцци 'string' должен быть str")

    
#     vowels = "aeiuo"
#     count = 0
#     for letter in string.lower():
#         if letter in vowels:
#            count += 1
#     return count


# print(count_vowels('tomatos') == 3)
# print(count_vowels("Celebration") == 5)
# print(count_vowels("Palm") == 1)
# print(count_vowels("Prediction") == 4)
# print(count_vowels("") == 0)
# print(count_vowels("234234234") == 0)
# print(count_vowels("FSDNFSNDVJBV{}WE{PEW3234}<fO") == 3)

# try:
#     count_vowels(10)
# except ValueError:
#     print(True)
#     pass
# except BaseException:
#     print(False)
# def count_points(string):
#     result = [0,0,0]
#     for char in string:
#         if char == "А":
#             result[0] += 1
#         elif char == "Б":
#             result[1] += 1
#         elif char == "В":
#             result[1] += 1
#     return result

# count_points("") == [0,0,0]

# def count_points(string):
#     result = {"A": 0,
#               "B": 0,
#               'C': 0}
    
#     for char in string:
#         if char in result:
#             result[char] += 1
#         else:
#             result[char] = 1

#     return result

# print(count_points(""))
# print(count_points('ADABDBCDCOOpPTTRKGKNKGJ'))
# def gimme_the_letters(string_):
#     string_ = string_.strip()
#     start = string_[0]
#     end = string_[-1]
#     result = ""

#     # start, end = string_.split('-')
#     alphabet = 'abcde...'
    

#     start_code = ord(start)
#     end_code = ord(end)
#     for code in range(start_code, end_code + 1):
#         result += chr(code)
#     print(result)
#     return result

# gimme_the_letters('a -d')
# gimme_the_letters(' d-   e ')

import string

 # 1. нао,орот заданный диапазон ,укв
#  2. большие буквы


# def gimme_the_letters(string_: str):
#     alphabet_lowercase = string.ascii_lowercase

#     start, end = string_.split('-')
#     is_reversed = False

#     if not ((start + end).islower() or (start + end).isupper()):
#         raise ValueError('Регистр диапазона букв должен быть одинаковым')

#     if start > end:
#         is_reversed = True
#         start, end = end, start

#     index_start = alphabet_lowercase.index(start.lower()) # 24
#     index_end = alphabet_lowercase.index(end.lower()) # 0

#     result = alphabet_lowercase[index_start:index_end+1]
#     if start.isupper():
#         result = result.upper()

#     if is_reversed:
#         return "".join(reversed(result))

#     return result




    

# print(gimme_the_letters("y-a"))
# print(gimme_the_letters("a-z"))
# print(gimme_the_letters("A-Y"))
# print(gimme_the_letters("Y-A"))
# print(gimme_the_letters("A-Z"))
# print(gimme_the_letters("a-Z"))