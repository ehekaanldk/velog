---
title: "[분석형AI]머신러닝"
date: "2025-04-06"
link: "https://velog.io/@ehekaanldk/%EB%B6%84%EC%84%9D%ED%98%95AI%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D"
series: "Uncategorized"
---

<h2 id="01-overview">01. Overview</h2>
<p>머신러닝 개념과 회귀와 분류에 대해서 개념을 학습한다. 
머신러닝 모데링 단계를 이해하고 실제 모델링하는 방법을 학습한다. </p>
<ol>
<li>머신러닝 모델링</li>
<li>모델 성능 평가</li>
<li>알고리즘 이해</li>
<li>모델 성능 튜닝</li>
</ol>
<h2 id="02-머신러닝-모델링">02. 머신러닝 모델링</h2>
<h3 id="021-머신러닝이란">02.1. 머신러닝이란?</h3>
<p>데이터를 가지고와서 탐색과정으로 데이터를 이해하고, 데이터를 전처리해서 완벽한 데이터를 사용해 머신러닝에 학습하도록 하는 것이다. 데이터 설계와 목적 정도는 꼭 필요하다.</p>
<p>모델은 지도학습과 비지도학습으로 구분한다.</p>
<ul>
<li>정답이 있는 데이터에 대한 학습을 지도학습이라 한다.</li>
<li>정답이 없는 데이터에 대학 학습을 비지도학습이라 한다. </li>
</ul>
<p>지도학습을 분류와 회귀로 나눌 수 있다. 
분류 : 0인지 1인지에 대해서 2가지 카테고리로 예측하는 것 (범주형에 대해서 예측)(binary)
회귀 : 측정값으로 카테고리를 예측하는 것 (수치형에 대해서 예측)</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/01ffea04-57cc-45d6-8b10-2cf406ca2959/image.png" />
알고리즘과 평가지표를 분류 문제와 회귀 문제에 맞게 사용해주어야 한다. 
문제의 유형을 정확히 파악하여 알고리즘과 평가 방법을 올바르게 선택해야 한다.</p>
<p>알고리즘
분류 : 로지스틱 회귀, 결정트리, 랜덤포레스트, KNN, XGB
회귀 : 선형 회귀, 결정트리, 랜덤포레스트, KNN, XGB</p>
<p>평가지표
분류 : 정확도, 재현율, 정밀도, 혼동행렬
회귀 : MSE, RMSE, MAE, MAPE, R2-score</p>
<hr />
<h3 id="022-데이터-분리">02.2. 데이터 분리</h3>
<p>데이터를 완벽하게 처리한 후에는 target값을 먼저 분리한다. 
<strong>features를 x라고 정의</strong>하고, <strong>target은 y로 정의</strong>한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/8fe27a3e-c878-4c78-8295-881ca05fd1e5/image.png" /></p>
<p>x와 y를 분리한 데이터에서 학습을 위한 데이터와 평가를 위한 데이터를 나눈다. 일반적으로 학습용과 테스트용은 8:2 비율로 나눈다. 테스트용 데이터의 y(정답)는 절대로 보여주지 않고, 학습의 결과를 y_pred로 저장해 학습이 끝난 후에 <strong>y_test(정답) 과 y_pred(예측)을 비교하여 평가</strong>한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/daf1aa49-c49a-467e-a879-ce91bcd5afde/image.png" /></p>
<pre><code>taret = '컬럼명'
x = data.drop(target, axis=1)
y = data.loc[:, target]</code></pre><p>target를 먼저 정의한 후에 drop()으로 제거된 결과를 반환 받아서 x라는 데이터프레임으로 정의한다. (drop에서 inpalce=True를 하지 않았음으로 원래의 데이터에 분리한 값이 반영되지 않는다.)</p>
<pre><code>x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)</code></pre><p>학습용 데이터의 x, 테스트용 데이터의 x, 학습용 데이터의 y, 테스트용 데이터의 y의 순서를 지켜줘야 한다. </p>
<hr />
<h3 id="023-scikit-learn">02.3. Scikit-learn</h3>
<p>지도/비지도 학습 알고리즘을 제공하는 파이썬 라이브러리이다. 
모델링을 위한 단계</p>
<ol>
<li>불러오기 : 사용할 알고리즘과 평가를 위한 함수를 import</li>
<li>선언하기 : 사용할 알고리즘용 함수로 모델 선언</li>
<li>학습하기 : 모델.fit(x_train, y_train)형태로 모델 학습 시키기</li>
<li>예측하기 : 모델.predict(x_test)형태로 예측한 결과 변수로 저장</li>
<li>평가하기 : 실제값과 예측값을 평가 함수에 전달해 성능 평가</li>
</ol>
<hr />
<blockquote>
<ul>
<li>회귀모델의 성능은 평균과 비교한다.</li>
<li><em>회귀 모델*</em>이 아무것도 못할 때 쓸 수 있는 <strong>가장 단순한 기준</strong>은 <strong>평균값</strong>이다. 
예를 들어 미래의 오존 농도를 이야기할 때, 아무것도 모르겠으면 데이터의 평균으로 예측하면 된다. </li>
</ul>
</blockquote>
<ul>
<li>분류모델의 성능은 최빈값과 비교한다.</li>
<li><em>분류 모델*</em>이 아무것도 못할 때 쓸 수 있는 <strong>가장 단순한 기준</strong>은 <strong>최빈값</strong>이다. 
예를 들어 데이터 중 70%가 고양이이고 30%가 개로 이루어져 있다면, 아무것도 몰라도 고양이라고 예측하면 70%는 맞을 것이다. </li>
<li>결론적으로 모델의 성능이 회귀 모델의 경우 평균보다 낮거나, 분류 모델의 경우 최빈값보다 못하면 아무것도 모르는 것보다 모델이 못하는 것으로 실패한 모델이 된다. </li>
<li>&quot;최소한 이 정도는 맞춰주어야 한다&quot;는 기준선이 되는 것을 <strong>baseline</strong>이라 한다.</li>
<li><strong>머신러닝에서의 baseline은 평균값이거나 최빈값이 된다.</strong> </li>
<li>베이스라인을 넘지 못하는 모델을 다시 설계가 필요하다. </li>
</ul>
<h3 id="실습">실습</h3>
<h4 id="1-환경준비">1. 환경준비</h4>
<p>라이브러리를 불러온다.</p>
<pre><code>import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings(action='ignore')
%config InlineBackend.figure_format = 'retina'</code></pre><p>sklearn을 불러와 버전을 확인한다.</p>
<pre><code># sklearn 버전 확인
import sklearn
print(sklearn.__version__)</code></pre><p>데이터를 읽어온다.</p>
<pre><code>path = '파일경로'
data = pd.rea_csv()</code></pre><h4 id="2-데이터-이해">2. 데이터 이해</h4>
<p>target은 'Ozone'으로 정의한다 .</p>
<ul>
<li>head()</li>
<li>tail()</li>
<li>info() : 열에 대한 정보</li>
<li>describe() : 기술 통계량</li>
<li>corr() : 상관관계(문자형 변수가 있으면 오류발생, numeric_only=True)
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/f6a719c7-680d-4c73-90c7-fefe2029e713/image.png" />
다음 이미지를 보면 모두 153데이터이지만 146으로 결측치가 있는 것을 알 수 있다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c2108acb-595d-48d1-9e4a-f38f0e08e778/image.png" /> <img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7408f1cf-c3c3-437a-a267-4f2c1e05a83e/image.png" />
간략한 heatmap과 scatter plot을 그려서 target과 큰 상관관계를 가지는 컬럼과 해당 컬럼과 taregt으로 산점도를 확인한다. 산점도에서는 최적의 직선을 찾는 것이 목표이다. 이상치가 있다면 어떻게 처리할지 고민해야 한다. </p>
<h4 id="3-데이터-준비">3. 데이터 준비</h4>
<p><strong>1)결측치 처리</strong>
데이터 결측치를 확인한다. 
<code>isnull().sum()</code></p>
<p>결측치를 처리한다. 
<code>ffill(inplace=True)</code></p>
<hr />
<p><strong>2) 변수제거</strong>
분석에 의미가 없다고 판단되는 필요없는 변수는 제거한다. </p>
<pre><code>drop_cols = ['Month', 'Day']
data.drop(columns=drop_cols, inplace=True)</code></pre><hr />
<p><strong>3) x, y 분리</strong>
우선 target 변수를 명확히 지정한다.
target을 제외한 나머지 변수들 데이터는 x로 선언한다.
target 변수 데이터는 y로 선언한다.</p>
<pre><code># target 확인
target = 'Ozone'

# 데이터 분리
x = data.drop(target, axis=1) # axis=1은 컬럼
y = data.loc[:, target] # y = data['target'] 가능</code></pre><hr />
<p><strong>4) 학습용, 평가용 데이터 분리</strong>
학습용, 평가용 데이터를 분리한다.</p>
<pre><code># 모듈 불러오기
from sklearn.model_selection import train_test_split

# 7:3으로 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)</code></pre><p>4개의 요소로 구성된 튜플로 제공하기 때문에 순서 주의!
렌덤하게 split하기 때문에 반복 실행 시 같은 결과를 얻기위해 random_state 지정한다.</p>
<h4 id="4-모델링">4. 모델링</h4>
<ul>
<li>본격적으로 모델을 선언하고 학습하고 평가하는 과정을 진행한다.</li>
<li>우선 회귀 문제인지 분류 문제인지 명확히 구분한다.</li>
<li><em>모델링*</em></li>
<li>알고리즘: LinearRegression</li>
<li>평가방법: mean_absolute_error</li>
</ul>
<p><strong>1) 불러오기</strong></p>
<pre><code># 1단계: 불러오기
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error</code></pre><p><strong>2) 선언하기</strong></p>
<pre><code># 2단계: 선언하기
model = LinearRegression()</code></pre><p><strong>3) 학습하기</strong></p>
<pre><code># 3단계: 학습하기
model.fit(x_train, y_train)</code></pre><p><strong>4) 예측하기</strong></p>
<pre><code># 4단계: 예측하기
y_pred=model.predict(x_test)</code></pre><p><strong>5) 평가하기</strong></p>
<pre><code># 5단계: 평가하기
print('mean:', mean_absolute_error(y_test, y_pred)) # 순서 주의 (정답, 예측)</code></pre><p>평가하기 단계에서 (정답,예측) 순으로 값을 넣어야 한다.</p>
<hr />
<p><strong>예측값과 실제값 비교</strong></p>
<pre><code># 예측값, 실젯값 확인
print(y_pred[:10])
print(y_test.values[:10])</code></pre><p> y_pred는 배열의 형태이고, y_test는 시리즈의 형태이다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/1275092e-60d2-45cf-b96b-5aeb505a00a4/image.png" /></p>
<pre><code># 예측값, 실젯값 시각화 비교
plt.plot(y_pred, label='predicted')
plt.plot(y_test.values, label='Actual')
plt.axhline(y_train.mean(), color='r') # 학습데이터의 평균
plt.legend()
plt.show()</code></pre><p>시각화를 통해서 예측값(y_pred)과 실제값(y_test)를 비교한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d2d279d4-fa97-4829-8004-f1131058c54e/image.png" /></p>
<h2 id="03-모델-성능-평가">03. 모델 성능 평가</h2>
<p>회귀 모델과 분류 모델의 성능 평가 방법과 평가 지표가 다르다. </p>
<p><strong>회귀모델 평가</strong>
예측값과 실제값이 가까울수록 좋다. 
예측값과 실제값 사이의 오차가 존재한다.
회귀 모델은 평균(baseline)보다 오차를 줄이는 것이 목표이다.
<strong>예측한 값과 실제 값의 오차</strong>로 모델 성능을 평가한다.</p>
<p><strong>분류모델 평가</strong>
오차가 아닌 맞춘 개수를 따진다.
분류 모델은 예측값이 실제값과 많이 같도록 하는 것이 목표이다.
<strong>정확히 예측한 비율</strong>로 모델 성능을 평가한다.</p>
<hr />
<p>실제값 : $$y$$ 또는 $$y_i$$
예측값 : $$\hat{y}$$ 또는 $$\hat{y}_i$$
오차 : $$e_i = y_i - \hat{y}_i$$
평균 : $$\bar{y}$$</p>
<hr />
<h2 id="회귀모델">회귀모델</h2>
<h3 id="031-오차-제곱의-합">03.1. 오차 제곱의 합</h3>
<p>데이터가 매우 많이 때문에 오차들에 대해서 하나의 숫자로 말해야한다. 학습한 데이터들의 대해서 오차들의 평균으로 이를 구해서 모델의 성능을 평가한다. 
<strong>전체 데이터에 대해 평균적으로 얼마나 오차를 가지고 있는지를 보여주는 지표</strong></p>
<ul>
<li>음수와 양수를 상쇄하기 위해서 제곱을 해서 더하고 평균을 구한다. Mean Squared Error</li>
<li>음수와 양수를 상쇄하기 위해서 제곱을 해서 더하고 루트를 씌운다. Root Mean Squared Error</li>
</ul>
<blockquote>
<p>오차 제곱의 합 : SSE
오차 제곱의 평균 : MSE (SSE/n)
오차 제곱 평균에 루트 : RMSE (root MSE)</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b1db9cdc-7835-4c5f-8ebd-0da26b4509dd/image.png" />
MSE를 가장 많이 사용하고, 오차제곱합의 평균으로 생각한다. </p>
<h3 id="032-오차-절대값의-합">03.2. 오차 절대값의 합</h3>
<ul>
<li>실제값과 모델의 예측값의 오차에 절대값을 씌우고 합의 평균을 구한다. Mean Absolute Error</li>
<li>실제값과 모델의 예측값의 오차의 비율에 절대값을 씌우고 합의 평균을 구한다. Mean Absolute Percentage Error</li>
</ul>
<blockquote>
<p>A오차 절대값의 합의 평균 : MAE
오차 비율 절대값의 합의 평균 : MAPE</p>
</blockquote>
<p>MSE, RMSE, MAE는 모두 에러값을 나타내는 것으로 작을수록 좋다.
클수록 좋은 값은 결정 계수 R^2(R-Squared)이다.</p>
<h3 id="033-결정-계수-r2r-squared">03.3. 결정 계수 R^2(R-Squared)</h3>
<p>실제값이 평균보다 가까워야 한다. 회귀 모델이 아무리 못해도 평균보다는 잘해야한다.
주어진 전체 오차의 범위는 (실제값과 평균값의 오차제곱의 합)이다. 평균값인 이유는 우리의 자존심..!
실제값과 평균값의 오차제곱의 합이 SST이다.</p>
<p>SSE : 모델이 예측 못한 오차 (실제값 vs 예측값)
SST : 전체 데이터의 오차 (실제값 vs 평균)
SSR : 모델이 설명한 부분 (예측값 vs 평균)
SSR = SSE + SST</p>
<p>R2-score는 전체 데이터의 오차에서 모델이 설명한 부분의 비율을 의미한다. </p>
<hr />
<p><strong>정리</strong>
SSE는 총 오차의 덩어리
MSE는 평균 제곱 오차
RMSE는 단위를 살려서 얼마만큼 틀렸는지 말해주는 지표
MAE는 예측과 실제 사이의 직접 거리를 보는 지표
MAPE는 실제값 대비 몇 퍼센트나 틀렸는지를 알려주는 지표</p>
<hr />
<p>$$\large MSE=\frac{1}{n}\sum_{i=1}^{n}(y_{i}-\hat{y}<em>{i})^2$$
$$\large RMSE=\sqrt{\frac{1}{n}\sum</em>{i=1}^{n}(y_{i}-\hat{y}<em>{i})^2}$$
$$\large MAE=\frac{1}{n}\sum</em>{i=1}^{n}|y_{i}-\hat{y}<em>{i}|$$
$$\large MAPE=\frac{1}{n}\sum</em>{i=1}^{n}\left |\frac{y_{i}-\hat{y}<em>{i}}{y</em>{i}}\right |$$
$$\large R^2=1-\frac{SSE}{SST}=1-\frac{\sum_{i=1}^{n}(y_{i}-\hat{y}<em>{i})^2}{\sum</em>{i=1}^{n}(y_{i}-\bar{y}_{i})^2}$$</p>
<hr />
<h2 id="분류-모델">분류 모델</h2>
<h3 id="034-혼동행렬과-평가지표">03.4. 혼동행렬과 평가지표</h3>
<p>정확도 : 1과 0을 정확히 예측한 비율
정밀도 precision : 예측의 관점에서 실제로 맞은 비율
재현율 recall : 실제의 관점에서 실제로 맞은 비율</p>
<p>재현율은 실제에 대해서 예측함으로 민감하기 때문에 민감도라고도 부른다. 민감도가 낮으면 죽을 수 있다..! 
비가 온다는 실제에 대해서 예측도 비가 온다고 하는 경우 =&gt; 민감도가 높다.
코로나 확진이라는 실제에 대해서 예측을 코로나 확진으로 못하는 경우 =&gt; 민감도가 낮다.</p>
<p>정밀도은 예측에 대해서 실제를 확인하기 때문에 맞지 않을 경우 조금은 짜증날 수 있다..ㅋㅋ
암이라는 예측에 대해서 실제 암이 아닌 경우 -&gt; 정밀도가 낮다.
비가 온다는 예측에 대해서 실제 비가 오는 경우 -&gt; 정밀도가 높다.</p>
<p>• TN(True Negative, 진음성): 음성으로 잘 예측한 것(음성을 음성이라고 예측한 것)
• FP(False Positive, 위양성): 양성으로 잘 못 예측한 것(음성을 양성이라고 예측한 것)
• FN(False Negative, 위음성): 음성으로 잘 못 예측한 것(양성을 음성이라고 예측한 것)
• TP(True Positive, 진양성): 양성으로 잘 예측한 것(양성을 양성이라고 예측한 것)
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a7227ad4-5ccd-4f87-95ee-60a98b7c5c81/image.png" /></p>
<p><strong>F1-score</strong>
정밀도와 재현율의 조화평균을 의미한다.
precision 과 recall을 모두 보고 싶을 경우에 사용한다. 
조화평균은 두 값의 평균에서 작은 값에 조금 치우치는 결과를 보인다.</p>
<p>정밀도와 재현율은 반대의 개념이다. 
정밀도를 높이는 것은 예측의 관점에서 실제 맞는 경우를 높이는 것이다. 
재현율을 높이는 것은 되도록이면 실제 관점에서 맞는 예측을 높이는 것이다. </p>
<p>정밀도를 높인다. Precision 100%
의사가 오진을 할까봐 염려가 된다. 누가봐도 암환자일 것 같은 사람에게만 암이라고 진단(예측)한다. 소극적으로 진단해서 정밀도가 100%로 만든다. 실제로 암인 사람을 암이라고 예측하는 확률이 떨어진다. =&gt; 재현율이 낮아진다. Recall 하락</p>
<p>재현율을 높인다. Recall 100%
보이스 피싱에 대해서 조금이라도 문제가 있으면 보이스 피싱으로 예측한다. 적극적으로 판단해서 재현율을 100%로 만든다. 예측을 보이스 피싱이라고 한 경우에서 실제 보이스 피싱인 경우의 확률이 떨어진다.
=&gt; 정밀도가 낮아진다. Precision 하락</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/81684702-0c60-4ec0-b9cc-a0e09722e9c3/image.png" /></p>
<hr />
<h3 id="실습-회귀">실습 (회귀)</h3>
<p><strong>1) MAE(Mean Absolute Error)</strong></p>
<pre><code># 모듈 불러오기
from sklearn.metrics import mean_absolute_error
# 성능 평가
mean_absolute_error(y_test, y_pred)</code></pre><p><strong>2) MSE(Mean Squared Error)</strong></p>
<pre><code># 모듈 불러오기
from sklearn.metrics import mean_squared_error

# 성능 평가
mean_squared_error(y_test, y_pred)</code></pre><p><strong>3) RMSE(Root Mean Squared Error)</strong></p>
<pre><code># 모듈 불러오기
from sklearn.metrics import root_mean_squared_error

# 성능 평가
root_mean_squared_error(y_test,y_pred)</code></pre><p><strong>4) MAPE(Mean Absolute Percentage Error)</strong></p>
<pre><code># 모듈 불러오기
from sklearn.metrics import mean_absolute_percentage_error

# 성능 평가
mean_absolute_percentage_error(y_test,y_pred)</code></pre><p><strong>5) R2-score</strong></p>
<pre><code># 모듈 불러오기
from sklearn.metrics import r2_score

# 성능 평가
r2_score(y_test, y_pred)</code></pre><p>r-score의 또다른 방법이다. 회귀모델일 경우</p>
<pre><code>model.score(x_test, y_test)</code></pre><h3 id="실습-분류">실습 (분류)</h3>
<p><strong>1) Confusion Matrix</strong></p>
<pre><code># 모듈 불러오기
from sklearn.metrics import confusion_matrix

# 성능 평가
print(confusion_matrix(y_test, y_pred))</code></pre><p><strong>2) Accuracy</strong></p>
<pre><code># 모듈 불러오기
from sklearn.metrics import accuracy_score

# 성능 평가
accuracy_score(y_test, y_pred)</code></pre><p><strong>3) Precision</strong></p>
<pre><code># 모듈 불러오기
from sklearn.metrics import precision_score

# 성능 평가
precision_score(y_test, y_pred, average=None)</code></pre><p><strong>4) Recall</strong></p>
<pre><code># 모듈 불러오기
from sklearn.metrics import recall_score
# 성능 평가
recall_score(y_test, y_pred, average=None)</code></pre><p><strong>5) F1-Score</strong></p>
<pre><code># 모듈 불러오기
from sklearn.metrics import f1_score

# 성능 평가
f1_score(y_test, y_pred, average=None)</code></pre><p><strong>6) Classification Report</strong></p>
<pre><code># 모듈 불러오기
from sklearn.metrics import classification_report

# 성능 평가
print(classification_report(y_test, y_pred))</code></pre><p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/63f17b67-61c7-4fad-8c8d-79369355f4c7/image.png" />
1이라고 예측했는데 실제 1인 확률은 0.90으로 확인한다.
binary분류에서는 모두 1에 대한 지표만 보여준다. classification report를 사용하면 1과 0에 대해서 모두 확인할 수 있다. 
또는 average=None 매개변수를 사용하면 1과 0을 모두 확인할 수 있다. </p>
<p>랜덤하게 발생하는 이유</p>
<ul>
<li>split단계에서 random_state=1로 설정했지만 decisionTreeClassifier에서 자체적으로 랜덤한 작업을 하기 때문에 random_state=1</li>
</ul>
<hr />
<h3 id="035-중간정리">03.5. 중간정리</h3>
<p>회귀 모델의 평가지표
MSE : 오차 제곱의 평균
RMSE : (오차 제곱의 평균)에 루트
MAE : 오차 절대값의 평균
MAPE : 오차 비율 절대값의 평균
R2-score : 1 - (오차제곱의 합/전체 오차 평균) : 모델이 데이터를 얼마나 잘 설명했는지를 나타내는 비율</p>
<p>분류 모델의 평가지표
Accuarcy : 정확히 예측한 비율
Precision : 예측 관점에서 정확히 예측한 비율
Recall : 실제 관점에서 정확히 예측한 비율
F1-score : precision과 recall의 조화평균</p>
<hr />
<h2 id="04-알고리즘-이해">04. 알고리즘 이해</h2>
<p>Linear regression 알고리즘
knn 알고리즘
decistion tree 알고리즘
random forest 알고리즘</p>
<h3 id="1선형회귀-linear-regression">1)선형회귀, Linear regression</h3>
<p>최선의 직선인 y=ax+b를 그린다. 기울기 a와 절편 b를 결정해야 한다.
기울기와 절편을 알면 최선의 직선을 알 수 있다. 
기울기는 가중치, 절편은 편향으로 부른다.
가장 최선의 직선은 실제 데이터값과의 오차가 적은 선으로 선택한다. 
MSE값이 최소가 되는 모델이 최선의 회귀모델이다. </p>
<p><strong>단순 회귀</strong>
독립변수 하나가 종속변수에 영향을 미치는 선형 회귀를 단순회귀라 한다. x값 하나만 y값을 설명하는 경우이다 .
회귀식 : y^ = w_0 + w_1 * x_1
최선의 가중치 w1과 편향 w0을 구한다.</p>
<p><strong>다중 회귀</strong>
여러 독립 변수가 종속변수에 영향을 미치는 선형 회귀를 다중회귀라고 한다. y값을 설명하기 위해서는 여러 개의 x값이 필요한 경우이다. 
회귀식 : y^ = w_0 + w_1<em>x_1 + w_2</em>x_2 + ... +w_n*x_n
최선의 가중치 w1, w2, w3, w4 ... 와 편향 w0을 구한다.</p>
<hr />
<h3 id="2-knn-알고리즘">2) KNN 알고리즘</h3>
<p>최근접 이웃이라는 의미로 근묵자흑 : 주변에 좋지 않은 사람들이 있으면 어두워진다는 의미와 같이, 가장 근접한 데이터을 기반으로 예측을 한다. 가장 근접한 K개의 데이터를 찾아 그 값들로 새로운 값을 예측하는 알고리즘이다.
인접한 데이터를 믿지 못하고 멀리 있는 데이터를 반영할 경우에는 모델이 단순해진다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/892c64f3-8e35-4f2e-b6c9-800fa020b465/image.png" />
회귀와 분류에서 사용되는 지도학습 알고리즘이다. </p>
<p><strong>k값의 중요성</strong></p>
<ul>
<li>회귀에서 사용 가능한 것은 이웃한 데이터들의 평균을 구한다.(인접한 데이터를 믿지 못하고 많이 반영하면 전체의 평균이 된다.)</li>
<li>분류에서 사용 가능한 것은 이웃한 데이터의 다수결로 구한다.(인접한 데이터를 믿지 못하고 많이 반영하면 전체의 최빈값이 된다.)
=&gt; K가 커질수록 모델이 단순해진다. k를 데이터 개수만큼 사용하게 되는 경우이다. 가장 복잡한 모델은  k가 1인 경우이다.</li>
<li>일반적으로 k를 1로 설정하지 않는다.</li>
<li>K는 홀수로 설정해 짝수인 경우 과반수 이상의 이웃이 나오지 않도록 한다.</li>
</ul>
<p>모델이 복잡하다는 것은 과적합으로 학습성능은 좋지만 실제 적용하면 좋은 결과가 나오지 않는 경우</p>
<p>적절한 k값을 구하는 것이 중요하다. k의 기본값은 5이다. k 값에 따라서 분류의 값이 달라진다. 자동으로 최적의 k를 구하는 알고리즘이 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c81389a8-455d-4b14-a368-7809e35a371a/image.png" /></p>
<p>그래프에서 확인할 때 변수의 값의 범위가 달라 오판하는 경우가 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/8ad5e5ab-9a9b-4653-92eb-520b99eef1dc/image.png" /></p>
<ul>
<li>k값을 적당하게 조절한다 </li>
</ul>
<hr />
<h3 id="scaling-전처리-작업">+Scaling (전처리 작업)</h3>
<p>Scale을 조절하여 변수마다 다른 범위를 가지는 것을 통일화한다.</p>
<ul>
<li>scaling 의 방법은 정규화와 표준화가 있다. </li>
<li>평가용 데이터도 학습용 데이터를 기준으로 동일하게 스케일링을 수행한다.</li>
</ul>
<p><strong>정규화 (normaliztion)</strong>
(값에서 최소값을 뺸 값)을 (최대값에서 최소값을 뺀 값)으로 나누면 각 변수의 값이 0과 1 사이의 값으로 만든다. <strong>거리가 나오는 데이터</strong>는 정규화 작업이 필요하다.</p>
<p><strong>표준화 (standardization)</strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ec626bc3-4b8c-4d77-a909-37718dd2d581/image.png" /></p>
<h3 id="3-decision-tree">3) Decision Tree</h3>
<p>특정 변수에 대한 의사결정 규칙을 나무 가지가 뻗는 형태로 분류해 나간다. 처음 시작하는 질문이 중요하다. 스케일링과 같은 전처리의 영향도가 크지 않다. </p>
<ul>
<li><p>분석과정을 실제 눈으로 확인이 가능하다. =&gt; 화이트박스 모델</p>
</li>
<li><p>knn은 k의 값이 작아지면 복잡해서 과적합이 발생한다.</p>
</li>
<li><p>트리의 깊이가 깊어지면 복잡해서 과적합이 발생한다. </p>
</li>
</ul>
<blockquote>
<p>의사결절트리에서의 튜닝은 트리의 깊이를 제한하는 방법(가지치기)이다. </p>
</blockquote>
<p>root node : 전체 자료를 갖는 시작하는 마디
depth (깊이) : 뿌리 마디로부터 끝 마디까지 연결된 마디의 개수</p>
<p><strong>지니 불순도</strong>
어떻게 가지를 뻣어나가는가? 에 대해서는 지니 불순도를 사용한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/db2e2ae7-ac6d-4a48-b163-1838ccba1543/image.png" />
분류 후에 얼마나 잘 분류했느지 평가하는 지표이다. 
불순도를 낮아지도록 하는 방향으로 질문을 한다. 
지니 불순도가 낮은 속성으로 의사결정 트리 노드를 결정한다. </p>
<p><strong>가지치기</strong>
가지치기를 하지 않으면 모델이 학습 데이터에 매우 잘 맞지만, 실제 평가 데이터에는 잘 맞지 않아 과적합이 발생한다. 일반화되지 못한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c130522d-e19b-4d6a-bb8e-e420376cc616/image.png" /></p>
<ul>
<li>max_depth 등의 하이퍼파라미터 값을 조정해 가지치기를 할 수 있다.</li>
<li>학습 데이터에 대한 성능은 낮아지지만, 평가 데이터에 대한 성능을 높일 수 있다. </li>
<li><strong>과적합</strong>이 발생하지 않도록 하고, <strong>모델의 일반화 성능</strong>을 향상시킨다. </li>
<li>회귀모델이라면 가중치를 줄인다.</li>
<li>분류모델이라면 과도한 분류 규칙을 줄인다.</li>
</ul>
<h3 id="4-random-forest">4) Random Forest</h3>
<p>랜덤포레스트는 의사결정나무가 여러개 있는 것이다. 대략 100개...???? 에 대해서 집계한다. 
랜덤포레스트는 부트스트래핑으로 각각의 데이터 셋으로 트리들 독립적 학습하여 예측 결과를 하나로 모아 예측을 수행하는 앙상블 모델이다. </p>
<p>가지치기로 튜닝한다.
배깅의 가장 대표적인 알고리즘이다. 
배깅은 bagging = bootstrap sample + aggregating
bootstrap은 랜덤하게 샘플데이터를 꺼내서 복원추출하여 데이터 샘플링
aggregating은 여러 개의 모델의 예측 결과를 하나로 모으는 것</p>
<p>랜덤하게 10개를 고른다.
랜덤포레스트는 랜덤하게 샘플링된 데이터에서 랜덤하게 선택된 변수로 서로다른 트리가 만들어지고 
앙상블은 약한 모델이지만 약한 모델을 여러개 사용하면 효과가 크다.</p>
<ul>
<li>n_estimators : 랜덤포레스트에서 랜덤하게 샘플링된 데이터로부터 트리의 개수는 기본적으로 100개 존재한다. </li>
<li>max_depth : 트리의 최대 깊이를 의미한다.(가지치기)</li>
</ul>
<h3 id="중간정리">중간정리</h3>
<p>linear regression은 회귀에서만 가능하다. 
knn은 회귀와 분류에서 모두 가능한다. 
의사 결정 트리는 분류와 회귀에서 모두 가능하다.</p>
<p>과적합 = 모델이 복잡하다
선형 회귀
최근접 이웃
의사결정 트리
랜덤 포레스트</p>
<hr />
<h3 id="실습6">실습6</h3>
<p>분류문제를 decision tree로 모델링한다. 
target은 'CHURN' 컬럼을 확인한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/4af46ac1-1f96-4c39-be8c-6b40cc3637ce/image.png" />
<strong>1) 의미없는 변수 제거</strong>
<strong>2) x, y 분리</strong>
<strong>3) 가변수화</strong>
데이터에 문자형이 있을 때 fit()을 하면 오류가 발생한다. 문자형을 숫자로 바꾸어야 한다. 
문자열 변수에 대해서</p>
<ul>
<li>one-hoting encoding한다.  get_dummies() 함수를 사용한다.</li>
<li>앞의 열 하나를 제거한다. <pre><code># 가변수화 대상: 'REPORTED_SATISFACTION, REPORTED_USAGE_LEVEL, CONSIDERING_CHANGE_OF_PLAN
dumm_cols = ['REPORTED_SATISFACTION','REPORTED_USAGE_LEVEL','CONSIDERING_CHANGE_OF_PLAN']
</code></pre></li>
</ul>
<h1 id="가변수화">가변수화</h1>
<p>x = pd.get_dummies(x, columns=dumm_cols, drop_first=True, dtype=int)</p>
<h1 id="확인">확인</h1>
<p>x.head()</p>
<pre><code>결과에서 데이터값에 문자가 없는지 반드시 확인해야 한다.
target 변수가 문자인 것은 보통 자동으로 처리해준다. 만약 안되는 것에 대해서는 라벨링을 적용한다. 타겟변수가 문자열인 것은 허용해준다고 생각한다. 
**4) 학습용, 평가용 데이터 분리**
**5) 모델링**
가지치기를 하지 않은 경우의 결과를 확인한다. 
![](https://velog.velcdn.com/images/ehekaanldk/post/a7426bcd-11c0-4333-bab2-345147bf79ba/image.png)

가지치기를 적용하면 예측을 더 잘한다. </code></pre><h1 id="2단계-선언하기">2단계: 선언하기</h1>
<p>model = DecisionTreeClassifier(max_depth=5, random_state=1)</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/cf1c41db-1d5a-4ecd-a60b-1aa782af375f/image.png)


#### 변수 중요도 시각화 
classification_report 는 feature_importances_ 으로 변수 중요도를 시각화할 수 있다. </code></pre><h1 id="변수-중요도-시각화">변수 중요도 시각화</h1>
<p>model.feature_importances_</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/31db0289-8451-4729-8003-37a8db45cdbb/image.png)

컬럼명만 가져올 수 있다. </code></pre><p>list(x)</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/7375ec9d-c354-4aa3-af14-d99f3a204716/image.png)

**변수 중요도를 시각화한다. **</code></pre><p>plt.figure(figsize=(4,5))
plt.barh(list(x), model.feature_importances_)</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/35c36a47-8af7-4a9f-9a5f-3ca143d2b471/image.png)
가지치기로 인해서 변수들이 사용되지 않아 시각화 그래프에서 값이 없는 것을 확인할 수 있다. 불순도를 제일 많이 줄이는 역할을 했다. 

사용한 decision tree 입장에서는 'OVERAGE' 컬럼인 것이다. 해당 컬럼이 처음 나무가지를 가르는 기준이 되었을 것이다. 다른 모델을 사용한 경우에는 다른 컬럼이 중요하다고 할 수 있다. 



&gt;트리 기반의 모델에서는 변수 중요도를 보는 것이 좋다!
linear regression을 사용한 경우에는 회귀계수를 보는 것이 좋다!

## 05. 모델 성능 튜닝
knn에서 k를 찾는방법과 decision tree나 random forest의 max_depth를 찾는 방법이 모델 성능 튜닝이다. 학습 데이터에 대해서 좋은 성능을 보여주는 튜닝이다.
최선의 파라미터를 찾아서 그것으로 학습을 하는 것이다. 

### 05.1. 하이퍼파라미터튜닝
KNN알고리즘의 n_neighbors, Decision Tree모델의 max_depth가 하이퍼파라미터가 된다.
k 값이 가장 클 때(=전체 데이터 개수) 가장 단순 모델
→ 평균, 최빈값
• k 값이 작을 수록 복잡한 모델이 됨

max_depth값이 작을 수록 트리 깊이가 제한되어 모델이 단순해 짐


---

**📦 파라미터 vs 하이퍼파라미터 비교**

|구분|    파라미터 (parameters)|    하이퍼파라미터 (hyperparameters)|
|--| --|--|
|정의|    모델이 학습으로 직접 얻는 값|    사람이 학습 전에 설정하는 값|
|조정 방식|    경사하강법 등으로 자동 조정됨    |그리드서치, 랜덤서치 등으로 수동 또는 자동 튜닝|
|예시|    선형 회귀의 w, b / 신경망의 가중치    |max_depth, n_neighbors, C, learning_rate, batch_size 등|


---


### 05.2. Grid search
가능한 모든 하이퍼파라미터 조합을 전부 실험하는 방식이다. 
하이퍼파라미터의 범위를 딕셔너리로 모두 선언해서 최적의 결과를 찾는 것이다. 
![](https://velog.velcdn.com/images/ehekaanldk/post/e73abfbf-c3a4-44eb-b4a9-e23f0ae801e7/image.png)
</code></pre><p>param_grid = {'max_depth': range(1, 51)}  # 1~50 전부</p>
<pre><code>max_depth을 1부터 50까지 50개의 값을 전부 계산해서 가장 성능 좋은 max_depth를 찾는 방식이다.


**Cross Validation**
모델의 성능을 더 정확하게 평가하기 위해 데이터를 여러 조각으로 나누어 여러번 학습 &amp; 검증하는 방법이다. 
 X_train(전체 데이터의 70%)을 가지고 cv=5로 교차 검증을 진행한다. 

 X_train = [fold1, fold2, fold3, fold4, fold5] 로 5등분 한다고 하면 

|반복 횟수|    학습 데이터|    검증 데이터|
| --- | :--- | :---: |
|1회차|    fold2 + fold3 + fold4 + fold5|    fold1|
|2회차|    fold1 + fold3 + fold4 + fold5|    fold2|
|3회차|    fold1 + fold2 + fold4 + fold5|    fold3|
|4회차|    fold1 + fold2 + fold3 + fold5|    fold4|
|5회차|    fold1 + fold2 + fold3 + fold4|    fold5|

각 반복마다 나오는 점수들을 평균 내서 최종 점수로 사용한다. **파라미터 조합 수 × cv 값 = 실제 모델 훈련 횟수**가 된다. 

### 05.3. Random search
전체 조합 중 이부를 무작위 추출해서 실험하는 방식이다. 
파리미터의 범위(짧게 잡아서)를 랜덤하게 선택해서 최적의 결과를 찾는 것이다. 
랜덤하게 지정한 것들만 골라서 최적의 결과를 

![](https://velog.velcdn.com/images/ehekaanldk/post/e73abfbf-c3a4-44eb-b4a9-e23f0ae801e7/image.png)

어떤 파라미터의 범위가 어디부터 어디까지인지 정한다. 
</code></pre><p>param_dist = {'max_depth': randint(1, 51)}  # 1~50 사이 무작위 정수</p>
<pre><code></code></pre><p>RandomizedSearchCV(
    estimator=모델,
    param_distributions=param_dist,
    n_iter=10,  # 무작위로 10번만 실험!
    ...
)</p>
<pre><code>max_depth을 1부터 50까지 사이에서 무작위로 10개(n_iter=10)만 골라서 계산한다. 무작위 10개 중에서 가장 성능 좋은 max_depth를 찾는 방식이다.

cv 값에 따라서 random search에서는 조합 수 대신 **n_iter x cv(교차검증 수) = 총 훈련 횟수** 가 된다. 

### 실습

파라미터의 범위를 딕셔너리로 선언한다. </code></pre><h1 id="파라미터-선언">파라미터 선언</h1>
<h1 id="max_depth-150">max_depth: 1~50</h1>
<p>param = {'max_depth' : range(1, 51)} # 어떤 파라미터의 범위가 어디부터 어디까지인지 정한다. </p>
<pre><code>cross validation은 하나의 파라미터에 대해서 5번 돌려서 평균을 구한다. 
random search이면 그중에 몇개만 골라라...
grid search는 모두 다 한다..

학습데이터에 대한 결과임으로 실제 평가 데이터에 대해서도 좋을 거라고 믿는거다.. 실제로 좋을지는 모름

실제 실무에서는 머신러닝을 많이 사용한다. 
어떤 변수를 제거하고 데이터를 사용하는지가 중요하다. 

## 06. 과정 Summary
</code></pre>
