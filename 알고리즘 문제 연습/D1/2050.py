import sys
sys.stdin = open("2050.txt", "r")

alpha = input()

for i in alpha:
    print(ord(i) - 64, end=' ')

# print(A)

# for idx, a in enumerate(alpha):
#     print(idx+1, end=' ')

# dic = {}
# for idx, a in enumerate(alpha):
#     dic.update({a: idx+1})
# print(dic)

# for val in dic.values():
#     print(val, end=' ')

# word = list(input())
# def my_swapcase(word):
#     result = ''
#     for char in word:
#         # 숫자로 바꿔야 함.
#         ascii_char = ord(char) # 아스키코드 숫자로 변경
#         if 65 <= ascii_char <= 90: # A ~ Z
#             result += chr(ascii_char+32) # 대문자에서 소문자로
#         elif 97 <= ascii_char <= 122: # a ~ z
#             result += chr(ascii_char-32) # 소문자에서 대문자로
#         else:
#             result += char
#     return result