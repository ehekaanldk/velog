---
title: "Cookie vs Session vs Token"
date: "2025-06-12"
link: "https://velog.io/@ehekaanldk/Cookie-vs-Session-vs-Token"
series: "Uncategorized"
---

<h2 id="cookie">Cookie</h2>
<blockquote>
<p>웹 서버가 클라이언트에게 정보를 기억시키기 위해 사용
결론적으로 클라이언트에게 저장되는 데이터 조각</p>
</blockquote>
<ul>
<li>클라이언트에 저장</li>
<li>key-value형태의 문자열 데이터</li>
</ul>
<pre><code>Set-Cookie: userid=kim123; Max-Age=3600</code></pre><ul>
<li>서버가 클라이언트에게 <code>userid=kim123</code> 이라는 정보를 저장하라고 지시한다.</li>
<li>사용자가 다시 접속하면 자동으로 서버에 해당 쿠키를 포함해서 요청</li>
</ul>
<h2 id="session">Session</h2>
<blockquote>
<p>서버 측에서 사용자의 상태를 기억하기 위해 유지하는 정보 저장 공간</p>
</blockquote>
<ul>
<li>서버에 저장</li>
<li>각 사용자마다 고유한 세션 ID를 생성해 관리</li>
<li>클라이언트는 세션 ID만 쿠키 형태로 가지고, 실제 데이터는 서버가 보관한다.</li>
<li>자동로그인, 테마 설정 등</li>
</ul>
<ol>
<li>사용자 로그인</li>
<li>서버가 세션을 생성 -&gt; 고유한 세션 ID발급</li>
<li>세션 ID가 쿠키 형태로 클라이언트에 저장됨</li>
<li>이후의 요청 시 클라이언트가 이 세션 ID를 서버에 전송</li>
<li>서버가 세션 ID로 사용자를 식별한다. </li>
</ol>
<p>단점) 
세션은 서버에 저장하는 형태로 데이터가 증가하면 부하가 증가
서버를 확장하게 되는 경우, 서버 간의 세션 공유가 불가능</p>
<h2 id="tokenjwt">Token(JWT)</h2>
<blockquote>
<p>사용자의 인증정보를 token으로 만들어서 클라이언트가 직접 보관하고, 요청 시마다 HTTP 헤더에 첨부해서 보낸다.</p>
</blockquote>
<ul>
<li>클라이언트가 보관</li>
<li>서버는 stateless로 상태를 기억하지 않음</li>
<li>token 안에는 사용자 정보와 서명이 포함된다. </li>
</ul>
<pre><code>xxxxx.yyyyy.zzzzz
|     |     |
헤더  페이로드  서명</code></pre><ul>
<li>헤더 : 토큰의 타입, 서명 알고리즘 정보</li>
<li>페이로드 : 토큰에 담고자하는 실제 데이터 (사용자 정보, 권한, 토큰 만료 시간 등)</li>
<li>서명 : 헤더+페이로드를 비밀키로 생성</li>
</ul>
<h2 id="비교--cookie-session-token">비교 : Cookie, Session, Token</h2>
<table>
<thead>
<tr>
<th>항목</th>
<th>Cookie</th>
<th>Session</th>
<th>Token (JWT)</th>
</tr>
</thead>
<tbody><tr>
<td>저장 위치</td>
<td>클라이언트</td>
<td>서버</td>
<td>클라이언트</td>
</tr>
<tr>
<td>인증 방식</td>
<td>값 저장 (간단 정보)</td>
<td>세션 ID로 사용자 식별</td>
<td>토큰 자체에 정보 포함</td>
</tr>
<tr>
<td>보안성</td>
<td>낮음 (위변조 위험)</td>
<td>높음 (서버 보관)</td>
<td>서명으로 위변조 방지 가능</td>
</tr>
<tr>
<td>확장성</td>
<td>좋음</td>
<td>나쁨 (서버 메모리 부담)</td>
<td>매우 좋음 (Stateless)</td>
</tr>
<tr>
<td>사용 예</td>
<td>자동 로그인</td>
<td>로그인 인증 유지</td>
<td>API 인증, 모바일 앱 인증</td>
</tr>
</tbody></table>
