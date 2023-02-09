# 함수

### 함수는 왜 사용할까요?

-  Decomposition(분해)

- len(), sum()의 실행결과 - > 어떻게 알았니? (이름으로 유추)

- ```python
  numbers = [1,2,3]
  result = 0 
  count = 0
  for num in numbers :
      result += num
      count += 1
  print(result / count) # 2.0
  
  
  numbers = [1,2,3]
  print(sum(numbers) / len(numbers)) # 2.0
  
  
  def average(numbers):
      return sum(numbers) / len(numbers)
  print(average(numbers)
  ```

함수를 쓰는 이유  =  보기쉽고 누구나 유추해서 사용 할 수 있음

함수의 내부구조를 변경할게 아니라면 몰라도 무방(함수의 장점,매력)

### 함수의 종류

- 내장함수
  
  - 파이썬에 기본적으로 포함된 함수

- 외장함수
  
  - impurt 문을 사용해서 외장 라이브러리에서 불러오는 함수

- 사용자 정의 함수
  
  - 직접 사용자가 만드는 함수



### 함수의 정의

INPUT(X) << parameters (입력)

``` 
function body
(code)
```

OUTPUT >> return (결과값)

### 함수의 기본 구조

- 함수 선언

```python
def name(date, mu = None) :
    blabla~##기능 코드 작성
    return output
```

- 함수 호출

```python
name()
```

간단

****

* Void function
  
  * 명시적인 return 값이 없는경우, None을 반환하고 종료

```python
def name():
    blabla~~
    print(blabla)
>>> blabla
```

* Value returning function

함수를 실행하면 return 값을 반환하고 **종료한다.**



### 주의- print vs return ****

* print 함수와 return의 차이점
  
  * print를 사용하면 호출될 때마다 값이 출력됨(주로 테스트를 위해 사용)
  
  * 데이터 처리를 위해서는 return 사용 (함수밖으로 값을 내보내줌)

* return은 항상 하나의 값 만을 반환
  
  * 두개 이상의 값을 반환하려면??
    
    ```python
        retrun A, B #,로 이어붙이면 자동으로 (tuple)로 묶여서 출력
        
        [A,B]를사용해서 리스트로 출력도 가능.
    ```

### Parameter와 Argument

* Parameter : 함수를 정의할 때, 함수 **내부**에서 사용되는 변수

* Argument : 함수를 호출할 때, 넣어주는 값

---

# Python의 범위(Scope)

#### Name Space : 어떤것을 할당했을때 컴퓨터가 임시로 저장해 놓는 공간

* Built-in Namespace : Python에 내장된 네임스페이스(len,sum )

* Global Namespace : Python으로 script가 실행될때 생성되는 네임스페이스

* Enclosing Namespace : 함수 안에 다른 함수가 들어있을때 바깥쪽에 있는 네임스페이스

* Local Namespace : 내가 어떠한 함수를 실행하면 함수 안쪽에 생성되는 네임스페이스

```
L < E < G < B 순으로 탐색.크기순
```

* 변수는 각자의 수명주기(lifecycle)가 존재
  
  * built-in scope
    
    * 파이썬이 실행된 이후부터 영원히 유지
  
  * global scope
    
    * 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  
  * local scope
    
    * 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### 그렇다면 수많은 네임스페이스의 저장된 이름들을 일일이 외워야 하나?

locals(), globals() 의 함수로 조회 가능

```python
x = '하'
def func1():
    global x  ## // nonlocal x
    x = '글로벌'
    print(x)

func1()    >>> 
print(x)    
```

( global x // nonlocal x )= global Ns 에 있는 x를 바꾼다.// 나를 감싸고있는 함수 바로 밖의 x를 바꾼다.

## 함수의 범위 주의

global을 사용하면 코딩이 쉬워짐. 하지만 남용 할 수록 변수의 가공이 어디서 어떻게 어느방향으로 되고있는지 **파악불가능.**


