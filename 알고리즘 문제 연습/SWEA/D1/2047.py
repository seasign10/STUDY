import sys
sys.stdin = open("2047.txt", "r")

text = input()
result = ''
for i in text:
    if i.islower:
        result += i.upper()
    else:
        result += i

print(result)