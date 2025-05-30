---
title: "[Spring] 더티 체킹"
date: "2025-05-29"
link: "https://velog.io/@ehekaanldk/JPA-%EB%8D%94%ED%8B%B0-%EC%B2%B4%ED%82%B9"
series: "Uncategorized"
---

<h3 id="더티-체킹dirty-checking">더티 체킹(Dirty Checking)</h3>
<p>영속성 컨텍스트가 관리하는 엔티티의 값이 변경되었는지 감지하고, 변경이 있으면 자동으로 UPDATE 쿼리를 생성하 DB에 반영</p>
<ul>
<li>&quot;Dirty&quot; = 더럽혀졌다, 값이 바뀌었다는 뜻</li>
<li>객체가 원래 상태에서 변조된(dirty) 걸 감지해서,</li>
<li>트랜잭션 커밋 시점에 변경된 값만 SQL로 반영한다.</li>
</ul>
<p>더티 체킹의 검사 대상은 영속성 컨텍스트가 관리하는 Entity로만 대상으로 한다.</p>
<h3 id="동작-과정">동작 과정</h3>
<p><img alt="스크린샷 2025-05-30 004102.png" src="attachment:cf80e6d1-d1a2-4d7a-b497-fc46e9a49760:%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2025-05-30_004102.png" /></p>
<ol>
<li><p><code>em.find()</code>로 엔티티(Book)를 조회함</p>
<p> → JPA는 이 객체를 <strong>영속성 컨텍스트</strong>에 등록하고</p>
<p> → <strong>초기 상태를 '스냅샷'으로 따로 저장</strong>해둡니다</p>
</li>
<li><p>우리가 <code>book.setTitle(&quot;Spring&quot;)</code>처럼 값을 바꾸면</p>
<p> → JPA는 &quot;값이 바뀌었구나&quot;를 기억함</p>
</li>
<li><p>트랜잭션이 끝나는 순간 (커밋)</p>
<p> → <strong>스냅샷과 현재 객체를 비교</strong>해서</p>
<p> → <strong>달라진 부분만 UPDATE SQL로 날림</strong></p>
</li>
</ol>
<h3 id="더티-체킹이-안되는-시점">더티 체킹이 안되는 시점</h3>
<ul>
<li><strong>객체가 영속 상태가 아닐 때</strong><ul>
<li>즉, <code>em.persist()</code>나 <code>em.find()</code> 없이 그냥 만든 객체는 감시 안 됨!</li>
</ul>
</li>
<li><strong><code>detach()</code>나 <code>clear()</code> 등으로 준영속 상태가 된 객체</strong><ul>
<li>이때는 아무리 <code>setXXX()</code> 해도 SQL 안 나감</li>
</ul>
</li>
</ul>
<table>
<thead>
<tr>
<th>항목</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td><strong>정의</strong></td>
<td>JPA가 <strong>영속 상태의 엔티티</strong>에서 <code>setXXX()</code>로 바뀐 값을 감지해서 <code>UPDATE SQL</code>을 자동 생성하는 기능</td>
</tr>
<tr>
<td><strong>적용 대상</strong></td>
<td>이미 DB에 존재하는 데이터를 <code>em.find()</code>로 불러온 객체 (즉, 영속 상태인 엔티티)</td>
</tr>
<tr>
<td><strong>개발자가 해야 할 것</strong></td>
<td>단순히 <code>setXXX()</code>로 값 변경만 하면 됨</td>
</tr>
<tr>
<td><strong>JPA가 자동으로 하는 것</strong></td>
<td>트랜잭션 <code>commit()</code> 또는 <code>flush()</code> 시점에 바뀐 필드를 비교해서 <code>UPDATE SQL</code>을 날림</td>
</tr>
</tbody></table>
