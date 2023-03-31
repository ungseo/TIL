
def find_possible(number, broken):
    if number == 0:
        return 0
    cnt = 0
    while number > 0:
        digit = number % 10
        if digit in broken:
            return None
        cnt += 1
        number //= 10
    return cnt


n = int(input())
m = int(input())

broken = set(input().split())

# 모든 채널을 돌면서 가능한 채널일 경우
# 채널 번호와 N 사이의 차이와 같이 버튼을 누르는 횟수를 계산
ans = abs(n - 100)

for channel in range(1000001):
    channel_str = str(channel)
    # 버튼이 고장나지 않은 경우에만
    if set(channel_str) & broken:
        continue
    # 가능한 채널일 경우
    ans = min(ans, abs(channel - n) + len(channel_str))

print(ans)
