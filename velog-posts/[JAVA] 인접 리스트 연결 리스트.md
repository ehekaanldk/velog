---
title: "[JAVA] 인접 리스트 연결 리스트"
date: "2025-06-05"
link: "https://velog.io/@ehekaanldk/JAVA-%EC%9D%B8%EC%A0%91-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8"
series: "Uncategorized"
---

<h2 id="인접-리스트-adjacency-list">인접 리스트 (Adjacency List)</h2>
<blockquote>
<p>그래프를 저장하는 방법 중 하나로 그래프의 연결 관계를 표현한다.
인접리스트는 배열 안에 리스트가 있는 구조이다. </p>
</blockquote>
<p>key-value 의 구조처럼 보일 수 있지만, 단순한 배열의 배열 구조이다. 
각 노드(키)에 연결된 노드들(값의 리스트)로 이해한다. </p>
<p>노드(정점) -&gt; 연결된 노드들의 리스트</p>
<p>노드 번호를 key처럼 사용하고,
연결된 노드들을 value값처럼 생각한다. </p>
<h2 id="인접-리스트-구현">인접 리스트 구현</h2>
<p><code>ArrayList&lt;Integer&gt;[]</code> 으로 자바에서 구현한다. </p>
<p>key-value 구조를 사용하고 싶을 때,
<code>HashMap&lt;Integer, List&lt;Integer&gt;&gt;</code> 을 사용하여 구현한다. </p>
<p>인접리스트는 배열 안에 리스트가 있는 구조이다. </p>
<pre><code>ArrayList&lt;Integer&gt;[] graph = new ArrayList[4];

// 예시 값:
graph[1] = [2, 3];
graph[2] = [1];
graph[3] = [1];
</code></pre><ul>
<li>배열의 인덱스를 key처럼 사용한다.</li>
<li>인접 리스트는 그래프에서 각 노드가 연결된 이웃 노드들을 효율적으로 저장할 수 있는 방식이다.</li>
<li>특히 연결이 적은 희소 그래프(sparse graph)에 유리하다.</li>
</ul>
<p><code>ArrayList&lt;Integer&gt;[] graph = new ArrayList[n + 1];</code>는  요소가 arraylist 인 배열을 만들기만 했을 뿐, null값들로 채워진 상태이다.
배열의 요소들을 ArrayList 객체임으로 실제 리스트 객체를 넣는 작업이 필요하다. </p>
<pre><code>  for (int i = 1; i &lt;= n; i++) {
    graph[i] = new ArrayList&lt;&gt;();
}
</code></pre><h2 id="비교">비교</h2>
<table>
<thead>
<tr>
<th>형태</th>
<th>사용 예</th>
<th>구조 설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>ArrayList&lt;Integer&gt;[]</code></td>
<td>DFS/BFS 자주 쓰임</td>
<td>인덱스가 &quot;키&quot; 역할, 값은 연결된 노드 리스트</td>
</tr>
<tr>
<td><code>Map&lt;Integer, List&lt;Integer&gt;&gt;</code></td>
<td>노드 번호가 복잡하거나 비연속적일 때</td>
<td>완전한 Key-Value 구조</td>
</tr>
</tbody></table>
<h2 id="연결-리스트-linked-list">연결 리스트 (Linked List)</h2>
<p>자료구조 자체로 리스트의 한 형태이다. 
데이터를 순서대로 저장하고 각 노드가 다음 노드를 가리키는 방식이다. </p>
<p><code>LinkedList&lt;Integer&gt;</code> 로 구현한다.</p>
