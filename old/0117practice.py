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


#break 반복문을 중간에 멈추고 싶을때 for , while (break는 함수 종류가 아님)
lst = [10,20,30,40,50,60,70]

for i in lst:
  if i == 50:
    break
  print(i,end=' ')

a = 3
print(a)

lst = [[1,2,3],[1,2,3],[1,2,3]]
for i in range(3):
  for j in range(4):
    if lst[i][j] == 2 :
      
      break
    print(lst[i][j], end = ' ')

print()
#continue    # 반복문 맨 위로 올라감. 아래코드 실행 x
lst= [1,2,3,4,5,6,7]

for i in lst:
  if i == 5:
    
    continue
  print(i,end=' ')
  
  
lst = [[1,2,3],[1,2,3],[1,2,3]]
for i in range(3):
  for j in range(3):
    if lst[i][j] == 2:
      continue
    print(lst[i][j],end= ' ')
    
def abc():
  global aa,bb
  aa=3
  bb=5
  print(aa,bb)
  
abc()
print(aa,bb)

def getsum3(a,b=6,c=7):
  return a+b+c

ret = getsum3(4)
print(ret)

# Default parameter  항상 우측에 적어야한다..!! (b =6,c=7)

# 패킹!!! (값들을 묶어서 하나의 변수로 할당하는것을 패킹이라한다.)

num = [1,2,3,4,5]
num2 = [1,2,3,4,5]
print(num,num2)


# 언패킹!! (묶어진 값들을 여러 변수에 나누는것을 언패킹이라고 한다.)
a,b,c,d,e = num
print(num)

a,b,*c = num
print(c)

# 아스트리스크 = *
# 아스트랄  = * 

def getsum(*a):
  sum = 0
  print(a)
  for i in a:
    sum+=i
  return sum


result = getsum(1,2,3)
print(result)

di ={'kevin' : '1', 'john': '2', 'bob' : '3' }


def print_info(**args):
  print(*args)
  for i,j in args.items():
    print(i,j)

print_info(**di)


# map 
# 리스트나 튜플같은 순회 가능한 데이터구조 값들에 함수를 일괄적으로 적용하고
# 적용 후 값을 map이라는 객체로 반환

# 사용법 map(함수,iterebles)

num = ['1', '2', '3']
lst1 = []

for i in num :
  lst1.append(int(i))

print(lst1)

lst2=map(int,num)
print(lst2)
print(list(lst2))

lst1 = [1,2,3]
lst2 = [4,5,6]
#lst3 라는 리스트에 lst1과 lst2 의 합을 저장하는 리스트로 만든 후 출력

def func(a,b):
  return a+b

lst3 = map(func,lst1,lst2)

print(list(lst3))