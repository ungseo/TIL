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
import random

def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list                                

trump_card_list = making_card_list()    #### 카드 리스트 생성

random.shuffle(trump_card_list)  ##카드 섞기

shape_rank_dict = {'clover':1,'heart':2,'diamond':3,'spade':4}  ## 쉐잎의 우열 나눠주기
num_rank_dict ={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10': 10,'J':11,'Q':12,'K':13,'A':14} ## 문자를 포함한 카드숫자에 우열 나눠주기
p1_win = 0  ##승리 수 카운트
p2_win = 0

while True:
    player1 = trump_card_list.pop()
    player2 = trump_card_list.pop()
    n1 = str(player1[1])    #딕셔너리 밸류값을 추출하기위해 str타입으로 통일
    n2 = str(player2[1])    # ''
    s1 = player1[0]         ## 보기편하게 shape_rank_dict의 키값을 변수로 지정
    s2 = player2[0]
    
    if num_rank_dict[n1] == num_rank_dict[n2]:         ## 두 플레이어의 숫자랭크가 같다면
        if shape_rank_dict[s1] > shape_rank_dict[s2]:       ##쉐잎 랭크까지 비교해서 승자 출력후 승자카운트 +1
            print(f'{player1} {player2} player1 win!')
            p1_win += 1
        else :
            print(f'{player1} {player2} player2 win!')
            p2_win += 1
    elif num_rank_dict[n1] > num_rank_dict[n2]:         ## 여기부터는 숫자값 크기 비교후 승자 출력/ 승자카운트 +1
        print(f'{player1} {player2} player1 win!')
        p1_win += 1
    else:
        print(f'{player1} {player2} player2 win!')
        p2_win += 1
    
    if p1_win == 6 :                      ## 승자카운트가 6이 되면 반복문(게임)종료.
        print(f'{p1_win}:{p2_win} Finally player1 win')
        break
    elif p2_win == 6:
        print(f'{p2_win}:{p1_win} Finally player2 win')
        break





