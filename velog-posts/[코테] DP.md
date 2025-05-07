---
title: "[코테] DP"
date: "2025-05-06"
link: "https://velog.io/@ehekaanldk/%EC%BD%94%ED%85%8C-DP"
series: "Uncategorized"
---

<p>DP문제를 풀기 위한 사고 루틴</p>
<h3 id="1단계-dp문제인가">1단계. DP문제인가?</h3>
<blockquote>
<p>“문제를 풀기 위한 최적해(최소값/최대값/경우 수 등)가 이전 결과에 의존하는가?”</p>
</blockquote>
<ul>
<li>전체 문제를 작은 문제로 나누어서 풀 수 있는가?</li>
<li>이전 결과를 활용해 현재 상태를 계산하는가?</li>
<li>키워드 : 최대, 최소, 방법 수, 경우의 수, 경로 수 </li>
</ul>
<p>ex) 금액을 만들 수 있는 방법 수
&quot;N개의 선택 중 최대/최소값&quot;
&quot;어떤 방법의 수&quot;
&quot;경로의 수&quot;</p>
<h3 id="2단계-dp배열을-정의한다">2단계. DP배열을 정의한다.</h3>
<blockquote>
<p>dp[i]가 뭘 의미하는지 말로 설명할 수 있는가?</p>
</blockquote>
<ul>
<li><code>dp[i]</code>를 말로 정의한다.</li>
</ul>
<p>ex) <code>dp[i]</code> = i원을 만드는 경우의 수 
dp[i] = i번째 계단까지 올라오는 최대 점수
dp[i] = i원을 만들 수 있는 경우의 수
dp[i] = i번째까지 고려했을 때의 최대 점수
dp[i][j] = i번째 물건까지 고려해서 무게 j일 때의 최대 가치</p>
<h3 id="3단계-초기값은-무엇인가">3단계. 초기값은 무엇인가?</h3>
<blockquote>
<p>dp[0]은 뭘 의미하고, 몇이여야 하는가?</p>
</blockquote>
<ul>
<li>0이나 1로 시작하는 경우가 많다.</li>
<li><code>dp[0]=1</code>이면, 0원을 만드는 방법은 아무것도 사용하지 않는 1가지</li>
</ul>
<p>ex)
<code>dp[i] = dp[i-1] + dp[i-2]</code> (피보나치형)
<code>dp[i] = max(dp[i-1], dp[i-2] + score[i])</code> (선택형)
<code>dp[i] += dp[i - coin]</code> (누적형)</p>
<h3 id="4단계-점화식을-만든다">4단계. 점화식을 만든다.</h3>
<blockquote>
<p><code>dp[i]</code>가 어떻게 계산이 되는가?</p>
</blockquote>
<ul>
<li>가진 도구를 하나씩 사용한다. </li>
<li>이것을 마지막에 썼다고 생각하면? =&gt; 이전 값에서 시작된다. </li>
</ul>
<p>ex)
<code>dp[0]</code> = 1 → &quot;0원을 만드는 방법 1가지&quot;
<code>dp[0]</code> = 0 → &quot;0까지의 최댓값은 0&quot;</p>
<h3 id="5단계-반복-구조-설계">5단계. 반복 구조 설계</h3>
<blockquote>
<p>i를 어디서 부터 어디까지 돌려야 하는가?</p>
</blockquote>
<ul>
<li>경우의 수 : 도구(동전) 먼저 for문</li>
<li>순열까지 고려 : 금액 먼저 for문</li>
<li>한번씩만 쓸 수 있는 경우 : 뒤에서부터 순회</li>
</ul>
<p>단일 DP: for i in range(1, N+1)</p>
<p>다중 상태 (예: 배낭): for i in range(N), for w in range(W+1)</p>
<p>상태 압축 가능 여부도 판단 (1차원, 2차원)</p>
<h3 id="6단계-의미-확인">6단계. 의미 확인</h3>
<blockquote>
<p>dp[i] 값은 논리적으로 맞는가?</p>
</blockquote>
<ul>
<li>각 <code>dp[i]</code>에 어떤 값이 쌓이고 있는지 직접 구해본다.</li>
<li>예를 들어 dp[3] = 2라면,
&quot;3이라는 값이 두 가지 방법으로 만들어졌는가?&quot; 스스로 설명해보기</li>
</ul>
<h2 id="결론">결론</h2>
<blockquote>
<p>직접 손으로 작성해본다. 
dp 배열을 한 줄 적고, 어디에서 더해졌는지 추적한다. 
이래서 += 이다!</p>
</blockquote>
