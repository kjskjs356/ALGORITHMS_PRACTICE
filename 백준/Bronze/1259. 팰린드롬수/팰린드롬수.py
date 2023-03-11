# 11259 팰린드롬수

while True:
    num = input()
    if int(num) == 0:
        break
    num2 = num[::-1]
    if num == num2:
        print('yes')
    else:
        print('no')