from unicodedata import digit


num1 = int(input())
num2 = 0
while num1 > 0:
    digit = num1 % 10
    num1 = num1 // 10
    num2 = num2 * 10
    
    num2 = num2 + digit
print(num2)