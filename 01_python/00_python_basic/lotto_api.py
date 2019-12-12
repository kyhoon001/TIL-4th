import requests
import random

# 최근인 888회 로또번호 가져오기
res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=888')
lotto = res.json()
# print(lotto)

# 당첨번호 6개만 가져오기
winner = []
for i in range(1, 7):
    winner.append(lotto[f'drwtNo{i}'])

# 랜덤 로또번호 추출
numbers = sorted(random.sample(range(1,46),6))
    
matched = 0
for num in numbers:
    if num in winner:
        matched += 1

# matched = len(set(winner) & set(numbers))

# 반복문(1등 당첨될때까지 로또를 몇번이나 사야하는지)
cnt = 0
while matched < 6:
    numbers = sorted(random.sample(range(1,46),6))
    matched = 0
    for num in numbers:
        if num in winner:
            matched += 1
    cnt += 1
    print(cnt)
    print(winner)
    print(numbers)
    
    if matched == 6:
        print('1등입니다!!!')
    elif matched == 5:
        if lotto['bnusNo'] in numbers: # 보너스 번호 확인
            print('2등입니다!!')
        else:
            print('3등입니다!')
    elif matched == 4:
        print('4등입니다.')
    elif matched == 3:
        print('5등입니다..')
    else:
        print('꽝입니다..')