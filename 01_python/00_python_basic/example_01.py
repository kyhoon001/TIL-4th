import random

#1. 변수를 활용한 반복 인사
greeting = '안녕하세요.'

print(greeting)
print(greeting)
print(greeting)
print(greeting)
print(greeting)

#2. 리스트 자료형 만들고 출력하기
menus = ['순남시래기','양자강','타코벨']
print(menus[1])

#3. 딕셔너리 자료형 만들고 출력하기
phone_book = {'순남시래기':'02-1234-5678', '양자강':'02-3142-5356', '타코벨':'02-646-2342'}
print(phone_book['타코벨'])

# 4. 반복문을 활용하여 여러번 인사할 수 있도록 해봅시다.
for i in range(5):
    print(greeting)

print(greeting)

n = 0
while n < 5:
    print(greeting)
    # n = n + 1
    n += 1

#5. 외장함수인 random을 활용하여 임의의 로또번호 출력하기
numbers = random.sample(range(1,46),6)
print(numbers)