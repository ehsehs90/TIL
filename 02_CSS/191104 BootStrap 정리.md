## BootStrap

###### Bootstrap 을 활용하여 나의 페이지를 꾸며보자

### CDN (Content Delivery Network)

- 컨텐츠 (CSS, JS, Image) 를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크 데이터를 제공하는 시스템 
  - 개발 (end-user)의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)
  - 외부 서버를 활용함으로써 본인 서버의 부하가 적어진다
  - 보통 적절한 수준의 캐시 설정으로 빠르게 로딩할 수 있다.



## 1. Utilites

- Class 로 정의되어 있어서 class로 접근하면 된다



### 1.1 Spacing

###### Bootstrap Spacing

- `.mr-0` : margin-right = 0

- `.py-0` : padding y 축(top,bottom) = 0

- `.mt-1` : margin-top : 0.25rem = 4px

  `.mt-2` : margin-top : 0.5rem = 8px

  `.mt-3` : margin-top : 1.0rem = 16px

- `.mx-auto` : 가운데 정렬

### 1.2 Color

> [Bootstrap Colors](https://getbootstrap.com/docs/4.3/utilities/colors/)



- `.text-primary`
- `.text-dark`
- `.text-secondary`
- `.text-success`
- `.text-warning`
- `.text-info`
- `.text-light`
- `.text-danger`
- `.text-white`
- `.text-white-50`
- `.text-black`
- `.text-black-50`



### 1.3 Border

- border
- border-top
- border-right
- border-bottom
- border-left



#### 1.3.1 Border Radius

- rounded
- rounded-top
- rounded-right
- rounded-bottom
- rounded-left
- rounded-circle
- rounded-pill
- rounded-0
- rounded-sm
- rounded-lg

pill vs rounded



### 1.4 Display

- `.d-none` : none 속성으로 변경한다.
- `.d-block` : block 속성으로 변경한다.
- d-sm-none d-md-block
  - small size에서는 none
  - medium size에서는 block



#### 1.4.1 반응형



### 1.5 Position

- .position-static
- .position-retative
- .fixed
  - .fixed-top
  - .fixed-bottom



### 1.6 Text

- .`text-center` : text-align : center
- .font-weight-bold : font-weight : bold



## 2. Layout

> https://getbootstrap.com/docs/4.3/layout/grid/



- 가장 가까운 곳은 container로 감싼다.
  - container-fluid : 양 옆에 여백없이 꽉차게
- Bootstrap은 12칸
  - 4칸 / 4칸 / 4칸 으로 나눈다
  - 만약 6/8/4로 나눈 경우, 자동으로 줄을 바꿔 칸을 나눈다.



#### 2.1 Grid options

#### 2.2 Column Wrapping

#### 2.3 Nesting

- 9칸 안에 12칸 (6/6 또는 8/4) 으로 중첩해서 적용할 수 있다.

#### 2.4 Offset

- 상쇄
- .col-md-6 .offset-md-3
  - 앞에 3칸 띄우고 6칸 채우기

<details class="details-reset details-overlay details-overlay-dark" style="box-sizing: border-box; display: block;"><summary data-hotkey="l" aria-label="Jump to line" role="button" style="box-sizing: border-box; display: list-item; cursor: pointer; list-style: none;"></summary></details>

- © 2019 GitHub, Inc.