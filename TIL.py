# # 2023/01/18

# ''' 
# filter
# 리스트나 튜플과 같은 순화 가능한 데이터구조 값들을 함수에 적용하는데
# 적용후 값중 True만 변환!! filter 라는 객체로 변한

# # 리스트에서 짝수만
# '''
# # num = [1,2,3,4,5,6,7,8,9]

# # def get_even(t):
# #     return True if t%2 == 0 else False

# # result = filter(get_even, num)
# # print(list(result))
# '''
# lambda 함수
# 익명함수.. 함수를 간략하게 적기 위해서 사용!!

# #숫자 2개 입력받고 두 getsum이라는 함수로 전달
# #get sum 함수에서 전달받은 두수의 합을 return
# # return 받은 값 출력하기
# '''
# # a,b = map(int,input().split())

# # def getsum(x, y):
# #     return x+y
# # print(getsum(a,b))

# # #람다이용

# # result =(lambda a,b:a+b)(3,5)
# # print(result)

# # sum2 = (lambda a,b:a+b)
# # print(sum2(3,5))

# # lst1 = [1,2,3,4,5]
# # lst2 = [6,7,8,9,10]

# # #두 리스트 값들의 합을 lst3에 람다 함수를 사용하여 값을 채운 후 출력하기
# # #lst3 = [7,8,11,13,15]

# # lst3 = list(map(lambda x, y : x+y,lst1,lst2))
# # print(lst3)

# lst = list(range(100))
# # 리스트에서 짝수만 빼오기
# # filter , lambda 같이 사용

# even_lst= filter(lambda even:even % 2 == 0,lst)
# lst3 = map(lambda x : x %2 == 0, lst)
# print(list(even_lst))
# print(list(lst3))
# #일괄적용 (리스트나 튜플같은 순환가능한 데이터 구조에 일괄적용) = map()
# #데이터에 일괄적용하는데 True 값만 따로 저장하겠다 = filter
# #lambda 익명함수 (사용자 함수를 직접 적지 않고 간단하게 함수 사용하고 싶을때 사용)

# # recursion 재귀!! 재귀호출

# for i in range(1,11):
#     print(i,end= ' ')
# for i in range(10,0,-1):
#     print(i,end=' ')
    
# print()

# def abc(level):
#     if level==11:
#         return
#     print(level,end=' ')
#     abc(level+1)
#     print(level,end=' ')

# abc(1)

# # # 1 2 3 3 2 1
# for i in range(1,4):
#     print(i, end= ' ')
# for i in range(3,0,-1):
#     print(i,end= ' ')
# print()
# # ###################################################################

# def print3(number):
#     if number == 4:
#         return
#     print(number,end = ' ')
    
#     print3(number+1)
#     print(number,end=' ')


# print3(1)

# ''' 
# 문자열 
# 리스트 튜플 딕셔너리 셋 관련 메소드
# copy( 깊은복사 얕은복사)


# '''

st = 'apple,banana,mango'

# ## 문자 'a'가  존재하는지 확인하고자 합니다.

index = st.find('a') ## 없으면 -1값 반환
index = st.find('a',1) #>> 1번 인덱스부터 찾겠다.
print(index) ## 0번 인덱스에 있음!

alpha = st.index('p')
print(alpha) ## 없으면 버그남!!

#대소문자 확인!!
st = 'apple,banana,mango'
print(st.isupper())  ## True or False 값 반환  >> False
print(st.islower())  ##  >> True
print(st.isalpha())  ## 다 알파벳이냐? >> False (,때문에)

print(st.count('a'))  ## a 5개있음. = int(5)

## join (합치기)
st = ['a','p','p','l','e']
str2 = "".join(st)  ## apple
print(str2)
##리스트 안에 문자를 합치는데 사이사이에 ,를 넣어라.

str2 = ','.join(st)

print(str2)

st = ['apple','banana','mango']

str3 =' '.join(st)
print(str3)

st = 'apple,banana,mango'
## 모두 대문자/소문자로 바꾸기

str2 = st.upper()
print(str2)
str2 = st.lower()
print(str2)

## 공백지우기
st ='  apple  '
str2 = st.lstrip()    ## 왼쪽의 공백을 없앤다.//오른쪽은 rstrip//양쪽은 strip
print(str2)
str3 = st.strip() 
print(str2)
## 교체 replace

str2 = st.replace('ap','mp')
print(str2)

##리스트 값 추가
st = ['apple', 'banana', 'mango']
st.append('orange')
st.insert(1,'orange') ## 리스트 값을 중간 또는 맨 앞에 추가할때 사용
print(st)


st = [1,2,3]
str2 = [4,5]
st.append(str2)
print(st)

st = [1,2,3]
str2 = [4,5]    
st.extend(str2)    ## st + str2 와 같음
print(st)


## ctrl + F2 일괄로 변수 바꾸기

## 리스트 값 지우기
st = [1,2,3]

st.pop()
print(st)

st = [1,2,3,4,1,2,3,4]
st.remove(4)   #맨처음걸린거 하나만지움//없으면 오류뜸
print(st)

st = [1,2,3,4,1,2,3,4]

del st[3:]
print(st)

st = [1,2,3,4,1,2,3,4]

st.reverse()
print(st)

print(st[::-1])

a1 = [6,3,9]
print(a1)
a1.sort()  ##오름차순 디폴트
print(a1)
a1.sort(reverse=True) ## 내림차순########################중요!~!~!~!!!!!!!!!!!
print(a1)

a2 = [6,3,9]    
ret=sorted(a1)    ## 원본데이타를 바꾸지않고 바꾼상태의 데이타를 새로운 변수에 입력한다.
print(a2,ret)
ret = sorted(a2,reverse=True)
print(ret)

## lambda를 이용한 sort도 가능
lst = list(range(10))
print(lst)

ret = sorted(lst,key = lambda x:x)
print(ret)

ret = sorted(lst,key=lambda x:x,reverse=True)  #내림차순!!!
print(ret)

lst = [(3,'banana'),(2,'apple'),(1,'carrot')]
ret = sorted(lst,key = lambda x:x[0])

print(ret)

# 튜플 !!!!
st ={'kevin':1, 'john':2,'bob':3}

st['kate'] = 'hi'

print(st)

st['kevin'] = 11
print(st)

del st['kate']
print(st)

lst = st.keys()
print(lst)
print(list(lst))

lst = st.values()
print(list(lst))

lst  = st.items()
print(list(lst))   ## 튜플의 형태로 (key,value) 반환

## 딕셔너리 값 출력하기
st = {'kevin' :1, 'john' : 2, 'bob' :3}
print(st.get('keein','값없음 없다구요~~!~!'))  ### value 값 뽑을때 get함수로 출력 추천


## 딕셔너리 값 정렬하기
st = {'kevin':27, 'john': 22, 'bob' : 35}

## 아이들의 나이가 적은 순으로 (오름차순으로)딕셔너리를 정렬하기!!
## dict(딕셔너리 전용 함수) 사용
ret=dict(sorted(st.items(),key=lambda x:x[1]))

print(ret)

##copy 
lst=[1,2,3]
lst2 = lst
lst[0] = 100
print(lst2)  ### [100,2,3]

## 그냥 변수할당과 카피의 차이
lst= [1,2,3]
# lst2=lst.copy()
lst2 = lst[:]

lst[0] = 100
print(lst2)  ### [1,2,3]


## 2차원배열에서 문제가생김 (얕은복사)
lst = [[1,2],[3,4]]
lst2=lst.copy() 
lst[0][0] = 100
print(lst2[0][0])

## 깊은 복사
import copy
lst = [[1,2],[3,4]]
lst2= copy.deepcopy(lst)
lst[0][0]= 100
print(lst2[0][0])

## 주소값을 찍어보자
a = 5
b = 5
print(id(a),id(b)) ##같음
lst = [1,2,3]
lst2 =lst
print(id(lst),id(lst2))## 같음

lst= [1,2,3]
lst2 =lst[:]
print(id(lst),id(lst2))  ##다름

lst = [[1,2], [3,4]]
lst2 = lst[:]
print(id(lst[0]),id(lst2[0]))  ##같음


lst = [[1,2], [3,4]]
lst2 =copy.deepcopy(lst2)
print(id(lst[0]),id(lst2[0]))
