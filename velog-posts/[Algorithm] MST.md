---
title: "[Algorithm] MST"
date: "2025-04-18"
link: "https://velog.io/@ehekaanldk/Algorithm-MST"
series: "Uncategorized"
---

<h2 id="mst">MST</h2>
<p>MST는 모든 지점을 가장 적은 비용(minimize)으로 연결(spanning)하는 방법(tree)이다. </p>
<blockquote>
<p>목표 : 도로나 인터넷 망을 모든 마을을 서로 연결하기 위함이다. 이때 공사비용도 적게 들여서 연결</p>
</blockquote>
<p>tree의 의미 자체가 사이클(빙글빙글 도는 것) 없이 모든 점이 하나로 이어져 있는 구조이다. </p>
<p>MST는 가장 싸게 연결하는 트리를 의미한다. </p>
<ul>
<li>모든 장소 연결 ⇒ 선(node)과 비용(weight)을 가장 적게</li>
</ul>
<p>MST를 구하기 위한 방법에는 대표적인 2가지 알고리즘</p>
<ul>
<li>크루스칼 알고리즘</li>
<li>프림 알고리즘</li>
</ul>
<hr />
<h3 id="크루스칼-알고리즘">크루스칼 알고리즘</h3>
<p>전체 지도를 먼저 보고, 가장 싼 길부터 선택한다. </p>
<ul>
<li>도구 : union-find<ul>
<li>그룹 : 이미 서로 연결된 마을의 모임</li>
<li>Find : “이 마을이 어떤 그룹에 속해 있는가?” (=같은 그룹인가?)</li>
<li>Union :  “아직 다른 그룹이라면, 하나의 그룹으로 합친다!”</li>
</ul>
</li>
<li>사용법<ul>
<li><ol>
<li>모든 도로를 가격순으로 정렬한다. (제일 싼 도로부터 보기 쉽게!)</li>
</ol>
</li>
<li><ol start="2">
<li>싼 도로부터 하나씩 고른다.</li>
</ol>
</li>
<li><ol start="3">
<li>그 도로를 골랐을 때
a. 만약 이미 연결된 마을끼리 다시 연결된다면 ❌ (사이클!)
 b. 아니면 연결 ✅</li>
</ol>
</li>
<li><ol start="4">
<li>모든 마을이 다 연결될 때까지 반복</li>
</ol>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="프림-알고리즘">프림 알고리즘</h3>
<p>아무 지점이나 잡고, 거기서부터 주변으로 확장해간다.</p>
<ul>
<li><p>도구 : 우선순위 큐</p>
<ul>
<li>큐의 우선순위가 있는 것으로 가중치가 우선순위가 된다.</li>
<li>큐에 연결할 수 있는 마을들의 (비용, 목적지)를 넣는다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a8e0741c-977f-419e-875e-a6b75b96ed5d/image.png" /></li>
</ul>
</li>
<li><p>사용법</p>
<ul>
<li><ol>
<li>아무 마을을 하나 시작점으로 정한다.</li>
</ol>
</li>
<li><ol start="2">
<li>그 마을과 연결된 도로 중에서 가장 싼 도로를 고른다. </li>
</ol>
</li>
<li><ol start="3">
<li>그 도로를 통해 연결된 마을을 새로 그룹에 추가한다.</li>
</ol>
</li>
<li><ol start="4">
<li>연결된 마을 전체에서 주변 마을로 가는 도로 중에서 가장 싼 것을 고른다. </li>
</ol>
</li>
<li><ol start="5">
<li>모든 마을이 연결될 때까지 반복</li>
</ol>
</li>
</ul>
</li>
</ul>
