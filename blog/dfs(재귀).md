# dfs(재귀)





# 중복순열

```python



```



# 순열

```python





```





# 조합

```python
name = '1234'
cnt = 0
path = ['']*3

def abc(level,start):
    if level == 3:
        for i in range(3):
            print(path[i],end = ' ')
        print()
        return
    for i in range(start, 4):
        path[level] = name[i]
        abc(level+1,i+1)
        path[level] = 0

abc(0,0)# level, start


print(cnt)
```



# 중복조합

```python
name = '1234'
cnt = 0
path = ['']*3

def abc(level,start):
    global cnt
    if level == 3:
        cnt += 1
        for i in range(3):
            print(path[i],end = ' ')

        print()
        return
    for i in range(start, 4):
        path[level] = name[i]
        abc(level+1,i)  ## +1 만 빼주면 중복조합 완성 
        path[level] = 0

abc(0,0)# level, start


print(cnt)

```



# 모든 부분집합 출력하기

- 방법 1

```python
cnt = 0
name = ['A','B','C','D']
path = ['','','','']
def dfs(level, idx):
    global cnt
    print(''.join(path))
    cnt += 1
    if level == 4:
        return

    for i in range(idx,4):
        path[level] = name[i]
        dfs(level+1, i+1)
        path[level] = ''

dfs(0,0)
print(cnt)
```

- 방법 2

``` python
