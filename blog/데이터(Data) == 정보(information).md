# 데이터(Data) == 정보(information)

- 저장이나 처리에 효율적인 형태로 변환된 정보(information)

### 무한하게 증가하는 데이터

- 매일 초당 2억개의 메일 전송되며 3만명이 넷플릭스를 시청

- 배달의 민족 월평균 주문 약 6천만건 (2020)

- 전세계 모든 데이터의 약 90%는 2015년 이후 생산된 것 (IBM)

- "2025년 전세계 데이터 생성량 175 ZB에 이를것" - Seagate(2017)
  
  - 175ZB ? 
    
    - DVD로 나누어 담아 연결하면 달에 23번 방문하거나 지구를 22번 회전 가능
    
    - 평균 25mb/s로 다운로드 할 경우 18억년 소요

### 데이터는 뜨겁다

- 2022 전 세계 데이터센터 전력 소비량 250TWh로 남아공 국가 소비전력 추월

(남아공은 세계 16위 전력 소비국)

- 북극에 가까운 스웨덴 지역에 데이터 센터 설립 추진

- 미국 댈러스시에서 사용하는 물의 30% 냉각수에 사용 (구글 댈러스 데이터 센터)
  
  - 바다에 넣으려는 시도 (Microsoft - Project Natick)

### 중간정리

1. 우리는 매순간 데이터를 생성해 내고 있다.

2. 따라서 무한하게 증가하는 데이터를 '잘'저장하고 관리하는 기술이 필요하다.

## 파일을 이용한 데이터 관리

- 파일을 이용한 데이터 관리
  
  - 우리는 일반적으로 데이터를 파일에 저장한다.
  
  - 장점
    
    - 운영체제에 관계없이 어디에서나 쉽게 사용가능
    
    - 이메일이나 메신저를 이용해 간편하게 전송 가능
  
  - 단점
    
    - 성능과 보안적 측면에서 한계가 명확
    
    - 대용량 데이터를 다루기에 적합하지 않음
    
    - 데이터를 구조적으로 정리하기에 어려움
    
    - 확장이 불가능한 구조

## 표(스프레드 시트)를 이용한 데이터 관리

- 스프레드 시트(엑셀 시트) 을 사용

- 스프레드 시트 컬럼(열)을 통해 데이터의 유형을 지정하고 레코드(행)을 통해 구체적인 데이터 값을 포함
  
  - 단점
    
    - 무한하게 커질 수 없음(100만 행 정도가 최대)
    
    - 데이터 보안 측면
    
    - 데이터 무결성 측면

# 데이터베이스(Database)

"A databasse is an organized collection of data"

# DBMS(Database Management System)

"Database management systems (DBMSs) are specially designed software applications that interact with the user, other applications and the database itself to capture and analyze data" == **사용자와 상호작용하며 데이터 베이스를 조작하는 프로그램**

- SQLite

- MySQL

- mongoDB

- ORACLE

- PostgreSQL

- redis

- MariaDB

- elasticsearch 
  
  - 등등....

# 데이터베이스의 종류

### 관계형 데이터베이스 vs 비관계형 데이터 베이스

#### SQL vs NoSQL

- Relation(관계)
  
  - 수학  > 집합/논리 > 관계
  
  - 표 형식으로 정리된 데이터베이스

- 비관계 No != Not/ No == Not Only
  
  - 관계형 데이터베이스의 한계를 극복하기 위해 조금 더 유연한 데이터베이스
