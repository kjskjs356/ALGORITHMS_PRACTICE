# 5373 큐빙
from collections import deque

def rotate_cube(command, arr):
    if command == 'U+':
        arr[0][5], arr[1][5], arr[2][5], arr[2][4], arr[2][3], arr[1][3], arr[0][3], arr[0][4] = \
        arr[0][3], arr[0][4], arr[0][5], arr[1][5], arr[2][5], arr[2][4], arr[2][3], arr[1][3]
        for _ in range(3):
            arr[3].append(arr[3].popleft())
    elif command == 'U-':
        arr[0][3], arr[0][4], arr[0][5], arr[1][5], arr[2][5], arr[2][4], arr[2][3], arr[1][3] = \
        arr[0][5], arr[1][5], arr[2][5], arr[2][4], arr[2][3], arr[1][3], arr[0][3], arr[0][4]
        for _ in range(3):
            arr[3].appendleft(arr[3].pop())
    elif command == 'D+':
        arr[6][5], arr[7][5], arr[8][5], arr[8][4], arr[8][3], arr[7][3], arr[6][3], arr[6][4] = \
        arr[6][3], arr[6][4], arr[6][5], arr[7][5], arr[8][5], arr[8][4], arr[8][3], arr[7][3]
        for _ in range(3):
            arr[5].appendleft(arr[5].pop())
    elif command == 'D-':
        arr[6][3], arr[6][4], arr[6][5], arr[7][5], arr[8][5], arr[8][4], arr[8][3], arr[7][3] = \
        arr[6][5], arr[7][5], arr[8][5], arr[8][4], arr[8][3], arr[7][3], arr[6][3], arr[6][4]
        for _ in range(3):
            arr[5].append(arr[5].popleft())
    elif command == 'F+':
        arr[3][5], arr[4][5], arr[5][5], arr[5][4], arr[5][3], arr[4][3], arr[3][3], arr[3][4] = \
        arr[3][3], arr[3][4], arr[3][5], arr[4][5], arr[5][5], arr[5][4], arr[5][3], arr[4][3]
        arr[3][6], arr[4][6], arr[5][6], arr[6][5], arr[6][4], arr[6][3], arr[5][2], arr[4][2], arr[3][2], arr[2][3], \
        arr[2][4], arr[2][5] = \
        arr[2][3], arr[2][4], arr[2][5], arr[3][6], arr[4][6], arr[5][6], arr[6][5], arr[6][4], arr[6][3], arr[5][2], arr[4][2], arr[3][2]
    elif command == 'F-':
        arr[3][3], arr[3][4], arr[3][5], arr[4][5], arr[5][5], arr[5][4], arr[5][3], arr[4][3] = \
        arr[3][5], arr[4][5], arr[5][5], arr[5][4], arr[5][3], arr[4][3], arr[3][3], arr[3][4]
        arr[2][3], arr[2][4], arr[2][5], arr[3][6], arr[4][6], arr[5][6], arr[6][5], arr[6][4], arr[6][3], arr[5][2], \
        arr[4][2], arr[3][2] = \
        arr[3][6], arr[4][6], arr[5][6], arr[6][5], arr[6][4], arr[6][3], arr[5][2], arr[4][2], arr[3][2], arr[2][3], \
        arr[2][4], arr[2][5]
    elif command == 'B+':
        arr[3][11], arr[4][11], arr[5][11], arr[5][10], arr[5][9], arr[4][9], arr[3][9], arr[3][10] = \
        arr[3][9], arr[3][10], arr[3][11], arr[4][11], arr[5][11], arr[5][10], arr[5][9], arr[4][9]
        arr[3][0], arr[4][0], arr[5][0], arr[8][3], arr[8][4], arr[8][5], arr[5][8], arr[4][8], arr[3][8], arr[0][5], arr[0][4], arr[0][3] = \
        arr[0][5], arr[0][4], arr[0][3], arr[3][0], arr[4][0], arr[5][0], arr[8][3], arr[8][4], arr[8][5], arr[5][8], arr[4][8], arr[3][8]
    elif command == 'B-':
        arr[3][9], arr[3][10], arr[3][11], arr[4][11], arr[5][11], arr[5][10], arr[5][9], arr[4][9] = \
        arr[3][11], arr[4][11], arr[5][11], arr[5][10], arr[5][9], arr[4][9], arr[3][9], arr[3][10]
        arr[0][5], arr[0][4], arr[0][3], arr[3][0], arr[4][0], arr[5][0], arr[8][3], arr[8][4], arr[8][5], arr[5][8], arr[4][8], arr[3][8] = \
        arr[3][0], arr[4][0], arr[5][0], arr[8][3], arr[8][4], arr[8][5], arr[5][8], arr[4][8], arr[3][8], arr[0][5], arr[0][4], arr[0][3]
    elif command == 'L+':
        arr[3][2], arr[4][2], arr[5][2], arr[5][1], arr[5][0], arr[4][0], arr[3][0], arr[3][1] = \
        arr[3][0], arr[3][1], arr[3][2], arr[4][2], arr[5][2], arr[5][1], arr[5][0], arr[4][0]
        arr[3][3], arr[4][3], arr[5][3], arr[6][3], arr[7][3], arr[8][3], arr[5][11], arr[4][11], arr[3][11], arr[0][3], arr[1][3], arr[2][3] = \
        arr[0][3], arr[1][3], arr[2][3], arr[3][3], arr[4][3], arr[5][3], arr[6][3], arr[7][3], arr[8][3], arr[5][11], arr[4][11], arr[3][11]
    elif command == 'L-':
        arr[3][0], arr[3][1], arr[3][2], arr[4][2], arr[5][2], arr[5][1], arr[5][0], arr[4][0] = \
        arr[3][2], arr[4][2], arr[5][2], arr[5][1], arr[5][0], arr[4][0], arr[3][0], arr[3][1]
        arr[0][3], arr[1][3], arr[2][3], arr[3][3], arr[4][3], arr[5][3], arr[6][3], arr[7][3], arr[8][3], arr[5][11], \
        arr[4][11], arr[3][11] = \
        arr[3][3], arr[4][3], arr[5][3], arr[6][3], arr[7][3], arr[8][3], arr[5][11], arr[4][11], arr[3][11], \
        arr[0][3], arr[1][3], arr[2][3]
    elif command == 'R+':
        arr[3][8], arr[4][8], arr[5][8], arr[5][7], arr[5][6], arr[4][6], arr[3][6], arr[3][7] = \
        arr[3][6], arr[3][7], arr[3][8], arr[4][8], arr[5][8], arr[5][7], arr[5][6], arr[4][6]
        arr[8][5], arr[7][5], arr[6][5], arr[5][5], arr[4][5], arr[3][5], arr[2][5], arr[1][5], arr[0][5], arr[3][9], arr[4][9], arr[5][9] = \
        arr[3][9], arr[4][9], arr[5][9], arr[8][5], arr[7][5], arr[6][5], arr[5][5], arr[4][5], arr[3][5], arr[2][5], arr[1][5], arr[0][5]
    elif command == 'R-':
        arr[3][6], arr[3][7], arr[3][8], arr[4][8], arr[5][8], arr[5][7], arr[5][6], arr[4][6] = \
        arr[3][8], arr[4][8], arr[5][8], arr[5][7], arr[5][6], arr[4][6], arr[3][6], arr[3][7]
        arr[3][9], arr[4][9], arr[5][9], arr[8][5], arr[7][5], arr[6][5], arr[5][5], arr[4][5], arr[3][5], arr[2][5], \
        arr[1][5], arr[0][5] = \
        arr[8][5], arr[7][5], arr[6][5], arr[5][5], arr[4][5], arr[3][5], arr[2][5], arr[1][5], arr[0][5], arr[3][9], arr[4][9], arr[5][9]
    return arr


T = int(input())
for tc in range(1, T + 1):
    cube = [deque(['.', '.', '.', 'w', 'w', 'w', '.', '.', '.', '.', '.', '.']),
            deque(['.', '.', '.', 'w', 'w', 'w', '.', '.', '.', '.', '.', '.']),
            deque(['.', '.', '.', 'w', 'w', 'w', '.', '.', '.', '.', '.', '.']),
            deque(['g','g','g','r','r','r','b','b','b','o','o','o']),
            deque(['g','g','g','r','r','r','b','b','b','o','o','o']),
            deque(['g','g','g','r','r','r','b','b','b','o','o','o']),
            deque(['.','.','.','y','y','y','.','.','.','.','.','.']),
            deque(['.','.','.','y','y','y','.','.','.','.','.','.']),
            deque(['.','.','.','y','y','y','.','.','.','.','.','.'])]
    # 회전 수
    n = int(input())
    rotate = input().split()
    for turn in rotate:
        cube = rotate_cube(turn, cube)
    for i in range(3):
        for j in range(3, 6):
            print(cube[i][j], end='')
        print()