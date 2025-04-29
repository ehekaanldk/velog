---
title: "[자료구조] Heap"
date: "2025-04-26"
link: "https://velog.io/@ehekaanldk/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-Heap"
series: "Uncategorized"
---

<h2 id="1-heap">1. Heap</h2>
<p>힙은 특별한 규칙을 가진 트리 모양 자료구조이다.</p>
<p>값을 정렬된 상태로 유지하는 이진 트리 구조이다. </p>
<blockquote>
<p>빠르게 가장 큰값이나 가장 작은값을 뽑아야 할 때 쓰는 자료구조이다.</p>
</blockquote>
<hr />
<h2 id="2-heap의-종류">2. Heap의 종류</h2>
<p>최대 힙 : <strong>부모 노드</strong>가 항상 자식 노드보다 <strong>크다.</strong> =&gt; 제일 큰값이 root
최소 힙 : <strong>부모 노드</strong>가 항상 자식 노드보다 <strong>작다.</strong> =&gt; 제일 작은값이 root
<img src="https://velog.velcdn.com/images/ehekaanldk/post/4aa49802-912a-4716-8fa9-287cf975ba35/image.png" width="600px" /></p>
<hr />
<h2 id="3-heap의-특징">3. Heap의 특징</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>레벨(Level) i</td>
<td>위에서부터 층수. 0층, 1층, 2층... 숫자 세는 것</td>
</tr>
<tr>
<td>높이(Height) h</td>
<td>트리 전체가 몇 층짜리냐. 맨 아래까지 몇 층 있냐</td>
</tr>
</tbody></table>
<h3 id="31-완전-이진-트리--왼쪽부터-꽉-채운-트리">3.1. 완전 이진 트리 =&gt; 왼쪽부터 꽉 채운 트리</h3>
<p>노드를 추가하거나 삭제할 때, 항상 아래쪽부터 꽉 채운다. 
마지막 층은 꽉 안 찰 수 있다. 
높이가 최소화된다.</p>
<p>마지막 층을 제외하고는 꽉 채운다. =&gt; $$2^h -1$$ (h는 높이)
마지막 층을 제외하고는 각 층 i마다 $$2^i$$ </p>
<h3 id="32-heap의-높이는-olog-n">3.2. heap의 높이는 O(log N)</h3>
<p>한 층 내려갈 때마다 노드의 수는 2개로 늘어난다. (지수함수)</p>
<ul>
<li>0층 =&gt; 노드 1개</li>
<li>1층 =&gt; 노드 2개</li>
<li>2층 =&gt; 노드 4개</li>
<li>3층 =&gt; 노드 8개</li>
</ul>
<p>반대로 전체 노드가 N이면,  $$2^0 + 2^1 + 2^2 + ... + 2^h$$ 이다.
$$N ≈ 2^h$$  으로 양쪽에 로그를 취해서 $$h ≈ log₂(N)$$</p>
<p>힙에서의 높이가 $$log₂(N)$$ 이고 삽입하거나 삭제하는 연산은 높이 만큼 위 아래로 이동해야 한다. 
시간이 걸리는 정도를 표현한 단위인 O()에 넣어서 $$O(log N)$$ 으로 작성한다.</p>
<hr />
<h2 id="4-heap의-연산">4. Heap의 연산</h2>
<h3 id="삽입-연산-">삽입 연산 :</h3>
<p>새로운 요소가 들어오면 맨 마지막에 삽입한다.
삽입 후 새로운 요소를 부모 노드들과 교환해서 위로 올라간다.
힙의 성질을 만족한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/6c1b4120-c071-4f6e-b9d9-6147412d79e9/image.gif" /></p>
<h3 id="삭제-연산-">삭제 연산 :</h3>
<p>항상 먼저 루트 요소를 삭제한다.
삭제 후 맨 마지막 노드를 루트로 올린다.
자식 노드들과 교환해서 아래로 내려간다.
힙의 성질을 만족한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ec2fd072-cf9a-4ea7-bb9c-2e7052b53a58/image.gif" /></p>
<p>Q. 중간의 값을 삭제하고 싶으면 중간을 삭제하는가?
A. 힙은 맨 위의 root만 삭제가 가능하고, 중간의 값을 골라서 삭제하는 것은 힙 규칙에 어긋난다. </p>
<blockquote>
<p>힙은 단지 자식&gt;=부모, 부모&gt;=자식 의 규칙을 준수할 뿐 중간 값이 어디인지는 규칙이 없다.</p>
</blockquote>
<p>Q. 그러면 삭제한 루트자리에 삭제하고 싶은 중간의 값을 올리는가?
A. 항상 루트를 삭제하고 맨 마지막 노드를 올린다. 힙은 값을 기준으로 움직이지 않고 구조를 유지해야한다.</p>
<blockquote>
<p>트리처럼 보이지만 큐처럼 하나씩 빠져나가는 구조</p>
</blockquote>
<hr />
<h2 id="5-heap의-구현">5. Heap의 구현</h2>
<h3 id="51-배열을-이용한-구현">5.1. 배열을 이용한 구현</h3>
<p>완전이진트리 =&gt; 각 노드에 번호를 붙인다. =&gt; 배열의 인덱스</p>
<p>루트노드의 인덱스         = <code>0</code>
왼쪽 자식노드의 인덱스    = <code>(부모의 인덱스)*2</code>
오른쪽 자식노드의 인덱스     = <code>(부모의 인덱스)*2 +1</code>
부모의 인덱스 = <code>(자식의 인덱스)/2</code></p>
<h3 id="52-우선순위-큐를-사용한-구현java">5.2. 우선순위 큐를 사용한 구현(java)</h3>
<pre><code>PriorityQueue&lt;Integer&gt; heap = new PriorityQueue&lt;&gt;(); // 기본은 최소 힙
PriorityQueue&lt;Integer&gt; maxHeap = new PriorityQueue&lt;&gt;(Comparator.reverseOrder()); // 최대 힙</code></pre>
