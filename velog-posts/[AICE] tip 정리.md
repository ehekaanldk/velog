---
title: "[AICE] tip 정리"
date: "2025-04-17"
link: "https://velog.io/@ehekaanldk/AICE"
series: "Uncategorized"
---

<ol>
<li><code>.copy()</code> 으로 이전의 데이터에 변화를 준 후 새로운 데이터명으로 부여할 때 <code>copy</code> 후에 변화를 준다. 이전의 데이터를 남겨두어야 drop과 같은 수행에서 오류가 발생하면 이전으로 돌아가기 편하다.</li>
</ol>
<ol start="2">
<li><code>조건식.mean()</code> 은  예를 들어 &quot;<em>&quot;이면 True를 아니면 다 False로 만들어서, 1과 0의 mean()으로 <strong>값의 비율</strong>을 구한다. ```('\</em>'인 행의 수) / (전체 행의 수)``` 와 같다.</li>
</ol>
<ol start="3">
<li><p><code>조건식.sum()</code>은 <strong>조건식에 맞는 행의 개수</strong>를 의미한다. </p>
</li>
<li><p><code>df['컬럼명'].replace(기존값, 바꿀값)</code> 은 반환해주지 않기 때문에 inplace=True를 적용하거나 , 다시 할당한다. </p>
</li>
<li><p><code>pd.to_numeric()</code>이나 <code>.astype()</code>으로 타입 변환을 한다. <code>pd.numeric(컬럼명, downcast='integer')</code>로 타입을 지정해준다. <code>.astype('int')</code>으로 타입을 지정해준다. </p>
</li>
<li><p><code>데이터프레임.drop(columns=컬럼명)</code> 에서는 기본값으로 drop 변환 후에 반영까지 하지않기 때문에 반드시 <code>데이터프레임.drop(columns=컬럼명, inplace=True)</code>를 해주는 것을 습관화하자.</p>
</li>
</ol>
<p>binary_crossentropy 는 타깃 레이블의 형태가 0또는 1의 이진분류일 때,
categorical_crossentropy 는 타깃 레이블의 형태가 one-hot encoding일 때,
sparse_categorical_crossentropy 는 타깃 레이블의 형태가 정수 인덱스일 때,</p>
<ol start="7">
<li><code>[표현식 for 변수 in 반복가능한객체]</code> 리스트 컴프리헨션을 알고 있으면 유용하다. 조건문을 추가하여 <code>[표현식 for 변수 in 반복가능한객체 if 조건]</code> 사용할 수도 있다. 
<code>[참일때 if 조건 else 거짓일때 for 변수 in 반복가능한객체]</code> 삼항 연산자를 사용한 버전도 알아두자.</li>
</ol>
<ol start="8">
<li><p>Pandas에서의 시리즈 간의 산술연산은 <code>+</code>를 통해서 <strong>시리즈 간의 원소별 덧셈</strong>을 수행한다. </p>
</li>
<li><p>Pandas에서 새로운 컬럼을 추가하는 방법은 <code>df['컬럼명'] = 값</code> 과 <code>df.insert()</code> 방식이 있다. 두방법의 차이는 ``df.insert(위치, 컬럼명, 값)<code>는 위치를 지정할 수 있다.</code>df['컬럼명'] = 값``` 방법은 해당 컬럼이 자동으로 생성돼서 맨 오른쪽에 추가된다. </p>
</li>
</ol>
<ol start="10">
<li>데이터분할에서의 주의점 <code>train : valid : test = 8 : 1 : 1</code> 의 경우는 먼저 전체 데이터를 <code>train : test = 9 : 1</code> 로 split을 먼저 해준 후에 나누어준 train에 대해서 train을  <code>train : valid = 8 : 1</code> 으로 split하여 전체적인 학습과 검증, 평가의 비율을 맞춰준다. 분수도 적용이 가능하다. </li>
</ol>
<ol start="11">
<li>y데이터에 대해 label이 1부터 10까지의 데이터로 이루어져 있을 때, 8개의 값만 존재하고 2개의 값이 존재하지 않다는고 했을 때, 모델링의 <code>n_class</code>를 8로 설정하지 않도록 주의해야한다. 
<code>[2,8,5,6,7,4,3,10]</code> 의 값만 존재하는 데이터이지만 8로 설정하게 되면 <code>[1,2,3,4,5,6,7,8]</code> 로 설정되어 분류 모델의 의도와 맞지 않게 된다. 데이터의 명세서를 잘 확인해서 모델링 과정에서 반영해야 한다. </li>
</ol>
