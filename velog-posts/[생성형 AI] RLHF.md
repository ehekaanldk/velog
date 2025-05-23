---
title: "[생성형 AI] RLHF"
date: "2025-05-22"
link: "https://velog.io/@ehekaanldk/%EC%83%9D%EC%84%B1%ED%98%95-AI-RLHF"
series: "Uncategorized"
---

<h2 id="rlhfreinforcement-learning-from-human-feedback">RLHF(Reinforcement Learning from Human Feedback)</h2>
<blockquote>
<p>사람이 좋은 답변을 골라주고, 그걸 기준으로 AI를 더 똑똑하게 만드는 방법</p>
</blockquote>
<p>🔍 기존 강화학습의 한계</p>
<ul>
<li>보상을 주기 어렵거나 명확하지 않을 때 비효율적이다.</li>
<li>에이전트가 무수히 많은 랜덤한 액션을 하고 우연히 좋은 경험을 획득 =&gt; 학습이 느리고, 안정성 떨어짐</li>
</ul>
<p>🔍 왜 인간의 주관적인 피드백을 구지 받아야 하는가?</p>
<ul>
<li>LLM은 정답이 없는 열린 질문에 대응해야 한다. </li>
<li>전통적인 학습 방식만으로는 '사람이 진짜 원하는 답변'을 만들기 어렵다.</li>
<li>언어모델이 답변을 잘못 배울 수 있다. </li>
<li>사람의 주관적인 선호(preference) 가 가장 믿을 수 있는 보상 신호가 된다.</li>
</ul>
<h2 id="rlhf의-과정">RLHF의 과정</h2>
<h3 id="1-supervised-fine-tuningsft">1. Supervised Fine-Tuning(SFT)</h3>
<ul>
<li>지도학습 기반의 파인튜닝으로 기본 언어 모델을 파인튜닝</li>
<li>사람이 진짜로 선호하는 응답인지에 대한 지표가 충분히 반영되지 않음</li>
</ul>
<h3 id="2-reward-model-학습">2. Reward Model 학습</h3>
<ul>
<li>하나의 질문에 대해 AI가 만든 <strong>여러 응답</strong>을 사람에게 보여준다.</li>
<li>사람이 A vs B 중 더 <strong>적절하거나 선호되는 응답</strong>을 선택한다. (Pair 방식) =&gt; HF</li>
<li>이 데이터를 바탕으로 <strong>보상 점수를 예측하는 모델(Reward model)</strong>을 학습</li>
</ul>
<p>📌 추가 개념:</p>
<ul>
<li><p>일대일에 대한 결과를 기반으로 여러 응답들 간의 상대적 순위를 학습한다. 
=&gt; ranking function 형태의 reward 모델이 학습된다.</p>
</li>
<li><p>기존의 RL은 정답이 정해진 문제</p>
</li>
<li><p>기존의 RL과 달리 &quot;명확한 정답은 없지만 좋은 쪽을 고를 수는 있다.&quot; 가 반영된다.</p>
</li>
<li><p>응답 생성에 대한 휴먼 피드백의 리워드를 제시하면서 강화학습을 통한 파인튜닝이 가능해진다.</p>
</li>
</ul>
<h3 id="3-ppoproximal-policy-optimization">3. PPO(Proximal Policy Optimization)</h3>
<blockquote>
<p>강화학습의 한 알고리즘으로 , Reward model의 보상 점수를 기준으로 언어모델을 업데이트한다.</p>
</blockquote>
<table>
<thead>
<tr>
<th>구성 요소</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Action</strong></td>
<td>언어 모델(Agent)이 생성한 응답</td>
</tr>
<tr>
<td><strong>Reward</strong></td>
<td>Reward Model이 부여한 응답 품질 점수</td>
</tr>
<tr>
<td><strong>Update</strong></td>
<td>더 높은 보상을 받은 응답을 <strong>더 자주 생성하도록</strong> 언어 모델의 파라미터를 조정</td>
</tr>
</tbody></table>
<p>PPO는 기존의 방식에서 너무 벗어나지 않도록 조심조심 조절하는 강화학습 알고리즘이다.
&quot;변화는 하되, 너무 멀리 벗어나지 말자&quot;</p>
<h2 id="정리">정리</h2>
<p>RLHF는 주관적인 기준(예: 공감, 정중함, 창의성 등)을 반영하기에 매우 유용하다.</p>
<p>하지만 비용(휴먼 피드백 수집) 과 안정성 문제(PPO 학습 불안정) 가 있어,
최근에는 대체 방식으로 DPO (Direct Preference Optimization) 도 많이 사용되고 있다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/6bb93e5a-0af7-4388-aab2-01d23f75e98d/image.png" /></p>
<table>
<thead>
<tr>
<th>구성요소</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Environment</strong></td>
<td>언어모델이 응답을 생성하는 대화 상황</td>
</tr>
<tr>
<td><strong>RL Algorithm</strong></td>
<td>PPO와 같은 강화학습 알고리즘</td>
</tr>
<tr>
<td><strong>Action</strong></td>
<td>언어모델이 생성한 문장 또는 응답</td>
</tr>
<tr>
<td><strong>Observation</strong></td>
<td>환경에서 받은 정보 (질문이나 맥락)</td>
</tr>
<tr>
<td><strong>Reward Predictor</strong></td>
<td>사람이 더 좋아한 응답을 기반으로 학습된 <strong>Reward Model</strong></td>
</tr>
<tr>
<td><strong>Human Feedback</strong></td>
<td>사람의 선택(더 좋은 응답)을 통해 보상을 학습시킴</td>
</tr>
<tr>
<td><strong>Predicted Reward</strong></td>
<td>언어모델의 응답에 대해 보상 점수를 예측</td>
</tr>
</tbody></table>
<h2 id="추가">추가</h2>
<h3 id="강화학습">강화학습</h3>
<blockquote>
<p>Action을 하면 Reward를 받고, 그 Reward를 최대화하는 방향으로 스스로 학습하는 AI</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/2d72943f-4ff7-448c-a5b1-3a02791ff287/image.png" /></p>
<table>
<thead>
<tr>
<th>구성요소</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Agent</strong></td>
<td>학습 대상 (AI, 로봇, 챗봇 등)</td>
</tr>
<tr>
<td><strong>Environment</strong></td>
<td>행동 결과가 나타나는 세계 (게임, 시뮬레이션, 대화 등)</td>
</tr>
<tr>
<td><strong>Action</strong></td>
<td>에이전트가 하는 선택 (움직이기, 말하기 등)</td>
</tr>
<tr>
<td><strong>Reward</strong></td>
<td>행동의 결과로 받는 점수</td>
</tr>
<tr>
<td><strong>Observation (State)</strong></td>
<td>환경에서 받은 현재 상황 정보</td>
</tr>
</tbody></table>
<p>Agent는 보상을 많이 받을 수 있는 행동을 경험으로 학습하게 된다. </p>
<h3 id="rl-vs-rlhf">RL vs RLHF</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>일반 강화학습</th>
<th>RLHF</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Reward 제공자</strong></td>
<td>환경 자체가 보상 제공</td>
<td>사람이 선호도를 기준으로 보상 학습</td>
</tr>
<tr>
<td><strong>Reward 형태</strong></td>
<td>점수나 성공/실패 신호</td>
<td>사람이 고른 &quot;더 좋은 응답&quot;</td>
</tr>
<tr>
<td><strong>학습 방식</strong></td>
<td>명확한 보상 기준</td>
<td>모호한 기준을 인간이 직접 판단</td>
</tr>
<tr>
<td><strong>Reward Model 존재 여부</strong></td>
<td>없음 (환경이 직접 보상)</td>
<td>✅ 있음 (예측기 필요)</td>
</tr>
</tbody></table>
