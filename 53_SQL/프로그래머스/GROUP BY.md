# GROUP BY



### 고양이와 개는 몇 마리 있을까

동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해보자. 이 때 고양이가 개 보다 먼저 조회되도록 하자

> GROUP BY 가 있어야  COUNT를 쓸 수 있다.
>
> GROUP BY 로 묶을 컬럼 값
>
> - 특정한 분류를 기준으로 값을 묶어야 할 때 GROUP BY를 사용한다. 
> - GROUP BY 절을 사용하면 이 절에 사용한 컬러만을 SELECT 절에 사용을 해야 하며, COUNT 와 같은 내장함수는 이 컬럼을 기준으로 작동한다. 
> - 따라서 GROUP BY ANIMAL_TYPE 을 사용했으므로 SELECT 에도  ANIMAL_TPYE만을 사용해야 한다

```sql
SELECT ANIMAL_TYPE , COUNT(*) COUNT FROM ANIMAL_INS GROUP BY(ANIMAL_TYPE)
```



해당 문제에서 고양이가 먼저 나오게 나와야 한다는 조건이 있다 ( 이 문제는 안해도 자동으로 됨 )

이 때 **CASE** 를 이용해서 ORDER BY 에 추가해주면 된다

```sql
/*My SQL*/

SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS COUNT
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY 
CASE ANIMAL_TYPE
	WHEN 'Cat' THEN 1
	WHEN 'Dog' THEN 2
	ELSE 3
END
```



### 동명 동물 수 찾기

동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회.

- 이름이 없는 동물은 집계에서 제외
- 결과는 이름 순

> Having 절 -   GROUP BY 절로 그룹화 했을 때 조건절을 쓴다(NULL값을 제외하고 통계내는 						것 유의)
>
> - COUNT(*) 는 NULL값도 포함해서 모든 레코드 갯수를 센다
> - COUNT(표현식) 은 표현식에서 값이 NULL 이 들어가면 제외하고 센다

```sql
SELECT NAME, COUNT(NAME) FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) >=2 ORDER BY NAME
```





### 입양 시각 구하기(1)

몇 시에 입양이 가장 활발하게 일어나는지 알아보고싶다.

- 9시부터 19시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문

- 결과는 시간대 순 정렬

```sql
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT 
FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <=19 
GROUP BY HOUR(DATETIME)
```

> 포인트는 DATETIME을 어떻게 시간별로 가공하냐는 것이다.
>
> - GROUP BY HOUR(DATETIME) 을 이용해서 DATETIME 을 시간별로 나눌 수 있고 WHERE절에서 HOUR(DATETIME) >=9, HOUR(DATETIME) <= 19를 넣어줘서 9시부터 19시 사이의 값만 받을 수 있다.
> - **HOUR() = MYSQL 의 function**





### 입양 시각 구하기 (2)

몇 시에 입양이 가장 활발하게 일어나는지 알아보고싶다.

- 9시부터 19시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문

- 결과는 시간대 순 정렬

> POINT
>
> 전체 시간대를 구해야한다 = 테이블에 없는 시간대를 만들어줘야 한다.
>
> 1) 그래서 시간 정보를 갖고 있는 새로운 테이블을 만들어서 이와  JOIN 해야한다.
>
> 2) 아님 변수를 설정한다
>
> 	-  set @x : -1  // 초기 변수 설정
> 	-  @x = @x +1 // 칼럼 내 데이터에서 변수에 변화를 줄 때 사용

```sql
/* 풀이 1 */
SELECT H1.HOUR, IFNULL(H2.COUNT, 0)
FROM (
    SELECT 0 as HOUR
    UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 
    UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9 UNION SELECT 10
    UNION SELECT 11 UNION SELECT 12 UNION SELECT 13 UNION SELECT 14 UNION SELECT 15
    UNION SELECT 15 UNION SELECT 16 UNION SELECT 17 UNION SELECT 18 UNION SELECT 19
    UNION SELECT 20 UNION SELECT 21 UNION SELECT 22 UNION SELECT 23) H1
LEFT JOIN (
    SELECT HOUR(DATETIME) AS 'HOUR', COUNT(*) AS 'count'
    FROM ANIMAL_OUTS
    GROUP BY HOUR) as H2 on H1.hour = H2.hour ORDER BY H1.HOUR;
    
/* 풀이 2 */
set @hour = -1;
SELECT (@hour := @hour + 1) AS HOUR,
        (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour ) as COUNT
FROM ANIMAL_OUTS
WHERE @hour <23;
```



### 

