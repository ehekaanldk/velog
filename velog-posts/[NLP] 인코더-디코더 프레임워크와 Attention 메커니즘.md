---
title: "[NLP] 인코더-디코더 프레임워크와 Attention 메커니즘"
date: "2025-04-19"
link: "https://velog.io/@ehekaanldk/NLP-%EC%9D%B8%EC%BD%94%EB%8D%94-%EB%94%94%EC%BD%94%EB%8D%94-%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC"
series: "Uncategorized"
---

<h2 id="기존-language-model-lm">기존 Language Model (LM)</h2>
<h3 id="개념">개념</h3>
<p>기존의 LM(language model)은 다음 단어를 예측하거나 분류 문제를 풀었다. </p>
<p><code>&quot;나는 밥을&quot;</code> -&gt; <code>다음 단어는?</code></p>
<h3 id="구조">구조</h3>
<p><strong>RNN LM</strong>
: 단어를 하나씩 입력받아 순차적으로 다음 단어 예측</p>
<h3 id="한계">한계</h3>
<p>RNN으로 순차적으로 데이터를 처리하면서 병렬처리의 어려움과 장기 의존성의 문제가 발생하였다. </p>
<ul>
<li><strong>병렬 처리문제</strong>
기존의 RNN은 모두 데이터를 순차적으로 처리해 병렬화가 어려움</li>
<li><strong>장기 의존성 문제</strong>
긴 문장에서 앞부분의 정보가 사라지거나 약해져서 의미가 제대로 학습되지 않음</li>
</ul>
<hr />
<h2 id="rnn-기반-seq2seq">RNN 기반 Seq2Seq</h2>
<h3 id="개념-1">개념</h3>
<p>RNN 기반의 seq2seq는 입력 시퀀스를 받아 출력 시퀀스로 변환하는 문제이다. </p>
<p>기계번역이나 요약을 수행하였다. </p>
<h3 id="구조-1">구조</h3>
<p><strong>인코더</strong>
: 입력 문장을 하나의 벡터로 인코딩
<strong>디코더</strong>
: 그 벡터를 바탕으로 출력 문장을 한 단어씩 생성</p>
<p><code>&quot;나는 밥을&quot;</code> -&gt; [인코딩] -&gt; <code>I ate rice</code></p>
<h3 id="한계-정보의-병목">한계: 정보의 병목</h3>
<p>인코더의 마지막 은닉 상태가 정보의 병목이 발생한다. </p>
<p>디코더는 인코더의 마지막 은닉 상태만 참조해서 입력으로 출력을 만들어내기 때문에 전체 입력 시퀀스의 의미가 담겨야 한다. </p>
<p>시퀀스가 길어지면 고정된 하나의 context vector로 압축하는데 시작 부분의 정보가 손실이 된다. </p>
<blockquote>
<p>시작 단어들의 의미가 뒤로 갈수록 희미해지고, 출력에 반영되지 않게 된다.</p>
</blockquote>
<hr />
<p>시퀀스-투-시퀀스는 인코더-디코더의 프레임워크의 초기 형태이다. </p>
<p>인코더-디코더 프레임워크는 시퀀스-투-시퀀스 문제를 해결하기 위한 하나의 구조 또는 <strong>전략적인 방법</strong> 중의 하나이다.</p>
<hr />
<h2 id="인코더-디코더-프레임워크">인코더-디코더 프레임워크</h2>
<h3 id="개념-2">개념</h3>
<p>하나의 입력 시퀀스를 받아서, 의미 있는 벡터로 인코딩하고 이를 바탕으로 새로운 출력 시퀀스를 생성하는 구조이다.</p>
<h3 id="구조-2">구조</h3>
<ul>
<li><p><strong>인코더 (문장의 의미를 요약)</strong>
: 입력 시퀀스의 정보를 마지막 은닉 상태라는 고정된 형태의 context vector로 압축한다. </p>
</li>
<li><p><strong>디코더 (단어를 한 개씩 예측)</strong>
: 인코더가 만든 벡터를 입력으로 받아 출력 시퀀스를 생성한다. </p>
</li>
</ul>
<p><code>입력 시퀀스 -&gt; [인코더] -&gt; context vector -&gt; [디코더] -&gt; 출력 시퀀스</code></p>
<h3 id="인코더">인코더</h3>
<ul>
<li>입력: <code>나는 밥을</code></li>
<li>출력: <code>context vector (하나의 의미 벡터 또는 여러 hidden states)</code></li>
</ul>
<h3 id="디코더">디코더</h3>
<p>매 timestep마다 다음 단어를 예측한다. 
예측한 단어를 다시 다음 예측의 입력으로 사용한다. </p>
<hr />
<h2 id="rnn-seq2seq-vs-인코더-디코더-프레임워크">RNN Seq2Seq VS 인코더-디코더 프레임워크</h2>
<blockquote>
<p><strong>RNN Seq2Seq는 인코더-디코더 프레임워크의 한 구현이다.</strong></p>
</blockquote>
<table>
<thead>
<tr>
<th>구분</th>
<th>RNN 기반 Seq2Seq</th>
<th>인코더-디코더 프레임워크</th>
</tr>
</thead>
<tbody><tr>
<td>💡 개념</td>
<td>인코더-디코더 구조를 RNN으로 구현한 방식</td>
<td>입력→출력 변환을 위한 전체 구조 (개념/틀)</td>
</tr>
<tr>
<td>🧱 구성 요소</td>
<td>RNN 인코더 + RNN 디코더</td>
<td>인코더 + 디코더 (모델 구조에 따라 RNN, LSTM, Transformer 등 다양하게 구성 가능)</td>
</tr>
<tr>
<td>🏗️ 관계</td>
<td>구현체 (방법)</td>
<td>구조적 프레임워크 (틀)</td>
</tr>
<tr>
<td>📌 예시</td>
<td>LSTM Seq2Seq, GRU Seq2Seq</td>
<td>RNN Seq2Seq, Transformer, BERT2GPT 등 다양한 모델 포함 가능</td>
</tr>
</tbody></table>
<ul>
<li>인코더-디코더 프레임워크는 = &quot;자동차의 틀&quot;</li>
<li>RNN Seq2Seq = &quot;엔진을 RNN을 쓴 자동차&quot;</li>
</ul>
<p><strong>RNN 기반의 Seq2Seq</strong>
<code>입력 시퀀스 → [RNN 인코더] → context vector → [RNN 디코더] → 출력 시퀀스</code></p>
<p><strong>Transformer 기반의 Seq2Seq</strong>
<code>입력 시퀀스 → [Transformer 인코더] → 인코더 출력들 → [Transformer 디코더 (with attention)] → 출력 시퀀스</code></p>
<hr />
<h2 id="attention-메커니즘">Attention 메커니즘</h2>
<p>입력시퀀스에서 <strong>은닉 상태를 만들지 않고</strong>, 스텝마다 인코더에서 디코더가 참고할 은닉 상태를 출력한다. </p>
<p><strong>디코더</strong>가 <strong>인코더의 모든 은닉 상태에 접근</strong>한다. </p>
<p>모든 상태를 동시에 사용하기 위해서 <strong>어떤 상태를 먼저 사용할지 우선순위</strong>를 정한다.</p>
<h3 id="개념-3">개념</h3>
<p>디코더가 단순히 하나의 벡터(context vector)에만 의존하는 대신, <strong>입력의 모든 단어(hidden state)</strong> 를 <strong>중요도</strong>에 따라 동적으로 활용한다. </p>
<h3 id="구조-3">구조</h3>
<p><strong>1. 중요도 계산</strong>
디코더가 현재 hidden state와 인코더의 각 단어 hidden state를 dot product해서 유사도를 계산한다.
<code>유사도 = 디코더 hidden × 인코더 hidden</code></p>
<p><strong>2. softmax로 정규화</strong>
계산된 중요도들을 softmaxt함수에 넣어서 attention score를 얻는다.
<code>softmax -&gt; 각 인코더 단어가 얼마나 중요한지 비율을 표현</code></p>
<p><strong>3. weighted sum</strong>
인코더의 각 hidden state에 2에서 구한 attention score를 곱해서 모두 더해 하나의 새로운 벡터 attetion context vecotr를 생성한다. 
<code>context vector = Σ (score_i × encoder_hidden_i)</code></p>
<p><strong>4. 디코더에게 전달</strong>
attention context vector를 디코더의 입력에 같이 넣어서 다음 단어 예측에 사용한다. </p>
<p>문장이 길어져도 timestep마다 중요한 단어를 골라서 참고가 가능하다.</p>
<h3 id="해결">해결</h3>
<ul>
<li>디코더가 예측할 때, 인코더의 모든 단어를 다시 참고한다.  </li>
<li>중요한 단어에 가중치를 주는 방식이다.<blockquote>
<p>인코더의 정보를 다 볼 수 있으면서 <strong>정보의 손실/병목 문제가 해결</strong>되었다. </p>
</blockquote>
</li>
</ul>
<p>하지만, 
여전히 순차적으로 데이터를 처리함으로 병렬 처리가 불가능하다는 단점이 있다. </p>
<h3 id="한계--디코더의-특성순차적-처리">한계 : 디코더의 특성(순차적 처리)</h3>
<p>디코더는 이전 단어의 결과를 기반으로 다음 단어를 예측하기 때문에 단어를 하나씩 순서대로 생성할 수 밖에 없다. </p>
<ul>
<li><p>일반 Attention은 인코더의 모든 은닉 상태를 참고할 수 있게 해주긴 하지만,</p>
</li>
<li><p>디코더가 <strong>자기 자신이 이전에 생성한 단어를 기반</strong>으로 작동하는 이상,</p>
</li>
<li><p>단어를 하나씩 순서대로 생성할 수밖에 없어 → <strong>순차적</strong></p>
</li>
</ul>
<hr />
<h2 id="self-attention">Self-Attention</h2>
<p>신경망의 같은 층에 있는 모든 상태에 대해서 어텐션을 작동시키는 방법이다. </p>
<h3 id="개념-4">개념</h3>
<p>한 문장의 각 단어가 자기 자신을 포함한 모든 단어들과 관계를 맺으면서, 그 관계(=유사도, 중요도)에 따라 자신을 더 풍부하게 표현하는 방법</p>
<blockquote>
<p><strong>같은 문장 내에서 단어들 간의 관계</strong>를 파악하는 것이 핵심이다.</p>
</blockquote>
<table>
<thead>
<tr>
<th>항목</th>
<th>일반 Attention</th>
<th>Self-Attention</th>
</tr>
</thead>
<tbody><tr>
<td>적용 위치</td>
<td>디코더가 인코더의 출력에 주의</td>
<td>문장 안에서 자기 자신 포함 모든 단어에 주의</td>
</tr>
<tr>
<td>관계 대상</td>
<td>디코더 ↔ 인코더</td>
<td>인코더 내 또는 디코더 내에서 단어들끼리</td>
</tr>
<tr>
<td>예시</td>
<td>&quot;나는 밥을&quot; → &quot;I ate rice&quot; (출력 예측 시 입력 참조)</td>
<td>&quot;나는 밥을 먹었다&quot; 안에서 &quot;나는&quot;이 &quot;먹었다&quot;를 주의</td>
</tr>
</tbody></table>
<h3 id="구조-4">구조</h3>
<p>각 토큰에 대해서 고정된 임베딩을 사용하는 대신 전체 시퀀스를 사용해 각 임베딩의 가중 평균을 구하는 것이 기본 개념이다. </p>
<p><strong>1. 각 단어(토큰)을 벡터로 변환</strong>
각각 임베딩된 벡터를 준비한다. 
<code>나는</code>, <code>밥을</code>, <code>먹었다.</code> -&gt; 각각의 임베딩</p>
<p><strong>2. Query, Key, Value로 변환</strong>
각 단어 벡터를 3가지로 분리한다. </p>
<ul>
<li>Query (Q): 내가 관심을 가지려는 기준</li>
<li>Key (K): 다른 단어가 가진 정보의 &quot;열쇠&quot;</li>
<li>Value (V): 최종적으로 참고할 정보<pre><code>나는 → Q1, K1, V1
밥을 → Q2, K2, V2
먹었다 → Q3, K3, V3</code></pre></li>
</ul>
<p><strong>3. 유사도 계산(Query, Key)</strong>
어텐션 점수를 유사도 함수를 사용해 Query와 Key가 서로 얼마나 관련되는지 계산한다. 
<code>Q1 • K1</code>, <code>Q1 • K2</code>, <code>Q1 • K3</code> (dot product=점곱)</p>
<p><code>sᵢⱼ = dot(Qᵢ, Kⱼ)</code></p>
<p>Query와 Key가 비슷하면 점곱 결과가 크다. 
어텐션 점수는 n개의 입력 토큰이 있는 시퀀스의 경우 크기가 nxn인 어텐션 점수 행렬이 만들어진다. </p>
<pre><code>         K1     K2     K3
       ┌─────┬─────┬─────┐
Q1 →   │ s11 │ s12 │ s13 │   ← &quot;나는&quot;이 각 단어를 얼마나 주목하는지
Q2 →   │ s21 │ s22 │ s23 │   ← &quot;밥을&quot;이 ...
Q3 →   │ s31 │ s32 │ s33 │   ← &quot;먹었다&quot;가 ...
       └─────┴─────┴─────┘
</code></pre><p><strong>4. softmax로 가중치 계산</strong>
점수들을 softmax로 정규화 -&gt; 총합이 1인 가중치
행마다 어떤 key(단어)를 주목하는지를 나타낸다.</p>
<pre><code>         K1      K2      K3
       ┌──────┬──────┬──────┐
Q1 →   │ 0.2  │ 0.5  │ 0.3  │  ← softmax of [s11, s12, s13]
Q2 →   │ 0.1  │ 0.6  │ 0.3  │  ← softmax of [s21, s22, s23]
Q3 →   │ 0.3  │ 0.3  │ 0.4  │  ← softmax of [s31, s32, s33]
       └──────┴──────┴──────┘
</code></pre><p><strong>5. Value들의 가중합</strong>
각 단어의 Value에 가중치를 곱해서 모두 더함 -&gt; 새로운 표현 벡터
<code>context₁ = 0.2 × V1 + 0.5 × V2 + 0.3 × V3</code>
각 행은 <strong>한 단어의 context vector를 생성할 때 쓰이는 가중치</strong>이다.</p>
<blockquote>
<p>즉, &quot;나는&quot;이라는 단어는
&quot;밥을&quot;, &quot;먹었다&quot;와의 관계를 계산해서
자기 자신을 다시 표현하게 됨</p>
</blockquote>
<h3 id="해결-1">해결</h3>
<p>전체 문장을 한번에 고려하여 단어 간 관계를 학습한다. </p>
<blockquote>
<p><strong>각 단어가 문장 내 다른 모든 단어들과의 관계를 계산해서, 그 단어만의 “관계 기반 가중치 세트”</strong>를 가지게 된다.
즉, 각 단어마다 <strong>자신 기준의 attention 가중치(= 한 행)</strong>가 생긴다.</p>
</blockquote>
<ul>
<li>하나의 벡터에 압축하려고 했던 것 -&gt; 모든 단어가 모든 단어를 보고 표현하면서 <strong>정보의 병목을 해결</strong></li>
<li>먼 단어 간의 정보가 약해짐 -&gt; 모든 단어가 모든 단어와 연결되어 <strong>장기 의존성을 해결</strong></li>
<li>순차적 처리만 가능 -&gt; Q, K, V 연산으로 <strong>병렬처리</strong>가 불가능했던 문제를 <strong>해결</strong></li>
</ul>
<p>self-attention을 통해서 순차적 데이터처리를 병렬처리가 가능하게 해결</p>
