T = int(input())
for tc in range(1, T+1):
    bit_lst = list(map(int,map(str,input())))
    edit = 0
    st_idx = 0
    for i in range(len(bit_lst)):
        if bit_lst[i] == 1:
            st_idx = i
            edit += 1
            break


    switch = 1

    for i in bit_lst[st_idx:]:
        if switch == i: continue
        edit += 1
        if i == 1:
            switch = 1
        else:
            switch = 0

    if st_idx == 0 and bit_lst[0] == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {edit}')
