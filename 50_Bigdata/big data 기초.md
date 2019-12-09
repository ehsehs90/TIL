# big data 기초

```python
import tensorflow as tf
##training data set

x = [1,2,3]
y = [1,2,3]  #label

W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

H = W*x + b     
```



# 선형회귀(linear regression)

> 가장 큰 목표는 가설의 완성
>



 가설(hypothesis) = Wx + b

### W와 b를 정의(Weight & bias 정의)


W = tf.Variable(tf.random_normal([1]), name="weight")  # W값 = 1차원 1개 "Weight"= 해당 tensoflow를 내부적으로 사용하기 위한 이름

b = tf.Variable(tf.random_normal([1]), name="bias")



# Hypothesis(가설)

우리의 최종 목적은 training data에 가장 근접한

Hypothesis를 만드는것(W와b를 결정)

잘 만들어진 가설은W 가 1에 가깝고 b가 0에 가까워야 한다. cost값은 최소값


H = W*x + b #결과값 당연히 node.

# cost(loss) function 

> 최적의H를 만들기 위해서 필요

우리의 목적은 cost함수를 최소로 만드는 W와 b를 구하는 것.

cost = tf.reduce_mean(tf.square(H-y)) #reduce_mean() : 평균구하는 함수



## cost function minimize

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01) #0.01이라는 러닝메이트를 이용해서 위쪽의 cost함수를최소화 시키기 위해 도와주는 함수를 만들자.

train = optimizer.minimize(cost)


텐서플로가 제공하는 최소화시키는것을 하나 만들어서

cost함수를 최소화할거다.



## runner 생성

sess = tf.Session()

## Global variable의 초기화

sess.run(tf.global_variables_initializer()) #variable이라는 W와 b사용하기 때문에 초기화작업한번 진행한다



## 학습진행

for step in range(3000):

_, w_val, b_val, cost_val = sess.run([train,W,b,cost])  ## sess.run해가지고 node를 4개 읽어서 각각 매핑되는 값을 넣는다.


if step % 300 == 0: # 300 600 900 일떄만 print해서 찍겠습니다

print("{},{},{}".format(w_val,b_val,cost_val))







## 경사하강법 gredient decent

```python

import tensorflow as tf


##training data set(받아드려서 프로그램으로 넘기기위한 공간)

x=tf.placeholder(dtype=tf.float32)

y=tf.placeholder(dtype=tf.float32)

## training data set

x_data=[1,2,3,4]

y_data=[4,7,10,13]



# Weight & bias ---W값의 초기값= random하게 0에 근사한 값으로 주자(아무거나 주면 이상해짐)

W = tf.Variable(tf.random_normal([1]), name="weight") ##weight라는 이름으로 w에 대한 tensorflow변수 선언

b = tf.Variable(tf.random_normal([1]), name="bias")


#Hypothesis

H = W*x + b


# cost(loss) function : 어떻게하면 저 1차함수graph가 trainingData에 가장 근접하까.....?하고 만든거임

cost = tf.reduce_mean(tf.square(H-y)) ##기본적인 cost function : 직선 -원래데이타 (차) 제곱의 형태로 만들었따. 2차함수



## cost function 을 최소화 시키기 위한 작업 ::경사하강법:gredient decent:(미어캣미어캣 찾다 가장 경사 급한쪽으로 가는 거) -

## loop를 돌아야함//알고리즘 복잡함 ::: tensorflow가 자체적으로 제공해주는 노드 있음 gradientDecentOptimizer

## learning_rate 값이 작으면 경사하강법 할때 경사 젤 급한쪽 찾아도 아주찔끔찔끔씩 움직인다.우리는 일반적으로 0.01쓸거임

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01) ##현재위치에서 찾아서 0.01이동

train = optimizer.minimize(cost) ##이거 실행하면 내부적으로 cost 최소화되면서 w.b값을 잡아준다 ##반복해야하기 떄문에 노드잡아준다.



# tensorflow graph동작시키려면 runner필요함 -> runner는 Session필요 && 초기화


sess = tf.Session()

sess.run(tf.global_variables_initializer()) ##tensorflow가 갖고있는 전역변수들을 초기화 시켜준다



## 준비 끝났으면 학습 가즈악~! 3000번 반복 가즈앗

for step in range(3000):

_, cost_val = sess.run([train,cost],feed_dict={x:x_data,y:y_data}) ##cost값이 최소화 되는걸로 학습이 제대로 되는지 확인하기 위해 뽑아서 보기 (변수 _: 사용하지 않겠다는 의미)

## 뭘 줘야해? 먹이데이터를 줘야함 - 데이터가 있어야 실행이.

if step% 300 == 0: ##300번마다

print(cost_val)


## prediction ::최종목적인 H

sess.run(H, feed_dict={x :[300]}) ## x라는 값에 내가 알고싶은 파라미터 ㄱㄱ(주의! x는 배열형태로 줬다 위에서 )


# Cost function 은 어떤 형태의 함수여야 하냐! convex function이여야 함

# Linear regression. 선형적인 데이터여야 한다.

# 따라서 앞으로 쓸 데이터가 선형적인지 아닌지도 확인하기 위해 matplotlib.pyplot 도 import시켰다.



```

#### 온도에 따른 오존량 예측

##### .csv 파일 read

```python
import tensorflow as tf

import numpy as np

import pandas as pd

import warnings

import matplotlib.pyplot as plt



warnings.filterwarnings(action="ignore")


df = pd.read_csv("./data/ozone/ozone.csv", sep="," )

display(df.head())

```



##### 필요한 column만 추출

```python

df2 = df[['Ozone','Temp']] #fancy indexing

#display(df2.head())

#결치값 처리(제거)


df3=df2.dropna(how="any", inplace=False) #how="all" : Ozone, Temp 에 둘다 NaN인경우 지워.


print(df2.shape)

print(df3.shape) ##결치값 제거한 것

```

##데이타를 보건데 완벽한 선형은 아닌듯 보인다.

##저기 보면 하나 딸랑 튀어난 이상한 점 있다 => 정제해야할 필요가 있어보인다.

## Why? 저런이상한 데이터가 머신러닝에 가중치를 많이줌.

##placeholder



x=tf.placeholder(dtype=tf.float32)

y=tf.placeholder(dtype=tf.float32)


#training data set


#데이터 정제 가즈아~!~!(밑에 내려갔따 올라오심)

#normalization : (요소값 - 최소값) / (최대값 - 최소값) : 무조건 1보다 작은값으로 떨어짐( 0이상 1이하)

x_data = (df3["Temp"]-df3["Temp"].min()) / (df3["Temp"].max() - df3["Temp"].min()) ##DataFrame 에서 Series형태로 데이터 뽑아씀

y_data = (df3["Ozone"]-df3["Ozone"].min())/ (df3["Ozone"].max() - df3["Ozone"].min())

# Weight & bias

W = tf.Variable(tf.random_normal([1]), name="weight")

b = tf.Variable(tf.random_normal([1]), name="bias")


#Hypothesis

H= W*x +b


#cost function

cost = tf.reduce_mean(tf.square(H-y))


#최소화 노드 생성

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

train = optimizer.minimize(cost)


#Session, 초기화

sess = tf.Session()

sess.run(tf.global_variables_initializer())


#학습(train)

for step in range(3000):

_, cost_val = sess.run([train, cost], feed_dict={x:x_data, y:y_data})


if step % 300 == 0:

print("cost:{}".format(cost_val))



#display(df3) # x와 y의 데이터 값 차이가 꽤 난다. 그래서 자꾸 발산한다. 이걸 정규화 할 필요가 있다. (Row data 정규화)

##그래야 제대로 된 costfunction이 일어나고 제대로 된 학습이 생길 수 있다.

#normalization : (요소값 - 최소값 ) / (최대값 - 최소값) : 무조건 1보다 작은값으로 떨어짐( 0이상 1이하)

##따라서 x, y 값은 무조건 0~1사이 값으로 정규화 할 수 있습니다.

###standardization : (요소값 - 평균) / 표준편차

#이 두가지 기법중 하나를 사용해 데이터를 정제한 후 학습시켜야 함.

## 변수가 1개일 때의 hypothesis

Hx = Wx+b

# 변수가 3개일 때의 hypothesis

H(x1,x2,x3) = w1x1+ w2x2+ w3x3 +b


#이렇게 많은 입력변수를 어떻게 처리할 까?

#-Matrix 이용!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Matrix multiplication

```python


import tensorflow as tf


##training data set

x_data = [[73,80,75],

[93,88,93],

[89,91,90],

[96,98,100],

[73,66,70]]


y_data = [[152],[185],[180],[196],[142]]


#placeholder


X = tf.placeholder(shape=[None,3],dtype=tf.float32) ##[5,3]

##이렇게 shape(내가 입력하는값의 shape)을 해줄 수 있는데 받아드릴때 Matrix 형태로 상관하지 않고 넣겠다 머 이런너낌[None,3]으로 가자

Y = tf.placeholder(shape=[None,1],dtype=tf.float32) ##[5,1]


##x와 w 를 곱해 y로 떨어져야 한다. (5.3) (3.1) (5.1) 따라서 W는 (3.1) 입니다

#Weight & bias

W = tf.Variable(tf.random_normal([3,1]), name="weight")

b = tf.Variable(tf.random_normal([1]), name="bias")


# Hypothesis

#H= W*x+b

H= tf.matmul(X,W)+b

##텐서플로우가 제공하는 행렬 곱 함수


#Cost function

cost=tf.reduce_mean(tf.square(H-Y)) #원래 일차원 벡터였던 h-x. 지금현재는 매트릭스인데 알아서(같은 행과 같은 열의) 차의 제곱알아서 해줌squre이


#학습노드 생성

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)


#Session & 초기화

sess= tf.Session()

sess.run(tf.global_variables_initializer())


for step in range(3000):

_, cost_val = sess.run([train,cost], feed_dict={X:x_data, Y:y_data})

if step % 300 ==0:

print(cost_val)



#정규화 안하고 학습시켜주면 발산해버림 ->왜? 정규호ㅏ 안했자나

```

## Temp가지고 Ozone 예측 가즈아~

df33=df[["Solar.R","Temp","Wind","Ozone"]]

df44=df33.dropna(how="any", inplace=False) ##정제한 녀석.


df55=df44[["Solar.R","Temp","Wind"]] ##정제한 녀석을 갖고 column get.

df66=df44[["Ozone"]] ##정제한 녀석을 갖고 column get.

display(df44.shape)

display(df55.shape)

display(df66.shape)

*************안되는 이유 remind*************

df6=df[["Ozone"]]

df7=df6.dropna(how="any", inplace=False)

display(df7)

display(df7.head())

display(df7.shape)

#x_data = (df3["Temp"]-df3["Temp"].min()) / (df3["Temp"].max() - df3["Temp"].min()) ##DataFrame 에서 Series형태로 데이터 뽑아씀

#y_data = (df3["Ozone"]-df3["Ozone"].min())/ (df3["Ozone"].max() - df3["Ozone"].min())



#training data set

x_data = (df55-df55.min()) / (df55.max() - df55.min())



#y_data = [[(df7["Ozone"]-df7["Ozone"].min()) / (df7["Ozone"].max() - df7["Ozone"].min())]]

y_data1 = df66["Ozone"].values.reshape(-1,1) ##-1은 뒤에 값 따르겠다는 뜻임.

y_data = (y_data1- y_data1.min())/(y_data1.max()-y_data1.min())


#placeholder


X = tf.placeholder(shape=[None,3],dtype=tf.float32) ##[5,3]

##이렇게 shape(내가 입력하는값의 shape)을 해줄 수 있는데 받아드릴때 Matrix 형태로 상관하지 않고 넣겠다 머 이런너낌[None,3]으로 가자

Y = tf.placeholder(shape=[None,1],dtype=tf.float32) ##[5,1]


##x와 w 를 곱해 y로 떨어져야 한다. (5.3) (3.1) (5.1) 따라서 W는 (3.1) 입니다

#Weight & bias

W = tf.Variable(tf.random_normal([3,1]), name="weight")

b = tf.Variable(tf.random_normal([1]), name="bias")


# Hypothesis

#H= W*x+b

H= tf.matmul(X,W)+b

##텐서플로우가 제공하는 행렬 곱 함수


#Cost function

cost=tf.reduce_mean(tf.square(H-Y)) #원래 일차원 벡터였던 h-x. 지금현재는 매트릭스인데 알아서(같은 행과 같은 열의) 차의 제곱알아서 해줌squre이


#학습노드 생성

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)


#Session & 초기화

sess= tf.Session()

sess.run(tf.global_variables_initializer())


for step in range(3000):

_, cost_val = sess.run([train,cost], feed_dict={X:x_data, Y:y_data})

if step % 300 ==0:

print(cost_val)



#정규화 안하고 학습시켜주면 발산해버림 ->왜? 정규호ㅏ 안했자나

## multiple linear regression

#### Ozone data 학습 및 예측

```python


import tensorflow as tf

import numpy as np

import pandas as pd

from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv("./data/ozone/ozone.csv", sep=",")


#필요한 컬럼만 추출

df.drop(["Month","Day"],axis=1, inplace=True) #저거 2개빼면 Ozone solar.r wind temp 이케남음



df.drop(column="~~~> ~~<") 
#결치값 처리(제거)

df.dropna(how="any", inplace=True)

# x데이터 추출

df_x = df.drop("Ozone",axis=1, inplace=False)

# y데이터 추출

df_y = df["Ozone"]

#display(df_x)


#training data set

x_data = MinMaxScaler().fit_transform(df_x.values)

y_data = MinMaxScaler().fit_transform(df_y.values.reshape(-1,1))


#display(y_data)




#placeholder


X=tf.placeholder(shape=[None,3], dtype=tf.float32)

Y=tf.placeholder(shape=[None,1], dtype=tf.float32)


#Weight & bias

W= tf.Variable(tf.random_normal([3,1]), name="weight")

b = tf.Variable(tf.random_normal([1]), name="bias")


#Hypothesis

H=tf.matmul(X,W)+b


#cost function

cost= tf.reduce_mean(tf.square(H-Y))


#train node생성

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)


#Session. & 초기화

sess= tf.Session()

sess.run(tf.global_variables_initializer())


#학습진행

for step in range(30000):

_, cost_val = sess.run([train,cost],feed_dict={X:x_data ,Y:y_data})


if step % 3000 == 0:

print(cost_val)


#prediction

print(sess.run(H, feed_dict={X:[[190,4.7,67]]}))
```

