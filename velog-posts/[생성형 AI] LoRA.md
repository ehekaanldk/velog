---
title: "[생성형 AI] LoRA"
date: "2025-05-08"
link: "https://velog.io/@ehekaanldk/%EC%83%9D%EC%84%B1%ED%98%95-AI-LoRA"
series: "Uncategorized"
---

<ul>
<li><p><strong>LoRA (Low-Rank Adaptation)</strong></p>
<p>  <strong>LoRA</strong>는 사전 학습된 대형 모델을 전체 미세조정(fine-tuning)하지 않고,</p>
<p>  <strong>일부 저랭크 행렬(A, B)만 학습</strong>해 <strong>빠르고 가벼운 튜닝</strong>을 가능하게 하는 기술입니다.</p>
<blockquote>
<p>기존 가중치와의 차이만 보정해 학습하는 방식이며,
LLM(GPT, BERT 등)의 <strong>튜닝 비용</strong>을 크게 줄일 수 있습니다.</p>
</blockquote>
</li>
</ul>
<ul>
<li>사용하는 이유
사전 학습된 거대 LLM(GPT, BERT 등)은 수십억 갱의 파라미터를 가지고 있다. <strong>전체를 파인튜닝하려면</strong> GPU 메모리도 많이 들고 시간이 오래 걸린다. </li>
</ul>
<h3 id="lora-방식-weight는-고정-보정만-학습">LoRA 방식: Weight는 고정, 보정만 학습</h3>
<p>미세튜닝 시에 사전학습 모델의 레이 대부분은 고정 (freeze) 하고 , 일부 어텐션 레이어의 가중치 행렬만 낮은 랭크의 행렬 분해로 표현 후 학습한다. </p>
<p>$y = x \cdot (W + \Delta W)\quad \text{where } \Delta W = A \cdot B$</p>
<p>즉,</p>
<p>$y=x⋅W+x⋅A⋅B$</p>
<h3 id="구성">구성:</h3>
<ul>
<li>$A \in \mathbb{R}^{d \times r}$: 입력 축소 (down projection)</li>
<li>$B \in \mathbb{R}^{r \times k}$: 출력 복원 (up projection)</li>
<li>$r≪d,k$: 매우 작은 값 (보통 4~8)</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b60e607b-b90b-4312-8666-7e8b1797449a/image.png" /></p>
<table>
<thead>
<tr>
<th>행렬</th>
<th>크기</th>
<th>역할</th>
<th>의미</th>
</tr>
</thead>
<tbody><tr>
<td><strong>A</strong></td>
<td>2K × r</td>
<td>입력 축소</td>
<td>입력 차원 $2K$ → 저랭크 차원 $r$로 압축</td>
</tr>
<tr>
<td><strong>B</strong></td>
<td>r × 2K</td>
<td>출력 복원</td>
<td>저랭크 $r$ → 다시 원래 출력 차원 $2K$로 복원</td>
</tr>
</tbody></table>
<p><strong>LoRA에서 A·B의 결과가 기존 W와 같은 크기를 갖도록 만드는 이유는, W + A·B 형태로 보정하기 위해서이.</strong> 이 덧셈은 shape이 다르면 불가능하기 때문이다.</p>
