# ### 3Days practice
# import copy
#
# lst = input().split(',')
# arr = []
# for i in lst:
#     a = i.lower()
#     arr.append(a)
#
# for i in arr:  # 0번째 i == 'apple'
#     if 'rotten' in i:  # 넘어가고, 1번째 i == 'rottenbanana'
#         i = i[6:]  # 'rottenbanana' = 'banana'로 변경
#
#     else:
#         i = i
#
# print(arr)
#
# # arr[1] = arr[1][6:]
#
# print(arr)

# st = input()
#
# if len(st) % 2 == 1 :
#     print(st[len(st)//2])    ## 3자리면 1번쨰 5자리면 2번째 7자리면 3번째
# else :
#     a = len(st)//2
#     print(st[a-1:a+1])   ## 2자리면 [0,1] 4자리면 [1,2] 6자리면[2,3]


# infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
# result = 0
# for i in infos:
#     result += i['age']
# ss

# print(result)


# blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
# bt_di = dict()
# for i in ['A','B','O','AB'] :
#     bt_di[i] = blood_types.count(i)

# print(bt_di)
# water_lst = []
# salt_lst = []
# for i in range(5):
#     info = input('% g형식으로 입력해주세요. 완료되면 Done을 입력해주세요: ').split()
#     if info[0] == 'Done':
#         break
#     else :
#         rate, water = info
#         water_lst.append(int(water))
#         salt_lst.append(int(rate) * int(water)/100)

# water = sum(water_lst)
# salt = sum(salt_lst)

# print(f'{round((salt/water)*100,2)}%')

# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('윤년입니다.')
# else : 
#     print('평년입니다.')

# line_lst = []
# for i in range(3):
#     s_triangle = input()
#     line_lst.append(s_triangle)                 ## 입력받은 문자를 line_lst에 추가

# for i in range(3):
#     line_lst[i] = float(line_lst[i])            ## 실수로 변환
# line_lst.sort()             
# a, b, c = line_lst                              ## 변의 길이순으로 a,b,c 배정


# if a + b > c :                                  ##삼각형의 조건
#     if a == b == c :
#         print('정삼각형')
    
#     elif (a == b and b!= c) or (b == c and a != b):        
#         print('이등변삼각형')
        
#         if a**2 + b**2 == c**2 :                ## 직각이등변삼각형이면 '이등변삼각형'과 '직각삼각형'두개 출력
#             print('직각삼각형')                  ## 루트값때문에 c입력이 안되서 직각이등변삼각형을 출력할 수가없네요
    
#     elif a**2 + b**2 == c**2 :
#         print('직각삼각형')
        
#     else:
#         print('삼각형')

# else:
#     print('삼각형아님')    
    

# st = input()

# st1 = st[3:-4]

# print(st1)

## 요청과 썩은 과일찾기 예제
# import random

# def making_card_list() -> list:
# 	card_list = []

# 	for shape in ["spade", "heart", "diamond", "clover"]:

# 		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

# 			card_list.append((shape, number))

# 	return card_list                                

# trump_card_list = making_card_list()    #### 카드 리스트 생성

# random.shuffle(trump_card_list)  ##카드 섞기

# shape_rank_dict = {'clover':1,'heart':2,'diamond':3,'spade':4}  ## 쉐잎의 우열 나눠주기
# num_rank_dict ={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10': 10,'J':11,'Q':12,'K':13,'A':14} ## 문자를 포함한 카드숫자에 우열 나눠주기
# p1_win = 0  ##승리 수 카운트
# p2_win = 0

# while True:
#     player1 = trump_card_list.pop()
#     player2 = trump_card_list.pop()
#     n1 = str(player1[1])    #딕셔너리 밸류값을 추출하기위해 str타입으로 통일
#     n2 = str(player2[1])    # ''
#     s1 = player1[0]         ## 보기편하게 shape_rank_dict의 키값을 변수로 지정
#     s2 = player2[0]
    
#     if num_rank_dict[n1] == num_rank_dict[n2]:         ## 두 플레이어의 숫자랭크가 같다면
#         if shape_rank_dict[s1] > shape_rank_dict[s2]:       ##쉐잎 랭크까지 비교해서 승자 출력후 승자카운트 +1
#             print(f'{player1} {player2} player1 win!')
#             p1_win += 1
#         else :
#             print(f'{player1} {player2} player2 win!')
#             p2_win += 1
#     elif num_rank_dict[n1] > num_rank_dict[n2]:         ## 여기부터는 숫자값 크기 비교후 승자 출력/ 승자카운트 +1
#         print(f'{player1} {player2} player1 win!')
#         p1_win += 1
#     else:
#         print(f'{player1} {player2} player2 win!')
#         p2_win += 1
    
#     if p1_win == 6 :                      ## 승자카운트가 6이 되면 반복문(게임)종료.
#         print(f'{p1_win}:{p2_win} Finally player1 win')
#         break
#     elif p2_win == 6:
#         print(f'{p2_win}:{p1_win} Finally player2 win')
#         break


# sample_list = [11,22,33,55,66]

# # 주어진 리스트의 4번째 자리에 있는 항목을 제거하고 변수에 할당해주세요.

# a = sample_list.pop(3)

# print(a)

# # sample_list의 가장 뒤에 44를 추가해보세요.

# sample_list.append(77)

# print(sample_list)

# # 할당해놓은 변수의 값을 sample_list의 2번 index에 추가해 보세요

# sample_list.insert(2,a)

# print(sample_list)

# my_tuple = ( 11,22,33,44,55,66)
# new_tuple = my_tuple[3:-1]

# print(new_tuple)

## 얕은복사 :
# a = [1,2,3,4,5]
# b = a

# b[1] = 7

# print(a,b)


# a  = [1,2,['a','b']]

# b = a[:]

# print(a,b)

# b[2][0] = 0 
# print(a,b)

# test_list = [1,2,3,7,4,6,5]

# test_list.sort()
# print(test_list)

# scores = [('eng',88),('sci',90),('math', 80)]
# # 정렬
# def check(x):
#     return x[1]

# print(scores)
# scores.sort(key=lambda x:x[1])
# print(scores)


## 6-1 실습 크롤링을 통한 서비스 개발 예제 1
# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('861123 2345678'))

# B. 출력예시
# 970103*******
# 861123******* 

# def de_identify(id):
#     if len(id) == 14:
#         return id[:6]+'*******'
#     elif len(id) == 13:
#         a = id.replace(id[6:],'*******')
#         return a

# grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

# grain_lst.sort(key=lambda x:x[1],reverse=True)

# print(grain_lst[0][0])



# def count_vowels(x):
#     a = x.count('a')
#     e = x.count('e')
#     i = x.count('i')
#     o = x.count('o')
#     u = x.count('u')
#     return a+e+i+o+u

# print(count_vowels('apple')) #=> 2
# print(count_vowels('banana')) #=> 3

# 반복문을 활용한 방법 
# def sum_of_digit(x):
#     x = str(x)
#     result=0
#     for i in x:
#         result += int(i)
#     print(result)
#     return result

#반복문을 활용하지 않은 방법
# def sum_of_digit(x):
#     lst = map(int,list(str(x)))
    
#     print(sum(lst))
#     return sum(lst)




# sum_of_digit(3904) # 16

# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g

# salt_list = []
# water_list = []

# for i in range(5):
#     lst = input('소금물의 농도(%)와 소금물의 양(g)을 입력하시오: ').split()
#     if lst[0] == 'Done':
#         break
#     else:
#         ratio = int(lst[0][:-1])
#         ratio = ratio/100
#         water = float(lst[1][:-1])
#         salt_list.append(ratio*water)
#         water_list.append(water)

# salt = sum(salt_list)
# water = sum(water_list)

# print(f'{round((salt/water)*100,1)}%,{round((water),2)}g')

    
# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

# print('a')


## 7-1 실습

class Nationality():
    
    def __init__(self,name):
        self.name = name
    
    def output(self):
        return (f'나의 국적은 {self.name}')
        


korea_nationality = Nationality("대한민국")
print(korea_nationality.output()) # 나의 국적은 대한민국


## 7-3 실습

# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0


class Calculator():
    
    def add(x,y):
        return (f'{x} + {y} = {x + y}')
    
    def substract(x,y):
        return (f'{x} - {y} = {x - y}')
    
    def multuply(x,y):
        return (f'{x} * {y} = {x * y}')
    
    def divide(x,y):
        
        try:
            return (f'{x} / {y} = {x / y}')
        except(ZeroDivisionError):
            return (f'0으로 나눌 수 없습니다.')

print(Calculator.add(1,2))
print(Calculator.substract(2,1))
print(Calculator.multuply(3,4))
print(Calculator.divide(4,0)) 

import math


def fee(minutes, distance):
    ## 대여비 계산
    lental_time = math.ceil(minutes/10) 
    lental_charge = 1200
    
    lental_fee = lental_time * lental_charge
    ## 보험료 계산
    ins_charge = 525
    ins_time, injury_time = divmod(minutes, 30)
    if injury_time >=20:
        ins_time += 1
    
    insurance_fee = ins_charge * ins_time
    ## 주행요금 계산
    dft_charge = 170
    sale_charge = int(170 * (1/2))
    
    if distance > 100:
        dis1, dis2  = 100, distance - 100
        driving_fee = dis1 * dft_charge + dis2 * sale_charge
    
    else:
        distance = distance
        driving_fee = distance * dft_charge
         
    return (f'대여요금: {lental_fee}\n보험료: {insurance_fee}\n주행요금: {driving_fee}\n카쉐어링 서비스 요금:{lental_fee+insurance_fee+driving_fee}')

print(fee(600, 110))



## 7-5실습
import random
class ClassHelper():
    
    def __init__(self,name):
        self.name = name
        
    def pick(self,num):
        result = random.sample(self.name, k=num)
        return result
        
    def match_pair(self):
        
        mate_list = []
        lst = self.name[:]
        
        ran = len(lst)//2
        random.shuffle(lst)
        
        for i in range(ran):
            temp = []
            
            if len(lst) <= 3:
                temp.append(lst)
    
            else:
                for j in range(2):
                    temp.append(lst.pop())
            
            mate_list.append(temp)        
        return mate_list

ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])


print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())


## 7-6 과제

class Doggy():
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self,name,kind):
        self.name = name
        self.kind = kind
        Doggy.num_of_dogs += 1
        
    def bark(self):
        return (f'{self.name}: 왈!왈!')
    
    def death(self):
        Doggy.num_of_dogs -= 1
        del self
        
    def birth(self):
        Doggy.birth_of_dogs += 1
    
    @classmethod
    def get_status(cls):
        print(f'강아지 수: {cls.num_of_dogs}')
        print(f'새로태어난 강아지 수: {cls.birth_of_dogs}')
        
dog1 = Doggy('somi','Maltiz')
dog2 = Doggy('dubu','Hound')
dog3 = Doggy('jjongE','Jindotgae')

dog4 = Doggy('jjangA','Maltiz')
dog5 = Doggy('Hiii','Hound')

dog4.birth()
dog5.birth()


print(dog1.bark())
Doggy.get_status()

## 7-7 과제


def collatz(num):
    
    if num % 2 == 0:
        count = 0
        for i in range(500):
            count += 1
            num = num % 2
            if num == 1:
                break
        if num != 1:
            return -1
        else:
            return count
        
    elif num % 2 == 1:
        num = num*3+1
        count = 0
        for i in range(500):
            count += 1
            num = num % 2
            if num == 1:
                break
        if num != 1:
            return -1
        else:
            return count

print(collatz(6)) #=> 8
# collatz(16) #=> 4
# collatz(27) #=> 111
# collatz(626331) #=> -1

