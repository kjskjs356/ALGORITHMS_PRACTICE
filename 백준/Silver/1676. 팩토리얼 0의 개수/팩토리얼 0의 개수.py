# 1676 팩토리얼 0의 개수

n = int(input())
def five_count(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt
    
print(five_count(n))