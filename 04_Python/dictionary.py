#1. 딕셔너리만들기
lunch = {
    '중국집' : '032'
    }

lunch = dict (중국집 = '032')


#2. 딕셔너리 내용추가하기
lunch['분식집'] = '031'

#3. 딕셔너리 내용 가져오기(2가지)
artists = {
    '아티스트' : {
        '민수' :'민수는 혼란스럽다',
        '아이유': '좋은날'
    }
}

# 민수의 대표곡을 출력해보세요?

print(artists["아티스트"]["민수"])
print(artists.get("아티스트").get("민수"))

#1.4딕셔너리 반복문 활용하기
#1.4.1 기본 활용
for key in lunch:
    print(key)          #key로 출력됨
    print(lunch[key])   #key 로 value 추출


#1.4.2 .items : Key, value 모두 가져오기
for key, value in lunch.items():
    print(key, value)


#1.4.3 .values : Value만 가져오기
for value in lunch.values():
    print(value)

# Key만 가져오기
for key in lunch.keys():
    print(key)
