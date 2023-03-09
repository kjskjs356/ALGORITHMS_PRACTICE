# 1085 직사각형에서 탈출

x, y, w, h = map(int, input().split())
print(min(abs(x), abs(w - x), abs(y), abs(h - y)))