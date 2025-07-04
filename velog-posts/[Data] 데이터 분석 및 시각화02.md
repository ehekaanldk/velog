---
title: "[Data] 데이터 분석 및 시각화02"
date: "2025-04-02"
link: "https://velog.io/@ehekaanldk/DAY05%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D-%EB%B0%8F-%EC%8B%9C%EA%B0%81%ED%99%9402"
series: "Uncategorized"
---

<h2 id="review">review</h2>
<p>수치형 변수는 크기를 비교할 수 있는 연속적인 숫자를 갖는 변수이다.</p>
<ol>
<li>x만 사용하는경우는  y는 자동으로 수치형 변수를 선택하도록 두는 경우입니다. 이때 x는 각범주를 나타내고  범주에 대해 수치형 데이터의 분포를 보여줍니다. </li>
</ol>
<ol start="2">
<li><p>x와 y 매개변수 둘다 사용하는경우는  범주형 변수와 수치형 변수 간의 관계를 시각화합니다. 일반적으로 x는 범주형 변수를 나타내고 y는 수치형 변수를 나타내게 됩니다.</p>
</li>
<li><p>hue매개변수와 survivied 컬럼을 두는 경우 의미의 차이는?
hue 매개변수는 범주형 변수로 각 그룹을  색상으로 구분하고 특정 범주에 대해 비교를 더 명확히 할 수 있도록 도와줍니다. suervived에 따라 색상을 다르게 표기함으로써 각 클래스 내에서  분포차이를 비교 할 수 있습니다.</p>
</li>
</ol>
<h2 id="05-단별량-분석">05 단별량 분석</h2>
<h3 id="051-단변량-분석-①---수치형">05.1. 단변량 분석 ① - 수치형</h3>
<h4 id="1-환경준비">1. 환경준비</h4>
<h4 id="2-수치화">2. 수치화</h4>
<ul>
<li><p>round() : 몇번째자리에서 반올림한다.</p>
</li>
<li><p>mean() : 평균을 구한다.</p>
</li>
<li><p>median() : 가장 가운데 위치한 중앙값</p>
</li>
<li><p>mode() : 가장 빈번하게 나타나는 최빈값</p>
<pre><code>titanic['Pclass'].mode()[0]
titanic['Pclass'].value_counts().idxmax()</code></pre><p>최빈값의 인덱스를 가져온다. value_counts()로 범주형의 값을 읽어와 index가 max인 값을 가져온다.</p>
</li>
<li><p>describe() : 4분위수와 함께 기술 통계를 보여준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/e7e19140-a1a9-4074-ac5f-60822d1d7fc7/image.png" />
시리즈를 [] 중괄호에 넣어주면 시리즈를 데이터프레임으로 만들어 줄 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/0af80bfd-064a-48a8-9d8f-8994e0989ef9/image.png" />
시리즈는 .T 가 안되지만, 데이터프레임은 .T 를 사용하여 가로로 돌릴 수 있다. </p>
</li>
</ul>
<h4 id="3-시각화">3. 시각화</h4>
<p>수치형 데이터는 분포와 흐름을 본다.</p>
<p>데이터의 분포는 히스토그램, density plot, box plot으로 확인한다.
<strong>histogram</strong>
히스토그램은 데이터의 분포를 확인하는 가장 기본적인 시각화 도구이다.</p>
<pre><code>sns.histplot(x='Ozone', data=air)
plt.show()</code></pre><pre><code>sns.histplot(x=air['Temp'])
plt.show()</code></pre><pre><code>sns.histplot(air['Wind'])
plt.show()</code></pre><p>다음은 모두 실행이 된다. </p>
<p><strong>density plot</strong>
수치형의 데이터 분포, 밀도를 확인 한다.
Pandas로도 plot() 메소드에서 kind매개변수를 kde로 지정해서 그릴 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/9e967d5d-e40f-44f5-a9be-6b6dba3afdbd/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7f589cc9-550c-46ef-9836-2f8e942699ea/image.png" />
seaborn을 이용한 방법이 값이 길게 늘어지지 않고 깔끔하게 나온다.</p>
<blockquote>
<p>확률밀도함수
셀 수 있는 값의 분포(이산 확률 분포, 주사위)는 표로 표현할 수 있다. 
셀 수 없는 값의 분포(연속 확률 분포, 학생들의 키)는 표로 표현할 수 없어 그래포로 표현한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/41efe834-b2e1-43b4-84bf-ff99c0d97479/image.png" />
a와 b사이의 확률을 구하고자 하면 그래프 아래의 색이 채워진 면적
정규분포의 확률
커널밀도함수는 실제 데이터에 대해서 그리기 때문에 정규분포와 다름</p>
</blockquote>
<p><strong>box plot</strong>
수치형의 데이터 분포를 확인 한다.
데이터의 결측치가 있으면 matplotlib은 그려지지 않는다. seaborn은 제외하고 그려준다. </p>
<pre><code>plt.boxplot(x='Fare', data=titanic, vert=False)
plt.show()</code></pre><p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b227d704-0daa-4f31-8fdd-67cf9621c307/image.png" />
matplotlib으로 box plot를 그린다. 기본적으로 세로로 그래프가 그려지며 vert=False를 하면 가로로 그릴 수 있다. matplotlib은 y에 컬럼을 주면 오류가 발생한다.</p>
<pre><code>sns.boxplot(x='Fare', data=titanic)
plt.show()</code></pre><p>seaborn은 y에 컬럼을 주면 세로로 세울 수 있다.</p>
<pre><code>sns.boxplot(x='Age', data=titanic,  width=0.2, color='w', medianprops={'color':'tab:orange'})
plt.axvline(titanic['Age'].mean(), color='r', linewidth=0.5, linestyle=':')
plt.show()</code></pre><p>box plot에서는 평균이 표현되지 않는다. 평균은 따로 구해서 그려야 한다.</p>
<p><strong>시계열 데이터 시각화</strong>
수치형의 데이터 분포를 확인 한다.
x축에 맞게 선 그래프로 표현한다. </p>
<ul>
<li><strong>Matplotlib</strong>의 <strong>plot()</strong> 함수를 사용해 Line Plot을 그립니다.</li>
<li><strong>Seaborn</strong>의 <strong>lineplot()</strong> 함수를 사용해 Line Plot을 그립니다.<pre><code>air['Date'] = pd.to_datetime(air['Date'])
</code></pre></li>
</ul>
<p>plt.plot('Date', 'Ozone', data=air, label='Ozone')
plt.plot('Date', 'Temp', data=air, label='Temp')
plt.xlabel('Date')
plt.legend()
plt.show()</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/8873242e-82e9-4a52-8964-3859dd075dd3/image.png)
</code></pre><p>sns.lineplot(x='Date', y='Ozone', data=air, label='Ozone')
sns.lineplot(x='Date', y='Temp', data=air, label='Temp')
plt.legend()
plt.show()</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/5922ac08-f41c-4349-9d67-d1d5ef45ebb3/image.png)

---
실습03</code></pre><h1 id="통게량">통게량</h1>
<p>carseat[['Sales']].describe().T</p>
<pre><code>변수들에 대해서 기초 통계량을 구한다.
</code></pre><h1 id="시각화">시각화</h1>
<p>plt.subplot(1,3,1)
sns.histplot(carseat['Sales'])</p>
<p>plt.subplot(1,3,2)
sns.kdeplot(carseat['Sales'])</p>
<p>plt.subplot(1,3,3)
sns.boxplot(carseat['Sales'])</p>
<p>plt.tight_layout()</p>
<pre><code>변수들에 대해서 데이터를 시각화해서 나타낸다. 시각화는 sns.histplot(), sns.kdeplot(), sns.boxplot() 함수를 사용한다.

---

### 05.2. 단변량 분석 ② - 범주형
범주형 변수에는 정해진 몇 개의 값이 여럿 모여있는 변수이다. 
- count로 볌주값이 몇개씩 있는지
- 전체에서 각각이 차지하는 비율은 어떤지

범주형 데이터로 살짝 변환하였음!
![](https://velog.velcdn.com/images/ehekaanldk/post/d8c4ed6e-aab9-45c9-ae04-f7e0cf2aa803/image.png)

#### 1. 수치화
**value_counts()**
value_counts() : 범주형 변수에 포함된 범주값 각각의 개수를 카운드
- normalize=True : 개수가 아닌 비율로 확인한다. </code></pre><p>print(titanic['Pclass'].value_counts() / len(titanic))</p>
<pre><code>normalize 매개변수를 사용하지 않고 len(데이터명)으로 데이터의 비율을 구할 수 있다. 
- unique() : 범주값 자체를 확인한다.</code></pre><p>titanic['Pclass'].unique()</p>
<h1 id="array3-1-2-dtypeint64">array([3, 1, 2], dtype=int64)</h1>
<pre><code>- sorted() : 정렬된 결과를 보여준다. 원본에 반영하지 않는다. (sort()는 정렬의 결과를 원본에 반환한다.)</code></pre><p>sorted(titanic['Pclass'].unique())</p>
<pre><code>
&gt;![](https://velog.velcdn.com/images/ehekaanldk/post/d2e3bdf6-59c9-4efc-85b9-39289ddd9aad/image.png)
다음과 같을 때 머신러닝을 적용하면 1을 맞추는 확률부터 0을 맞추는 확률이 더 높다. 실제 데이터는 0이 대부분이고 1이 2% 밖에 되지 않는다. 실제 1은 기계고장 등에 대한 확률임으로 예측의 의미가 매우 크다. 
</code></pre><p>col = 'AgeGroup'
print(titanic[col].value_counts())
print('-' * 20)
print(titanic[col].value_counts(normalize=True))</p>
<pre><code>변수들의 빈도수와 비율을 구할 수 있다. 
![](https://velog.velcdn.com/images/ehekaanldk/post/6aa573b3-2931-4cbf-89a9-dea80e401bda/image.png)
시리즈의 데이터 형태의 Name 값은 시리즈가 데이터프레임이 될 때 컬럼명이 된다. 
![](https://velog.velcdn.com/images/ehekaanldk/post/dcae610c-a648-46bc-a0ed-7ec55c1e02bf/image.png)

#### 2. 시각화
범주형 데이터의 시각화는 count plot, bar plot, pie chart, heatmap를 통해 시각화한다. 

**bar plot**
범주이름과 범주값이 필요하기 때문에 집계 작업(count)를 선행해야 한다. 
- Pandas의 **value_counts()** 를 사용하여 집계합니다.
    - 집계 결과의 index: 범줏값 이름
    - 집계 결과의 values: 값</code></pre><p>temp = titanic['Pclass'].value_counts()
temp
print(temp.index) # 범주값
print(temp.values) # 범주값 개수</p>
<pre><code>데이터프레임에서 데이터명.index, 데이터명.values 로 범주값과 범주값 개수에 접근할 수 있다. 

- bar() 함수로 시각화합니다.</code></pre><p>temp = titanic['Pclass'].value_counts()</p>
<p>plt.bar(x=temp.index.astype(str), height=temp.values)
plt.show()</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/87f9a7b5-0552-4674-a924-0b8a5b654f39/image.png)


- 가로 그래프를 그릴 때는 barh()함수로 그려야 한다. </code></pre><p>temp = titanic['Pclass'].value_counts()
plt.barh(y=temp.index.astype(str), width=temp.values)
plt.show()</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/e7741159-bb91-4022-8b6a-b50866d3b652/image.png)

- seaborn에서는 **count plot()**으로 집계와 그래프를 함께 그려준다. </code></pre><p>sns.countplot(x='Pclass', data=titanic)
plt.show()</p>
<pre><code>matplolib으로 그린 barplot은 자동으로 count()가 큰값으로 정렬되고, seaborn은 값의 순서와 문자열의 경우 나타난 순서에 따라서 정렬된다.


**pie chart**
- 범주별 값의 빈도수가 아닌 **비율을 비교**할 때는 Pie Chart를 사용합니다.
    - x(값) : 범주값의 실제값이 비율로 내부에 작성된다. 
    - labels : 외부에 작성되는 범주값이다.
    - autopct : 내부에 작성된는 값에 %를 달아준다.
- 파이의 각도와 방향을 조절할 수 있다. 
    - startangle=90: 90도 부터 시작
    - counterclock=False: 시계 방향으로
- 파이 간격과 그림자를 조절할 수 있다. 
    - explode=[0.05, 0.05, 0.05]: 중심으로 부터 1, 2, 3을 얼마만큼 띄울지
    - shadow=True: 그림자 추가</code></pre><p>temp02 = titanic['Sex'].value_counts()
print(temp02.index)
print(temp02.values)</p>
<pre><code>Pandas를 사용하여 pie chart를 그릴 때 value_counts로 먼저 집계를 하는 것이 필요하다. index와 values는 함수가 아니라 속성값으로 접근해야 하는 점을 주의한다. </code></pre><p>plt.pie(x=temp02.values, labels=temp02.index, autopct='%1.f%%')
plt.show()</p>
<pre><code>autopct를 설정해주지 않으면 내부에 적을 범주값의 실제값의 자료형을 지정해주지 않아서 작성되지 않는다. 주의하기!

---
실습</code></pre><p>col = 'Urban'
temp=carseat[col].value_counts()
print(temp)
print('-'*20)
print(carseat[col].value_counts(normalize= True))</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/1b0dc3b1-f652-4570-8c65-4e7770f653c6/image.png)</code></pre><p>plt.subplot(1,2,1)
sns.countplot(x=carseat[col])</p>
<p>plt.subplot(1,2,2)
plt.pie(x=temp.values, labels=temp.index, autopct='%1.f%%')</p>
<p>plt.tight_layout()
plt.show()</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/0642c666-22bc-49e9-b076-da075acc7295/image.png)

## 06. 이변량 분석
타이타닉 데이터에서 나이가 많을수록 요금이 많이 내는가?
두 변수 간의 관계를 살펴보기 위해 시각화와 수치화를 사용한다. 
### 06.1. 이변량 분석 ① - 수치형 → 수치형
두 수치형 데이터 사이에서의 상관관계를 분석한다.

#### 1. 시각화
두 수치형 변수의 관계를 시각화한다. 
&gt; 상관분석 
상관분석은 수치형 변수x 에 대한 수치형 변수y 의 관계를 분석할 때 사용된다.
- 두 수치형 변수 관계는 **산점도**를 사용해 시각화한다. 
- 두 수치형 변수의 관계를 비교할 때 직선(Linearity)를 중요하게 본다.

**산점도**
scatter plot(산점도)는 두 변수 간의 관계를 나타내는 그래프이다. 
- 점들의 분포 형태를 통해서 두 변수 간의 상관관계를 파악한다. 
- matplotlib의 scatter() 메서드를 통해서 산점도 그래프를 그릴 수 있다. 
- 데이터의 폭이 얇을수록 강한 상관관계를 가진다.
- seaborn의 scatterplot() 메서드로 산점도 그래프를 그린다.</code></pre><p>plt.scatter(x='Temp', y='Ozone', data=air, s=10, c='g')
plt.xlabel('Temp')
plt.ylabel('Ozone')
plt.show()</p>
<pre><code>산점도의 marker와 color를 지정해 줄 수 있다. 
![](https://velog.velcdn.com/images/ehekaanldk/post/23c30265-311b-44e1-ab9c-6e7a2ffd9218/image.png)
양의 상관관계를 가짐을 볼 수 있다. 
![](https://velog.velcdn.com/images/ehekaanldk/post/ff2cdc07-74c0-46e4-be8e-cb30e46e84f6/image.png)
가운데 점에 대해서 오른쪽 아래의 위치한 데이터들은 강한 상관관계를 유지하지 않는다. </code></pre><p>plt.scatter(x=air['Wind'], y=air['Ozone'])
plt.xlabel('Wind')
plt.ylabel('Ozone')
plt.show()</p>
<pre><code>간략화하여 작성해 산점도 그래프를 그릴 수 있다. x값의 값이 유사한 컬럼들 사이에서는 2개의 그래프를 그릴 수 있다. </code></pre><p>sns.scatterplot(x='Temp', y='Ozone', data=air)
plt.show()</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/753526e3-a42b-49d1-a71c-de858b6cd101/image.png)
seaborn으로 그린 산점도에서는 겹치는 값이 edgecolor=white(기본값)으로 입체감있게 나타난다. 

![](https://velog.velcdn.com/images/ehekaanldk/post/5ad6caf7-fff5-4076-82b5-464b5d876f69/image.png)
범주형 변수에 대해서 수치형 변수를 보았지만 의미적으로는 의미가 있다..

- 수치화만으로는 확인이 불가능할 수 있다. 
- 시각화도 필요하다. 

![](https://cqeacademy.com/wp-content/uploads/2018/06/Scatter-Plots-and-Correlation-Examples.png)
- 직선이고 오른쪽 위로 향할 때, 강한 양의 상관관계를 의미한다. 
- 산점도의 폭에 따라서 강한지 약한지가 나타난다. 
- 직선이고 왼쪽 아래를 향할 떄, 강한 음의 상관관계를 의미한다. 

**Pair plot**
- **Seaborn**의 **pairplot()** 함수는 데이터프레임의 모든 숫자형 변수 쌍에 대한 **산점도**와 **히스토그램**을 같이 그려줍니다.
- pair plot은 수치형 변수에 대해서만 시각화한다. </code></pre><p>sns.pairplot(air)
plt.show()</p>
<pre><code>
**Joint plot**
- **Seaborn**의 **jointplot()** 함수는 두 개의 변수 사이의 관계를 시각화하기 위한 유용한 도구입니다.
- 기본적으로 **산점도**를 그려주고, **히스토그램**으로 각 변수의 분포를 보여줍니다.
- **kind** 매개변수를 사용하여 **reg, hex, kde** 등 다양한 형태의 그래프를 그릴 수 있습니다.</code></pre><p>sns.jointplot(x='Solar.R', y='Ozone', data=air, kind='hex', marginal_kws=dict(bins=20))
plt.show()</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/8ba7ad54-7a3f-4d25-b191-401bd17a2a52/image.png)


#### 2. 수치화
수치형 변수와 수치형 변수의 관계를 비교하고자 할 때는 상관분석을 수행한다. 
상관계수와 p-value를 사용하여 두 변수의 상관관계를 확인할 수 있다. 
&gt;- 상관계수 r
    - 두 변수 간의 선형 관계의 강도와 방향을 측정하는 통계 지표이다.
    - -1 부터 1 사이의 값을 가진다. 
    - 강함: 0.5 &lt; |𝑟| ≤ 1
    - 중간: 0.2 &lt; |𝑟| ≤ 0.5
    - 약함: 0.1 &lt; |𝑟| ≤ 0.2
    - (거의)없음: |𝑟| ≤ 0.1
    - scipy.stats 라이브러리의 pearsonr() 함수로 상관관계를 확인한다.
</code></pre><p>result = <strong>spst.pearsonr</strong>(air['Temp'], air['Ozone'])</p>
<p>print(result)
print('* 상관계수:', result[0])
print('* p-value:', result[1])</p>
<pre><code>
pearsonr() 메서드의 결과값 중 첫번쨰 값이 상관계수가 되고, 두번째 값이 유의수준 p-value가 된다. 

&gt;- 유의수준 p-value
    - 우리의 대립가설이 맞다고 받아드릴 때, 선택이 잘못될 확률을 의미한다. 
    - 귀무 가설이 맞을 확률(대립가설이 틀릴 확률)과 동일하다.
    - 값이 매우 작을수록 좋다.
    - p-value는 대립가설이 받아들여질 때 실수일 확률이다. 
    - **주의**: 결측치가 있으면 계산되지 않습니다. 반드시 .notnull()로 제외하고 수행해야 한다.


&gt;대립가설(주장) : 두 수치형 변수가 상관관계가 있다. 
귀무가설(일반적인 가설, 없어져야 하는 가설) : 두 수치형 변수가 상관관계가 없다.

</code></pre><p>air['Solar.R'].notnull()</p>
<pre><code>notnull()은 null아 아닌것들이 True가 되고, null인 것들을 False가 된다. </code></pre><p>air2 = air.loc[air['Solar.R'].notnull(), :]
result = spst.pearsonr(air2['Solar.R'], air2['Ozone'])</p>
<p>print(result)
print('* 상관계수:', result[0])
print('* p-value:', result[1])</p>
<pre><code>loc[] 안에 넣어서 True인 것만 가져오도록 한다. 

- Pandas의 corr() 메소드를 사용해서 변수들 간의 상관계수를 한번에 확인할 수 있다. </code></pre><p>air.corr(numeric_only=True)</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/e08471ac-0fa8-437e-99b7-0310fd0d462f/image.png)
</code></pre><p>air.corr(numeric_only=True).style.background_gradient()</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/8600e95b-0e4a-4664-964c-c725d51a3068/image.png)
.style.background_gradient() 를 추가하여 heatmap과 유사하게 그래프를 그릴 수 있다. 

- **Seaborn**의 **heatmap()** 함수로 상관계수를 시각화 할 수 있다.</code></pre><p>plt.figure(figsize=(6, 6))
sns.heatmap(air.corr(numeric_only=True),
            annot=True,
            fmt='.3f',
            cmap='Blues',
            vmin=-1,
            vmax=1,
            square=True,
            cbar=False)
plt.show()</p>
<p>```
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/50c0af09-d605-4069-9afc-c5503afd6390/image.png" /></p>
<p>p-value는 상관관계가 있다 없다할 때 도움을 주는 값이다.
상관계수는 상관관계의 강함과 약함을 나타내는 값이다.</p>
<p>상관관계가 적은 값을 제거하라는 아니다.</p>
<h4 id="3-상관계수의-한계">3. 상관계수의 한계</h4>
<p>상관계수는 방향이 아닌 폭을 의미한다. 상관계수가 0이더라도 의미를 가질 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/f1d41a5a-b3ce-4337-81a8-5aa1975d22ef/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/22a0a778-8344-4eeb-9517-253c503d4107/image.png" />
상관관계가 없다고 판단할 수 있다. 상관계수의 값이 매우 작고, p-value가 높은 값으로 상관관계가 없을 가능성이 높다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d99c9c5e-adbe-4fab-a3f2-084f134c1611/image.png" />
시각화를 해보면 패턴과 의미를 가진다. 수치화해서 하나의 숫자로 요약하는 데는 많은 장점이 있지만, 한계도 존재한다. </p>
<p>약한 상관관계는 상관관계가 없다와 같은 의미를 가진다. </p>
<h2 id="07-가설과-가설검정">07 가설과 가설검정</h2>
<p>모집단(Population) : 대상 전체의 영역(미래의 데이터)
표본(sample) : 대상의 일부 영역(과거의 데이터)</p>
<p>가설은 모집단(Population)에 대한 가설 수립이다. 표본(sample)을 가지고 가설이 진짜 그러한지 검증한다. </p>
<p>고객의 이탈여부가 (y/n) 일 때 이탈여부(target)에 요인이 되는 값(x)을 뽑아서 초기 가설을 수립한다. </p>
<blockquote>
<p>귀무가설 H_0 가 모두가 주장하는 바이다. (무로 돌아간다는 의미를 가진다. 없어졌으면 하는 가설)</p>
</blockquote>
<ul>
<li>현재의 가설</li>
<li>보수적인 입장
대립가설 H_1 가 내가 주장하는 바이다. (연구를 통해서 밝혀내는 바이다.)</li>
<li>연구가설</li>
<li>새로운 가설</li>
</ul>
<p>우리가 가지고 있는 데이터인 표본(sample)에 대해서 대립가설을 확인하고 모집단(Population)도 맞을 것이라고 주장한다. 
• 대립가설: 매장지역(𝑥2)에 따라 수요량(𝑦)에 차이가 있다.
• 귀무가설: 매장지역(𝑥2)에 따라 수요량(𝑦)에 차이가 없다.
• 얼마나 큰 지, 얼마나 작은 지 또는 흔한 결과인지, 드문 결과인지 판단한다.</p>
<p>어느정도 차이에 따라서 차이가 크고 작다고 말할 것인가를 보면 상위와 하위의 각각 2.5%에 포함되면 차이가 있다고 판단한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b6759037-3681-4600-87e8-aa07b202879d/image.png" />
• 약 5%보다 작은 영역이면 차이가 크다고 할 수 있을 것임
• 대립가설이 맞다고 볼 수 있을 것임
• 이 면적의 의미는 <strong>대립가설이 맞다고 할 때 이 판단이 틀릴 확률</strong></p>
<h3 id="검정-통계량">검정 통계량</h3>
<p>가설을 입증하기 위해 검정통게량을 계산한다. </p>
<ul>
<li>t-통계량</li>
<li>x^2(카이제곱)-통계량</li>
<li>f-통계량</li>
</ul>
<p>p-value의 값이 0.05보다 작으면 대립가설을 받아들인다. 다른 검정 통계량을 계산해 기준인 p-value
에 따라서 받아들일지 판단한다. </p>
<h3 id="유의수준-유의확률">유의수준, 유의확률</h3>
<p>대립가설이 맞다고 받아들일 때, 틀릴 확률과 5%를 비교한다. </p>
<ul>
<li>5%보다 작다면 -&gt; 대립가설을 채택한다.</li>
<li>5%보다 크다면 -&gt; 귀무가설을 채택한다. </li>
</ul>
<p>대립가설이 맞다고 받아들일 때 틀릴 확률이 유의확률, p-value이다. 
유의수준 5%
• 5%: 피셔의 밀크티로 부터 유래
• 1%: 조금 더 보수적인 기준 (예: 의학, 제조 공정 분야)</p>
<h2 id="08-과정-summary">08 과정 summary</h2>
