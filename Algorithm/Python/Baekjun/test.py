import sys
li=str(sys.stdin.readline().rstrip())
ans=0
imm=0
minus=0
for i in range(len(li)):
    if(li[i]=='-' or li[i]=='+'):
        if minus==1:
            ans-=imm
            imm=0
        else:
            ans+=imm
            imm=0
    else:
        imm=imm*10
        imm+=int(li[i])
    if(li[i]=='-'):
       minus=1
if minus==1:
    ans-=imm
else:
    ans+=imm
print(ans)