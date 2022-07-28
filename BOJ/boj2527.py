# 2527 직사각형

rect = []
for _ in range(1):
    rect_len = (list(map(int, input().split())))
    rect.append(rect_len)

#한 줄씩 검토
for i in range(len(rect)):
    x1, y1 = set(list(range(rect[i][0], rect[i][2]+1))), set(list(range(rect[i][1], rect[i][3]+1)))
    x2, y2 = set(list(range(rect[i][4], rect[i][6]+1))), set(list(range(rect[i][5], rect[i][7]+1)))

    #'a' 케이스 => 가로, 세로 합집합 2이상
    if len(x1 & x2) >= 2 and len(y1 & y2) >= 2:
        print('a')

    #'b' 케이스 => 가로 2 이상 세로 1 혹은 가로1 세로 2이상, 한 선분만 겹침
    elif len(x1 & x2) >= 2 and len(y1 & y2) == 1 or len(x1 & x2) == 1 and len(y1 & y2) >= 2:
        print('b')
    
    #'c' 케이스 => 가로, 세로 둘다 1, 한 점만 겹침
    elif len(x1 & x2) == 1 and len(y1 & y2) == 1:
        print('c')
    
    #'d' 케이스 => 나머지 케이스 가로 세로 겹치는거 없음
    else:
        print('d')