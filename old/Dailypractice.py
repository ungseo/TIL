# 근의 공식을 출력하는 함수를 작성하라.

a = 3
b = 6
c = -5
def gongsik(a,b,c):
    global x1, x2
    x1 = (-b + (b**2 - 4*a*c) ** (1/2)) / 2*a
    x2 = (-b - (b**2 - 4*a*c) ** (1/2)) / 2*a
    print(round(x1,4) ,round(x2,4))


gongsik(a,b,c)

# 튜플 이용하기.

# todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]

# # todo_new = input()
# # todo_num = int(input())

# todo.append((todo_new,todo_num))

# print(todo)

# set 이용하기

orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
order_lst = list(map(str,orders.split(',')))



print(f'{len(order_lst)}잔 주문이 들어왔습니다.')

a= list(set(order_lst))
print(sorted(a))


a = '2' #정수 2로 바꾼 후 10을 더한 값을 출력해 주세요.

print(int(a)+10)
print(ord(a)-ord('0')+10)  # ord('2') = 50 , ord('0') = 48

a= -3 
print(abs(a))   # 절댓값 a
print(id(a))    # 주소값 a
print(pow(3,2)) # 3의 2제곱 (제곱근)

import random

a=[1,2,3,4,5,6,7]

print(random.sample(a,2))  

def rabit():
    print('slslslslslsl')
    print('sielsislxf.s')
    
# 두 숫자를 전달받고 합을 돌려주는 (변환하는) 함수를 만들도록

def getsum(a,b):    ##return 은 함수를 꺼버린다. (주의)
    return a+b
    return a*b      ## 작동 x
a=3
b=7

print(getsum(5,2))  # a,b = 매개변수 parameter
                    # 3,4 = 인자값 argument
                    # 7
print(a,b) ## = 10


## return x return y  #  (x, y) 값 2개반환 (튜플 사용)
def getsum(a,b):
    return a+b,a*b

ret = getsum(3,8)
print(ret)
print(type(ret))


## 값 2개 반환 전역변수 사용
sum1= 0
gop1= 0

def getsum2(a,b):
    global sum1,gop1
    sum1=a+b
    gop1=a*b

ret = getsum(5,6)

# 아이스 음료 주문이 몇 개 들어왔는지 확인하세요.
# 메뉴 별 주문 수를 출력하세요.
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
ice_order = orders.count('아이스')
print(ice_order,'잔')

order_lst = list(map(str,orders.split(',')))
print(order_lst)

idx = -1
for menu in order_lst:
    idx += 1
    if order_lst[idx:].count(menu) == 1:
        menu_set = 0
        
        menu_set += order_lst.count(menu)
        print(f'{menu} : {menu_set}잔')
    
    
# 짝꿍바꾸기

lst = list(map(str,input().split()))
print(lst)