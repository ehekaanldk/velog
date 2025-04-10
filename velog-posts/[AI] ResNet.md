---
title: "[AI] ResNet"
date: "2025-04-10"
link: "https://velog.io/@ehekaanldk/AI-ResNet"
series: "Uncategorized"
---

<h2 id="resnet">ResNet</h2>
<p>layer를 쌓을수록 미분을 반복하면서 미분값이 작아지고, weight (가중치)의 영향이 작아지는 gradient vanshing 문제가 발생</p>
<p>gradient vanshing문제를 해결하기 위해 <strong>지름길</strong>을 만들어서 딥러닝이 너무 깊어져도 잘 학습할 수 있도록 도와주는 구조이다.</p>
<p>ResNet은 입력값 x를 그대로 다음 층(layer)에 더해주는 모델이다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/64ee2221-18fd-411e-a54f-8db5960b240e/image.jpeg" /></p>
<p>   최종적으로 H(x) 전체를 학습하는 대신에, 입력x로부터 달라져야 하는 F(x)만 학습한다.</p>
<p>   $H(x) = F(x) + x ⇒ F(x) = H(x) -x$</p>
<p>   입력x에서 우리가 원하는 출력 H(x)까지 가기 위해 추가로 필요한 정보이기 때문에 잔차라고 부른다.</p>
<p>   $F(x)$ : 학습할 신경망의 출력</p>
<p>   $x$ : 이전 layer의 입력값을 그대로 전달</p>
<p>   $y = F(x) +x$ </p>
<p>   $\frac{∂y}{∂x} = \frac{∂F(x)}{∂x} + \frac{∂x}{∂x} = \frac{∂F(x)}{∂(x)} +1$</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7a7891ba-287f-48a8-9fe6-388ab6298938/image.png" /></p>
<h2 id="전이학습transfer-learning">전이학습(transfer learning)</h2>
<p>전이학습은 사전학습된 모델을 새로운 작업에 다시 활용하는 방법</p>
<ul>
<li>초반의 전반적인 학습 : 기존 모델의 초기 layer는 프리징하여 파라미터를 고정</li>
<li>후반의 구체적인 학습 : 새로운 데이터에 맞춰 일부 layer에서만 재학습(파라미터 업데이트) 
ex) </li>
<li>기존의 weight는 고정하고, 마지막 FC layer만 학습</li>
</ul>
<p>기존의 학습된 모델에 데이터를 추가하여 기존 모델의 일부와 함께 학습한다.<br />사전 학습된 모델을 활용함으로써 전체 데이터셋에 라벨링 할 필요가 없다.<br />시간을 절약하면서 원하는 성능 유지</p>
<p><strong>파인튜닝 VS 전이학습</strong>
전이학습은 사전 학습된 모델과 새로 학습한 도메인이 다를 경우 성능 저하</p>
<p>파인튜닝은 전이학습의 한 형태로 사전 학습된 모델 전체 또는 일부 레이어를 새로운 작업에 맞게 재학습하는 방법이다. 보통 전이학습에서 <strong>고정했던 레이어를 다시 학습 가능하게 한다.</strong>
ex) </p>
<ul>
<li>ResNet을 가져와서, 마지막 block (layer4)부터 다시 학습</li>
<li>BERT 모델을 NLP 감정 분석에 맞게 전체 또는 일부 파라미터 미세 조정</li>
</ul>
<table>
<thead>
<tr>
<th>항목</th>
<th>전이학습 (Transfer Learning)</th>
<th>파인튜닝 (Fine-Tuning)</th>
</tr>
</thead>
<tbody><tr>
<td><strong>정의</strong></td>
<td>사전학습된 모델을 다른 작업에 활용하는 전략</td>
<td>전이학습 모델을 새 작업에 맞게 미세 조정</td>
</tr>
<tr>
<td><strong>학습 범위</strong></td>
<td>주로 feature extractor는 고정, 출력층만 학습</td>
<td>전체 또는 일부 레이어 파라미터를 업데이트</td>
</tr>
<tr>
<td><strong>목표</strong></td>
<td>기존 지식을 재사용</td>
<td>기존 모델을 현재 작업에 최적화</td>
</tr>
<tr>
<td><strong>언제 사용?</strong></td>
<td>빠르게 전이하고 싶을 때</td>
<td>전이한 모델을 더 성능 좋게 만들고 싶을 때</td>
</tr>
<tr>
<td><strong>학습률</strong></td>
<td>새 층만 학습하므로 보통 일반적 학습률</td>
<td>기존 weight 보호를 위해 낮은 학습률 사용</td>
</tr>
<tr>
<td><strong>포함 관계</strong></td>
<td>상위 개념</td>
<td>하위 개념 (전이학습 안에서 쓰임)</td>
</tr>
</tbody></table>
<p>참고
<a href="https://kr.appen.com/blog/transfer-learning/">https://kr.appen.com/blog/transfer-learning/</a></p>
