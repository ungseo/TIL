T = int(input())
for tc in range(1, T + 1):
    sentence = input()

    for i in range(2, 11):
        if sentence[:i] == sentence[i:2 * i]:
            print('#{} {}'.format(tc, i))
            break
