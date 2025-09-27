# print('Tom'.isalpha())
# print('Tom6'.isalnum())
# print('003'.isdecimal())
# print('034'.isdigit())
# print('0045'.isnumeric())
# print())


# for i in range(1, 51):
#     print(i * 11)

# count = 0
# n = 1
# while count <= 50:
#     if n % 11 == 0:
#         count += 1
#         print(n)
#     n += 1

# for n in range(10,100):
#     number_1 = n // 10 
#     number_2 = n % 10
#     if number_1 + number_2 == 7:
#         print(n)

# for n in range(10,100):
#     s = str(n) 
#     number_1 = int(s[0])
#     number_2 = int(s[1])
#     if number_1 + number_2 == 7:
        # print(n)


# for n in range(100, 1000):
#     sum_ = 0
#     for digit in str(n):
#         sum_ += int(digit)
#     if sum_ == 7:
#         print(n)


#def is_palindrome(string: str):
#    return "".join(reversed(string)) == string
#        #return string == string[::-1]



    
    

# print(is_palindrome('') == False)
# print(is_palindrome('123') == False)
# print(is_palindrome('12321') == True)
# print(is_palindrome('казак') == True)


#def is_palindrome(string: str) -> bool:
#    """Возвращает True, если string является палиндромом. False в ином случае."""
#    if string == "":
#        return False
    
#    left = 0
#    right = len(string)-1
    
#    for _ in range(len(string)):
#        if string[left] != string[right]:
#            return False
#        left += 1
#        right -= 1
        
#    return True


#print(is_palindrome('') == False)
#print(is_palindrome('123') == False)
#print(is_palindrome('12321') == False)
#print(is_palindrome('казак') == True)
#print(is_palindrome('1221') == True)

#a = [5,6,7]
#for item in a:

#for i in range(len(a)):
#	print(a[i])

#for n in range(0, 101):
#	if 


#def is_isogram(string: str):
#    #return len(set(string)) == len(string)
#    #for i in range(0, len(string)):
#    #    count = 0
#    #    for j in range(i, len(string)):
#    #        if string[i] == string[j]:
#    #            count += 1
#    #        if count > 1:
#    #            return False
#    #return True

#    #for char in string:
#    #    if string.count(char) > 1:
#    #        return False
#    #    else:
#    #        return True

#    result = ''
#    for char in string:
#        if char in result:
#            return False
#        result += char
#    return True
    

            

#assert is_isogram('helol') == False
#assert is_isogram('helo') == True


#name = 'Tommy'
#l = list(name)
#l.reverse()
#result = "".join(l)
#print(result)
