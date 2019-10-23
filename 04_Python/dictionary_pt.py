'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

average = sum(score.values())/len(score)
print(average)

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    '민승': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    '건희': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')



total_score = 0
length = 0

for student_score in scores.values():
    for subject_score in student_score.values():
        total_score += subject_score
        length +=1

print(total_score/length)



# 3. 도시별 최근 3일의 온도입니다.
cities = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
'''
출력 예시)
서울 : 평균온도
대전 : 평균온도
광주 : 평균온도
부산 : 평균온도
'''


for name, temp in cities.items():
    average_temp = sum(temp)/ len(temp)
    print(f"{name}:{average_temp}")
# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')


cold =0
hot =0
count =0
cold_city =''
hot_city =''

for name, temp in cities.items():
    if count==0:
        cold = min(temp)
        hot = max(temp)
        cold_city = name
        hot_city = name
    else:
        #도시의 최저기온을 비교해서 업데이트
        if min(temp) <cold:
            cold=min(temp)
            cold_city=name

        #도시의 최고기온으 비교해서 업데이트
        if max(temp) > hot:
            hot= max(temp)
            hot_city = name
        count+=1

print(cold_city)
print(hot_city)
# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

# 1) 약식
2 in cities["서울"]

if 2 in cities['서울']:
    print("네")
else:
    print("노")