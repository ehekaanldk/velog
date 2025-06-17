---
title: "[Algorithm] 이진탐색"
date: "2025-06-13"
link: "https://velog.io/@ehekaanldk/Algorithm-%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89"
series: "Uncategorized"
---

<h2 id="이진탐색">이진탐색</h2>
<blockquote>
<p>이진탐색/이분탐색은 <strong>정렬된 배열</strong>를 전체로 중간값을 기준으로 탐색 범위를 반씩 줄여가며 원하는 값을 찾는 알고리즘</p>
</blockquote>
<ul>
<li>탐색 범위를 절반씩 줄여나간다. </li>
<li>선형탐색에 비해 빠른 속도를 보장한다. </li>
</ul>
<h3 id="이진탐색의-조건">이진탐색의 조건</h3>
<ul>
<li>배열이 정렬되어 있어야 한다</li>
<li>오름차순 또는 내림차순으로 정렬되어야 한다.</li>
<li>정렬되지 않은 경우 정렬 작업이 필요하다.</li>
</ul>
<p>선형탐색
배열이나 리스트와 같은 데이터 구조에서 특정한 값을 찾는 알고리즘 중 하나이다.</p>
<h2 id="이진탐색-특징">이진탐색 특징</h2>
<table>
<thead>
<tr>
<th>항목</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>시간복잡도</td>
<td><strong>O(log n)</strong> (매번 탐색 범위를 반으로 줄임)</td>
</tr>
<tr>
<td>공간복잡도</td>
<td><strong>O(1)</strong> (재귀를 사용하지 않을 경우)</td>
</tr>
<tr>
<td>사용 조건</td>
<td>데이터가 반드시 <strong>정렬</strong>되어 있어야 함</td>
</tr>
<tr>
<td>활용 예</td>
<td>정렬된 배열 탐색, 파라메트릭 서치, lower_bound / upper_bound</td>
</tr>
</tbody></table>
<ul>
<li>for문 배열 전체를 순회하면서 값을 찾는다. </li>
<li>이진 탐색은 중간값을 찾아서 탐색 범위를 반으로 줄이면서 값을 찾는다. </li>
</ul>
<h2 id="이진탐색의-과정">이진탐색의 과정</h2>
<p><strong>arr = [1, 3, 5, 7, 9, 11, 13]에서 9를 찾는 과정</strong></p>
<ol>
<li><p>시작 인덱스 low = 0</p>
</li>
<li><p>끝 인덱스 high = 6</p>
</li>
<li><p>중간 인덱스 mid = (low + high)/2 = 3 으로 arr[3] = 7</p>
</li>
<li><p>찾는 값 9가 mid보다 큼으로 왼쪽을 버린다.</p>
</li>
<li><p>low = mid + 1 (mid의 값을 알기 때문에 찾는 값이 mid였으면 바로 찾음)</p>
</li>
<li><p>mid = (4+6)/2 = 5 으로 arr[5] = 11</p>
</li>
<li><p>찾는 값 9가 mid보다 작음으로 오른쪽을 버린다.</p>
</li>
<li><p>high = mid -1 (mid를 기준으로 오른쪽을 버리고 왼쪽만 남아서 )</p>
</li>
<li><p>mid = (4+4)/2 = 4 으로 arr[4] = 9</p>
</li>
<li><p>찾게된다.!!</p>
</li>
</ol>
<h2 id="이진-탐색-수도코드-pseudo-code">이진 탐색 수도코드 (Pseudo-code)</h2>
<h3 id="while-사용">while 사용</h3>
<pre><code>binarySearch(array, target);
    low = 0
    high = array.length - 1

    while low &lt;= high:
        mid = (low + high)/2

        if array[mid] == target
            return mid
        else if array[mid] &lt; target
            low = mid + 1
        else
            high = mid - 1
    return -1 // 찾지 못한 경우</code></pre><h3 id="재귀-방식">재귀 방식</h3>
<p>mid로 찾을 찾은 경우를 제외하고는 
해당 조건에 따라 매개변수를 변경해서
다시 재귀함수 binarySearchRecursive를 호출한다.</p>
<pre><code>function binarySearchRecursive(array, target, low, high):
    if low &gt; high:
        return -1  // 탐색 실패 (base case)

    mid = (low + high) / 2

    if array[mid] == target:
        return mid  // 탐색 성공

    else if array[mid] &lt; target:
        return binarySearchRecursive(array, target, mid + 1, high)  // 오른쪽 절반 재귀 탐색

    else:
        return binarySearchRecursive(array, target, low, mid - 1)  // 왼쪽 절반 재귀 탐색
</code></pre>
