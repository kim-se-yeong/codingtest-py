# https://www.acmicpc.net/problem/2309

# 1. 9명의 난쟁이의 키를 입력받는다.
# 2. 모든 난쟁이의 키 합을 구한다.
# 3. 두 명의 난쟁이를 뽑아서 빼면 된다.

_list = []
for i in range(9):
    _list.append(int(input()))

total = sum(_list) # 모든 난쟁이의 키 합
f1, f2 = 0, 0

for i in range(len(_list)):
    for j in range(i + 1, len(_list)):
        if total - (_list[i] + _list[j]) == 100:
            f1, f2 = i, j
            break

_list.pop(f2)
_list.pop(f1)

_list.sort()

for i in range(len(_list)):
    print(_list[i])

# _result = []
# for i in range(len(_list)):
#     if _list[i] == f1 or _list[i] == f2:
#         continue
#     else:
#         _result.append(_list[i])

# _result.sort()

# for i in range(len(_result)):
#     print(_result[i])