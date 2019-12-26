## IS NULL



### 이름이 없는 동물의 아이디

```sql
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NULL
```



### 이름이 있는 동물의 아이디

```sql
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL
```



### NULL 처리하기

- 이름이 없는 동물의 이름은 "No name" 으로 표시하기

```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME , SEX_UPON_INTAKE FROM ANIMAL_INS 
```

- MYSQL 에서는 NVL 이 없고 대신 IFNULL 을 사용한다
- IFNULL( 컬럼 명, NULL 시 값)

> NAME 의 컬럼 값이 비면 'No name' 을 줘서 NAME 컬럼에 NULL 대신 들어온다

