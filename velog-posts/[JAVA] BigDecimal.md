---
title: "[JAVA] BigDecimal"
date: "2025-05-20"
link: "https://velog.io/@ehekaanldk/JAVA-BigDecimal"
series: "Uncategorized"
---

<h2 id="bigdecimal-개요">BigDecimal 개요</h2>
<p>자바에서 float와 double 타입은 부동소수점 방식을 사용한다. 이는 실수를 정확한 실수값이 아닌 근사값으로 저장한다는 단점을 가진다. 이를 해결하기 위해 BigDecimal을 사용한다. </p>
<blockquote>
<p>BigDecimal은 자바에서 정밀한 소수점 연산을 위해서 사용하는 클래스이다. </p>
</blockquote>
<p>부동 소수점 연산에서 발생하는 오차를 방지하고 무한 소수와 같은 정밀한 게산이 필요할 때 유용하게 사용된다. </p>
<p>특히 금융, 세금, 과학 계산 등 실수 계산의 정확성이 중요한 분야에서 필수적으로 활용된다.</p>
<hr />
<h2 id="부동-소수점">부동 소수점</h2>
<h3 id="floatdouble의-한계">float/double의 한계</h3>
<p>자바에서의 float와 double 타입은 IEEE 754 이진 부동소수점 표현을 따른다. </p>
<p>0.1 을 정확하게 이진수로 표현할 수 없어서 내부적으로 0.10000000000000000555... 와 같은 오차 발생한다. </p>
<hr />
<h2 id="bigdecimal">BigDecimal</h2>
<p>BigDecimal은 정확한 10진수 표현을 지원하여 소수점 오류 없이 정밀한 연산이 가능하다. </p>
<h3 id="내부구조">내부구조</h3>
<p>BigDecimal은 내부적으로 정수와 지수를 사용하여 값을 저장한다. </p>
<pre><code>intValue x 10^scale </code></pre><ul>
<li>intValue : 정수값(정확히 저장됨, 내부적으로 Integer)</li>
<li>scale : 소수점 이하 자리 수</li>
</ul>
<h3 id="타입">타입</h3>
<p>BigDecimal는 reference 타입으로 참조형으로 분류된다. </p>
<p>객체이기 때문에 값을 비교할 때는 <code>equals()</code>를 사용해야 한다. </p>
<table>
<thead>
<tr>
<th>구분</th>
<th><code>float</code> / <code>double</code></th>
<th><code>BigDecimal</code></th>
</tr>
</thead>
<tbody><tr>
<td>타입 종류</td>
<td>기본형 (Primitive Type)</td>
<td>참조형 (Reference Type)</td>
</tr>
<tr>
<td>메모리 저장</td>
<td>스택(stack)</td>
<td>힙(heap)</td>
</tr>
<tr>
<td>연산 방식</td>
<td>연산자 (<code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>)</td>
<td>메서드 (<code>add()</code>, <code>divide()</code> 등)</td>
</tr>
<tr>
<td>오차 가능성</td>
<td>있음 (부동소수점 오차)</td>
<td>없음 (정확한 10진 계산)</td>
</tr>
<tr>
<td>불변 객체</td>
<td>❌ (변경 가능)</td>
<td>✔️ (불변 객체)</td>
</tr>
</tbody></table>
<h3 id="연산">연산</h3>
<p>BigDecimal는 기본형처럼 +,-,*,/ 같은 연산자를 직접 사용할 수 없다. 
reference type은 불변 객체이기 때문에 메서드를 이용하여 연산을 수행한다. </p>
<table>
<thead>
<tr>
<th>연산</th>
<th>메서드</th>
</tr>
</thead>
<tbody><tr>
<td>더하기</td>
<td><code>add()</code></td>
</tr>
<tr>
<td>빼기</td>
<td><code>subtract()</code></td>
</tr>
<tr>
<td>곱하기</td>
<td><code>multiply()</code></td>
</tr>
<tr>
<td>나누기</td>
<td><code>divide(scale, RoundingMode)</code></td>
</tr>
<tr>
<td>나머지</td>
<td><code>remainder()</code></td>
</tr>
<tr>
<td>절댓값</td>
<td><code>abs()</code></td>
</tr>
<tr>
<td>음수화</td>
<td><code>negate()</code></td>
</tr>
<tr>
<td>비교</td>
<td><code>compareTo()</code> / <code>equals()</code></td>
</tr>
</tbody></table>
<hr />
<h2 id="bigdecimal-divide-정리">bigdecimal divide() 정리</h2>
<p>📌 1. divide(BigDecimal divisor)</p>
<ul>
<li>기본 나눗셈</li>
<li>단점: 결과가 무한소수이면 예외(ArithmeticException) 발생</li>
</ul>
<pre><code>BigDecimal a = new BigDecimal(&quot;1&quot;);
BigDecimal b = new BigDecimal(&quot;3&quot;);
BigDecimal result = a.divide(b); // ⚠️ ArithmeticException 발생 가능</code></pre><p>📌 2. divide(BigDecimal divisor, int scale, RoundingMode roundingMode)</p>
<ul>
<li>가장 일반적으로 사용하는 형태</li>
<li>scale: 소수점 아래 자릿수</li>
</ul>
<p>roundingMode: 반올림 방식 (예: RoundingMode.HALF_UP)</p>
<pre><code>BigDecimal a = new BigDecimal(&quot;1&quot;);
BigDecimal b = new BigDecimal(&quot;3&quot;);

BigDecimal result = a.divide(b, 10, RoundingMode.HALF_UP); 
System.out.println(result); // 출력: 0.3333333333</code></pre><p>📌 3. divide(BigDecimal divisor, RoundingMode roundingMode)</p>
<ul>
<li>나눗셈 결과가 정확히 나눠지지 않을 경우, 자동으로 scale을 계산하고 반올림 처리</li>
<li>scale을 지정하지 않아도 되지만 정밀도 제어가 어렵다</li>
</ul>
<pre><code>BigDecimal a = new BigDecimal(&quot;10&quot;);
BigDecimal b = new BigDecimal(&quot;3&quot;);

BigDecimal result = a.divide(b, RoundingMode.HALF_UP); // 내부적으로 적절한 scale 지정
</code></pre><h3 id="roundingmode-종류">RoundingMode 종류</h3>
<ul>
<li>HALF_UP : 일반적인 반올림 방식</li>
<li>HALF_DOWN : 5는 버린다.</li>
<li>UP : 무조건 올림</li>
<li>DOWN : 무조건 내림</li>
<li>FLOOR : 음수는 더 작은 쪽으로 내림</li>
<li>CEILING : 양수는 더 큰 쪽으로 올림</li>
<li>HALF_EVEN : 짝수 쪽으로 반올림(은행식)</li>
<li>UNNECESSARY : 반올림 없이 정확히 나눠떨어져야 함(아니면 예외발생</li>
</ul>
