n = int(input()) # 거스름돈

coin_lst = [10, 70, 110]

lst = [[0 for i in range(n+1)] for _ in range(len(coin_lst))]

for coin in range(3):
    for i in range(10,n+1, 10):
        if i % coin_lst[coin] == 0:
            lst[coin][i] = i//coin_lst[coin]
        else:
            if i//coin_lst[coin] == 0:
                lst[coin][i] = lst[coin-1][i]
            else:
                if lst[coin-1][i] > i//coin_lst[coin] + lst[coin-1][i%coin_lst[coin]]:
                    lst[coin][i] = i//coin_lst[coin] + lst[coin-1][i%coin_lst[coin]]
                else:
                    lst[coin][i] = lst[coin-1][i]
min_coin = 21e8
for i in range(3):
    if lst[i][n] < min_coin:
        min_coin = lst[i][n]

print(min_coin)



# coin_cnt = 0 # 초기 코인값
# jjaturi = n
# for i in range(3):
#     cnt = 0
#     cnt, jjaturi = jjaturi//coin_lst[i] , jjaturi%coin_lst[i]
#     coin_cnt += cnt
#
# for i in range(coin_cnt):
#