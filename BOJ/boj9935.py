# 9935 문자열 폭발 풀이

arr = list(input())
target = list(input())
stack = []
for i in range(len(arr)):
    stack.append(arr[i])
    #target 글자수 만큼 스택쌓였으면 target글자 인지 체크
    if i >= len(target) - 1:
        if stack[-1:-len(target) - 1:-1] == target[::-1]:
            for _ in range(len(target)):
                stack.pop()
if stack == []:
    print('FRULA')
else:
    print(''.join(stack))