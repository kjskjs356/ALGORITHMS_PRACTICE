# 1206 view 풀이
# 2022-08-08

import sys
sys.stdin = open('input.txt','r')

#조망 확보가능한 인덱스에서 조망 칸 수 계산
def func_max(arr ,idx):
	if arr[idx - 1] > arr[idx - 2]:
		max1 = arr[idx - 1]
	else:
		max1 = arr[idx - 2]
	if arr[idx + 1] > arr[idx + 2]:
		max2 = arr[idx + 1]
	else:
		max2 = arr[idx + 2]
	if max1 >= max2:
		return arr[idx] - max1
	else:
		return arr[idx] - max2
# 길이 구하는 함수
def func_len(arr):
	cnt = 0
	for _ in arr:
		cnt += 1
	return cnt

for tc in range(1, 11):
	#test 다 받아오기
	T = int(sys.stdin.readline())
	arr = list(map(int, sys.stdin.readline().split()))
	#문제 풀이
	result = 0
	for i in range(2, func_len(arr) - 2):
		if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
			result += func_max(arr, i)
	print(f'#{tc} {result}')