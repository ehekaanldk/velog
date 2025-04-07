---
title: "[분석형AI] 딥러닝_회귀모델링"
date: "2025-04-06"
link: "https://velog.io/@ehekaanldk/%EB%B6%84%EC%84%9D%ED%98%95AI-%EB%94%A5%EB%9F%AC%EB%8B%9D"
series: "Uncategorized"
---

<h2 id="01-overview">01. Overview</h2>
<p>딥러닝 기초를 잘 이해하면서 회귀, 분류 모델링을 수행하고, 모델 성능을 평가하고 최적화할 수 있다.</p>
<h3 id="011-crisp-dm">01.1. CRISP-DM</h3>
<p>Cross-Industry Standard Process for Data Mining</p>
<p>인공지능 방법론</p>
<blockquote>
<p>AI와 데이터를 기반으로 한 비즈니스 문제 해결 방법론/ 혹은 절차이다. </p>
</blockquote>
<p>면접에서 회사마다 해결해야 하는 비즈니스 모델이 많다
문제를 찾아 비즈니스 문제해결사가 되기를..</p>
<p>무엇이 문제인가?</p>
<p>문제가 해결되었는가?</p>
<h3 id="012-모델과-모델링">01.2. 모델과 모델링</h3>
<p>머신러닝은 데이터를 분석해서 패턴을 학습하는 알고리즘이다. 머신러닝은 사람이 feature 즉, 특징을 만들어주어야 하지만, 특징을 스스로 찾아내는 딥러닝에 대해서 배워본다. </p>
<p>신경망 구조를 통해 복잡한 패턴을 스스로 학습하는 방법이 딥러닝이다. 
딥러닝은 특징을 스스로 자동추출한다. </p>
<p><strong>데이터 안에는 패턴이 담겨 있으며</strong> 패턴이 전혀 없는 데이터를 노이즈라고 한다. </p>
<ul>
<li>데이터 분석 : 데이터를 일일히 보고 패턴을 찾는 과정</li>
<li>모델 : 데이터로부터 패턴을 찾아 수학식으로 정리해 놓은 것</li>
<li>모델링 : 가능한한 오차가 적은 모델을 만드는 과정</li>
</ul>
<p><strong>머신러닝</strong>
규칙에 영향을 주는 중요한 파라미터를 알고리즘에게 찾아봐!
사람이 데이터를 분석하고 전처리해서 모델이 학습할 수 있는 형태로 특징을 뽑아주어야 한다. 
머신러닝에서는 패턴을 찾는 과정을 사람이 도와주는 것이다. </p>
<p><strong>딥러닝</strong>
규칙에 영향을 주는 중요한 파라미터를 인공신경망(다층 신경망)에게 찾아봐!
데이터를 넣기만 하면, 특징을 뽑고 분석하는 과정까지도 모델이 스스로 한다.
데이터 분석부터 예측까지 모든 걸 자동으로 해주는 시스템이다. </p>
<p>*<em>특징을 찾는 과정을 머신러닝은 사람이 직접 설계한다. 딥러닝은 특징을 스스로 자동으로 추출한다. *</em></p>
<p>모델의 목적 : 샘플을 가지고 전체를 추정
샘플 : 표본, 부분집합
전체 : 모집단, 전체집합
추정 : 예측, 추론</p>
<p> <strong>모델의 성능 평가</strong>
 모델의 성능은 오차(error)를 통해 계산됩니다.</p>
<ul>
<li>모델링 : train error를 최소화 하는 모델을 생성하는 과정</li>
<li>모델 튜닝 : validation error를 최소화 하는 모델 선정</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/3a3074ff-0163-4517-a529-94638a02eebb/image.png" /></p>
<p>머신러닝에서는 새로운 feature를 추출하는 피쳐 엔지니어링 과정이 =&gt; 모델의 성능에 큰 영향을 준다.</p>
<p>과거의 데이터를 가지고 미래의 데이터를 예측하는 것이다. 과거는 일부의 데이터이고 일부 데이터를 사용해서 만든 결과물과 전체는 차이가 발생한다. 이것이 바로 오차이다!</p>
<blockquote>
<p>텐서는 자료형 중에 하나!
값이 하나인 스칼라도 텐서라고도 부르고
백터도 1-way 텐서라고도 부른다.</p>
</blockquote>
<h3 id="numpy">+numpy</h3>
<p>list는 파이썬의 기본 리스트이다. (숫자, 문자 섞어도 가능)
<strong>ndarray</strong>는 numpy의 배열로 <strong>데이터 타입이 모두 같아야 한다.</strong> (백터 수학 연산에 최적화)
Series는 pandas의 인덱스를 가질 수 있는 1차원 배열이다.
DataFrame은 pandas의 행과 열 모두 인덱스를 가질 수 있는 2차원 배열이다. </p>
<p>ndarray.shape : ndarray의 차원과 크기를 튜플 형태로 나태난다.</p>
<h3 id="tensor">Tensor</h3>
<p>딥러닝에서는 <strong>Pandas의 DataFrame형태 그대로 딥러닝 모델에 넣을 수 없다.</strong> 반드시 데이터가 Tensor의 형태가 되어야 한다.</p>
<blockquote>
<p><strong>딥러닝에서 데이터를 GPU에서 빠르게 처리하기 위해서는 반드시 tensor이여야 한다.</strong></p>
</blockquote>
<table>
<thead>
<tr>
<th>항목</th>
<th>머신러닝</th>
<th>딥러닝</th>
</tr>
</thead>
<tbody><tr>
<td>데이터 형태</td>
<td>DataFrame, ndarray 등 사용 가능</td>
<td>반드시 Tensor</td>
</tr>
<tr>
<td>모델 입력 방식</td>
<td>일반 수치 연산 (벡터/배열 중심)</td>
<td>GPU 병렬 연산을 위한 텐서 필요</td>
</tr>
<tr>
<td>라이브러리</td>
<td>Scikit-learn 등</td>
<td>PyTorch, TensorFlow 등</td>
</tr>
<tr>
<td>내부 처리</td>
<td>비교적 단순한 수학적 계산</td>
<td>행렬(텐서) 연산을 대규모로 반복</td>
</tr>
</tbody></table>
<p>Tensor는 숫자로 이루어진 다차원의 배열을 말한다. 차원의 수에 따라서 이름이 다르다. 텐서는 데이터를 담는 상자라고 생각한다.  </p>
<blockquote>
<p><strong>딥러닝에서는 tensor를 입력, 출력, 가중치, 모든 연산의 기본 단위로 사용한다.</strong> </p>
</blockquote>
<p>tensor.shape : 텐서의 행과 열로 크기를 알려준다. 
tensor.dtype : 텐서의 요소의 자료형을 알려준다.
tensor.device : 텐서의 연산의 위치를 알려준다.</p>
<h3 id="tensor-1">tensor</h3>
<p>텐서를 위한 라이브러리를 가져온다. </p>
<pre><code>import torch
import numpy as np
import pandas as pd</code></pre><p>리스트를 만들어서 텐서로 변환이 가능하다. torch.tensor()함수를 사용해서 텐서로 변환할 수 있다. </p>
<pre><code>data = [[1,2], [3,4], [5,6]]
x_data = torch.tensor(data)
x_data</code></pre><p>넘파일 array를 가지고 텐서로 변환이 가능하다. 
데이터프레임을 사용해서는 텐서로 변환이 안된다. (데이터프레임은 지원하지 않는다.)</p>
<p><strong>tensor의 속성</strong>
shape
tensor.shape : 텐서의 행과 열로 크기를 알려준다. 
tensor.dtype : 텐서의 요소의 자료형을 알려준다.
tensor.device : 텐서의 연산의 위치를 알려준다.</p>
<pre><code># GPU가 사용 가능한 경우에는 GPU에, 그렇지 않은 경우에는 CPU에 할당
if torch.cuda.is_available():
    tensor = x_np.to(&quot;cuda&quot;)
else:
    tensor = x_np.to(&quot;cpu&quot;)

# 텐서가 어느 디바이스에 할당되어 있는지 확인
print(tensor.device)</code></pre><p>tensor.to(&quot;cuda&quot;) 를 통해서 GPU에 할당이 가능하다.
런타임 &gt; 런타임 유형 변경 &gt; 하드웨어 가속기 변경</p>
<p>넘파이는 데이터프레임과 유사하다. 
df.loc[0. :], df.loc[:, 0]</p>
<p>torch.cat() 메서드는 텐서를 붙여라라는 의미이다. dim=0일 때는 행방향으로 아래 위로 붙인다. dim=1일 경우에는 열방향으로 좌우로 붙인다. </p>
<p>torch에서 지원하는 행렬의 곱이 @이다. 행령의 곱 @은 순서가 다르면 값이 다르다.</p>
<p>텐서에서의 요소는 element라고 부른다. 요소 곱(element-wise product) * 는 element끼리의 합으로 계산한다.</p>
<p>알아야 하는 내용</p>
<ul>
<li>미분</li>
<li>선형대수(벡터와 행렬)</li>
<li>통계</li>
</ul>
<p>데이터프레임은 바로 텐서로 변환이 안되기 때문에 넘파이로 변환해서 텐서로 변환한다. </p>
<pre><code># 넘파이로 바꾸기
x_np = x.values
y_np = y.values</code></pre><p>텐서</p>
<ul>
<li>데이터 로더는 텐서로 불가능하고, 텐서 데이터셋을 만들어 주어야 한다. </li>
<li>데이터 로더는 내가 정한 사이즈(데이터건수)만큼 뽑아준다. </li>
</ul>
<p>넘파이 
파이토치는 반드시 텐서나 텐서 데이터셋을 요구한다. 
텐서를 가지고 모델링이 가능하다. 
딥러닝은 체할까봐 범위를 정해서 쪼개서 학습시킨다.
텐서 혹은 텐서 데이터셋을 쪼개는 방법이 데이터 로더이다.
데이터로더를 만들면 x따로 y따로가 아닌 합쳐진 형태인 텐서 데이터셋으로 만들어주어야 한다. </p>
<hr />
<h2 id="02-딥러닝-개요">02. 딥러닝 개요</h2>
<h3 id="021-딥러닝-코드-구조">02.1. 딥러닝 코드 구조</h3>
<h4 id="데이터전처리-1">데이터전처리 1</h4>
<ul>
<li><strong>nan조치</strong>
<code>data.isnull().sum()</code> 로 결측치를 확인한다.
<code>data.ffill(inplace=True)</code> 로 결측치를 이전 값으로 채운다.
<code>data.drop(columns=drop_cols, inplace=True)</code> 로 분석에 의미가 없다고 판단되는 변수를 제거한다. </li>
<li><strong>가변수화 (one-hot encoding)</strong>
<code>x = pd.get_dummies(x, columns=dumm_cols, drop_first=True, dtype=int)</code> 로 범주형 데이터를 수치형 데이터로 one-hot encoding한다. <code>drop_first=True</code> 로 카테고리(3) 중에서 하나를 제거하고 나머지(2)만 가변수화해서 중복을 제거한다.</li>
<li><strong>스케일링</strong>
<code>scaler = MinMaxScaler()</code> 로 스케일러를 선언해준다. <code>x_train = scaler.fit_transform(x_train)</code> 로 학습데이터에 대해서만 <code>fit_transform()</code> 으로  fit과 적용을 모두 해준다. <code>x_val = scaler.transform(x_val)</code> 으로 검증데이터와 평가데이터에 대해서는 <code>transform()</code>으로 적용만 해준다.
거리 기반 알고리즘인 knn을 사용할 때는 스케일링을 반드시 해야 한다./ 결정트리나 랜덤 포레스트, 그래디언트 부스팅은 스케일링 필요없다.</li>
</ul>
<blockquote>
<ul>
<li><strong>딥러닝에서는 스케일링을 꼭 해야한다.</strong> 딥러닝에서는 계산이 반복적으로 누적이 되고, 많은 양의 가중치와 활성화 함수가 연쇄 작용하여 스케일링을 거의 모든 경우에 필수적으로 사용해주어야 한다.<ul>
<li>fit() : 데이터를 기준으로 <strong>평균, 표준편차, 등을 계산해 기준</strong>을 만든다.</li>
<li>transform() : 그 기준으로 데이터를 <strong>변환만 실행</strong></li>
<li>fit_transform() : 두 과정을 한번에 처리한다.</li>
</ul>
</li>
</ul>
</blockquote>
<ul>
<li>train 데이터에서만 fit_transform()을 사용해야 한다.</li>
<li><em>validation과 test데이터*</em>에서는 <strong>반드시 transform()만 사용</strong>해야 한다. 
val과 test에는 데이터의 정보가 학습되어 들어가면 절대 안된다. =&gt; <strong>Data Leakage</strong></li>
<li>추가) x와 y 분리
<code>target = 'Ozone'</code>으로 타겟이 될 y값의 변수를 지정해준다. <code>x = data.drop(target, axis=1)</code> 과 <code>y = data.loc[:, target]</code> 으로 데이터를 분리한다.</li>
<li><strong>데이터 분할</strong>
<code>x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=.2, random_state = 20)</code>으로  학습용과 검증용 또는 학습용과 평가용으로 적절한 비율에 맞게 분리한다.</li>
</ul>
<h4 id="데이터전처리-2">데이터전처리 2</h4>
<ul>
<li><strong>텐서로 변환</strong><ul>
<li>tensor로 변환
x와 y는 ndarray의 데이터로 딥러닝 모델이 바로 처리할 수 없다. 
딥러닝 모델에 넣을 수 있는 형식인 tensor로 변환한다. 
<code>x_train_tensor = torch.tensor(x_train, dtype=torch.float32)</code> 으로 텐서로 바꾼다.
<code>y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)</code> 로 Series형태의 y_train을 <code>.values</code>로 넘파이 배열로 바꾸고 <code>veiw(-1,1)</code>로 텐서의 shape을 [n]에서 [n,1]로 바꾸어준다.</li>
<li>Tensor Dataset로 묶기
tensor로 만든 x와 y의 데이터를 한 쌍으로 관리한다.
모델이 학습할 때, x-&gt;y 예측이 자연스럽도록 도와준다.</li>
</ul>
</li>
<li><strong>Data Loader</strong>
Data Loader는 딥러닝에서 데이터를 한 덩이씩(batch단위)를 자동으로 꺼내주는 도구이다. 한번에 때려넣으면 GPU가 터진다. <strong>데이터를 조금씩 나눠서 미니 배치 학습을 해야한다.</strong> </li>
</ul>
<blockquote>
<p><strong>Data Loader의 역할</strong></p>
</blockquote>
<ul>
<li>미니배치 처리 : <code>batch_size=32</code> 는 데이터를 32개씩 쪼개준다.(한 미니 배치에 들어갈 데이터수)</li>
<li>셔플 처리 : <code>shuffle=True</code> 는 학습 전에 순서를 랜덤으로 섞어 과적합을 방지한다.</li>
<li>반복(iter) : <code>for batch in loader</code> 로 미니 배치 단위로 순차적으로 뽑아 데이터 반복이 가능하다.</li>
<li><em>간단하게 데이터 공급 매니저*</em>로 생각한다. 
=&gt; loader는 배치단위로 학습을 하기 위함이기에 validation를 loader로 만들어주지 않아도 된다.</li>
</ul>
<h4 id="모델링">모델링</h4>
<ul>
<li>모델 설계</li>
<li>Loss &amp; Optimizer</li>
<li>학습</li>
<li>학습 곡선 검토<h4 id="예측-및-검증-평가">예측 및 검증 평가</h4>
</li>
<li>예측 </li>
<li>검증</li>
</ul>
<hr />
<h3 id="022-학습이란">02.2. 학습이란?</h3>
<p>오차를 최소화하는 파라미터(가중치)를 찾는다.
학습의 단계</p>
<ol>
<li>가중치에 초기값을 할당한다.</li>
<li>예측 결과를 뽑는다.</li>
<li>오차(실제값-예측값)을 계산한다. loss function</li>
<li>오차를 줄이는 방향으로 가중치를 조정한다. Optimizer Adam + lr</li>
<li>다시 1단계로 올라가 반복한다. </li>
</ol>
<h3 id="023-가중치-조정">02.3. 가중치 조정</h3>
<p>가장 쉬운 가중치 조정은 가장 쉬운 예측은 평균을 내는 방법이다. 평균은 가중치를 모두 같은 값을 부여하여 다 똑같이 중요하다는 의미이다. 
오래된 과거보다 가장 가까운 과거를 따르는 것이다. 마르스코프 체인(마코프체인?)
가중치가 모두 같지 않다고 생각해서 가중치를 다르게 준다. 최적의 가중치를 찾기 위해서...</p>
<p>편향은 기본값으로 입력값에 영향을 받지 않는 값의의미를 가진다.</p>
<hr />
<h3 id="024-오차-계산">02.4. 오차 계산</h3>
<h4 id="loss-function">loss function</h4>
<ul>
<li>loss function : 오차(예측값-실제값)를 계산</li>
</ul>
<h3 id="025-가중치-조정">02.5. 가중치 조정</h3>
<h4 id="optimizer">optimizer</h4>
<ul>
<li>Optimizer : 가중치 조절
오차를 최소화하도록 가중치를 업데이트하는 역할이다. 최근에는 Adam 옵티마이저로 좋은 성능을 보인다. </li>
</ul>
<h4 id="learning-rate">learning rate</h4>
<ul>
<li>learning rate : 얼마만큼 가중치를 조정할지 결정
업데이트할 비율을 말하며 걸음걸이의 보폭을 조정한다고 표현한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/182c0363-9c43-4a4a-8d4c-9b5dc7e95886/image.png" /></li>
</ul>
<h3 id="026-학습을-위한-하이퍼파라미터">02.6. 학습을 위한 하이퍼파라미터</h3>
<h4 id="batch_size">batch_size</h4>
<ul>
<li>batch_size : 미니 배치의 크기(건수)
전체 데이터를 적절히 나누어서 배치단위로 학습한다. (학습=가중치 업데이트)
딥러닝에서는 배치 단위로 가중치를 업데이트한다. 
batch_size로 미니배치학습을 하게 된다면 하나의 미니 배치마다 예측-&gt;손실계산-&gt;역전파-&gt;가중치 업데이트가 진행된다. </li>
</ul>
<h4 id="epoch">epoch</h4>
<ul>
<li>epoch : 전체 데이터를 몇 번 반복 학습할지 결정
학습 데이터를 반복해서 학습하면서 최적의 가중치를 찾는다. 케이스마다 최적의 값이 다르다.
epoch도 하이퍼파라미터로 모델 학습 시, 사람이 정해 주어야 하는 옵션이다. </li>
</ul>
<h3 id="027-학습곡선">02.7. 학습곡선</h3>
<h4 id="학습곡선">학습곡선</h4>
<p>모델의 학습이 잘 되었는지 파악하기 위한 그래프이다. 정답은 아니지만 경향을 파악하는 데 유용하다. 
각 epoch마다 train error와 val error가 어떻게 줄어들고 있는지 확인한다. </p>
<p><strong>바람직한 학습곡선</strong>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/dd1c1344-914c-4af2-8216-1ca9fa149741/image.png" /></p>
<ul>
<li><ol>
<li>초기의 epoch에서는 오차가 크게 줄어든다.</li>
</ol>
</li>
<li><ol start="2">
<li>오차 하락이 점점 꺾인다.</li>
</ol>
</li>
<li><ol start="3">
<li>오차가 점점 완만해진다.</li>
</ol>
</li>
</ul>
<p><strong>바람직하지 않은 학습곡선</strong></p>
<ul>
<li><ol>
<li>학습이 덜된 경우 : 오차가 줄어들다가 학습이 종료되었다. <ul>
<li>epoch 늘린다.</li>
<li>lr 을 크게한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/cf2af741-5a5d-4950-927a-b00373f04dd0/image.png" /></li>
</ul>
</li>
</ol>
</li>
<li><ol start="2">
<li>train_error가 들쭉날쭉한 경우 : 가중치 조절이 세밀하지 않아 step이 크다.<ul>
<li>lr 을 줄인다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c859fe9f-4dc0-495e-b995-1758cb455c5a/image.png" /></li>
</ul>
</li>
</ol>
</li>
<li><ol start="3">
<li>과적합으로 과도하게 학습된 경우 : train_error는 계속 줄어들지만, val_error는 어느순간부터 커진다.<ul>
<li>epoch 줄인다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/5c2a69b8-8e1c-45a1-b080-6ef6c86754e6/image.png" /></li>
</ul>
</li>
</ol>
</li>
</ul>
<h4 id="추가--train">추가 + train()</h4>
<p>train() 은 dataloader(미니 배치단위 학습을 위한 매니저)와 model과 loss_fn(손실함수)와 Optimizer(가중치 조정), device(GPU할당)</p>
<ul>
<li><p><code>len(dataloader.dataset)</code> 으로 전체 데이터셋의 크기를 알 수 있다.(전체 데이터 수) </p>
</li>
<li><p><code>len(dataloader)</code> 으로 총 미니 배치의 배수로 (전체 데이터 수/batch_size)이다.</p>
<blockquote>
<p><strong>데이터의 크기는 데이터 건수, 개수를 의미한다.</strong></p>
</blockquote>
</li>
<li><p><code>tr_loss=0</code> 으로 전체 학습 동안의 총 loss를 저장할 변수</p>
</li>
<li><p><code>model.train()</code> 으로 학습모드(train mode)로 전환한다. </p>
</li>
<li><p><code>for batch, (X, y) in enumerate(dataloader):</code> 으로 Data Loader에서 미니배치마다 x와 y를 하나씩 꺼내면서 반복한다.</p>
</li>
<li><p><code>X, y = X.to(device), y.to(device)</code> 텐서 연산을 GPU로 설정한 device에서 수행하도록 설정한다.</p>
</li>
<li><p><code>pred = model(X)</code> 으로 모델에 입력값 X를 넣어서 예측값을 생성한다.</p>
</li>
<li><p><code>loss = loss_fn(pred, y)</code> 으로 손실함수로 예측값과 실제값의 차이를 계산하고 - <code>tr_loss += loss</code>로 이후에 평균을 구하기 위해 전체 loss에 누적한다.</p>
</li>
<li><p><code>loss.backward()</code> 으로 손실함수를 기준으로 각 파라미터의 기울기(gradient)를 계산한다.</p>
</li>
<li><p><code>optimizer.step()</code> 으로 계산된 기울기를 바탕으로 모델의 가중치를 업데이트한다. =&gt; 학습</p>
</li>
<li><p><code>optimizer.zero_grad()</code> 이전 배치의 기울기가 누적돼서 학습이 꼬이지 않도록 기울기를 0으로 초기화한다.</p>
</li>
<li><p><code>tr_loss /= num_batches</code> 으로 모든 배치의 loss를 평균내서 1 epoch동안의 평균 손실값을 계산한다.</p>
<pre><code>def train(dataloader, model, loss_fn, optimizer, device):
  size = len(dataloader.dataset)                  # 전체 데이터셋의 크기
  num_batches = len(dataloader)                   # 배치 크기
  tr_loss = 0
  model.train()                                   # 훈련 모드로 설정(드롭아웃 및 배치 정규화와 같은 계층을 훈련 모드로 변경)
  for batch, (X, y) in enumerate(dataloader):     # batch : 현재 배치 번호, (X, y) : 입력 데이터와 레이블
      X, y = X.to(device), y.to(device)           # X.to(device), y.to(device): 입력 데이터와 레이블을 지정된 장치(device, CPU 또는 GPU)로 이동

      # Compute prediction error
      pred = model(X)
      loss = loss_fn(pred, y)
      tr_loss += loss

      # Backpropagation
      loss.backward()             # 역전파를 통해 모델의 각 파라미터에 대한 손실의 기울기를 계산
      optimizer.step()            # 옵티마이저가 계산된 기울기를 사용하여 모델의 파라미터를 업데이트
      optimizer.zero_grad()       # 옵티마이저의 기울기 값 초기화. 기울기가 누적되는 것 방지

  tr_loss /= num_batches          # 모든 배치에서의 loss 평균

  return tr_loss.item()</code></pre></li>
</ul>
<h3 id="028-활성화-함수">02.8. 활성화 함수</h3>
<p>현재 layer의 결과값이 다음 layer로 어떻게 전달할지 결정/변환해주는 함수이다. 
선형의 경우 은닉층 hidden layer를 아무리 추가해도 그냥 선형 회귀에서 변하지 않는다. </p>
<ul>
<li><p>hidden layer에서 선형 함수를 비선형 함수로 변환해 주는 역할이다. </p>
</li>
<li><p>ouput layer에서는 결과 값을 다른 값으로 변환해 주는 역할이다. </p>
<blockquote>
<p>*<em>비선형성을 만들어주는 것이 활성화 함수의 목적이다. *</em></p>
</blockquote>
</li>
<li><p>input : 입력값</p>
</li>
<li><p>hidden layer : input과 output layer사이의 내부 계산을 수행하는 층(여러 개 가능)</p>
</li>
<li><p>output layer : output을 출력하는 층</p>
</li>
</ul>
<p>회귀모델 : ReLU()를 많이 사용한다. 
분류모델 : 이진분류에서는 sigmoid()함수, 다중분류에서는 softmax()함수를 사용한다.</p>
<p><strong>hidden layer에서의 activation function</strong>
비선형성을 부여하여 신경망이 복잡한 관계를 학습한다.
ReLU(), tanh(), sigmoid()</p>
<p><strong>output layer에서의 activation function</strong>
output의 결과를 내는 layer인 output layer에서는 <strong>문제의 종류(분류/회귀)에 따라서 다르다.</strong>
회귀 : <strong>활성화함수를 사용하지 않음</strong>
<strong>활성함수라는 제한 없이 자유롭게 숫자값을 예측해야 하기 때문에</strong> 회귀 모델링에서는 활성화함수가 필요없다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/9c413481-e592-4a61-9b53-5e9760c492cc/image.png" /></p>
<pre><code>model = nn.Sequential(
    nn.Linear(10, 64),
    nn.ReLU(),
    nn.Linear(64, 1)      # ← 활성화 함수 없음 (회귀)
)</code></pre><hr />
<h2 id="03-회귀-모델링">03. 회귀 모델링</h2>
<h3 id="031-환경설정">03.1. 환경설정</h3>
<ul>
<li>환경 설정 : 라이브러리 불러오기</li>
<li>필요 함수 생성 : <ul>
<li>make-dataset은 텐서로 바꾼다. dataloader로 만들기 위해서 tensordataset으로 합친다. dataloader를 생성한다.</li>
<li>train은 오차를 계산하고 예측하고, feed forward와 back propagation 과정을 수행한다.데이터로더를 배치 단위로 잘라서 가중치 업데이트를 한다.</li>
<li>evaluate는 모델의 결과를 평가한다. </li>
</ul>
</li>
<li>학습곡선</li>
<li>GPU준비<h3 id="032-데이터-준비">03.2. 데이터 준비</h3>
</li>
<li>x와 y를 나눈다.</li>
<li>가변수화로 문자형 데이터를 숫자로 바꾼다.</li>
<li>데이터분할</li>
<li>Scaling (거리 기반 알고리즘인 knn을 사용할 때는 스케일링을 반드시 해야 한다./ 결정트리나 랜덤 포레스트, 그래디언트 부스팅은 스케일링 필요없다.)
  train 데이터는  loader로 만들어야 한다 반드시!</li>
</ul>
<blockquote>
<p>Q. validation 데이터는 loader로 만들어주지 않아도 되나요? 
=&gt; loader는 배치단위로 학습을 하기 위함이기에 validation를 loader로 만들어주지 않아도 된다.</p>
</blockquote>
<h3 id="033-모델링-피쳐3개">03.3. 모델링 (피쳐3개)</h3>
<ul>
<li>딥러닝을 위한 준비작업인 data loader로 만들기</li>
<li>모델 선언
nn.Linear(입력, 출력) 레이어 한개를 추가한다. layer는 앞단에서의 연결의 개수가 가중치에 관련이 있다. nn.Linear()는 앞에서 오는 피쳐들에 대해서 모두 연결되었다는 의미로 <strong>Fully connected layer , Dense Layer</strong>라고 한다.
값을 사용하지 않는다는 것을 언더바로 표시한다._<pre><code>n_feature = x.shape[1]
</code></pre></li>
</ul>
<h1 id="모델-구조-설계">모델 구조 설계</h1>
<p>model1 = nn.Sequential(
        nn.Linear(n_feature, 1)
        ).to(device)</p>
<p>print(model1)</p>
<pre><code>#### 손실함수 선언 Loss function</code></pre><p>loss_fn = nn.MSELoss()
optimizer = Adam(model1.parameters(), lr=0.1)</p>
<pre><code>&gt;loss function
loss function은 손실함수나 목적함수라 부른다. 회귀모델의 목적함수는 MSEloss를 사용한다. 
![](https://velog.velcdn.com/images/ehekaanldk/post/6fadd846-b39e-4334-8e98-e1a41963ab00/image.png)
실제 모델 평가에서와 수식이 다르지만 미분을 처리하는 데에서 차이가 발생하고 특별히 의미없다. 

#### 옵티마이저 선언 Optimizer
&gt;optimizer
오차를 최소화하도록 가중치를 조금씩 업데이트하는 역할이다.
Adam은 스텝의 사이즈와 관성을 반영해서 찾아가는 거의 끄빵왕이다.~(ㅋㅋㅋㅋ)
업데이트할 비율은 learning rate으로 조절이 필요하다.
optimizer(업데이트 할 파라미터, 업데이트할 비율)

&gt;learning rate
가중치를 업데이트하는 과정에서 가중치의 조정정도..?
가중치를 조정하면서 오차를 조금씩 줄인다. 미분은 순간 변화량! 
learning rate을 늘리는 것 : 가중치가 너무 크게 조정되어서 loss가 들쑥날쑥
learning rate를 줄이는 것 : 가중치가 아주 조금씩 조정되어서 최소값에 도달하려면 세월아 네월아

#### 학습루프
- 학습곡선
주어진 환경에서 학습이 잘 되었느지 적절하게 확인할 수 있는 방법
![](https://velog.velcdn.com/images/ehekaanldk/post/b0614b0f-8094-42c0-9969-2359e0f4179b/image.png)</code></pre><p>dl_learning_curve(tr_loss_list, val_loss_list)</p>
<pre><code>
epoch은 train set 전체를 학습하는 횟수(1만건의 train set을 5epoch으로 학습시키면 5만건)

텐서-&gt; 넘파이
MAE와 MAPE는 sklearn의 함수로 텐서를 인식하지 못하기 때문에 텐서로 변화해서 구한다. 

epoch : 주어진 train set을 몇 번 반복 학습할지 결정
파라미터(= 가중치) : 학습을 하는 과정에서 업데이트할 가중치를 머신이 찾는다.
하이퍼파라미터 : 학습 곡선을 보면서 학습률을 사람이 찾는다.

학습곡선이란
모델 학습이 잘 되었는지 파악하기 위한 그래프이다. 정답이 아니고 경향을 파악한다. 
그래프를 읽는 방법
1. 축의의미를 파악한다. 
2. 그래프의 모양을 확인한다. (꺽이는 지점이 나온다)
3. 바람직한 학습곡선인지 확인한다.

학습이 덜 된 경우는 
들쑥날쑥하면 lr을 좀 줄인다.</code></pre><p>loss_fn = nn.MSELoss()
optimizer = Adam(model1.parameters(), lr=0.1)</p>
<pre><code>
### 03.4. 모델 평가</code></pre><p>loss, pred = evaluate(x_val_ts, y_val_ts, model3, loss_fn, device)</p>
<p>mae = mean_absolute_error(y_val_ts.numpy(), pred.numpy())
mape = mean_absolute_percentage_error(y_val_ts.numpy(), pred.numpy())</p>
<p>print(f'MSE : {loss}')
print(f'MAE : {mae}')
print(f'MAPE : {mape}')</p>
<pre><code></code></pre>
