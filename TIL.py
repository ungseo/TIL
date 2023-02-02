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


# # '''

# st = 'apple,banana,mango'

# # ## 문자 'a'가  존재하는지 확인하고자 합니다.

# index = st.find('a') ## 없으면 -1값 반환
# index = st.find('a',1) #>> 1번 인덱스부터 찾겠다.
# print(index) ## 0번 인덱스에 있음!

# alpha = st.index('p')
# print(alpha) ## 없으면 버그남!!

# #대소문자 확인!!
# st = 'apple,banana,mango'
# print(st.isupper())  ## True or False 값 반환  >> False
# print(st.islower())  ##  >> True
# print(st.isalpha())  ## 다 알파벳이냐? >> False (,때문에)

# print(st.count('a'))  ## a 5개있음. = int(5)

# ## join (합치기)
# st = ['a','p','p','l','e']
# str2 = "".join(st)  ## apple
# print(str2)
# ##리스트 안에 문자를 합치는데 사이사이에 ,를 넣어라.

# str2 = ','.join(st)

# print(str2)

# st = ['apple','banana','mango']

# str3 =' '.join(st)
# print(str3)

# st = 'apple,banana,mango'
# ## 모두 대문자/소문자로 바꾸기

# str2 = st.upper()
# print(str2)
# str2 = st.lower()
# print(str2)

# ## 공백지우기
# st ='  apple  '
# str2 = st.lstrip()    ## 왼쪽의 공백을 없앤다.//오른쪽은 rstrip//양쪽은 strip
# print(str2)
# str3 = st.strip() 
# print(str2)
# ## 교체 replace

# str2 = st.replace('ap','mp')
# print(str2)

# ##리스트 값 추가
# st = ['apple', 'banana', 'mango']
# st.append('orange')
# st.insert(1,'orange') ## 리스트 값을 중간 또는 맨 앞에 추가할때 사용
# print(st)


# st = [1,2,3]
# str2 = [4,5]
# st.append(str2)
# print(st)

# st = [1,2,3]
# str2 = [4,5]    
# st.extend(str2)    ## st + str2 와 같음
# print(st)


# ## ctrl + F2 일괄로 변수 바꾸기

# ## 리스트 값 지우기
# st = [1,2,3]

# st.pop()
# print(st)

# st = [1,2,3,4,1,2,3,4]
# st.remove(4)   #맨처음걸린거 하나만지움//없으면 오류뜸
# print(st)

# st = [1,2,3,4,1,2,3,4]

# del st[3:]
# print(st)

# st = [1,2,3,4,1,2,3,4]

# st.reverse()
# print(st)

# print(st[::-1])

# a1 = [6,3,9]
# print(a1)
# a1.sort()  ##오름차순 디폴트
# print(a1)
# a1.sort(reverse=True) ## 내림차순########################중요!~!~!~!!!!!!!!!!!
# print(a1)

# a2 = [6,3,9]    
# ret=sorted(a1)    ## 원본데이타를 바꾸지않고 바꾼상태의 데이타를 새로운 변수에 입력한다.
# print(a2,ret)
# ret = sorted(a2,reverse=True)
# print(ret)

# ## lambda를 이용한 sort도 가능
# lst = list(range(10))
# print(lst)

# ret = sorted(lst,key = lambda x:x)
# print(ret)

# ret = sorted(lst,key=lambda x:x,reverse=True)  #내림차순!!!
# print(ret)

# lst = [(3,'banana'),(2,'apple'),(1,'carrot')]
# ret = sorted(lst,key = lambda x:x[0])

# print(ret)

# # 튜플 !!!!
# st ={'kevin':1, 'john':2,'bob':3}

# st['kate'] = 'hi'

# print(st)

# st['kevin'] = 11
# print(st)

# del st['kate']
# print(st)

# lst = st.keys()
# print(lst)
# print(list(lst))

# lst = st.values()
# print(list(lst))

# lst  = st.items()
# print(list(lst))   ## 튜플의 형태로 (key,value) 반환

# ## 딕셔너리 값 출력하기
# st = {'kevin' :1, 'john' : 2, 'bob' :3}
# print(st.get('keein','값없음 없다구요~~!~!'))  ### value 값 뽑을때 get함수로 출력 추천


# ## 딕셔너리 값 정렬하기
# st = {'kevin':27, 'john': 22, 'bob' : 35}

# ## 아이들의 나이가 적은 순으로 (오름차순으로)딕셔너리를 정렬하기!!
# ## dict(딕셔너리 전용 함수) 사용
# ret=dict(sorted(st.items(),key=lambda x:x[1]))

# print(ret)

# ##copy 
# lst=[1,2,3]
# lst2 = lst
# lst[0] = 100
# print(lst2)  ### [100,2,3]

# ## 그냥 변수할당과 카피의 차이
# lst= [1,2,3]
# # lst2=lst.copy()
# lst2 = lst[:]

# lst[0] = 100
# print(lst2)  ### [1,2,3]


# ## 2차원배열에서 문제가생김 (얕은복사)
# lst = [[1,2],[3,4]]
# lst2=lst.copy() 
# lst[0][0] = 100
# print(lst2[0][0])

# ## 깊은 복사
# import copy
# lst = [[1,2],[3,4]]
# lst2= copy.deepcopy(lst)
# lst[0][0]= 100
# print(lst2[0][0])

# ## 주소값을 찍어보자
# a = 5
# b = 5
# print(id(a),id(b)) ##같음
# lst = [1,2,3]
# lst2 =lst
# print(id(lst),id(lst2))## 같음

# lst= [1,2,3]
# lst2 =lst[:]
# print(id(lst),id(lst2))  ##다름

# lst = [[1,2], [3,4]]
# lst2 = lst[:]
# print(id(lst[0]),id(lst2[0]))  ##같음


# lst = [[1,2], [3,4]]
# lst2 =copy.deepcopy(lst2)
# print(id(lst[0]),id(lst2[0]))

# st = 'banana'

# flag = st == str
# if flag==True:
#     print('a')


## 주어진 문자열에서 숫자,문자,기호가
##  각각 몇개인지를 판단하는 함수를 작성해보세요.


    


# 문자 : 10개,숫자 : 3개, 기호 : 7개


# T,M = list(map(int,input().split()))
# cook = int(input())
# t, m = divmod(T * 60 + M + cook, 60)

# if t >= 24:
#     print(t-24, m)  
# else:
#     print(t,m)

## 객체지향 <> 절차지향 프로그래밍

class calculator():  ## 클래스
    numberOfCalcul=0  ##속성  // 클래스 변수
    
    def __init__(self):  ## 매서드  ## init == 인스턴스 만들면 실행 ## 생성자함수 (constructor)
        self.result= 0  ## 속성 // 인스턴스 변수
        calculator.numberOfCalcul += 1
        
    def getsum(self,value): ## 매서드
        self.result += value
        return self.result
    
cal1 = calculator()   ## cal1 == 인스턴스 // 객체
## 인스턴스 변수란?? 인스턴스가 개인적으로 가지고 있는 속성(attribute)




print(cal1.getsum(3))
print(cal1.getsum(4))
print(cal1.getsum(5))

# print(cal1.numberOfCalcul)

print()

cal2 = calculator()
print(cal2.getsum(6))
print(cal2.getsum(7))
print(cal2.getsum(1))
print(cal2.numberOfCalcul)
# 클래스 변수란??
# 한 클래스의 모든 인스턴스가 공유하는 값을 의미


print(cal2.numberOfCalcul)

# 주의점!!
# 클래스 변수 값을 변경시 무조건 상상 클래스.클래스변수 형식으로 변경해야 함!!

calculator.numberOfCalcul = 6 ## 인정

print(cal1.numberOfCalcul)
print(cal2.numberOfCalcul)


print()
print()

## 안됨...
cal1.numberOfCalcul = 10

print(cal1.numberOfCalcul)  ## 10

calculator.numberOfCalcul = 20
print(cal1.numberOfCalcul)  ## 10
print(cal2.numberOfCalcul)  ## 20

'''
결론
클래스 변수 : 모든 인스턴스가 공유.
인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
인스턴스변수 : 인스턴스별로 독립되어 있음.
각 인스턴스가 값을 따로 지정해야 할 떄 사용
'''

#===========================================

# 클래스 / 인스턴스(객체)
# 클래스 - 속성/매서드
# 속성- 클래스변수/ 인스턴스 변수

# 3. 매서드
#   1.인스턴스 매소드
#   2.클래스 매소드
#   3. 스태틱 매소드

class plus_minus:
    
    # def data(self,first,second):  ## 인자값으로 객체 a, 3, 5를 각각 뜻한다
    #     self.first=first
    #     self.second=second
    
    def __init__(self,first,second):       
        self.first = first
        self.second = second
        
    def plus(self):  ##플러스값을 반환하는 매소드 완성
        return self.first + self.second
    
    def minus(self):  ##마이너스 값을 반환하는 매소드완성
        return self.first - self.second

a = plus_minus(3,5)
# a.data(3,5)

b =plus_minus(2,7)
# b.data(2,7)

print(a.first,b.second)

print(a.plus())

print(a.minus())

## __??__ 매직 메서드 (init add str 등) == 인스턴스 생성하자마자 자동 호출!!!

'''
특수한 매서드를 사용함으로써, 파이썬의 행위를 여러가지로 커스터마이즈를 할 수 있다. 
파이썬 문자열에서 + 연산자를 사용하면 두 문자열이 합쳐 지는 것은 
파이썬이라는 언어를 만들 때 문자열에 관한 클래스에 덧셈 연사이 되도록 클래스 안에 정의를 해 놓았기 떄문이다.
'''

# class car:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
    
#     def __add__(self,another):      ## __add__ 라는 매직매서드를 커스터마이징 해서 덧셈 연산을 지원하도록 하겠다.
#         return self.price + another.price
    
#     def __str__(self):
#         return (f'{self.name}의 가격은 {self.price}입니다.')
# kia= car('k8',300)
# bmw= car('m5',500)


# # print(kia.price+bmw.price)를  ## 800
# # print(kia+bmw) # 커스터마이징 할 것이다. ## 이거 지금 출력하면 버그남

# ## magic 매서드 사용해서 커스터마이징

# print(kia+bmw)

# # print(f'{kia.name}의 가격은 {kia.price}입니다.')

# print(kia)
# print(bmw)

# del kia

# print(kia)

'''
데코레이터
장식하는사람 이라는 뜻
함수를 하나 만드는데 그 함수를 직접 수정하지 않고 함수에 기능을 추가하고자 할때 사용

1.먼저 데코레이터 사용 안한 예

이름과 나이를 출력해주는 각각의 함수를 정의해보자
'''
## 데코 사용 x

# def call_name(name):
#     print('반짝'*5)
#     print(name)
#     print('샤방'*5)

# def call_age(age):
#     print('반짝'*5)
#     print(age)
#     print('샤방'*5)

# def call_nickname(nick):
#     print(nick)
    
# call_name('최민호')
# call_age(39)

## 데코 사용

# def deco(func):
    
#     def wrapping(value):      
#         print('반짝'*5)
#         func(value)
#         print('샤방'*5)
#     return wrapping

# @deco
# def call_name(name):
#     print(name)

# @deco
# def call_age(age):
#     print(age)
    
# call_name('최민호')
# call_age(39)


#========================================

class car:
    @staticmethod
    def add_price(one,another):
        print(one+another)
        
## 정적 메소드에서는 @staticmethod 를 붙입니다.
## 그리고self가 없다!! (self는 인스턴스 메서드 사용)
## add_price 함수의 매개변수를 넣는데 self 사용하지 않습니다.

car.add_price(400,800)

'''
정적 메서드를 호출 할 떄는 클래스에서 바로 매서드를 호출하면 됩니다.
클래스의 인스턴스가 없어도 문제 될 것 없음

다시한번 말하지만 정적 매서드는 인스턴스 매서드 처럼 
self를 받지 않습니다. 그래서 보통 정적메서드는 
self와 같은 속성을 다루지 않고 단지 

함수의 행동(기능)(메서드내용만) 하는 메서드를 클래스에 정의 할떄 사용한ㄷ.ㅏ
그래서 호출할떄 클래스에서 바로 메서드를 호출함!!

car.add_price(400,800)

그러나 
인스턴스가 있다면 인스턴스로도 static method에 접근은 가능
이건 파이썬에서 가능!!

인스턴스로 정적메소드 호출은 잘 하지 않음 그이유는!!!!
정적 메서드를 사용하는 이유!!

이 메서드는 클래스의 인스턴스에 어떠한 변화도 일으키지 않는
함수라는 의미를 내포하고 암시할 때 사용한다. 
'''

# a7 = car()

# a7.add_price(500,600)

# ## 클래스 매서드

# ## 몇명이 파이를 만들었는지 확인하는 코드를 클래스 매서드를 사용해보자

# class make_pie:
#     cnt = 0
#     def __init__(self,name):
#         self.name = name
#         make_pie.cnt += 1
        
#     @classmethod
#     def number_Of_Pies(cls):
#         print(f'파이를 {cls.cnt} 명이 만들고 있습니다.')
        
#     @classmethod
#     def create(cls,name):   ## 클래스 내부에서 클래스 안에 있는 메소드를 호출하는 함수
#         p = cls(name)
#         return p
        
        
# a = make_pie('kevin')
# b = make_pie('jane')
# c = make_pie('jhon')

# print(make_pie.cnt)

# make_pie.number_Of_Pies()

# make_pie.create('aiden')
# make_pie.create('bob')

# make_pie.number_Of_Pies()

# # print(
# def emoji_decorator(func):
#     def wrapper(name):
#         func(name)
#         print("^~^//")
#     return wrapper

# def add_tears(func):
#     def wrapper(name):
#         func(name)
#         print('ㅠ,.ㅠ')
#     return wrapper



# @add_tears
# @emoji_decorator    
# def ko_hello(name):
#     print(f'안녕하세요, {name}님!')
# @add_tears
# @emoji_decorator    
# def en_hello(name):
#     print(f'Hello, {name}!')




  
    

    
# en_hello('ungseo')


# class MyClass:
    
#     def method(self):
#         return 'instance method', self
    
#     @classmethod
#     def classmethod(cls):
#         return 'class method', cls
    
#     @staticmethod
#     def staticmethod():
#         return 'static method'
    
# my_class = MyClass()

# print(my_class.method())
# print(my_class.classmethod())
# print(my_class.staticmethod())


# class Person():
#     def __init__(self,name):
#         self.name =name
        
#     def greeting(self):
#         return f'안녕, {self.name}'
    
# class Mom(Person):
#     gene = 'XX'
    
#     def swim(self):
#         return '엄마가 수영'

# class Dad(Person):
#     gene = 'XY'
    
#     def walk(self):
#         return '아빠가 걷기'
    
# class FirstChild(Dad,Mom):
#     def swim(self):
#         return '첫째가 수영'
    
#     def cry(self):
#         return '첫쨰가 응애'
    
    
# baby1 = FirstChild('아가')
# print(baby1.cry())
# print(baby1.swim())
# print(baby1.walk())
# print(baby1.gene) 

# class Person():
#     def __init__(self):
#         self._age = 0
#     @property    
#     def age(self):     ##getter
        
#         print('게터 호출')
#         return self._age
#     @age.setter
#     def age(self,age):  ## setter
#         print('세터 호출')
#         self._age = age

    
  
# # ///

# p1  = Person()

# p1.age = 25 
# print(p1.age)

class plus_minus:
    def __init__(self,first,second):
        self.first = first
        self.second = second
        
    def plus(self):
        result = self.first+self.second
        return result

    def minus(self):
        result = self.first-self.second
        return result
    
a = plus_minus(3,5)

class morefunction(plus_minus):
    def __init__(self, first, second, third):
        super().__init__(first, second)  ## super는 부모클래스의 init 메소드를 그대로 가져온 것
        self.third = third              ## third만 추가

    def mul(self):
        result = self.first * self.second*self.third
        return result

        
# a = plus_minus(3,5)
# print(a.first,a.second)
# a = morefunction(4)

# pirnt(a.third)
# print(a.mul())

# a = morefunction(3,4,5)
# print(a.mul())
# print(a.plus())

# 메서드 오버라이딩
# 오버라이딩이란 덮어쓰기를 말한다.
#부모클래스에 있는 메서드!!! 를 동일한 이름으로 자식클래스에서 다시 만드는 것이다.
#(부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 떄 사용)

## 부모 클래스에서 상속받은 plus의 메소드의 기능에서
## 숫자 2개가 아닌 숫자 3개의 합이 100이 넘는다면
## '버그'라고 출력이 되도록
## 자식클래스에서 plus의 메소드 업그레이드가 되도록 가정하자.

class plus_minus:
    def __init__(self,first,second):
        self.first = first
        self.second = second
        
    def plus(self):
        result = self.first+self.second
        return result

    def minus(self):
        result = self.first-self.second
        return result
    


class morefunction(plus_minus):
    def __init__(self, first, second, third):
        super().__init__(first, second)  ## super는 부모클래스의 init 메소드를 그대로 가져온 것
        self.third = third              ## third만 추가

    def mul(self):
        result = self.first * self.second*self.third
        return result
    
    def plus(self):
        get_sum = self.first+self.second+self.third
        
        if get_sum>100:
            print('버그')
        else:
            return print(get_sum)
        
    def parents_plus(self):
        ret = super().plus()
        return ret
        
a = morefunction(1,1,99)
a.plus()
t = morefunction(500,400,200)
print(t.parents_plus())
print(morefunction.mro())

## 이처럼 부모클래스의 plus 메서드를
## 새롭게 다시 정의하는 것을 '메서드 오버라이딩'이라고 한다.
## 이번에는 자식클래스에서 plus 메서드를 다시 정의 했지만 (메서드 오버라이딩을 했지만)

## 부모 클래스에서의 plus 메서드를 자식클래스에서도 또 사용하고 싶다면???
## 이때 super()를 이용할 수 있다. 

class Person():
    def __init__(self,name,age):
        self.name=name
        self.__age=age  ## 언더스코어 2개를 붙여
        
    def getter(self):
        return self.__age
    
    def setter(self,value):
        self.__age=value

k =Person('kevin', 39)

print(k.getter())
k.setter(29)
print(k.getter())

## 클래스의 private한 속성값을 getter와 setter를 이용해서 확인 그리고 값 변경이 가능ㅎㅁ
## 그 다음에는 위 코드를 좀더 간단하게 적기 위해 데코레이터를 사용할 것이다.

## getter 메소드에는 @property 라는  데코레이터를 사용하고
## setter 메소드에는 @변수.setter 로 데코레이터를 사용할 것이다.


class Person():
    def __init__(self,name,age):
        self.name=name
        self.__age=age  ## 언더스코어 2개를 붙여
    
    @property    
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,value):
        self.__age=value
        

k = Person('kevin',39)

print(k.age)
k.age = 29
print(k.age)


## 참고로 @property 데코레이터 사용을 하면 메서드 호출시 ()를 생략해야 한다.
## 관례상 setter getter 함수명은 변수명을 따른다.
from collections import Counter


lst = ['apple','mango','banana','mango','apple','mango','banana','mango','apple']

# counter 는 리스트 안에 중복된 데이터가 각각 몇개씩 있는지 알려준다.

print(Counter(lst))

ret = dict(Counter(lst))

print(ret)

st = 'an apple mangop'

ret = dict(Counter(st))
print(ret)

ret = sorted(ret.items(),key = lambda x:x[1],reverse=True)

print(ret)
print(ret[0])
print()
st = 'an apple mangop'
## st요소를 세어 , 최빈값 n개를 반환한다. 
ret = Counter(st).most_common(1)
print(ret)

## 추가적으로 Counter를 가지고 덧셈 뺄셈도 지원합니다. 

a = Counter('apple')
b = Counter('mango')
print(a)
print()
print(b)
print()
print(a+b)
print()
print(a-b)

a.subtract(b)

print()
print(a)