---
title: "[JAVA] 2차원 배열 정렬"
date: "2025-05-14"
link: "https://velog.io/@ehekaanldk/Java-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%A0%95%EB%A0%AC"
series: "Uncategorized"
---

<h2 id="정렬">정렬</h2>
<h2 id="1차원-배열에서의-정렬">1차원 배열에서의 정렬</h2>
<p><code>Arrays.sort()</code> 을 사용하여 손쉽게 정렬이 가능하다.</p>
<h2 id="2차원-배열에서의-정렬">2차원 배열에서의 정렬</h2>
<p><code>compare()</code> 함수를 구현해야 한다. 
2차원 배열의 각 요소를 비교하는 로직은 compare()함수로 두 배열의 요소를 비교하여 정렬 순서를 결정하는 역할을 한다. </p>
<p>첫 번쨰 열을 기준으로 오름차순으로 정렬하고, 첫 번째 열의 값이 같다면 두번 째 열을 기준으로 오름차순으로 정렬하는 방식으로 구현할 수 있다. </p>
<h3 id="comparator">comparator</h3>
<p>자바에서의 Arrays.sort()는 기본적으로 오름차순 정렬을 한다. 사용자 정의 기준이나 2차원 배열을 정렬하기 위해서는 정렬 기준을 의미하는 comparator를 지정해주어야 한다.</p>
<p><code>Arrays.sort(arr, comparator);</code></p>
<h3 id="람다식-사용">람다식 사용</h3>
<p>2차원 배열을 람다식을 사용하여 간단하게 정렬할 수 있다. </p>
<p>람다식 compare() 함수를 대체하여 정렬 기준을 명시적으로 표현한다. </p>
<p>*<em>comparator를 람다식으로 표현한 것
*</em>
<code>(a, b) -&gt; Integer.compare(a[0], b[0])</code></p>
<p>다음은 아래와 같은 의미이다. </p>
<pre><code>new Comparator&lt;int[]&gt;() {
    public int compare(int[] a, int[] b) {
        return Integer.compare(a[0], b[0]);
    }
}</code></pre><ul>
<li>a와 b는 각각의 2차원 배열의 한 행을 의미한다. (int[])</li>
<li>a[0], b[0]은 각 행의 첫번째 원소이다. </li>
<li>Integer.compare(a[0], b[0])는 두 값을 비교해서 정렬 기준 반환</li>
</ul>
<h3 id="compare">compare</h3>
<p>compare()함수는 x와 y를 비교해서 다음 값을 반환한다. </p>
<pre><code>Integer.compare(x, y) =&gt;

- 음수 → x &lt; y
- 0   → x == y
- 양수 → x &gt; y</code></pre><p>음수를 리턴하면 x 가 먼저
0을 리턴하면 순서 그대로
양수를 리턴하면 y가 먼저</p>
<h3 id="두-번째-열-기준-내림차순-정렬">두 번째 열 기준 내림차순 정렬</h3>
<p><code>Arrays.sort(arr, (a,b) -&gt; Integer.compare(b[1], a[1]));</code></p>
<p>arr에서 (a,b) 두개의 행에서 각각의 두 번째 요소 a[1], b[1] 를 오름차순으로 비교한다. 
내림차순으로 비교할 때는 b[1], a[1] 으로 작성한다. </p>
<h3 id="오름차순-vs-내림차순">오름차순 vs 내림차순</h3>
<table>
<thead>
<tr>
<th>정렬 기준</th>
<th>정렬 방향</th>
<th>코드 예시</th>
</tr>
</thead>
<tbody><tr>
<td>첫 번째 열</td>
<td>오름차순</td>
<td><code>(a, b) -&gt; Integer.compare(a[0], b[0])</code></td>
</tr>
<tr>
<td>첫 번째 열</td>
<td>내림차순</td>
<td><code>(a, b) -&gt; Integer.compare(b[0], a[0])</code></td>
</tr>
<tr>
<td>두 번째 열</td>
<td>오름차순</td>
<td><code>(a, b) -&gt; Integer.compare(a[1], b[1])</code></td>
</tr>
<tr>
<td>두 번째 열</td>
<td>내림차순</td>
<td><code>(a, b) -&gt; Integer.compare(b[1], a[1])</code></td>
</tr>
</tbody></table>
