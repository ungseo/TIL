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
    

st = input()

st1 = st[3:-4]

print(st1)