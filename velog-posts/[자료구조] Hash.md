---
title: "[자료구조] Hash"
date: "2025-05-05"
link: "https://velog.io/@ehekaanldk/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-Hash"
series: "Uncategorized"
---

<h2 id="1-hash">1. Hash</h2>
<p>HASH는 우편함과 같다. 
친구에게 편지를 보내고 싶을 때, 친구의 집 우편함 번호를 알고 있다면 쉽게 편지를 넣을 수 있는 것처럼 hash는 이름-&gt;우편함 위치 를 빠르게 찾는 방법이다. </p>
<blockquote>
<p>키(key)를 기반으로 데이터를 빠르게 찾기 위한 구조</p>
</blockquote>
<p>Hash는 데이터를 빠르게 검색하거나 저장하기 위해 사용하는 자료구조이다. 
어떤 키(key) 값을 특정한 주소(인덱스)로 바꾸어주는 방식이다. </p>
<p>리스트에서는 값을 찾기 위해서는 하나하나 다 비교해서 찾아야 한다. 
해시에서는 바로 해당 위치로 이동해서 찾을 수 있어서 시간복잡도가 O(1)이 된다.</p>
<h2 id="2-hash-function">2. Hash Function</h2>
<p>임의의 길이를 갖는 임의의 데이터를 고정한 길이의 데이터로 매핑하는 단방향 함수이다. </p>
<blockquote>
<p>키(key)를 숫자(인덱스)로 바꾸는 함수</p>
</blockquote>
<p>예를 들어 어떤 숫자를 10으로 나누었을 때의 그 나머지를 구하는 함수도 해시함수이다. </p>
<p>해시 함수는 보통 입력의 범위(정의역)보다 출력값의 범위(치역)가 작아서 서로 다른 입력값에도 동일한 값이 출력되는 경우가 존재하고 이를 충돌이라고 한다.</p>
<h2 id="3-구성요소">3. 구성요소</h2>
<ol>
<li>Key : 이름표</li>
<li>Value : 실제 데이터</li>
<li>Hash Function : 키를 숫자로 바꾸는 계산식</li>
<li>배열 : 데이터를 저장하는 고정된 크기의 저장 공간</li>
</ol>
<h2 id="4-해시-충돌collision">4. 해시 충돌(collision)</h2>
<blockquote>
<p>서로 다른 키가 같은 숫자(인덱스)가 나오는 현상</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/50cd0d89-eb2e-4ab6-adc8-c2b3d5ec6520/image.png" /></p>
<h3 id="해결방법">해결방법</h3>
<ul>
<li>체이닝 : 같은 칸에 여러 값을 linkedlist처럼 연결</li>
<li>오픈 어드레싱 : 빈 자리를 찾아서 다른곳에 저장
자바의 HashMap은 보통 체이닝 + 트리 구조로 충돌을 해결한다. </li>
</ul>
<h2 id="5-java에서-구현">5. Java에서 구현</h2>
<table>
<thead>
<tr>
<th>자료구조</th>
<th>특징</th>
<th>사용 목적</th>
</tr>
</thead>
<tbody><tr>
<td><strong>HashMap&lt;K, V&gt;</strong></td>
<td>키(K)와 값(V)을 한 쌍으로 저장</td>
<td>어떤 <strong>키로 값을 찾고 싶을 때</strong></td>
</tr>
<tr>
<td><strong>HashSet&lt;E&gt;</strong></td>
<td>값(E)만 저장 (중복 없음)</td>
<td><strong>중복 제거</strong>, 빠른 존재 확인</td>
</tr>
</tbody></table>
<h3 id="hashmap">HashMap</h3>
<p><code>HashMap&lt;String, Integer&gt; map = new HashMap&lt;&gt;()</code> 
으로 키만 해싱해서 키-값을 저장한다.
&lt;K, V&gt; 에서 K는 키의 타입, V는 값의 타입을 작성한다. </p>
<p><code>map.add(&quot;Key1&quot;, 100)</code> 으로 값을 추가한다.</p>
<p><code>map.get(&quot;Key1&quot;)</code> 으로 값을 조회한다. </p>
<p>보통 hash를 사용하는 문제는 문자열이 주어졌을 때, 가장 많이 등장한 문자와 횟수를 출력하는? </p>
<ul>
<li>문자열에서 중복 문자 세기</li>
<li>배열에서 중복 숫자 제거</li>
</ul>
<h3 id="hashset">HashSet</h3>
<p><code>HashSet&lt;String&gt; set = new HashSet&lt;&gt;()</code>으로 값을 키처럼 해싱해서 저장한다. 중복 없이 값이 있는지 확인할 때 사용한다. </p>
<h3 id="주요함수">주요함수</h3>
<table>
<thead>
<tr>
<th>함수</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>add(E element)</code></td>
<td>요소 추가</td>
</tr>
<tr>
<td><code>remove(Object o)</code></td>
<td>요소 제거</td>
</tr>
<tr>
<td><code>contains(Object o)</code></td>
<td>요소가 있는지 확인 (true/false)</td>
</tr>
<tr>
<td><code>isEmpty()</code></td>
<td>비어 있는지 확인</td>
</tr>
<tr>
<td><code>size()</code></td>
<td>요소 개수 반환</td>
</tr>
<tr>
<td><code>clear()</code></td>
<td>모든 요소 삭제</td>
</tr>
<tr>
<td><code>iterator()</code></td>
<td>반복자 반환 (for-each 가능)</td>
</tr>
</tbody></table>
<table>
<thead>
<tr>
<th>함수</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>put(K key, V value)</code></td>
<td>키-값 쌍 저장</td>
</tr>
<tr>
<td><code>get(Object key)</code></td>
<td>키에 해당하는 값 가져오기</td>
</tr>
<tr>
<td><code>remove(Object key)</code></td>
<td>키-값 쌍 삭제</td>
</tr>
<tr>
<td><code>containsKey(Object key)</code></td>
<td>특정 키가 있는지 확인</td>
</tr>
<tr>
<td><code>containsValue(Object value)</code></td>
<td>특정 값이 있는지 확인</td>
</tr>
<tr>
<td><code>isEmpty()</code></td>
<td>비어 있는지 확인</td>
</tr>
<tr>
<td><code>size()</code></td>
<td>키-값 쌍 개수</td>
</tr>
<tr>
<td><code>clear()</code></td>
<td>모든 내용 삭제</td>
</tr>
<tr>
<td><code>keySet()</code></td>
<td>키들만 모은 Set 반환</td>
</tr>
<tr>
<td><code>values()</code></td>
<td>값들만 모은 Collection 반환</td>
</tr>
<tr>
<td><code>entrySet()</code></td>
<td>키-값 쌍을 모두 가져오는 Set (for-each용)</td>
</tr>
<tr>
<td><code>getOrDefault(K key, V defaultVal)</code></td>
<td>값이 없을 경우 기본값 반환</td>
</tr>
</tbody></table>
<h3 id="주의">주의</h3>
<p>HashSet과 HashMap은 순서를 보장하지 않는 자료구조이다. </p>
<p>인덱스 접근이 필요한 경우 =&gt; list, array가 적합</p>
<p>내부적으로 해시테이블 구조를 사용하기 때문에 
요소를 배열의 특정 인덱스가 아니라
해시 함수로 계산된 위치에 저장한다. </p>
<p>순서를 보장하지 않는 자료구조에서는 &quot;빠른 접근&quot;이 핵심이다. </p>
<ol>
<li>중복제거 
<code>HashSet&lt;E&gt;</code> 에서 
add() 값 추가(중복은 무시), contains() 값이 있는지 확인, remove() 값 삭제<pre><code>String[] names = {&quot;철수&quot;, &quot;영희&quot;, &quot;철수&quot;, &quot;민수&quot;};
</code></pre></li>
</ol>
<p>HashSet uniqueNames = new HashSet&lt;&gt;();
for (String name : names) {
    uniqueNames.add(name);  // 중복된 &quot;철수&quot;는 한 번만 저장됨
}
System.out.println(uniqueNames);  // 중복 없이 출력</p>
<pre><code>2. 값의 개수 세기
```HashMap&lt;K,V&gt;```에서 
put(k, v)로 값 설정 및 갱신, get(k) 값 가져오기, getOrDefault(K key, defaultVal) 키가 없으면 기본값 반환</code></pre><p>HashMap&lt;String, Integer&gt; countMap = new HashMap&lt;&gt;();
String[] words = {&quot;apple&quot;, &quot;banana&quot;, &quot;apple&quot;};</p>
<p>for (String word : words) {
    countMap.put(word, countMap.getOrDefault(word, 0) + 1);
}
System.out.println(countMap);  // {apple=2, banana=1}</p>
<pre><code>

3. 빠른 검색
```HashSet&lt;E&gt;``` 또는 ```HashMap&lt;K, V&gt;```

hashset에서 ```contains(value)```
hastmap에서 ```containsKey(key), containsValue(value)```

</code></pre><p>HashSet blockedUsers = new HashSet&lt;&gt;();
blockedUsers.add(&quot;baduser123&quot;);</p>
<p>if (blockedUsers.contains(&quot;baduser123&quot;)) {
    System.out.println(&quot;접근 차단!&quot;);
}</p>
<pre><code>4. 값 저장
```HashMap&lt;K, V&gt;```
</code></pre><p>HashMap&lt;String, Integer&gt; scores = new HashMap&lt;&gt;();
scores.put(&quot;철수&quot;, 90);
scores.put(&quot;영희&quot;, 85);</p>
<p>System.out.println(scores.get(&quot;철수&quot;));  // 90 출력</p>
<pre><code>
</code></pre>
