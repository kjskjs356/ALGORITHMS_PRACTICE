# 1242_암호코드 스캔 풀이
# 2022-09-20

hex = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

ratio = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}


def hex_change(arr):
    result = ''
    for i in range(len(arr)):
        result += hex[arr[i]]
    return result


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().strip().split())
    field = list(set(input().strip() for _ in range(N)))
    field.sort()
    field.pop(0)
    result = 0
    numbers = []
    for arr in field:
        tmp = ''
        binary_code = hex_change(arr).lstrip('0') + '0'
        odd = even = 0
        cnt = 0
        n1 = n2 = n3 = 0
        for i in range(len(binary_code)):
            if binary_code[i] == '1' and n2 == 0:
                n1 += 1
            elif binary_code[i] == '0' and n1 != 0 and n3 == 0:
                n2 += 1
            elif binary_code[i] == '1' and n2 != 0:
                n3 += 1
            elif n3 != 0:
                cnt += 1
                m = min(n1, n2, n3)
                secret = ratio[(n1 // m, n2 // m, n3 // m)]
                tmp += str(secret)
                if cnt == 8:
                    if (odd * 3 + even + secret) % 10 == 0 and tmp not in numbers:
                        result += odd + even + secret
                    numbers.append(tmp)
                    even = odd = cnt = 0
                    tmp = ''
                elif cnt % 2 == 0:
                    even += secret
                else:
                    odd += secret
                n1 = n2 = n3 = 0
    print('#{} {}' .format(tc, result))