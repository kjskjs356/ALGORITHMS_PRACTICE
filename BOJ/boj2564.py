# 2564 경비원

mapx, mapy = map(int, input().split())
N = int(input())
store_location = []

for i in range(N):
    store_location.append(list(map(int, input().split())))

target_diret, target_location = map(int, input().split())
total = 0

# 동 서 남 북 4가지 경우의 수 확인
# 1: 북, 2: 남, 3: 서, 4: 동

def time_foward(sd, sl, td, tl): # 시계방향 이동 (sd, sl : 가게 방향(동서남북), 위치 / td, tl : 대상 방향, 위치)
    if td == 1: # 북쪽 시작
        if sd == 1: # 상점 북쪽
            if tl < sl:
                return sl - tl
            else:
                return 2 * mapy + mapx + sl
        elif sd == 4: # 상점 동쪽
            return (mapx - tl) + sl
        elif sd == 2: # 상점 남쪽
            return mapy + (mapx - tl) + (mapx - sl)
        elif sd == 3: # 상점 서쪽
            return (mapx - tl) + mapy + mapx + (mapy - sl)

    elif td == 4: # 동쪽 시작
        if sd == 1: # 상점 북쪽
            return (mapy - tl) + mapx + mapy + sl
        elif sd == 4: # 상점 동쪽
            if tl < sl:
                return sl - tl
            else:
                return 2 * mapx + mapy + sl
        elif sd == 2: # 상점 남쪽
            return (mapy - tl) + sl
        elif sd == 3: # 상점 서쪽
            return mapx + (mapx - tl) + (mapy - sl)

    elif td == 2: # 남쪽 시작
        if sd == 1: # 상점 북쪽
            return tl + mapy + sl
        elif sd == 4: # 상점 동쪽
            return tl + mapy + mapx + sl
        elif sd == 2: # 상점 남쪽
            if tl > sl:
                return tl - sl
            else:
                return 2 * mapy + mapx + sl
        elif sd == 3: # 상점 서쪽
            return tl + (mapy - sl)
    
    elif td == 3: # 서쪽 시작
        if sd == 3:
            if tl > sl:
                return tl - sl
            else:
                return (mapy - tl) + 2 * mapx + mapy + sl
        elif sd == 1:
            return tl + sl
        elif sd == 4:
            return tl+ mapx + sl
        elif sd == 2:
            return tl + mapx + mapy + (mapx - sl)

def time_reverse(sd, sl, td, tl):
    if td == 1:
        if sd == 1:
            if tl > sl:
                return tl - sl
            else:
                return tl + 2 * mapy + mapx + (mapx - sl)
        elif sd == 3:
            return tl + sl
        elif sd == 2:
            return tl + mapy + sl
        elif sd == 4:
            return tl + mapy + mapx + (mapy - sl)
    
    elif td == 3:
        if sd == 3:
            if tl < sl:
                return sl - tl
            else:
                return (mapy - tl) + 2 * mapx + mapy + sl
        elif sd == 2:
            return (mapy - tl) + sl
        elif sd == 4:
            return (mapy - tl) + mapx + (mapy - sl)
        elif sd == 1:
            return (mapx - tl) + mapx + mapy + (mapx - sl)

    elif td == 2:
        if sd == 2:
            if tl < sl:
                return sl - tl
            else:
                return (mapx - tl) + 2 * mapy + mapx + sl
        elif sd == 4:
            return (mapx - tl) + (mapy - sl)
        elif sd == 1:
            return (mapx - tl) + mapy + (mapx - sl)
        elif sd == 3:
            return (mapx - tl) + mapy + mapx + sl

    elif td == 4:
        if sd == 4:
            if tl > sl:
                return tl - sl
            else:
                return tl + 2 * mapx + mapy + (mapy - sl)
        elif sd == 1:
            return tl + (mapx - sl)
        elif sd == 3:
            return tl + mapx + sl
        elif sd == 2:
            return tl + mapx + mapy + sl

for i in range(len(store_location)):
    result = min(time_foward(store_location[i][0], store_location[i][1], target_diret, target_location), time_reverse(store_location[i][0], store_location[i][1], target_diret, target_location))
    total += result

print(total)