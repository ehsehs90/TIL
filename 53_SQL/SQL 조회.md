# SQL 조회

```sql
SELECT 칼럼명1, 칼럼명2 
    [FROM 테이블명 ] 
    [GROUP BY 칼럼명] 
    [ORDER BY 칼럼명 [ASC|DESC]] 
    [LIMIT offset, 조회 할 행의 수]
```



## 그룹핑

### GROUP BY

특정 칼럼을 기준으로 데이터를 그룹핑함



### 문법

```sql
SELECT * FROM 테이블명 GROUP BY 그룹핑 할 기준 칼럼명
```



### 예제

```sql
DROP TABLE IF EXISTS 'students';
CREATE TABLE 'student'(
	'id' tinyint(4) NOT NULL,
	'name' char(4) NOT NULL,
    'sex' enum('남자','여자') NOT NULL,
    'address' varchar(50) NOT NULL,
    'distance' INT NOT NULL,
    'birthday' datatime NOT NULL,
    PRIMARY KEY ('id')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

``` sql
INSERT INTO `student` VALUES (2, '박재숙', '남자', '서울',  10, '1985-10-26 00:00:00');
INSERT INTO `student` VALUES (1, '이숙경', '여자', '청주', 200, '1982-11-16 00:00:00');
INSERT INTO `student` VALUES (3, '백태호', '남자', '경주', 350, '1989-2-10 00:00:00');
INSERT INTO `student` VALUES (4, '김경훈', '남자', '제천', 190, '1979-11-4 00:00:00');
INSERT INTO `student` VALUES (8, '김정인', '남자', '대전', 200, '1990-10-1 00:00:00');
INSERT INTO `student` VALUES (6, '김경진', '여자', '제주', 400, '1985-1-1 00:00:00');
INSERT INTO `student` VALUES (7, '박경호', '남자', '영동', 310, '1981-2-3 00:00:00');

```

 

### 조회

```sql
select sex from student group by sex;
select sex, sum(distance), avg(distance) from student group by sex;
```



## ORDER

지정된 칼럼을 기준으로 행을 정렬

### 문법

```sql
SELECT * FROM 테이블명 ORDER BY 정렬의 기준으로 사용할 열 [DESC| ASC]
```



### 조회

```sql
select * from student order by distance desc;
select * from student order by distance desc, address asc;
```



## index

색인, 조회할 때 원하는 행을 빠르게 찾을 수 있게 준비해둔 데이터



### 인덱스의 종류

- primary: 중복되지 않는 유일한 키
- normal : 중복을 허용하는 인덱스
- unique : 중복을 허용하지 않는 유일한 키
- foreign : 다른 테이블과의 관계성을 부여하는 키
- full text : 자연어 검색, myisam에서만 지원

### primary key

- 테이블 전체를 통틀어서 중복되지 않는 값을 지정해야 한다.
- where 문을 이용해서 데이터를 조회할 때 가장 고속으로 데이터를 가져올 수 있다.
- 테이블마다 딱 하나의 primary key를 가질 수 있다.

```sql
select * from student where id=3;
```

### unique key

- 테이블 전체를 통틀어서 중복되지 않는 값을 지정해야 한다. (== primary key)
- 고속으로 데이터를 가져올 수 있다.
- 여러개의 unique key를 지정할 수 있다.

```sql
select* from student where number=0534543;
```

### normal key

- 중복을 허용한다.
- primary, unique 보다 속도가 느리다.
- 여러개의 키를 지정할 수 있다.

```sql
select * from student where department='국문과'
```



### 중복키

- 하나의 키에 여러개의 칼럼을 포함

```sql
select * from student where department='국문과' AND address='제주';
```

## 인덱스의 정의 방법

- 자주 조회되는 칼럼에 적용
- 조회 시 오랜시간을 소모하는 컬럼에 적용
- 데이터가 긴 경우 인덱스를 사용하지 않는다.





## 여러개의 테이블 사용하기

데이터의 규모가 커지면서 하나의 테이블로 정보를 수용하기가 어려워지면 테이블을 분활하고 테이블 간의 관계성을 부여한다.

## JOIN

테이블간의 관계성에 따라서 복수의 테이블을 결합, 하나의 테이블인 것처럼 결과를 출력

## JOIN의 종류

- OUTTER JOIN : 매칭되는 행이 없어도 결과를 가져오고 매칭되는 행이 없는 경우 NULL로 표시한다.
  LEFT JOIN과 RIGHT JOIN이 있다.
- INNER JOIN : 조인하는 두개의 테이블 모두에 데이터가 존재하는 행에 대해서만 결과를 가져온다.

## 예제

### LEFT JOIN

가장 많이 사용되는 조인의 형태

```sql
SELECT s.name, s.location_id, l.name AS address, l.distance  FROM student AS s LEFT JOIN location AS l ON s.location_id = l.id;

```

###  OUTTER JOIN과 INNER JOIN의 차이

Location에서 제주를 삭제 후 OUTTER JOIN(LEFT JOIN)과 INNER JOIN의 차이를 비교

```sql
DELETE FROM location WHERE name='제주'; 
 
SELECT s.name, s.location_id, l.name AS address, l.distance  FROM student AS s LEFT JOIN location AS l ON s.location_id = l.id; 
 
SELECT s.name, s.location_id, l.name AS address, l.distance  FROM student AS s INNER JOIN location AS l ON s.location_id = l.id;
```

 아래 이미지는 JOIN의 종류에 따른 결과를 보여준다.



![img](SQL 조회.assets/1861.png)