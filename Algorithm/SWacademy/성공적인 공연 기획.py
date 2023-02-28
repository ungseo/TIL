# T = int(input())
# for tc in range(1, T + 1):
#     audience = list(map(int, map(str, input())))
#     clap_aud = audience[0]
#     hire = 0
#
#     for i in range(1, len(audience)):
#         if audience[i] == 0: continue
#         if clap_aud >= i:
#             clap_aud += audience[i]
#         else:
#             hire += i - clap_aud
#             clap_aud += i - clap_aud + audience[i]
#
#     print(f'#{tc} {hire}')
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     people = list(map(int, list(input())))
#     st = 1
#     needs = people[0]
#     empl = 0
#     while 1:
#         if st >= len(people):
#             break
#         if people[st] == 0:
#             st += 1
#             continue
#         if st > needs:
#             empl += st - needs
#             needs += empl + people[st]
#             st +=1
#         else:
#             needs += people[st]
#             st += 1
#     print(f'#{tc} {empl}')

T=int(input())
for test_case in range(1,T+1):
    st=list(map(int,input()))
    employ=0
# 2번째 사람부터 계산하기 시작
    for i in range(1,len(st)):
# 자릿수가 더 클 경우 모자란 만큼 사람을 고용하고
        if i>sum(st[:i]):
            employ+=(i-sum(st[:i]))
# 그자리에 그만큼 채워준다. (안하면 중복으로 세어짐)
            st[i-1]=(i-sum(st[:i]))
    print(f'#{test_case} {employ}')