from collections import deque
name=['A','B','C','D']
arr=[[0,1,1,0],
     [0,0,1,1],
     [0,1,0,1],
     [0,0,0,0]]
answer=[]  # 탐색순서 저장 후 출력
used=[0]*4

def bfs(st):
    q=deque()
    q.append(st)
    while q:
        now=q.popleft()
        answer.append(name[now])
        for i in range(4):
            if arr[now][i]==1:
                if used[i]==0:
                    used[i]=1
                    q.append(i)

used[0]=1
bfs(0)
print(*answer)