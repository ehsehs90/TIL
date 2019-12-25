# SUM, MAX, MIN

### 최댓값 구하기

> DATE 타입도 기본적인 연산이나 집계함수가 가능하다

```sql
/*my sql*/
SELECT DATETIME AS 시간 FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1

SELECT MAX(DATETIME) AS 시간 FROM ANIMAL_INS
```



### 최솟값 구하기

```sql
SELECT MIN(DATETIME) AS 시간 FROM ANIMAL_INS
```



### 동물 수 구하기

> 존재하는 모든 행을 가져온다 - COUNT(*)
>
> 만약 * 대신 COUNT(NAME) 이런 식으로 사용한다면 NAME 컬럼에 NULL 이 들어있지 않은 행 갯수를 가져오게 될 것이다.

```sql
SELECT COUNT(*) FROM ANIMAL_INS
```





### 중복 제거하기

> 1) 서브쿼리사용
>
> NAME 이 NULL 이 아니고 NAME 별로 GROUP을 해준 후 ANIMAL_INS 테이블의 NAME 들만 조회하는데 이후 밖에서는 이 행의 갯수만 COUNT(*) 로 세어주면 끝.

> 서브쿼리를 사용할 때 반드시 서브쿼리의 이름을 정해줘야 에러가 발생하지 않는다.

> 2) `DISTINCT`를 사용

```sql
/* 1 */
SELECT COUNT(*) 
FROM
(
    SELECT NAME
	FROM ANIMAL_INS
 	WHERE NAME IS NOT NULL
	 GROUP BY NAME
) SQ1
 
/* 2 */
SELECT COUNT(DISTINCT NAME) count
FROM ANIMAL_INS
```

