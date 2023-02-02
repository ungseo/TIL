import sys
sys.stdin = open("input.txt", "r")

# 1.문자열 입력 받고 출력해서 확인해보기
# st = 'hello'

# 1.주어지는 입력값은 아래와 같음
# hello

# 1.아래에 정답을 입력하시오
st=input()
print(st)


# 2.정수형 변수 입력 받고 출력해서 확인해보기
# N = 45
# A, B, C = 1, 2, 3

# 2.주어지는 입력값은 아래와 같음
# 45
# 1 2 3

# 2.아래에 정답을 입력하시오
t = int(input())
A,B,C = list(map(int,input().split()))

print(t)
print(A,B,C)


# 3.실수형 변수 입력 받고 출력해서 값이 잘 들어갔지 확인해보기
# F = 3.14
# A, B, C = 1.2, 2.3, 3.4

# 3.주어지는 입력값은 아래와 같음
# 3.14
# 1.2 2.3 3.4

# 3.아래에 정답을 입력하시오
num = float(input())
A,B,C = list(map(float, input().split()))
print(num)
print(A, B, C)


# 4.한 줄에 있는 공백으로 구분된 단어들을 각각 문자열로 리스트에 저장하고 출력해서 값이 잘 들어갔지 확인해보기
# lst = ['one', 'two', 'three']

# 4. 주어지는 입력값은 아래와 같음
# one two three

# 4.아래에 정답을 입력하시오
lst = list(input().split())
print(lst)


# 5.한 줄에 있는 공백으로 구분된 숫자들을 각각 숫자로 리스트에 저장하고 출력해서 값이 잘 들어갔지 확인해보기
# (map 함수를 이용하여 문자열을 숫자로 바꾼 후 리스트로 변환)
# lst = [1, 2, 45, 43]

# 5. 주어지는 입력값은 아래와 같음
# 1 2 45 43

# 5.아래에 정답을 입력하시오
lst = list(map(int,input().split()))
print(lst)


# 6.한 줄에 있는 공백없는 한자리 숫자들을 각각 숫자로 리스트에 저장하고 출력해서 값이 잘 들어갔지 확인해보기
# lst = [1, 2, 3, 4]

# 6. 주어지는 입력값은 아래와 같음
# 1234

# 6.아래에 정답을 입력하시오
st= list(input())
lst = list(map(int,st))
print(lst)

# 7.2차원 (N*N) 공백없는 한자리 숫자들을 2차원 arr에 저장하고 출력해서 값이 잘 들어갔지 확인해보기
# N=4
# lst=[[1,0,1,1],[1,0,0,1],[0,0,0,1],[1,0,0,0]]

# 7. 주어지는 입력값은 아래와 같음
# 4
# 1011
# 1001
# 0001
# 1000

# 7.아래에 정답을 입력하시오
N = int(input())
lst = []
for i in range(N):
    temp = list(map(int,list(input())))
    lst.append(temp)
print(lst)

# 8.2차원 (N*N) 정수값을 2차원 arr에 저장하고 출력해서 값이 잘 들어갔지 확인해보기 (N값과 arr값)
# N=4
# arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# 8. 주어지는 입력값은 아래와 같음
# 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# 8.아래에 정답을 입력하시오
N = int(input())
arr = []
for i in range(N):
    temp = list(map(int,input().split()))
    arr.append(temp)
print(arr)


# 9.(입력값 없음) 0값 10개를 가진 1차원 lst 생성 후 출력해서 값이 잘 들어갔지 확인해보기
# lst = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# 9.아래에 정답을 입력하시오
lst = [0] * 10
print(lst)


# 10.(입력값 없음) 0값 3 * 3 개를 가진 2차원 arr생성 후 출력해서 값이 잘 들어갔지 확인해보기
# arr = [[0, 0, 0],
#        [0, 0, 0],
#        [0, 0, 0]]

# 10.아래에 정답을 입력하시오
arr = [[0 for i in range(3)] for j in range(3)]


for i in arr:
    print(f'{i},')


# print('수고하셨습니다.')