number = [7, 10, 22, 4, 3, 17]

## 합구하기 sum()

sum = 0

for i in number:
    sum += i

print(sum)  ## 63

## 최댓값 구하기

maxV = number[0]
for i in number:
    if i > maxV:
        maxV = i

print(maxV)  ## 22

## 최솟값 구하기

minV = number[0]
for i in number:
    if i < minV:
        minV = i

print(minV)  ## 3

number = [7, 10, 22, 4, 3, 17, 22, 6, 4]

## number list 안에 가장 큰 값이 몇개 존재하나요??

maxV = number[0]
cnt = 0
for i in number:
    if maxV < i:
        maxV = i
for i in number:
    if i == maxV:
        cnt += 1

print(maxV, cnt)

## 선택정렬

# lst =  [4,7,1,8,2]
#
# for i in range(4):
#     for j in range(i+1,5,1):
#         if lst[i] > lst[j]:
#             lst[i],lst[j] = lst[j],lst[i]
#
# print(lst)

## 인서트 정렬

arr = [4,7,3,1,2]
lst = []

for i in range(5):
    lst.append(arr[i])
    for j in range(i):
        if lst[i] < lst[j]:
            lst[i],lst[j] = lst[j],lst[i]

print(lst)

# for i in range(len(a)):
#     result.append(a[i])
#     for j in range(i,0,-1):
#         if result[j-1]>result[j]:
#             result[j],result[j-1]=result[j-1],result[j]
#         else:
#             break
