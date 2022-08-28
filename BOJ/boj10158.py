# 10158 개미
# 수많은 시간초과, 메모리초과 이후에 알게된 방법...

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 현 위치에서 t만큼 이동 후 필드의 가로, 세로 길이로 나누어
# 위(오른쪽)로가는 중인지 아래(왼쪽)로 가는 중인지 체크
x = (p + t) // w
y = (q + t) // h
# 몫이 짝수면 위쪽(오른쪽)으로 가는중, 홀수면 아래쪽(왼쪽)으로 가는 중
if x % 2 == 1:
    x = w - (p + t) % w
else:
    x = (p + t) % w
if y % 2 == 1:
    y = h - (q + t) % h
else:
    y = (q + t) % h
print(x, y)