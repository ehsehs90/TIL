

## SELECT 

### 동물의 아이디와 이름( 오름차순 )

```sql
/* MySQL */
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC
```



### 여러 기준으로 정렬하기

- 이름순으로 정렬
- 같은 이름 내에서는 보호를 나중에 시작한 것을 먼저 조회

```sql
/* MySQL */
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME ASC, DATETIME DESC
```

> 다중 ORDER BY
>
> 방법은 간단히 뒤에 덧붙여 주면 된다



### 상위 n개 레코드

> Oracle을 많이 사용해본 경우에는 `ROWNUM`을 쓰려고 할텐데
>
> 문제는 MYSQL에서는 그게 없어서 대신 `LIMIT`을 사용해 줘야 한다

```sql
/* Oracle */
SELECT NAME FROM (SELECT NAME FROM  ANIMAL_INS ORDER BY DATETIME ASC ) WHERE ROWNUM=1 ;

/* MySQL */
 SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1
```



