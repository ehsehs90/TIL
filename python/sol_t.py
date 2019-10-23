#1

str=input('문자를 입력하세요')

print(f'마지막 글자는 {str[-1]}')
print(f'마지막 글자는 {str[len(str)-1]}')


#2
for number in range(numbers):
    print(number+1)

for number in range(1, numbers+1):
    prunt(number)


#3

#1. 첫번째방식

if number % 2:   #2로 나누었을 때 나머지가 나오면
    print('홀수')
else:
    print('짝수')

#2. 두번째 방식

if number % 2 == 0:
    pass
else:
    pass


#4

if a>= 90 and b>80 and c>85 and d>= 80:
    print('합격')
else:
    print('불합격')

#5
#.split() 사용할 수 있음

prices = input('물품 가격을 입력하세요')


#split 메서드를 통해 일정한 기준에 따라 분리해서 리스트에 담는다
split = prices.split(';')
result =[]

for make in makes:
    result.append(int(make))


#내림차순 정렬! .sort()메서드는 리스트 원본 자체를 바꾸어버린다
result.sort(reverse=True)

for price in result:
    print(price)
