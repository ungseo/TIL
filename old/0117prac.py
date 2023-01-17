# 1~ 100 까지 for문으로 출력
for i in range(1,101):
  print(i, end=' ')

## 한줄로
[i for i in range(1,101)]

#을 100번 출력하는 코드 완성해보기
for i in range(100):
  print('#')
  
a= ['#' for i in range(100)]
print(*a)

#다 한사람은 while문으로도 표현 해보기
n=0
while n != 100:
  n+=1
  print(n, end = ' ')
  
# 이차원리스트 출력 for 이용하여 출력하기
lst=[[1,2,3],[4,5,6]]

print(lst[0][1])  ## 2


## 이차원리스트 출력하기
for i in range(2):
  for j in range(3):
    print(lst[i][j],end=' ')
  print()
  
# 1차원 리스트
# 빈 리스트 하나 만든 후 lst의 값에 제곱을 한 값으로 채워넣기
# 새로 만들어진 리스트를 출력하기

lst = [[1,2,3],[4,5,6]]
multi = []

for i in range(2):
  for j in range(3):
    multi.append(lst[i][j] ** 2)

print(*multi)      ## 1 4 9 16 25 36

for i in multi:
  print(i, end = ' ')

# 2차원 리스트에 담기
lst = [[1,2,3],[4,5,6]]
multi = []

# for i in range(2):
#   multi.append([])
#   for j in range(3):
#     multi.append(0)

# for i in range(2):
#   for j in range(3):
#     multi[i][j] = lst[i][j] ** 2
    

for i in range(2):
  temp = [] 
  for j in range(3):
    temp.append(lst[i][j]**2)
    multi.append(temp)
print(multi)

# 딕셔너리

dic = {'kevin' :1, 'john' : 2, 'bob' : 3}

for i in dic:
  print(i,dic[i])
  
print(dic)

print()
for i,j in dic.items():
  print(i,j)

print()

for i in dic.values():
  print(i)

if True :
    print('hi')
    


lst = [[1,2,3],[1,2,3],[1,2,3]]
for i in range(3):
  for j in range(4):
    if lst[i][j] == 3 :
      break
    print(lst[i][j], end = ' ')