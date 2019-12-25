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



