---
title: "[MSA] Backend"
date: "2025-05-25"
link: "https://velog.io/@ehekaanldk/MSA-Backend"
series: "Uncategorized"
---

<h2 id="web-프로그래밍의-이해">Web 프로그래밍의 이해</h2>
<p>문서나 정보를 관리하는 기계를 사용하고 이를 체계화하고 한눈에 보기 쉽게한 것이 웹이다.</p>
<blockquote>
<p>HTTP 프로토콜을 기반으로 TCP/IP 네트워크 상에서 HTML을 통해 작성된, 하이퍼텍스트를 포함한 콘텐츠를 제공해 서비스 한 것이 웹의 시초이다.</p>
</blockquote>
<h3 id="웹-용어-정리">웹 용어 정리</h3>
<ul>
<li><p><strong>HTML</strong> : 웹 페이지의 언어로, <strong>웹페이지의 뼈대를 만드는 언어</strong>이다. 문법으로 문서를 만드는 규격를 말한다. 
하이퍼텍스트 기능을 가지는 문서를 만드는 언어로 웹 페이지를 위한 언어</p>
</li>
<li><p><strong>HTTP</strong> : 프로토콜 중의 하나로, <strong>웹에서의 데이터 교환 약속</strong>이다. </p>
<ul>
<li>브라우저가 서버에게 요청(request)를 보낸다.</li>
<li>서버는 요청의 내용을 담은 응답(respone)을 보내준다.</li>
</ul>
</li>
</ul>
<p>TCP/IP 계층에서 사용하는 프로토콜 중의 하나임</p>
<ul>
<li><p><strong>프로토콜</strong> : <strong>규약</strong>이라는 뜻으로 대체로 <strong>통신</strong>을 할 때, 자료를 주거나 받는 객체들 간에 어떻게 통신을 할 것인지 미리 협의한 약속들 (데이터 교환 약속)</p>
</li>
<li><p>하이퍼텍스트 : 웹 페이지에서 다른 페이지로 이동할 수 있도록 하는 것이다. 
<code>&lt;a href=&quot;https://google.com&quot;&gt;구글로 이동&lt;/a&gt;</code></p>
</li>
<li><p>네트워크 : 여러 대의 컴퓨터가 연결되어 정보를 주고받는 구조
통신을 하기 위한 기본 기반 시설 (인터넷)
인터넷에 가입-&gt;가입된 내 컴퓨터가 인터넷에 등장</p>
</li>
<li><p><strong>TCP/IP</strong> : 주요 프로토콜 중의 하나로,** 인터넷에서 통신을 할 때의 기본원칙**</p>
<ul>
<li><p>TCP(전송 제어 프로토콜) : 데이터를 잘게 나누고, 순서대로 안전하게 전송</p>
</li>
<li><p>IP(인터넷 프로토콜) : 각 컴퓨터의 주소(IP)를 알아내서 어디로 보낼지 결정하는 역할</p>
</li>
<li><p>A라는 컴퓨터가 B에게 메시지를 보내면, 
IP는 “B는 저기 있어요!” 라고 알려주고, TCP는 “이 메시지를 3조각으로 나눠서 순서대로 정확히 보낼게요!” 라고 함</p>
</li>
<li><p>IP는 주소, TCP는 포장,순서,재전송 등의 모든 배송 관리</p>
</li>
</ul>
</li>
</ul>
<hr />
<ol>
<li>클라이언트(client) - 🍽️ 손님<blockquote>
<p>👉 <strong>요청을 보내는 쪽</strong> (사용자)</p>
</blockquote>
</li>
</ol>
<ul>
<li>브라우저를 사용하는 사람이 클라이언트이다. </li>
<li>서버에게 '웹페이지를 보여줘' 라고 <strong>요청(request)를 보낸다.</strong></li>
</ul>
<ol start="2">
<li>서버(server) - ☕ 바리스타<blockquote>
<p>👉 <strong>요청을 받아서 응답을 해주는 쪽</strong></p>
</blockquote>
</li>
</ol>
<ul>
<li>웹페이지를 실제로 <strong>보관</strong>하고 있다. </li>
<li>클라이언트가 요청하면, 그에 맞는 데이터를 응답(response)로 보내준다.</li>
</ul>
<ol start="3">
<li>웹(Web) - 🏠 카페<blockquote>
<p>👉 인터넷에서 정보를 주고받기 위한 전체 시스템</p>
</blockquote>
</li>
</ol>
<ul>
<li>HTTP라는 규칙을 따르는 정보 교환 시스템</li>
<li>웹은 클라이언트와 서버가 HTTP로 통신하는 세계</li>
</ul>
<ol start="4">
<li>브라우저(Browser) - 📬 주문 창구 + 화면 디자이너<blockquote>
<p>👉 웹 페이지를 보여주는 프로그램 + 렌더링 도구</p>
</blockquote>
</li>
</ol>
<ul>
<li>사용자가 주소를 입력하거나 클릭하면,</li>
<li>클라이언트가 서버에 요청을 보내고</li>
<li>받은 HTML, CSS 등을 화면에 보여준다.</li>
</ul>
<ol start="5">
<li>렌더링 엔진 - 🖼️ 디자이너<blockquote>
<p>👉 HTML 같은 코드들을 눈에 보이는 웹페이지로 그려주는 프로그램</p>
</blockquote>
</li>
</ol>
<ul>
<li>브라우저 속에 들어있는 부품이다.</li>
</ul>
<ol start="6">
<li>서버 프로그래밍 👨‍🍳 바리스타의 레시피<blockquote>
<p>👉 서버가 '요청이 왔을 때 어떻게 처리할까?' 를 프로그래밍하는 것</p>
</blockquote>
</li>
</ol>
<ul>
<li>'로그인 시도면 어떻게 처리하지?' 등의 로직 작성</li>
<li>사용하는 언어/프레임워크: Python(Flask, Django), Java(Spring), JavaScript(Node.js) 등</li>
</ul>
<hr />
<h3 id="프로토콜">프로토콜</h3>
<p>브라우저의 요청과 서버의 응답 사이에는 데이터 교환 약속이 필요하다. </p>
<h3 id="httphyper-text-transfer-protocol">HTTP(Hyper Text Transfer Protocol)</h3>
<blockquote>
<p><strong>텍스트 기반의 통신규약</strong>으로, <strong>웹 클라이언트와 웹 서버 간의 데이터</strong>를 주고 받는 데 사용되는 프로토콜</p>
</blockquote>
<ul>
<li><p>포트 : 운영체제(OS) 가 여러 프로그램을 구분해서 통신할 수 있게 만든 통로
OS가 프로그램이 요청을 하면 포트를 임대해주는 것이다.</p>
</li>
<li><p>HTTP는 TCP/IP 프로토콜 기반이다.
👉 HTTP는 상위의 규칙으로 실제 데이터를 옮기는 것은 TCP/IP이다. </p>
<ul>
<li>HTTP는 주고받는 내용,</li>
<li>TCP/IP는 내용을 안전하게 정해진 장소로 보내는 수단</li>
</ul>
</li>
</ul>
<p>클라이언트는 <strong>서버의 IP(집주소)</strong>와 <strong>포트번호(동, 호수)</strong>를 알고 있어야 한다. </p>
<ul>
<li>클라이언트는 서버에 정보를 요청하는 쪽이다. </li>
<li><strong>통신사(ISP)</strong> 로부터 인터넷을 하기 위해 IP를 임대받는다.</li>
</ul>
<p>HTTPS는 보안이 강화된 HTTP이다.</p>
<ul>
<li>기본 포트를 사용하면 url에서 생략이 가능하다.</li>
<li>HTTPS는 보안이 강화된 것으로 기본 포트는 443이다.</li>
</ul>
<p>요청과 응답이 끝나면, <strong>서버는 클라이언트를 기억하지 않는다.</strong></p>
<ul>
<li>&quot;요청&quot;과 &quot;응답&quot;이 하나의 쌍으로 묶여서 처리된다.</li>
<li>요청과 응답이 한번 이루어지면 연결을 끊는다. </li>
<li>다시 새로운 정보가 필요할 때까지는 추가로 요청을 하지 않는다. 👉** 비연결성**</li>
</ul>
<p>비연결성으로 많은 클라이언트들과 연결을 할 수 있다. </p>
<ul>
<li>웹서버의 한계치의 요청을 많이 보내면 디도스발생</li>
<li>특정시간에 수많은 클라이언트들이 요청을 많이 보내는 상황(티켓팅)</li>
</ul>
<p>로그인한 상태는 유지하기 위해서는 클라이언트 정보를 저장한다.</p>
<ul>
<li>클라이언트 쪽에서의 저장이 쿠키</li>
<li>서버 쪽에서의 저장이 세션으로 저장해서 유지한다.</li>
</ul>
<p>웹 주소 URL은 웹에서 특정 자원을 요청하는 주소이다.</p>
<p><code>프로토콜://도메인:포트번호/디렉토리/파일</code> 으로 
<code>https://www.example.com:443/product/list.html</code></p>
<p>클라이언트가 url을 통해서 서버에 request를 보낸다. 서버는 해당 주소에 맞는 html, css등을 response로 보낸다. 브라우저는 이 response를 화면에 표시한다.</p>
<p>DNS는 클라이언트로부터 URL를 받아서 해당 URL에 해당하는 IP주소를 반환해주는 역할을 한다. </p>
<ul>
<li>사용자가 도메인 이름을 사용하여 웹 사이트에 접속</li>
<li>해당 도메인을 실제 네트워크상에서 사용하는 IP주소로 바꾸고 접속</li>
</ul>
<h4 id="http-요청-방식method-요약">HTTP 요청 방식(Method) 요약</h4>
<ul>
<li>GET은 서버에서 정보를 가져온다.</li>
<li>POST는 서버에 새로운 정보를 보낸다.</li>
</ul>
<table>
<thead>
<tr>
<th>메서드</th>
<th>역할</th>
<th>창고 비유</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>GET</strong></td>
<td>📥 가져오기</td>
<td>“박스 내용 좀 보여줘!”</td>
<td>데이터를 요청 (읽기 전용)</td>
</tr>
<tr>
<td><strong>POST</strong></td>
<td>📦 새로 만들기</td>
<td>“새 물건을 창고에 넣어줘!”</td>
<td>새로운 데이터 생성</td>
</tr>
<tr>
<td><strong>PUT</strong></td>
<td>🧼 전부 바꾸기</td>
<td>“이 물건 전체를 새 걸로 교체해줘!”</td>
<td>데이터 전체 수정</td>
</tr>
<tr>
<td><strong>PATCH</strong></td>
<td>🩹 일부 바꾸기</td>
<td>“물건 일부만 살짝 고쳐줘!”</td>
<td>데이터 일부 수정</td>
</tr>
<tr>
<td><strong>DELETE</strong></td>
<td>🗑️ 삭제하기</td>
<td>“이 물건 버려줘!”</td>
<td>데이터 삭제</td>
</tr>
</tbody></table>
<h4 id="http-status-code-정리">HTTP status code 정리</h4>
<p>HTTP requset, 
respone : status code + HTML문서</p>
<ul>
<li><p>2xx : Success
👉 서버가 클라이언트로부터 전달 받은 요청을 성공적으로 수행했음</p>
</li>
<li><p>3xx : Redirestion
👉 클라이언트가 보낸 요청을 완료하려면 서버에서 아직 추가적인 작업이 필요함
다른 경로를 같이주면서 이 경로로 가라고 요청을 준다..</p>
</li>
<li><p>4xx : Client Error
👉 클라이언트 에러로, 클라언트가 서버에 잘못된 요청을 했을 경우 발생함</p>
<ul>
<li>401 : 인증이 안됨(인증은 누구인지 밝혀라) =&gt; 로그인이 안된 상태</li>
<li>403 : 인가가 안됨(인가는) =&gt; 로그인은 되었지만 관리자의 컨텐츠를 볼 수 없음</li>
<li>404 : 클라이언트가 요청했는데 해당 페이지가 없음</li>
</ul>
</li>
<li><p>5xx : Server Error
👉 서버 에러로, 서버가 클라이언트의 요청은 잘 들어왔지만 서버에서 응답을 주지 못함</p>
<ul>
<li>500 : 서버가 다운되었을 때 (클라이언트가 잘못이 없는게 아님, 새로운</li>
<li>503 : 많은 사람들이 서버에 몰렸을 때</li>
</ul>
</li>
</ul>
<hr />
<h2 id="컴퓨터-네트워크-통신-구조의-계층화-모델">컴퓨터 네트워크 통신 구조의 계층화 모델</h2>
<h3 id="tcpip-4계층-모델">TCP/IP 4계층 모델</h3>
<ul>
<li>전체 인터넷과 웹 통신, 이메일, 게임, 채팅 등 모든 네트워크 통신이 이 구조를 따라 작동한다.</li>
<li>현재의 모든 인터넷은 4계층 구조에 기반해서 작동된다. </li>
</ul>
<table>
<thead>
<tr>
<th>계층 번호</th>
<th>이름</th>
<th>설명</th>
<th>주요 프로토콜</th>
</tr>
</thead>
<tbody><tr>
<td><strong>4계층</strong></td>
<td>애플리케이션 계층</td>
<td>사용자와 가장 가까움. 웹, 이메일, 채팅 등</td>
<td>HTTP, HTTPS, FTP, DNS</td>
</tr>
<tr>
<td><strong>3계층</strong></td>
<td>전송 계층</td>
<td>데이터 나눔, 오류확인, 순서관리</td>
<td>TCP, UDP</td>
</tr>
<tr>
<td><strong>2계층</strong></td>
<td>인터넷 계층</td>
<td>주소 결정, 어디로 보낼지 판단</td>
<td>IP, ICMP</td>
</tr>
<tr>
<td><strong>1계층</strong></td>
<td>네트워크 액세스 계층</td>
<td>실제 전송 (물리적 연결)</td>
<td>이더넷, Wi-Fi, ARP</td>
</tr>
</tbody></table>
<h4 id="tcp-vs-udp--전송-계층의-두-가지-방식">TCP vs UDP – 전송 계층의 두 가지 방식</h4>
<p>✅TCP(신뢰성 있는 연결)</p>
<ul>
<li>데이터가 유실되지 않도록 확인하고, 순서대로 전달</li>
<li>손실 시 재전송</li>
<li>ACK 확인 응답 기능 포함</li>
<li>유튜브는 용량이 큰 동영상을 여러 조각으로 쪼개고 TCP의 ack(확인요청)이 안오면 동영상이 끊긴다.</li>
</ul>
<p>✅UDP(빠르지만 확인 안함)</p>
<ul>
<li>빠른 속도이지만 유실될 수 있음</li>
<li>패킷 손실 무시</li>
<li>TCP와 반대되는 개념</li>
<li>중간에 1-2 패킷이 날라가도 동영상 재상을 하는데 문제가 없음(살짝 화질이 깨지는 정도?)</li>
</ul>
<h4 id="http와-ftp--응용-계층-프로토콜">HTTP와 FTP – 응용 계층 프로토콜</h4>
<p>✅HTTP</p>
<ul>
<li>웹브라우저와 웹서버 간 웹페이지 정보를 주고받는 통신 규약</li>
<li><code>GET/index.html</code>, <code>POST/login</code></li>
</ul>
<p>✅FTP</p>
<ul>
<li>파일을 주고받기 위한 프로토콜</li>
<li>FTP 클라이언트 &lt;-&gt; FTP 서버 구조</li>
<li>로그인 기반으로 디렉토리 안의 파일을 업로드/다운로드</li>
</ul>
<h4 id="운영체제와-하드웨어-관점">운영체제와 하드웨어 관점</h4>
<ul>
<li><p>응용 프로그램: 우리가 작성하는 웹 코드, 앱 등</p>
</li>
<li><p>운영체제(OS): 네트워크 통신을 위한 라이브러리(TCP/IP 스택 포함)를 제공</p>
</li>
<li><p>NIC (Network Interface Card): 랜카드/무선카드 → 컴퓨터를 물리적으로 네트워크에 연결</p>
</li>
<li><p>공유기/모뎀: 외부 네트워크(인터넷)와 집 내부 네트워크를 연결</p>
</li>
</ul>
<p>🔁 이 전체가 네트워크 계층 구조를 따라 데이터를 주고받는 체계로 작동함</p>
<h4 id="인터넷-계층--ip의-역할">인터넷 계층 – IP의 역할</h4>
<p>: 다른 네트워크에 있는 장치까지 데이터를 어떻게 전달할지를 정함</p>
<ul>
<li><p>IP 주소를 이용해 <strong>경로(Route)</strong>를 찾아가며 전달</p>
</li>
<li><p>네트워크 간 라우팅(Routing) 역할 수행</p>
</li>
<li><p>대표 프로토콜: IP, ICMP 등</p>
</li>
</ul>
<p>📌 실질적인 “길찾기 계층”이에요
예: 192.168.0.1 → 8.8.8.8</p>
<h4 id="패킷-교환망-vs-회선-교환망">패킷 교환망 vs 회선 교환망</h4>
<p>✅ 회선 교환망 (전화통화 개념)</p>
<ul>
<li><p>A ↔ B 사이에 고정된 회선을 연결하고 통신</p>
</li>
<li><p>장점: 안정적, 지연 없음</p>
</li>
<li><p>단점: 비효율적, 자원이 고정됨</p>
</li>
</ul>
<p>✅ 패킷 교환망 (인터넷 개념)</p>
<ul>
<li><p>데이터를 <strong>작은 조각(패킷)</strong>으로 나눠 보내고</p>
</li>
<li><p>필요한 경로를 그때그때 찾아 전송</p>
</li>
<li><p>장점: 효율적, 여러 사용자 동시 사용 가능</p>
</li>
<li><p>단점: 순서 바뀌거나 지연 발생 가능 → TCP가 해결</p>
</li>
</ul>
<p>💬 “계획하고 길을 짜준다”는 건 → 라우팅 테이블과 경로 선택(IP 계층의 역할)</p>
<hr />
<h2 id="웹의-동작-구조">웹의 동작 구조</h2>
<ol>
<li>웹 브라우저에서 도메인(URL)을 입력한다. </li>
<li>DNS 서버는 해당 도메인을 가진 IP주소를 웹 브라우저에게 전송한다. (도메인 -&gt; IP)</li>
<li>웹 브라우저는 IP주소의 해당 서버에 접속을 시도한다. -&gt; 웹 서버는 접속을 기다리다 접속 요청이 들어오면 수락한다. </li>
<li>웹 서버는 요청 내용을 분석하고 요청된 파일을 읽는다. </li>
<li>웹 서버는 파일 내용을 클라이언트에 전송한다. </li>
<li>웹 브라우저는 웹 서버로부터 받은 내용을 이용하여 HTML 태그를 분석해 화면을 구성한다. </li>
</ol>
<h3 id="정적-페이지--고정된-html을-로드하는-방식">정적 페이지 : 고정된 HTML을 로드하는 방식</h3>
<blockquote>
<p>모든 HTML파일이 서버에 미리 완성된 상태로 존재</p>
</blockquote>
<ul>
<li>서버는 해당 HTML 파일을 그대로 전달</li>
<li>화면에 변화를 주고자 하면 서버를 새로이 HTTP요청을 전송하고, HTML을 다시 전송 받아서 재 렌더링</li>
</ul>
<h3 id="동적-페이지--요청이-들어오면-html이나-데이터를-그때-만들어서-보내는-방식">동적 페이지 : 요청이 들어오면 HTML이나 데이터를 그때 만들어서 보내는 방식</h3>
<blockquote>
<p>spring처럼 서버가 요청을 받아서 로직을 처리하고, 필요한 결과를 만들어서 응답하는 방식</p>
</blockquote>
<p><strong>방법1. spring mvc(서버가 HTML까지 조립) =&gt; SSR</strong> 
: 서버에서 요청에 따라서 동적으로 화면(view)까지 만들어주는 방식
<code>[클라이언트] → 요청 → [서버: 컨트롤러 → 모델 → 뷰] → HTML 응답</code></p>
<ul>
<li>클라이언트가 request를 보내면,</li>
<li>서버가 DB에서 사용자 정보를 읽고</li>
<li>템플릿 엔진으로 HTML을 생성해서 응답</li>
<li>👉 서버가 화면까지 만들어서 보내준다.(백엔드 + 화면)</li>
</ul>
<p><strong>방법2. spring backend(서버는 데이터만, HTML은 프론트에서 조립) =&gt; CSR</strong>
: 서버에 데이터만 제공, 화면은 프로트엔드가 담당하는 방식</p>
<pre><code>[클라이언트] → HTML + JS 구성
          → 서버에 JSON 데이터 요청
          ← 서버는 JSON 응답만 해줌</code></pre><ul>
<li>서버는 HTML을 만들지 않음</li>
<li>클라이언트가 HTML + JS으로 화면을 먼저 구성하고</li>
<li>필요한 데이터만 서버에 <code>POST</code>, <code>GET</code>으로 요청한다.</li>
<li>👉 백엔드는 API만 제공하고, 프론트가 화면을 그린다.(REST API 서버)</li>
</ul>
<h3 id="ajaxasynchronous-javascript-and-xml">Ajax(Asynchronous JavaScript and XML)</h3>
<blockquote>
<p>화면을 전체 다시 로딩하지 않고, 일부 데이터만 요청하고 바꿀 수 있다.</p>
</blockquote>
<ul>
<li><p>JavaScript와 XML 형식을 이용한 비동기적 정보 교환 기법</p>
</li>
<li><p>자바스크립트를 통해서 <strong>서버와 브라우저가 비동기 통신</strong>을 주고 받으며 데이터를 전송할 수 있다. </p>
</li>
<li><p><strong>비동기 통신</strong> : 통신을 하면서 다른 처리를 <strong>동시에 병렬적</strong>으로 가능</p>
</li>
<li><p>랜더링 되는 타이밍과 상관없이 자바스크립트 엔진이 백그라운드에서 그때그때 데이터를 가져와서 업데이트한다. (새로고침하지 않아도 필요 부분만 랜더링된다.)</p>
</li>
</ul>
<h4 id="추가-랜더링">[추가] 랜더링</h4>
<p>: HTML, CSS, JavaScript파일을 받아와서 결과무을 화면에 그려내는 과정</p>
<ul>
<li>실제 HTML파일을 누가, 언제 구성하는냐에 따라서 CSR, SSR로 나눈다.</li>
</ul>
<h3 id="csrclient-side-rendering">CSR(Client Side Rendering)</h3>
<blockquote>
<p>서버는 HTML 껍데기만 보내고, javascript 가 나머지를 구성</p>
</blockquote>
<p>: 클라이언트인 브라우저가 렌더링을 처리하는 방식으로 서버에서 받은 데이터를 통해 브라우저가 view를 그리는 주체</p>
<ul>
<li>서버는 index.html만 보냄</li>
<li>브라우저는 javascript로 데이터 요청 (AJAX)</li>
<li>화면은 클라이언트가 조립</li>
</ul>
<table>
<thead>
<tr>
<th>장점</th>
<th>단점</th>
</tr>
</thead>
<tbody><tr>
<td>사용자 경험이 좋음</td>
<td>검색엔진이 읽기 어려움 (SEO 약함)</td>
</tr>
<tr>
<td>앱처럼 동작</td>
<td>첫 로딩이 느릴 수 있음</td>
</tr>
</tbody></table>
<h3 id="ssr-server-side-rendering">SSR (Server Side Rendering)</h3>
<blockquote>
<p>서버가 HTML을 완성해서 보내준다.</p>
</blockquote>
<p>: 서버 쪽에서 렌더링 준비를 끝마친 상태로 클라이언트에 전달하는 방식이다. </p>
<ul>
<li><p>브라우저가 요청하면</p>
</li>
<li><p>서버가 HTML생성</p>
</li>
<li><p>브라우저는 받은 HTML을 그대로 보여준다. </p>
</li>
<li><p>사용자가 웹사이트에 접속하면, 서버가 HTML을 렌더링해서 즉시 보여준다.</p>
</li>
</ul>
<table>
<thead>
<tr>
<th>장점</th>
<th>단점</th>
</tr>
</thead>
<tbody><tr>
<td>SEO에 강함 (검색엔진에 유리)</td>
<td>초기 로딩이 느릴 수 있음</td>
</tr>
<tr>
<td>첫 페이지 빨리 뜸</td>
<td>사용자 상호작용이 많아질수록 비효율</td>
</tr>
</tbody></table>
<hr />
<h2 id="클라이언트와-서버">클라이언트와 서버</h2>
<h3 id="3-tier-architecture">3-Tier Architecture</h3>
<blockquote>
<p>웹 시스템을 3가지 역할으로 나누어서 구성하는 방식</p>
</blockquote>
<ol>
<li>프리젠테이션 계층(클라이언트)</li>
</ol>
<ul>
<li>서버에서 응답을 받은 결과를 렌더링</li>
<li>서버에 원하는 데이터를 요청</li>
<li>프론트엔드</li>
</ul>
<ol start="2">
<li>웹/애플리케이션 서버</li>
</ol>
<ul>
<li>클라이언트에게 서비스를 제공</li>
<li>클라이언트의 요청에 데이터를 가공하여 응답</li>
<li>미들웨어 또는 백엔드<ul>
<li>프리젠테이션 계층</li>
<li>비즈니스로직 계층 : 실제 서비스가 하는일</li>
<li>데이터접근 계층 : DB에 저장하고 저장한 것을 활용</li>
</ul>
</li>
</ul>
<ol start="3">
<li>데이터베이스 서버</li>
</ol>
<ul>
<li>애플리케이션에서 사용되는 데이터를 영구적으로 저장하고 관리</li>
<li>데이터베이스에 접근하여 데이터를 읽거나 쓰는것을 관리하는 계층</li>
<li>데이터를 가지고 있는 서버</li>
</ul>
<hr />
<h2 id="프레임워크">프레임워크</h2>
<h3 id="프레임워크-1">프레임워크</h3>
<blockquote>
<p><strong>소프트웨어의 구체적인 부분에 해당하는 설계</strong>와 <strong>구현</strong>을 <strong>재사용</strong>이 가능하게끔 일련의 협업화 된 형태로 클래스들을 제공하는 것</p>
</blockquote>
<p>설명:</p>
<ul>
<li>거대한 틀을 제공하고, 개발자는 틀 안에서 코드를 작성해야 한다.</li>
<li>프레임워크가 전체 흐름을 제어한다. -&gt; 프레임워크가 주도</li>
</ul>
<p><strong>프레임워크 VS 라이브러리</strong></p>
<ul>
<li><p>소프트웨어의 로직,구동 패턴 등 틀을 만들어놓고
프레임워크는 틀에 맞추어서 소스코드를 개발해주어야 한다. (소프트웨어의 전체 설계까지 재사용)</p>
</li>
<li><p>라이브러리는 사용하고자하는 기능을 불러다가 사용한다. (기능을 재사용)</p>
</li>
</ul>
<h3 id="라이브러리">라이브러리</h3>
<blockquote>
<p>주로 소프트웨어를 개발할 때 필요한 기능 함수들을 모아놓은 소프트웨어
특정 작업을 수행하는 기능이나 메소드의 모음</p>
</blockquote>
<ul>
<li>개발자가 필요한 기능만 직접 가져와서 사용</li>
<li>코드 흐름을 개발자가 제어한다. -&gt; 개발자가 주도</li>
</ul>
<hr />
<h2 id="스프링-프레임워크">스프링 프레임워크</h2>
<h4 id="과거의-ejb란">과거의 EJB란?</h4>
<p><strong>Enterprise JavaBeans</strong>
자바 EE(Java Enterprise Edition)에서 제공하던
기업용 서버 애플리케이션 개발을 위한 컴포넌트 기술이다.</p>
<p>📌 쉽게 말해:
&quot;기업 규모의 복잡한 웹 서비스를 만들기 위해
Java에서 공식적으로 제공하던 무거운 서버 기술&quot;</p>
<h4 id="ejb가-너무-무서워서--가볍고-유연한-대안으로-등장한-것이-spring">EJB가 너무 무서워서 =&gt; 가볍고 유연한 대안으로 등장한 것이 Spring</h4>
<blockquote>
<p>자바 플랫폼을 위한 오픈 솟스 애플리케이션 프레임워크로써 엔터프라이즈급 애플리케이션을 개발하기 위한 모든 기능을 종합적으로 제공하는 경량화된 솔루션</p>
</blockquote>
<h3 id="spring의-특징">Spring의 특징</h3>
<h4 id="1-pojo-plain-old-java-object-기반의-구성">1. POJO (Plain Old Java Object) 기반의 구성</h4>
<blockquote>
<p>순수 자바 객체만 사용해서 프로그래밍 코드를 작성한다. 
프레임워크나 라이브러이에 의존하지 않는 가장 일반적인 순수 자바 객체</p>
</blockquote>
<ul>
<li><p>객체 지향적인 원리에 충실하면서 환경과 기술에 종속되지 않고 필요에 따라 재활용될 수 있는 방식</p>
</li>
<li><p>어노테이션, 상속, 구현 없이도 작동하는 클래스</p>
</li>
<li><p>유연하고 테스트가 쉽다.</p>
<pre><code>public class HelloService {
  public String sayHello() {
      return &quot;Hello, Spring!&quot;;
  }
}</code></pre><h4 id="2-ioc-inversion-of-control">2. IoC (Inversion of Control)</h4>
<blockquote>
<p>객체를 생성하고 관리하는 책임을 개발자가 아닌 스프링 컨테이너가 담당하는 것</p>
</blockquote>
</li>
<li><p>기존의 방식은 사용자가 new 연산을 통해서 객체을 생성한다. </p>
</li>
<li><p>Snack 클래스가 Juice 객체를 직접 생성한다.</p>
</li>
</ul>
<pre><code>public class Snack {
    private Juice juice;

    public Snack() {
        juice = new Juice(); // 직접 생성
    }
}
</code></pre><ul>
<li>IoC 방식은 스프링이 객체를 대신 만들어서 넣어준다. </li>
<li>Snack은 Juice에 대한 의존성을 외부 (spring ioc container) 에게 맡긴다.</li>
<li>Snack은 <code>Juice 가 필요하다는 사실만 선언</code>한다.<pre><code>public class Snack {
  @Autowired
  private Juice juice;
}
</code></pre></li>
</ul>
<pre><code>- juice는 @component, @Service, @Repository 로 스프링이 관리하는 Bean 객체여야 한다.
- @Autowired는 스프링 컨테이너가 관리하는 Bean만 주입할 수 있다.
</code></pre><p>@Component
public class Juice { }</p>
<p>@Component
public class Snack {
    @Autowired
    private Juice juice;
}</p>
<pre><code>
- 코드 제어의 흐름이 프레임워크에 종속되어 있다. 

#### 3. DI(Dependency Injection)
&gt; 어떤 객체가 필요로 하는 다른 객체(의존성)을 스프링이 주입해주는 것

📦 A 객체가 B 객체를 필요로 할 때, 스프링이 B 객체를 만들어서 A에게 넣어주는 것

생성자를 작성한다. 하지만 호출은 스프링 컨테이너가 주체이다.</code></pre><p>public OrderService(PaymentService paymentService) {
    this.paymentService = paymentService;
}</p>
<pre><code>
- 기존의 생성자 호출이다. 해당 부분을 스프링이 대신하면서 필요한 의존성을 주입해준다.</code></pre><p>PaymentService ps = new PaymentService();
OrderService os = new OrderService(ps);</p>
<pre><code>
- 최종적으로 코드를 작성해서 OrderService 가 PaymentService를 필요로 할때 스프링이 알아서 넣어준다.</code></pre><p>@Component
public class OrderService {</p>
<pre><code>private final PaymentService paymentService;

// DI (생성자 주입 방식)
public OrderService(PaymentService paymentService) {
    this.paymentService = paymentService;
}</code></pre><p>}</p>
<pre><code>
#### 특징 정리

&gt;결론적으로 스프링은 POJO 객체를 기반으로 , 
개발자가 직접 new로 객체를 만들지 않고 (IoC),
필요한 의존성은 스프링이 알아서 넣어준다.(DI)

&gt;=&gt; 의존성을 주입하는 과정에서 개발자가 new로 객체를 생성하지 않고,
스프링이 의존객체를 찾아서 주입해준다. 


---

### Bean

&gt; 스프링이 대신 만들어주고 관리해주는 자바 객체(클래스)

스프링의 특징인 IoC(제어의 역전) 개념에 따라서, 
개발자가 new로 직접 객체를 생성하지 않고,
스프링이 자동으로 대신 생성하고 관리해주는 객체가 Bean이 된다. 

- 햄버거 = 객체(클래스에서 new로 만든 실체)
- 내가 직접 햄버거를 만들면 = 직접 new로 객체 생성
- 햄버거 자동으로 만들어주는 가게 (스프링) ⇒ 햄버거가 자동으로 나옴 ⇒ 이게 Bean
- 결론적으로는 생성의 주체가 다를 뿐이다.

#### Bean의 생명주기</code></pre><p>[1] Bean 정의 확인 및 등록
      ↓
[2] Bean 객체 생성 (new)
      ↓
[3] 의존성 주입 (DI, setter or constructor)
      ↓
[4] 초기화 전 콜백 (BeanPostProcessor: postProcessBeforeInitialization)
      ↓
[5] 초기화 메서드 호출 (@PostConstruct or InitializingBean)
      ↓
[6] 초기화 후 콜백 (BeanPostProcessor: postProcessAfterInitialization)
      ↓
[7] 빈 사용
      ↓
[8] 컨테이너 종료 시 소멸 메서드 호출 (@PreDestroy or DisposableBean)</p>
<pre><code>

### Spring container

&gt; Bean 객체들을 만들어주고 보관하고, 필요하면 꺼내주는 관리자

스프링 애플리케이션이 실행되면,
제일 먼저 “컨테이너” 라는 공간이 만들어진다.
그 안에 필요한 모든 객체(Bean)을 만들어서 보관하고 관리한다.

- 스프링은 자동 햄버거 공장
- 공장이 자동으로 햄버거(Bean 객체) 를 만들고, 보관하고, 손님에게 준다.
- 이 공장의 전체 시스템이 스프링 컨테이너

#### spring container의 종류
1. BeanFactory
- bean을 등록하고 객체 생성, 조회, 호출 등의 다양한 기능을 담당한다.

- 객체간의 연관 관계를 설정, 클라이언트의 요청 시 빈을 생성한다.

- bean의 라이프 사이클을 관리한다.

- bean의 정의는 즉시 로딩해 오지만, **bean 사용되기 전까지는 인스턴스화 하지 않는다.**

- **getBean()** 으로 bean을 인스턴화하고 bean의 특성을 설정해야 bean의 생명 시작

2. ApplicationContext
- bean 팩토리에서 제공하는 모든 기능을 제공한다.

- 스프링에서 제공하는 여러 부가 기능을 추가로 제공한다.

- 컨테이너 생성 시 모든 bean 정보를 메모리에 로딩하여 bean 필요 시 즉시 사용 가능

- **bean 초기화 시점에 bean 을 생성**해두어서 필요할 때** 즉시 사용이 가능하다.**

실행시점에서의 applicationcontext 
: ```SpringApplication.run() → ApplicationContext 생성 및 초기화 → 애플리케이션 실행```

종료시점에서의 applicationcontext
: ```SpringApplication.close() → ApplicationContext.close() 호출 → Bean 소멸 및 리소스 해제```


### Bean 와 Spring ioc container
스프링은 자바 엔터프라이즈 기술을 사용하는 서버환경이다. 
클라이언트의 요청을 받아서 서버환경에서 처리할 때마다 내부에서 클래스 인스턴스를 생성하게 되면서 부하가 증가한다.
싱클톤(클래스의 인스턴스가 1개만 생성된다.)으로 부하의 증가를 해결한다.


### AOP (Aspect-Oriented Programming)
실제 프로그램을 만들다보면 공통적으로 반복되는 코드가 많다. 
- 에러처리
- 트랜잭션 처리
- 로깅
- 보안 검사

&gt; 공통 기능을 한 곳에 모아서 필요한 곳에 자동으로 끼워 넣는 방식

공통 로직은 Aspect로 모듈화하고, 핵심적인 비즈니스 로직에서 분리하여 재사용한다.

| 구성 요소         | 설명               | 비유               |
| ------------- | ---------------- | ---------------- |
| **Aspect**    | 공통 기능 묶음 클래스     | 단무지 담당자          |
| **Advice**    | 실제 끼워넣을 코드 (메서드) | 단무지를 넣는 동작       |
| **Pointcut**  | 어디에 끼워넣을지 지정     | “모든 김밥 만들 때”     |
| **JoinPoint** | 끼워넣을 실제 위치       | 김밥을 말기 직전        |
| **Weaving**   | 실제 코드에 끼워넣는 작업   | 단무지를 실제로 끼워넣는 순간 |





## OOP + OPJO

POJO는 특정 기술들이 종속성을 띄면, 객체지향적인 설계가 어려움
DB가 바뀐다고 코드가 다 바뀌면 안됨
=&gt; 객체지향적인 원리에 충실하면서, 환경과 기술에 종속되지 않고 필요에 따라서 재활용

SOLID
: 코드가 새로운 요구사항을 받으면서 코드가 커지고 복잡해지면 소프트웨어가 부패된다. 이를 설계 단계에서 해결을 하기 위함.
- SRP : 단일 책임의 원칙
모듈을 변경하고자할 때 해당 모듈은 변경의 이유가 하나뿐이여야 한다. 
응집도는 높게!, 결합도는 낮게! 설계한다.

- OCP : 개방-폐쇄 원칙
확장에는 열려있어야 하고(개방), 변경에는 닫혀 있어야 한다.
기존의 코드를 변경하지 않고 기능을 수정하거나 추가할 수 있도로 설계해야 한다. 
자주 변화하는 부분은 추상화하고 상속을 통해 구현한다. 

- LSP : 리스코드 치환 원칙
부모 객체와 자식 객체가 존재할 때, 부모 대신 자식이 들어갈 떄 자식이 부모를 완전히 대체가 가능하다. 

- ISP : 인터페이스 분리 원칙
객체는 자신이 호출하지 않은 메소드에 의존하지 않아야 한다. 
클라이언트의 목적과 용도에 적합한 인터페이스만을 제공하기 위해 인터페이스를 잘게 분리하는 것이다. 
```throw new UnspportedOperationException()``` 으로 기능을 사용하지 않지만, 인터페이스로 인해 구현이 필요하다. 
=&gt; 더 상세 인터페이스로 나누어서 선언

- DIP : 의존관계 역전 원칙
사용자가 상속 관계로 이루어진 모듈을 가져다 사용할 때, 하위 모듈의 인스턴스를 직접 가져다 쓰지 말고, **상위 인터페이스 타입의 객체**를 사용하라는 원칙이다.
상위 객체에서는 추상화된 모듈을 가져다쓰면서 하위 모듈의 변화에 따라 수정을 많이하지 않아도 된다. 


IoC : 제어의 역전
제어를 위임한다.
개발자가 제어를 관리하게 되면 강한 결합도, 유연성의 부족, 테스트의 어려움

---


## IoC 정리

### 1️⃣ 흐름 정리
- ```@Autowired``` 어노테이션을 통해서 해당 **클래스가 필요한 의존 객체임을 스프링에게 알린다. **

- 주입되는 객체는 스프링에서 관리하여 @component, @ service, @reposotory할 수 있는 **Bean 객체**이여야만 한다.

- 스프링은 bean 객체를 다루고, **bean을 생명주기를 관리**하는 **bean container**를 사용한다. 

- 스프링의 bean 컨테이너는 관리하는 bean 객체들만 의존성 주입 등의 관리가 가능하다. 

- **IoC**를 위해서는 **적용하는 객체가 반드시 bean 객체**이여야 하고, bean을 등록하는 2가지 방법

### 2️⃣ Bean 등록 방식
#### 1. 수동으로 등록하기
**개발자가 직접 메서드로 객체를 생성**해서 **bean으로 등록**한다. 
**설정 클래스 구성**을 ```@Configuration``` 을 사용하고, ```@bean``` 어노테이션으로 bean으로 등록할 객체를 **수동으로 스프링에게 알려준다.** 

- bean 생성 시 복잡한 조건이 필요한 경우
- 생성자 인자가 많은 경우
- 외부 라이브러리 클래스 사용 시 직접 수정이 불가하기에 
</code></pre><p>@Configuration
public class AppConfig {</p>
<pre><code>@Bean
public HelloService helloService() {
    HelloService service = new HelloService();
    // 초기 설정이나 외부 의존 주입 가능
    return service;
}</code></pre><p>}</p>
<pre><code>
#### 2. 자동으로 등록하기
bean으로 등록하고자 하는 클래스에 ```@component```를 붙인다.
해당 객체는 @service, @reposiory, @controller 으로 **스프링이 자동으로 bean을 등록한다.**
- 내가 만든 클래스에 bean을 등록하고자 할 때
- 단순한 서비스/레포지토리 구성에서 </code></pre><p>@Component
public class HelloService {
    public String greet() {
        return &quot;Hello!&quot;;
    }
}</p>
<pre><code>

### spring의 대표적인 어노테이션
- @Component : 자동 bean 등록 대상
- @Controller : 요청 처리 (데이터(model)를 view에 전달)
- @Service : 비즈니스 로직 (핵심 로직)
- @Repository : DB 접근
- @Configuration : @bean 메서드를 담는 설정 클래스 (bean 수동 등록 위치)
- @Bean : 수동 Bean 등록
- @ Autowired : 필요한 의존 객체를 자동으로 주입


## DI 정리

### 1️⃣ 흐름 정리
의존성은 한 객체의 코드에서 다른 객체를 사용하거나 다른 메서드를 호출할 때 발생한다. 

의존성의 정도를 결합도라고 나타낸다. 
- 강한 결합도는 new를 사용하여 생성한 객체에 의존하는 경우이다. 
- 약한 결합도는 인터페이스와 같은 추상화 클래스에 의존하는 경우이다.

고수준의 클래스가 저수준의 클래스의 객체를 필드로 가지면 강한 결합도가 된다. 이는 클래스의 변경이 자유롭지 않다. 
고수준의 클래스에 저수준의 클래스들의 상위 인터페이스를 필드로 가지면 약한 결합도가 된다. 인터페이스 클래스를 사용해 추상화하여 클래스 간의 의존성을 최소화하여 유연한 변경이 가능하다. 

의존성 주입은 객체가 필요한 의존 객체를 직접 생성하지 않고, 스프링컨테이너가 대신 주입해주는 방식이다.

### 2️⃣ 의존성 주입 방법
#### 1. 생성자 주입
&gt; 객체가 필요한 의존 객체를 생성자를 통해서 전달받는다. 
외부에서 생성자 파라미터로 Bean를 주입해준다.
객체 생성과 의존성 주입이 동시에 발생한다.

생성자에 @Autowired를 하면 스프링컨테이너에 @Component로 등록된 Bean에서 생성자에 필요한 Bean을 주입한다. 
- 스프링이 없었다면 ```this.airpodsService = new AirpodsService()``` 으로 직접 생성해서 의존성 주입한다.
- 스프링 bean ioc 컨테이너를 사용하여,```this.airpodsService = airpodsService``` 으로 생성된 bean을 자동으로 주입받는다.
</code></pre><p>@Component
public class AirpodsController {</p>
<pre><code>private final AirpodsService airpodsService;

@Autowired
public AirpodsController(AirpodsService airpodsService) {
    this.airpodsService = airpodsService;
}</code></pre><p>}</p>
<pre><code>- 생성자는 객체가 처음 만들어질 때 한번에 호출되고 
- 생성자에 의해 주입되는 의존 객체만 ```final```로 선언이 가능하다.
- 생성자가 1개이면 @Autowired 생략이 가능
- 생성자를 이용해서 의존 객체를 주입하면 **의존 객체가 반드시 있어야** 해서 **NULLable를 방지할 수 있다.**
- **생성자로 객체 생성과 동시에 주입한다.**

#### 2. 수정자 주입(setter)
&gt; 필드의 값을 변경하는 **수정자 메서드**를 통해서 의존 관계를 주입해준다. 
객체 생성 이후에 의존성 주입이 발생한다.


- 생성자 함수와 비슷하지만 다른 메서드(setter)로 현재의 기본 생성자는 생략되어 있다. 
- 스프링 컨테이너가 내부적으로 ```new OrderService()```를 호출해서 객체를 생성하게 된다. 
- 이후에 setter메서드 (현재는 ```setPaymentService```)를 호출해서(@Autowired가 붙어있음) ```paymentService``` bean을 주입한다. </code></pre><p>@Component
public class OrderService {</p>
<pre><code>private PaymentService paymentService;

@Autowired
public void setPaymentService(PaymentService paymentService) {
    this.paymentService = paymentService;
}</code></pre><p>}</p>
<pre><code>- **객체의 생성이 일어난 후에 주입을 한다.**
- ```@Autowired``` 입력해줘야 실행된다. 
- 스프링 bean으로 등록되지 않은 인스턴스도 주입이 가능하다. 
- **변경 가능성이 있는 의존관계**에서** 중간에** **setter 를 호출**해서 의존관계 변경이 가능하다.

#### 3. 필드 주입
&gt; @Autowired 를 필드에 직접 붙여서 의존 객체를 주입한다. 

- ```AirpodsController```의 기본생성자로 객체가 생성된다. 
- 스프링의 reflection 으로 클래스 내의 필드 중에서 ```@Autowired``` 가 붙은 필드를 검사한다.
- set() 메서드로 스프링이 관리하는 bean에 해당 필드를 직접 넣어준다. 
</code></pre><p>@Component
public class AirpodsController {</p>
<pre><code>@Autowired
private AirpodsService airpodsService;  // 필드 주입</code></pre><p>}</p>
<pre><code>- 리플렉션은 자바에서 클래스, 메서드, 필드 등의 구조를 실행 중에 동적으로 검사/조작하는 기능이다. 리플렉션 이전의 코드는 아래와 같다. </code></pre><p>AirpodsController controller = new AirpodsController();
controller.setService(new AirpodsService());</p>
<pre><code>- @Autowired는 필드에 직접 접근을 해야하는데 대부분 ```private```이여서 reflection으로 접근 제한을 무시한다.
- 필드에 bean을 직접 꽂아넣는 방식이다.

#### spring에서 DI
- 필드 주입은 final 선언이 불가능하고, 객체가 변하기 쉽다. 
- setter 주입은 final 선언이 불가능하고, public void로 구현하기에 관계를 주입받은 객체의 변형 가능성이 있다.
- setter 는 변경 가능성이 있는 경우에 사용을 권장한다. 
- 생성자 주입은 final로 객체의 불변성을 확보하고 nullable한 의존성 누락을 방지할 수 있다. 

---

## AOP 정리

### 1️⃣ 흐름 정리
AOP는 공통기능을 따로 빼서 관리하는 기술이다.
핵심 관심사와 횡단 괌심사로 관점을 분리하여, 필요할 때만 공통 기능(횡단 관심사)을 핵심 기능에 넣어주는 구조이다.
- 핵심 관심사는 각 클래스나 메서드가 실제로 해야 하는 주요 비즈니스 로직이다.
- 횡단 관심사는 공통적으로 필요하지만, 각각의 핵심 내용과는 직접적인 관련이 없는 부가 기능이다.

AOP는 **횡단 관심사를 따로 작성**해서 **핵심 관심사를 하는 도중에** 스프링이 **자동으로 끼워넣어준다. **

### 2️⃣ AOP용어 정리
- Aspect 
: 횡단 관심사를 구현하는 부가 기능들의 묶음(클래스 단위)이다. 
Advice와 Pointcut을 포함한다. 

- Advice 
: 실제로 끼워 넣을 코드(메서드) 
횡단 관심사를 구현하는 코드부분이다. 
Before, After, Around 등 종류가 있다.

- JointPoint 
: 핵심 관심사의 로직 실행 중에 끼워 넣을 수 있는 시점

- Pointcut : Advice를 적용할 대상(클래스, 메서드 등)을 지정하는 표현식
</code></pre>
