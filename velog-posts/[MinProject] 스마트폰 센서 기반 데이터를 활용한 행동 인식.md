---
title: "[MinProject] 스마트폰 센서 기반 데이터를 활용한 행동 인식"
date: "2025-04-15"
link: "https://velog.io/@ehekaanldk/miniproject1"
series: "Uncategorized"
---

<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/71f4a042-6bd3-477a-adc3-24614458c4fe/image.png" /></p>
<p><a href="https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones">https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones</a></p>
<h2 id="데이터-분석">데이터 분석</h2>
<ul>
<li><p>제공된 학습 데이터와 테스트 데이터 로드 (train, test, features)</p>
</li>
<li><p>필요 없는 열(subject) 제거</p>
</li>
<li><p>데이터 크기, 변수 수, 변수 타입 등 기본 정보 확인</p>
</li>
<li><p>Activity 값 분포 확인 (정적/동적 행동 비율)</p>
</li>
</ul>
<h2 id="eda-분석-가이드라인">EDA 분석 가이드라인</h2>
<ul>
<li><p>Activity 기준으로 정적(0)/동적(1) 이진 구분 라벨(Is_dynamic) 생성</p>
</li>
<li><p>행동별 카운트 시각화 (정적/동적, 각 세부 행동)</p>
</li>
<li><p>정적/동적별로 하위 3개 클래스 존재 확인</p>
</li>
<li><p>분류 기준을 기반으로 단계별 모델링 구조 구상</p>
</li>
</ul>
<h2 id="머신러닝-모델링-과정">머신러닝 모델링 과정</h2>
<ul>
<li><p>x, y 분리 (타겟: Is_dynamic 또는 Activity)</p>
</li>
<li><p>LabelEncoder를 사용해 Activity를 정수형 라벨로 인코딩</p>
</li>
<li><p>train/val 분리 시 stratify와 random_state 지정</p>
<p>스케일링: MinMaxScaler로 x_train만 fit_transform, 나머지 transform만 적용</p>
</li>
</ul>
<h2 id="딥러닝-모델링-과정">딥러닝 모델링 과정</h2>
<p>🔹 1단계: 이진 분류 (정적 vs 동적)</p>
<ul>
<li><p>출력층 Dense(1, activation='sigmoid'), 손실 함수 binary_crossentropy</p>
</li>
<li><p>모델 학습 후 정확도, F1-score, confusion matrix로 평가</p>
</li>
<li><p>y가 DataFrame 형태라 loss 오류 발생 → values.ravel()로 수정</p>
</li>
</ul>
<p>🔹 2단계: 세부 동작 분류 (정적/동적 각각 다중 분류)</p>
<ul>
<li><p>정적(0), 동적(1) 데이터를 필터링하여 각각 별도 모델 학습</p>
</li>
<li><p>출력층 Dense(3, activation='softmax'), 손실 함수 sparse_categorical_crossentropy</p>
</li>
<li><p>학습 후 argmax()를 통해 예측 클래스 추출 및 평가</p>
</li>
</ul>
<p>🔹 성능 비교</p>
<ul>
<li><p>모델 1~4개 각각 학습 및 테스트 데이터로 평가</p>
</li>
<li><p>정확도 및 macro F1-score를 DataFrame으로 정리하여 비교</p>
</li>
</ul>
<hr />
<h2 id="문제-발생-및-해결">문제 발생 및 해결</h2>
<h3 id="1-validation-성능과-test-성능-불일치">1. Validation 성능과 Test 성능 불일치</h3>
<p>val_loss는 0.9x로 모든 모델이 학습이 잘 이루어졌는데 test의 결과가 매우 안 좋음
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/beca04b5-8a9f-446a-a0ec-2a6cbd94a3c9/image.png" /></p>
<p>데이터의 분포에 문제가 있는지 확인한다. 크게 분포의 차이가 없을 알 수 있다. </p>
<div style="display: flex;">
  <img src="https://velog.velcdn.com/images/ehekaanldk/post/c48b5f63-870f-4780-8e9c-76d8c98ef042/image.png" width="48%" />
  <img src="https://velog.velcdn.com/images/ehekaanldk/post/5f618bdd-c8aa-4461-9ce0-e8bf3ebfa757/image.png" width="48%" />
</div>

<p><code>n_class</code> 을 잘못 설정하여 분류하는 범주가 문제의 의도와 다르게 학습된 것을 확인하였다. 
<code>n_class = train_0['Is_dynamic'].nunique()</code> 으로 설정하여 올바르게 <code>n_class</code>를 정의해줌으로써 올바르게 학습 후 평가 데이터에 대해서 아래와 같은 결과를 얻음
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/794bc5e5-446f-4460-b8f0-4983242b49a3/image.png" /></p>
<hr />
<h3 id="2-val_loss-진동-현상-발생">2. val_loss 진동 현상 발생</h3>
<ul>
<li>val_loss가 요동치고 있는 현상이 발생하였다. </li>
<li>모델이 완벽하게 학습되었는지 너무 fit한 학습으로 인한 과적합이 발생하였다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/413235de-b1c5-49a9-9ead-a11c2cf28a8a/image.png" /></li>
</ul>
<p>원인 설명
❗ 학습률이 너무 큼    손실 감소가 불안정하게 튀는 패턴 → learning rate가 커서 overshooting 발생 가능
❗ 배치 크기가 작음    작은 배치는 noise가 많아 val_loss에 요동 유발
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/6bbe683e-39f3-46ea-bfd6-dd2beb66730d/image.png" /></p>
<hr />
<h3 id="3-데이터-누수-data-leakage">3. 데이터 누수 (Data Leakage)</h3>
<h4 id="one-hot과-label-encoding의-차이점">one-hot과 label encoding의 차이점</h4>
<table>
<thead>
<tr>
<th>항목</th>
<th>One-hot encoding</th>
<th>Label encoding (정수 인코딩)</th>
</tr>
</thead>
<tbody><tr>
<td>y 형태</td>
<td>2D ([0,0,1,0,0,...])</td>
<td>1D ([2, 1, 3, ...])</td>
</tr>
<tr>
<td>출력층</td>
<td>Dense(n_class, activation='softmax')</td>
<td>동일</td>
</tr>
<tr>
<td>손실 함수</td>
<td>categorical_crossentropy</td>
<td>sparse_categorical_crossentropy</td>
</tr>
<tr>
<td>모델 출력</td>
<td>클래스 확률 (shape=(batch, n_class))</td>
<td>동일</td>
</tr>
<tr>
<td>메모리 사용량</td>
<td>더 큼 (n_class만큼 열 필요)</td>
<td>더 작음</td>
</tr>
<tr>
<td>성능 차이</td>
<td>거의 없음 (구현이 맞으면)</td>
<td>거의 없음</td>
</tr>
<tr>
<td>y 인코딩을 잘 맞춰서 (one-hot → categorical, label → sparse_categorical)만 쓰면 결과는 거의 같다</td>
<td></td>
<td></td>
</tr>
</tbody></table>
<table>
<thead>
<tr>
<th>실수</th>
<th>문제</th>
</tr>
</thead>
<tbody><tr>
<td>x_val에 fit_transform()</td>
<td>❌ val 정보가 학습에 누설됨</td>
</tr>
<tr>
<td>train/test 각각 fit()</td>
<td>❌ 서로 다른 기준으로 스케일됨 (불공정)</td>
</tr>
<tr>
<td>스케일링은 x_val에 대해서 fit_transform을 적용하면 데이터누수가 발생한다.</td>
<td></td>
</tr>
</tbody></table>
<blockquote>
<p>🔥 데이터 누수란?
모델이 훈련 중에 보지 말아야 할 정보(검증/테스트 데이터의 통계 정보)를 사용하는 것.</p>
</blockquote>
<p>fit()은 데이터의 요약과 정보 집계등의 과정을 수행한다. 
transform()은 fit을 바탕으로 스케일링을 수행한다. </p>
<p>✅ 2. fit()은 다음을 수행함
데이터 통계 요약 계산: 
    - MinMaxScaler: min, max
        - StandardScaler: 평균, 표준편차
        - 이 정보는 모델 학습의 기준(reference) 으로 저장됨</p>
<p>✅ 따라서 train 데이터에 대해서만 fit() 수행</p>
<p>✅ 3. transform()은 다음을 수행함
    - fit()에서 구한 통계값(min/max 등)을 기준으로
    - 데이터를 스케일링(정규화/표준화) 함
    - val이나 test에는 오직 transform()만 적용해야 함</p>
<table>
<thead>
<tr>
<th>함수</th>
<th>역할</th>
<th>어디에 사용해야 하나?</th>
</tr>
</thead>
<tbody><tr>
<td>fit()</td>
<td>통계 집계 (min/max, mean/std 등)</td>
<td>x_train 전용</td>
</tr>
<tr>
<td>transform()</td>
<td>스케일링 수행</td>
<td>x_val, x_test, x_train 모두 가능</td>
</tr>
<tr>
<td>fit_transform()</td>
<td>fit + transform 한 번에</td>
<td>오직 x_train</td>
</tr>
</tbody></table>
<hr />
<h3 id="4-test-데이터에서-스케일러-재선언">4. test 데이터에서 스케일러 재선언</h3>
<p>test데이터에 대해서 모델 검증 시 발생오류</p>
<pre><code>---------------------------------------------------------------------------
NotFittedError                            Traceback (most recent call last)
&lt;ipython-input-106-bb75a1704574&gt; in &lt;cell line: 0&gt;()
      2 # x_test도 x_val처럼 답이 있으면 안되기 때문에 fit없이
      3 scaler = MinMaxScaler()
----&gt; 4 x_test_scaled = scaler.transform(x_test)

2 frames
/usr/local/lib/python3.11/dist-packages/sklearn/utils/validation.py in check_is_fitted(estimator, attributes, msg, all_or_any)
   1755 
   1756     if not _is_fitted(estimator, attributes, all_or_any):
-&gt; 1757         raise NotFittedError(msg % {&quot;name&quot;: type(estimator).__name__})
   1758 
   1759 

NotFittedError: This MinMaxScaler instance is not fitted yet. Call 'fit' with appropriate arguments before using this estimator.</code></pre><p>test데이터에서 스케일러를 새로 선언하지 않는다 train에서 사용한 scaler를 그대로 가져온다.
✅train에서 만든 scaler는 train 데이터 기준 통계(min, max 등) 를 가지고 있음
✅test 데이터는 새로운 unseen 데이터이기 때문에 train 기준으로만 스케일링되어야 정확한 평가 가능
✅test 데이터로 fit() 또는 새로운 스케일러를 만들면: → 데이터 누수(Data Leakage) 발생</p>
