---
title: "[MSA] 마이크로서비스 모델링"
date: "2025-06-08"
link: "https://velog.io/@ehekaanldk/MSA-%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%84%9C%EB%B9%84%EC%8A%A4-%EB%AA%A8%EB%8D%B8%EB%A7%81"
series: "Uncategorized"
---

<h2 id="1-기존-조직-구조와-변화">1. 기존 조직 구조와 변화</h2>
<p>기존 조직 구조</p>
<ul>
<li>biz: 분석설계팀(요구사항 서비스의 분석설계)</li>
<li>dev: 개발팀</li>
<li>ops: 운영팀</li>
</ul>
<h3 id="bizdevops란">BizDevOps란?</h3>
<p>기존에는 개발(dev)과 운영팀(ops)이 분리되어 있었지만, 
민첩하고 빠른 서비스 개발과 운영을 위해 개발과 운영을 분리하지 않고 한팀으로 devops 로 통합 운영한다.
요구사항 도출부터 설계,개발, 운영까지 하나의 흐름으로 연결되도록 bizdevops로 업무와 IT의 벽이 허물어진 체계를 지향한다.</p>
<p>[기획(Biz)] → [개발(Dev)] → [배포/운영(Ops)] → [피드백] → 반복</p>
<h2 id="2-마이크로서비스-아키텍쳐msa-핵심-개념">2. 마이크로서비스 아키텍쳐(MSA) 핵심 개념</h2>
<blockquote>
<p>에자일로 빠르게 개발하기 위해서는
비즈니스 영역을 잘 알아야하고,
도메인 중심으로 소프트웨어를 설계하고,
설계할 때는 이벤트스토밍으로 쉽게 풀어간다.</p>
</blockquote>
<h3 id="21-에자일agile">2.1. 에자일(Agile)</h3>
<p>계획 다 짜놓고 오래 개발하지 말고
조금씩 만들고 빨리 테스트하면서 고쳐 나간다.
=&gt; 고객 가치를 빠르게 전달하는 개발 방법론</p>
<h3 id="22-클라우드-네이티브-애플리케이션">2.2. 클라우드 네이티브 애플리케이션</h3>
<blockquote>
<p>마이크로서비스 == 클라우드 네이티브 애플리케이션</p>
</blockquote>
<p>애자일을 실현하기 위한 기술적 환경, 즉 ‘어디서 어떻게 개발·배포할 것인가’에 대한 방식
CSP (Cloud Service Provider, 예: AWS, Azure, GCP)가 인프라를 관리하지만, 네이티브로 잘하는, 최적화된 이라는 의미를 담는다.
클라우드 인프라에 최적화된 방식으로 앱을 만들고,  서비스가 요청이 많아지면 자동으로 서비스를 늘려준다.</p>
<h3 id="23-모놀리식-아키텍쳐-vs-마이크로서비스-아키텍쳐">2.3. 모놀리식 아키텍쳐 VS 마이크로서비스 아키텍쳐</h3>
<h4 id="모놀리식-아키텍쳐">모놀리식 아키텍쳐</h4>
<ul>
<li><p>✔ 동기 호출이 일반적
내부 메서드 간 호출이므로 즉시 응답을 기다리는 구조 (동기적)</p>
</li>
<li><p>✔ 강한 결합 (Tight Coupling)
모든 컴포넌트가 하나의 애플리케이션 안에 tightly 연결되어 있음
하나가 바뀌면 다른 것도 영향을 받음</p>
</li>
<li><p>✔ 공유된 통합 DB 사용
하나의 중앙 DB를 모든 모듈이 함께 사용 </p>
</li>
</ul>
<h4 id="마이크로서비스-아키텍쳐msa">마이크로서비스 아키텍쳐(MSA)</h4>
<p>기능 단위(도메인 단위)로 작은 서비스들로 나누어서 개발하고 배포한다. 
각 서비스는 독립적인 DB와 배포 주기를 가진다. 
<strong>서로 REST API와 메시지 큐로 통신</strong>한다. </p>
<ul>
<li><p>🔁 동기/비동기 호출 모두 가능
마이크로서비스 간 통신은 보통 다음 둘 중 하나로 함:</p>
<ul>
<li>✅ 동기 호출 (REST API): 요청 → 응답 즉시 받음</li>
<li>✅ 비동기 호출 (Kafka, RabbitMQ 등): 메시지를 보내고 응답을 기다리지 않음
→ 느슨한 결합(Loosely Coupled) 가능</li>
</ul>
</li>
<li><p>❌ 공유 DB 사용 X (원칙적으로 금지)
각 서비스는 자신의 DB만 사용해야 함
다른 서비스의 DB에 직접 접근하지 않고, API나 메시지로 요청</p>
</li>
</ul>
<h3 id="23-도메인domain">2.3. 도메인(Domain)</h3>
<p><strong>Domain</strong> : 비즈니스 문제 영역(주문, 결제 등)</p>
<ul>
<li>우리가 만드는 서비스가 다루는 주제</li>
<li>업무 중심의 기능 단위</li>
<li><em>Bounded Context*</em> : 의미가 일관된 도메인 단위로 구분(주문: Order BC )</li>
</ul>
<p><strong>바운디드 컨텍스트(Bounded Context)</strong>
: 의미가 일관된 도메인의 경계
같은 단어라도 맥락에 따라 의미가 달라서 모델을 하나로 통합하면 문제가 된다.
하나의 컨텍스트 내부에서는 용어와 모델의 의미가 명확해야 한다. </p>
<table>
<thead>
<tr>
<th>바운디드 컨텍스트</th>
<th>주요 모델</th>
<th>핵심 책임</th>
</tr>
</thead>
<tbody><tr>
<td>주문(Order BC)</td>
<td>주문, 상품, 수량</td>
<td>상품 주문, 상태 관리</td>
</tr>
<tr>
<td>결제(Payment BC)</td>
<td>결제정보, 카드</td>
<td>결제 처리, 환불 등</td>
</tr>
<tr>
<td>배송(Shipping BC)</td>
<td>송장, 주소</td>
<td>배송 출발, 도착 확인 등</td>
</tr>
<tr>
<td>고객(CRM BC)</td>
<td>고객, 주소록</td>
<td>고객정보, 연락처</td>
</tr>
</tbody></table>
<h3 id="24-ddd-도메인-주도-설계">2.4. DDD (도메인 주도 설계)</h3>
<p>복잡한 비즈니스 요구사항을 잘 반영하기 위해, <strong>도메인을 중심으로 소프트웨어를 설계</strong>하는 방법론
=&gt; 개발자와 기획자가 같은 언어로 도메인을 잘게 나눠서 이해하고 설계</p>
<h3 id="25-ddd의-유형">2.5. DDD의 유형</h3>
<p>어떤 관점으로 도메인을 쪼갤지는 비즈니스 관점과 기술 관점에 따라 달라진다. 
사용자를 기준으로, 인프라를 기준으로, 쪼개진 하위 도메인을 세 가지 유형으로 분류할 수 있다. </p>
<ul>
<li>core domain : 상대적으로 가장 중요한 코어 도메인, 사용자와 인접한 부분(주문, 상품)</li>
<li>supportive : 내부 지원 기능, 출시되어 있는 것을 그대로 가져오는 부분(외부 솔루션으로 대체 가능)</li>
<li>generic : 일반 기능 (외부 솔루션을 사용한다. SaaS)</li>
</ul>
<blockquote>
<p>✅ Core 도메인은 내부에서 집중적으로 설계해야 하며,
Supportive와 Generic은 외부 솔루션이나 오픈소스 도입으로 대체 가능.</p>
</blockquote>
<hr />
<h2 id="3-애자일-개발은-위한-접근법-3가지">3. 애자일 개발은 위한 접근법 3가지</h2>
<p>애자일은 빠르게 변화하는 요구사항을 민첩하게 대응하고, 고객 중심의 가치를 빠르게 제공하기 위한 개발 방법론이다. 이를 실현하기 위해서 는 3가지의 핵심 아키텍쳐/프로세스를 가진다.</p>
<h3 id="1마이크로-서비스-아키텍쳐">1.마이크로 서비스 아키텍쳐</h3>
<ul>
<li>시스템을 작고 독립적인 서비스 단위로 분할</li>
<li>각 서비스는 자기만의 DB 와 로직을 가지며 독립적인 배포/운영</li>
<li>서비스 간의 직접 api 통신을 지양한다. (order가 직접 payment를 호출하지 않도록)</li>
</ul>
<h3 id="2이벤트-드리븐-아키텍쳐">2.이벤트 드리븐 아키텍쳐</h3>
<blockquote>
<p>서비스 간에 직접 통신하지 않고, pubsub이 <strong>이벤트라고 하는 제3의 공유 공간</strong>에 남기고 필요한 서비스가 구독(Subscribe)해서 반응하는 방식</p>
</blockquote>
<ul>
<li>주문이 통신에 필요한 정보를 이벤트로 잘 정리해서 이벤트 store에 저장한다.</li>
<li>주문팀의 코드 수정없이 이벤트 store에서 가져가서 사용한다.</li>
<li>메시지 큐 기반의 이벤트를 통신한다. </li>
</ul>
<table>
<thead>
<tr>
<th>용어</th>
<th>의미</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Publisher (발행자)</strong></td>
<td>이벤트를 생성해서 공유지대(PubSub)에 올림 (예: 주문 서비스)</td>
</tr>
<tr>
<td><strong>Subscriber (구독자)</strong></td>
<td>그 이벤트를 듣고 필요한 일을 함 (예: 결제 서비스, 배송 서비스)</td>
</tr>
<tr>
<td><strong>Pub/Sub 시스템</strong></td>
<td>Kafka, RabbitMQ 같은 <strong>중간 전달자(이벤트 저장소)</strong></td>
</tr>
</tbody></table>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ffe620a8-12b2-4bef-8eb4-e7b1a844d5a3/image.png" /></p>
<ul>
<li>서비스 간의 느슨한 결합</li>
<li>높은 확장성 및 유연성</li>
</ul>
<h3 id="3비즈데브옵스-프로세스bizdevops">3.비즈데브옵스 프로세스(bizdevops)</h3>
<ul>
<li>기획(Biz), 개발(Dev), 운영(Ops) 부서 간의 벽을 허물고 하나의 통합된 프로세스로 연결</li>
<li>고객의 피드백을 빠르게 반영하고, 전사적으로 서비스 개선 사이클을 단축</li>
</ul>
<pre><code>[Biz: 요구사항 정의]
      ↓
[Dev: 기능 설계 및 개발]
      ↓
[Ops: 배포 및 모니터링]
      ↑
[지속적 피드백 &amp; 개선]</code></pre><hr />
<h2 id="4-도메인-주도-설계ddd---자가치유적-구조화">4. 도메인 주도 설계(DDD) - 자가치유적 구조화</h2>
<p>DDD는 복잡한 비즈니스 요구를 반영한 소프트웨어를 만들기 위한 설계 철학과 실천 기법</p>
<blockquote>
<p>비즈니스 도메인에 집중해서 모델 중심의 설계를 지향한다. </p>
</blockquote>
<p>설계는 개발자와 도메인 전문가가 공통의 언어를 기반으로 협업한다. </p>
<p><strong>자가치유적 구조화</strong></p>
<ul>
<li>10,000 피트뷰로 DDD의 핵심 개념들을 전체구조를 이해하고, 개발 단계에서 top-down 방식으로 전체적인 큰 틀을 잡아서 구체화한다. </li>
<li>도메인 중심의 구조화로 내부에서 스스로 구조적 문제를 치유하고, 유지보수 가능한 구조를 의미한다. </li>
</ul>
<h3 id="41-ddd와-event-storming">4.1. DDD와 event storming</h3>
<ol>
<li><p>코어core와 지원support 부분으로 나눈다.
core : 핵심적, 잦은 변경 필요
support : 배포주기 잦지 않은 영역, 일부 사용자 한정</p>
</li>
<li><p>Business capability단위로 나눈다. </p>
</li>
</ol>
<ul>
<li>비즈니스 수행에 필요한 독립적 기능 단위로 분리한다. </li>
<li>조직도나 부서 구성에 맞춘다.</li>
<li>주문팀, 배송팀, 마케팅팀 등</li>
</ul>
<ol start="3">
<li>sub domain으로 나눈다. </li>
</ol>
<ul>
<li>업무 전문성 기준으로 분리한다.</li>
<li>하나의 도메인을 여러 하위 도메인으로 구분한다. </li>
<li>배송 도메인 -&gt; 송장 관리, 배송 추적, 수거 요청 등</li>
<li>회사마다 다르게 분리한다.</li>
</ul>
<ol start="4">
<li>aggregate 단위로 나눈다. </li>
</ol>
<ul>
<li>도메인 모델의 원자적 단위</li>
<li>더 이상 쪼갤 수 없게 나눈다. </li>
<li>ACID 가 준수되어야 하는 원자적 단위</li>
<li>*<em>Aggregate 는 table 에 준한다. *</em></li>
</ul>
<hr />
<h2 id="5-이벤트-스토밍event-storming">5. 이벤트 스토밍(Event Storming)</h2>
<p>도메인에서 일어나는 <strong>이벤드(사건) 을 중심</strong>으로 모델링한다.
서비스에 어떤일이 일어나는지를 <strong>포스트잇 붙이듯 정리하면서 모델링</strong>하는 방법
=&gt; DDD로 모델링하는 방법이 이벤트스토밍이다.</p>
<blockquote>
<p>복잡한 도메인을 시각적으로 탐색하고 모델링하는 기법
도메인 주도 설계(DDD)의 핵심 기법 중 하나로,
포스트잇을 이용해 도메인 안에서 발생하는 이벤트를 중심으로 흐름을 그려가며
모든 이해관계자(개발자, 기획자, 디자이너 등)가 함께 소통하고 도메인을 설계합니다.</p>
</blockquote>
<h3 id="51-구성-요소">5.1. 구성 요소</h3>
<table>
<thead>
<tr>
<th>구성 요소</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Domain Event</strong></td>
<td>도메인에서 실제로 일어난 사건. 시스템의 상태를 변화시킨 <strong>사실(Fact)</strong> 또는 결과 (예: ‘주문이 생성되었다’) <br />📌 <strong>과거형(PP형)</strong> 으로 작성</td>
</tr>
<tr>
<td><strong>Command</strong></td>
<td>사용자의 <strong>의도나 요청</strong>을 나타내며, 시스템이 처리해야 할 행동 (예: ‘주문을 생성한다’) <br />📌 <strong>현재형</strong> 으로 작성</td>
</tr>
<tr>
<td><strong>Actor</strong></td>
<td>Command를 발생시키는 주체, 즉 사용자나 외부 시스템</td>
</tr>
<tr>
<td><strong>Aggregate</strong></td>
<td>관련된 데이터와 로직이 모인 덩어리로, 여러 Entity, Value Object로 구성된 <strong>도메인의 일관성 단위</strong></td>
</tr>
<tr>
<td><strong>Policy</strong></td>
<td>특정 이벤트가 발생했을 때 <strong>자동으로 실행되는 비즈니스 규칙</strong>이나 처리 로직 (예: '주문이 생성되면 결제 요청')   *<em>Event에 대한 반응 *</em></td>
</tr>
<tr>
<td><strong>Read Model</strong></td>
<td>사용자에게 보여지는 데이터, 또는 Command 실행에 필요한 데이터를 효율적으로 제공하기 위한 모델 (CQRS 기반)</td>
</tr>
</tbody></table>
<p>Domain Event : 발생한 사실,결과, OUTPUT - pp형으로 작성,행동에 따른 결과
Command : 의사결정, INPUT, API, UI 버튼 - 현재형으로 작성,행동
Actor : 사용자
Aggregate : 구현제 덩어리, 시스템, 모듈 - 하나 이상의 엔터티, value objects 의 집합체
Policy : 정책, 반응 - Event에 대한 반응
Read Model : Command에 필요한 자료 - 유저가 참고하는 데이터, CQRS으로 수집</p>
<hr />
<h2 id="6-이벤트스토밍eventstorming-구현">6. 이벤트스토밍(Eventstorming) 구현</h2>
<p>🔁 이벤트스토밍 절차 요약
<strong>도메인 이벤트</strong> 발굴 (무엇이 일어났는가?)</p>
<p><strong>커맨드</strong>로 인한 인과 관계 정리 (무엇을 했기에?)</p>
<p><strong>정책</strong>에 따라 처리 방식 정의 (어떻게 반응할 것인가?)</p>
<p><strong>에그리게이트</strong>로 상태를 관리 (무엇이 바뀌는가?)</p>
<p><strong>리드모델/조회모델</strong> 정의 (사용자에게 어떤 정보를 보여줄까?)</p>
<p><strong>바운디드 컨텍스트</strong>로 경계 나누기 (어떤 책임을 어느 팀이 가질까?)</p>
<ul>
<li>모노릭스 아키텍쳐
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d474eaf0-7d26-4b06-9475-74a4364fe747/image.png" /></li>
<li>마이크로서비스 아키텍쳐
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/dce0bbcf-f00e-42b2-aa0b-37fc9bd514cc/image.png" /></li>
</ul>
<ul>
<li><p>&quot;Event는 domain 전문자(해당 팀)이 책임진다.&quot;
도메인 이벤트는 <em>무엇이 일어났는가</em> 를 나타내고, 해당 도메인을 잘 아는 팀이 작성한다.
<code>예약이 완료되었다</code> 는 예약관리팀의 책임!!!!</p>
</li>
<li><p>“Policy은 다른 집 자식이다!” 
→ 정책은 다른 도메인의 관심사에 반응으로, 다른 팀/컨텍스트가 소유하는 것이 맞음
<code>예약이 완료되면 알림을 보낸다</code> 는 알림팀의 policy!!!!!!!!</p>
</li>
</ul>
<h3 id="command">Command</h3>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/0b1af05f-c1d8-496b-8c1b-ebf8697636f2/image.png" /></p>
<ul>
<li>view -&gt; command -&gt; aggregate -&gt; domain event</li>
<li>command는 Aggregate를 통해서 도메인 상태를 변경</li>
<li>결과로 Domain Event를 발생</li>
</ul>
<h3 id="policy">Policy</h3>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/9cbd4d3c-3213-4e02-8e32-824ebf08960b/image.png" /></p>
<ul>
<li>Domain Event 발생 시, 구독하는 Policy가 자동 실행</li>
<li>Policy도 Aggregate에 상태 변경 요청 가능 </li>
<li><blockquote>
<p>또다른 Event 발생</p>
</blockquote>
</li>
<li><blockquote>
<p>다른 Command 호출 </p>
</blockquote>
</li>
<li><strong>whenever ~할 때마다</strong> 를 붙여서 자연스러우면 <strong>Policy을</strong> 붙인다.</li>
</ul>
<h3 id="domain-event">Domain Event</h3>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/2d8ed116-9dfd-4256-b583-1635437b4ce2/image.png" /> </p>
<ul>
<li>하나의 Event가 여러 Policy를 발생시킬 수 있다.</li>
<li>Policy는 필요에 따라 Aggregate 를 호출하거나 새로운 Command로 이어진다. </li>
</ul>
<h3 id="aggregate">Aggregate</h3>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/494ab0dc-b30f-403d-b72f-5997d853b7d2/image.png" /></p>
<ul>
<li>같은 Entity를 사용하는 연관 있는 도메인 이벤트들의 집합</li>
</ul>
<hr />
<h2 id="7-시나리오--이벤트스토밍-적용">7. 시나리오 : 이벤트스토밍 적용</h2>
<h3 id="기초-시나리오1">기초 시나리오1</h3>
<ol>
<li>고객이 상품을 선택하여 주문한다.</li>
<li>주문이 되면 상품 배송을 시작한다.</li>
<li>배송이 완료되면 상품의 재고량이 감소한다.</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/572e5779-7714-4c29-8f2d-0bc95a4dd8e6/image.png" /></p>
<p><strong>Policy는 &quot;자기 자리를 찾아가야 한다&quot;</strong></p>
<ul>
<li>Command는 API나 UI로부터 발생하는 사용자의 명시적 요청</li>
<li>Policy는 특정 Event에 반응하는 자동 처리 로직</li>
<li>따라서 <strong>Policy는 Command처럼 사용자의 요청에 직접 연결되면 안 된다</strong></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c5b692a1-a1db-42f6-b817-b4af38732535/image.png" />
다음과 같이 수정해야한다. </p>
<ul>
<li>사용자가 재고차감을 하는 것이 아니라 배송이 완료될 때마다 재고감소가 된다는 것이다. </li>
<li>사용자가 프론트에서 배송시작을 누르는 것이 아니라 주문할 때마다 배송이 시작되는 것이다.</li>
</ul>
<p><strong>Policy는 Event에 반응하며 자체적으로 실행되는 &quot;백그라운드 데몬&quot;처럼 작동한다.</strong></p>
<h3 id="시나리오2">시나리오2</h3>
<ol>
<li>고객이 주문을 취소할 수 있다 (Customer can cancel order)</li>
<li>주문이 취소되면 배달이 취소된다 (Whenever customer cancel an order, cook or delivery is canceled too)</li>
<li>배달이 수거되면 재고량이 증가한다</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/2fed966c-30a2-4f08-87c9-2568f23436cd/image.png" />
상품팀에 재고차감은 배송팀의 도메인 이벤트에 의해서 일어난다. </p>
<ul>
<li><p>주문팀은 이벤트를 발행(publish)할 뿐, 누가 이걸 구독(subscribe)할지 알지 못한다.</p>
</li>
<li><p>Publish는 목적지 없이 브로드캐스트
→ OrderCancelled 이벤트는 여러 팀(조리팀, 배달팀 등)이 자율적으로 구독하여 정책 실행</p>
</li>
</ul>
<blockquote>
<p>  Policy는 이벤트 소비자가 정의하고, publish는 소비자에 대해 몰라도 된다. -&gt; 느슨한 결합</p>
</blockquote>
<hr />
<h2 id="8-msa를-하되-비동기-메시징을-만드는-방법">8. MSA를 하되 비동기 메시징을 만드는 방법</h2>
<h3 id="단순한-resr-api-연동은-문제가-된다">단순한 RESR API 연동은 문제가 된다.</h3>
<blockquote>
<p>애써 나누어 놓은게 의미가 없어져 버린다.</p>
</blockquote>
<h3 id="비동기-메시징을-이용한-약결합-구조">비동기 메시징을 이용한 약결합 구조</h3>
<blockquote>
<p>해당 서비스가 스스로 생각해서 작업을 수행한다. </p>
</blockquote>
<ul>
<li>pub/sub 모델을 사용한다. : 발행과 구독으로 분리한다.</li>
<li>비동기 전송 : 응답을 기다리지 않는다.</li>
<li>유연성 : 수신자가 없어도 메시지 전송 가능!</li>
<li>내결함성 : 실패해도 재시도</li>
</ul>
<pre><code>[Service A] --이벤트 발행--&gt; [Kafka Topic] --구독--&gt; [Service B, C]</code></pre><h3 id="1-마이크로서비스-아키텍쳐">1. 마이크로서비스 아키텍쳐</h3>
<blockquote>
<p>시스템을 여러 개의 작고 독립된 서비스로 분리하여 구성
각 서비스는 자체 데이터베이스와 도메인을 갖고 독립 배포됨</p>
</blockquote>
<h3 id="2-이벤트-드리븐-아키텍쳐">2. 이벤트 드리븐 아키텍쳐</h3>
<blockquote>
<p>서비스 간의 직접 REST API로 통신하는 것이 아니라, <strong>이벤트를 발행(pub)하고 구독(sub)하는 구조</strong>
-&gt; 느슨한 결합, 확장성 확보, 장애 격리 가능하다.</p>
</blockquote>
<p>이벤트 기반 : 서비스는 필요한 정보를 이벤트를 통해 비동기로 전달한다. </p>
<p>브로드캐스트 방식 : 발행자는 목적지를 모르고 보내고, 수신자는 필요한 것만 듣는다. </p>
<h3 id="시나리오-구성-방식">시나리오 구성 방식</h3>
<ul>
<li><p>시나리오에서 결론을 먼저 가져온다. 
=&gt; 도출된 결과를 중심으로 Domain Event를 정의
=&gt; 도메인의 핵심 행동을 동사 pp형으로 표현</p>
</li>
<li><p>command는 사용자의 요청으로 동사 원형으로 표현</p>
</li>
<li><p>aggregate 는 상태 변경과 이벤트 발행 객체</p>
</li>
<li><p>policy는 이벤트에 반응하는 비즈니스 규칙이 된다. </p>
</li>
</ul>
<p><strong>Java 구현 대응</strong></p>
<table>
<thead>
<tr>
<th>개념</th>
<th>설명</th>
<th>Java 대응</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Command</strong></td>
<td>사용자 요청, API</td>
<td>REST API (<code>@PostMapping</code>, <code>@DeleteMapping</code>)</td>
</tr>
<tr>
<td><strong>Domain Event</strong></td>
<td>발생한 결과</td>
<td>Java 클래스 (POJO, JSON 직렬화)</td>
</tr>
<tr>
<td><strong>Aggregate</strong></td>
<td>상태 변경 및 이벤트 발행 객체</td>
<td>엔티티 + 상태관리</td>
</tr>
<tr>
<td><strong>Policy</strong></td>
<td>이벤트에 반응하는 비즈니스 규칙</td>
<td>비동기 이벤트 리스너 (<code>@KafkaListener</code>, 데몬 등)</td>
</tr>
</tbody></table>
<p>어그리거트 : Command를 받아 상태를 변경하고 Event를 발행하는 도메인 객체 묶음 (main이 되는 DB)</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/440d616a-af00-4db9-b8c5-7781d342d9aa/image.png" /></p>
<ul>
<li>aggregate는 도메인 내 핵심 객체의 그룹이다. </li>
<li>실제 DB 테이블 단위에 대응된다 </li>
<li>command를 통해 변화하고 결과로 event가 생성되어 외부로 발송된다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/268e39a3-cf3f-4828-9338-1c39770ecb88/image.png" /></p>
<ul>
<li>어그리거트는 Event에서 <code>속성 동기화</code> 버튼으로 부여할 수 있다. </li>
<li>event가 발생했을 때 aggregate 객체의 속성을 자동으로 갱신 가능</li>
</ul>
<p><strong>도메인 구분</strong></p>
<ul>
<li>order는 core</li>
<li>delivery는 support</li>
<li>product는 Context Dependent</li>
</ul>
<h2 id="9-command-의-생명주기와-이벤트-트리거">9. Command 의 생명주기와 이벤트 트리거</h2>
<p>Command는 사용자의 요청에 해당하며, 시스템의 상태 변경을 유발한다. </p>
<p>JAVA 기반 시스템에서 command 처리 중 <strong>생명주기 이벤트 (Lifecycle Hook)</strong> 으로 도메인 이벤트를 발생시키거나 후속처리를 트리거할 수 있다.</p>
<table>
<thead>
<tr>
<th>생명주기</th>
<th>실행 시점</th>
<th>활용 예</th>
</tr>
</thead>
<tbody><tr>
<td><code>@PrePersist</code></td>
<td>저장되기 직전</td>
<td>유효성 검사, 로깅, 생성 준비</td>
</tr>
<tr>
<td><code>@PostPersist</code></td>
<td>저장된 직후</td>
<td><strong>이벤트 발행</strong> <code>OrderPlaced</code></td>
</tr>
<tr>
<td><code>@PreUpdate</code></td>
<td>변경되기 직전</td>
<td>상태 체크, 변경 조건 확인</td>
</tr>
<tr>
<td><code>@PostUpdate</code></td>
<td>변경된 직후</td>
<td><strong>이벤트 발행</strong> <code>InventoryDecreased</code>, <code>DeliveryCompleted</code></td>
</tr>
<tr>
<td><code>@PreRemove</code></td>
<td>삭제되기 직전</td>
<td><strong>삭제 전 이벤트 발행</strong> <code>OrderCancelled</code></td>
</tr>
<tr>
<td><code>@PostRemove</code></td>
<td>삭제된 직후</td>
<td>로그 기록, 자원 정리</td>
</tr>
</tbody></table>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/1cd8ff3a-f52f-4811-ac66-3842fc5f00ae/image.png" /></p>
<p>command는 POST를 기본값으로 가진다. 
주문하기 command는 POST로 메서드를 지정한다. 
취소하기 command는 DELETE 메서드를 지정한다. </p>
<ol>
<li>사용자 command 보냄 (POST /orders)</li>
<li>new로 객체를 만든다. (아직은 비영속 상태)</li>
<li>save()함수를 실행하면서 데이터를 영속화된다. </li>
</ol>
<p>영속화되는 시점에 해당되는 트리거는 </p>
<ul>
<li>Pre Persist (저장 전에), </li>
<li>Post Persist (저장 후에) 가 해당된다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/63753b8b-a568-40b5-a73f-40a41e3bcff3/image.png" /></li>
</ul>
<table>
<thead>
<tr>
<th>구분</th>
<th>특징</th>
<th>사용 예</th>
</tr>
</thead>
<tbody><tr>
<td>Pre 계열</td>
<td>트랜잭션 중 실행됨, 예외 시 롤백 가능</td>
<td><code>@PrePersist</code>, <code>@PreRemove</code></td>
</tr>
<tr>
<td>Post 계열</td>
<td>트랜잭션 이후 실행됨, DB 반영 완료 후</td>
<td><code>@PostPersist</code>, <code>@PostUpdate</code></td>
</tr>
</tbody></table>
<hr />
<h2 id="cqrscommand-query-responsibility-segregation">CQRS(Command Query Responsibility Segregation)</h2>
<h3 id="cqrs란">CQRS란?</h3>
<blockquote>
<p>Command와 Query의 책임을 분리하여 처리하는 아키텍처 패턴</p>
</blockquote>
<ul>
<li><p>Command: 시스템의 상태 변경을 유발하는 동작 (쓰기)</p>
</li>
<li><p>Query: 시스템의 상태를 조회하는 동작 (읽기)</p>
</li>
<li><p>쓰기와 읽기의 모델과 저장소를 분리한다.</p>
</li>
</ul>
<h3 id="cqrs가-필요한-이유">CQRS가 필요한 이유?</h3>
<blockquote>
<p>마이크로서비스로 나눈 이상 각자의 데이터가 다 다르고, 각 도메인이 서로 다른 DB를 사용한다. 
=&gt; 직접적인 join이나 통합 쿼리가 불가능하다.</p>
</blockquote>
<ul>
<li><p>필요에 의해서 데이터를 모아두고 돌아다니는 도메인 이벤트(Event)를 모아두고 이에 따라 갱신한다. </p>
</li>
<li><p>읽기 전용 모델(Read model)을 따로 구성한다. </p>
</li>
<li><p>이벤트를 중심으로 데이터를 연동/갱신하는 구조를 <code>이벤트 드리븐 아키텍쳐</code> 또는 <code>CQRS</code>에서 구현한다. </p>
</li>
</ul>
<h3 id="cqrs와-event-driven의-연결">CQRS와 Event-driven의 연결</h3>
<blockquote>
<p>Event를 기반으로 데이터를 수신하고 Read Model을 객신하는 구조</p>
</blockquote>
<ul>
<li>CQRS : 특정 이벤트들을 받아서 하는 역할, 미리 만들어놓고 요청하면 만들어놓은 것을 읽기만 한다.</li>
<li>Event : 도메인 상태의 변경 사항을 나타낸다. </li>
<li>Read Model : event를 pub하여 조회 전용 데이터 구조(read model)을 구성</li>
<li>Query : 사용자의 요청에 대해 read model에서 조회</li>
</ul>
<p><strong>Query의 유형</strong></p>
<ul>
<li>query For Aggregate : get요청을 받아줄 수 있도록 만든 인터페이스, 단순히 select한다. 단일 조회</li>
<li>query For Multiful Aggregate : get를 여러번하는 것과 같다.</li>
</ul>
<h3 id="예시--마이페이지-조회">예시 : 마이페이지 조회</h3>
<h4 id="문제">문제</h4>
<ul>
<li>order, delivery, stock 도메인이 각기 다른 DB를 사용한다 </li>
<li>사용자가 마이페이지에 들어오면, 모든 데이터가 통합되어서 보여줘야 한다. </li>
</ul>
<h4 id="해결">해결</h4>
<ul>
<li>각 도메인의 이벤트를 마이페이지가 구독(subscribe)</li>
<li>이벤트를 기반으로 <strong>마이페이지 전용 read model</strong>을 생성/갱신</li>
</ul>
<h3 id="이벤트">이벤트</h3>
<ul>
<li><p>Create : OrderPlaced (주문 내역 생성)
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/3e2e3975-958b-418b-a928-7e3a4d572c9e/image.png" /></p>
</li>
<li><p>Update : Delivery completed (배송 상태 업데이트)
delivery가 complete될 때 Update한다.</p>
<ul>
<li>set : 어떻게 바꾸는가</li>
<li>where : 무엇을 바꾸는가</li>
</ul>
</li>
<li><p>Update : Order cancelled (주문 상태 취소로 변경</p>
</li>
<li><p>Update : shipping returned (반품 상태로 변경)</p>
</li>
</ul>
<h2 id="ddd-food-delivery-예제">DDD food delivery 예제</h2>
<p>기능적 요구사항</p>
<pre><code>- 고객이 메뉴를 선택하고, 선택한 메뉴에 대해 결제함으로써 주문이 발생한다.
- 주문이 되면 입점 상점주에게 주문정보가 전달된다.
- 상점주는 주문을 수락하거나 거절할 수 있다.
- 상점주는 요리 시작시와 완료 시점에 시스템에 상태를 입력한다.
- 고객은 아직 요리가 시작되지 않은 주문을 취소할 수 있다.
- 요리가 시작되면 고객 지역 인근의 라이더들에 배송정보가 전달된다.
- 라이더가 해당 요리를 Pick한 후, 출발전 앱에 등록하면 배송시작 정보가 앱을 통해 고객에게 통보된다.
- 고객은 주문상태를 중간중간 조회한다.
- 시스템은 주문상태가 바뀔 때 마다 카톡으로 알림을 발송한다.
- 라이더가 요리를 전달한뒤 배송확인 버튼을 탭하여, 모든 거래가 완료된다.</code></pre><p>(고객)
메뉴선택
메뉴결제
주문발생 : OrderPlaced</p>
<p>결제가 주된 것이 아님. 그저 행위일 뿐
요리가 시작되지 않은 요리를 취소할 수 있다는 로직일 뿐이고, 이는 나태내지 않는다 코드로 구현할 뿐</p>
<p>(상점주)
주문정보 받음
주문수락/거절
요리시작/완료
주문취소</p>
<p>주문 정보는 정보의 흐름이구만 ... 이벤트로써...? 아마 상점주에게만 가지는 정보일듯
수락했다 또는 거절했다의 행동 event =&gt; true, false로 분기처리가능
조리시작했다 또는 완료했다는 행동 event =&gt; command로 api를 각각나누는게 좋음</p>
<p>(라이더)
배송정보 전달
배송등록</p>
<h3 id="step1-event-command">step1. event, command</h3>
<ul>
<li>먼저 event를 만들어준다.</li>
<li>event의 결과를 도출하는 행위인 command를 만들어준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d6712da4-58b4-4a19-bcba-df7568f0cbd1/image.png" /></li>
</ul>
<hr />
<h3 id="step2-aggregate-actor">step2. aggregate, actor</h3>
<ul>
<li>aggregate 를 command와 event 사이에 넣어준다.</li>
<li>actor를 넣어준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/4860d079-7ead-484a-897b-2fe478aa90cd/image.png" /></li>
</ul>
<hr />
<h3 id="step3-policy">step3. policy</h3>
<ul>
<li><p>~ 되면, ~ 한다 와 같은 이벤트-반응 규칙을 명시한다.</p>
</li>
<li><p>주문이 되면, 상점주에게 주문정보가 전달된다. (-이면 -이다. policy가 필요하다)</p>
</li>
<li><p>요리가 시작되면, 라이더에게 배송정보가 전달된다. (policy 필요)</p>
</li>
<li><p>픽업이 되면, 사용자에게 주문상태가 전달된다. (policy 필요) 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/8984c91c-9ac5-44e0-936a-3e626c573c69/image.png" /></p>
</li>
</ul>
<hr />
<h3 id="step4-aggregate-필드-정의-및-command-event연결">step4. aggregate 필드 정의 및 command-event연결</h3>
<ul>
<li>aggregate 안에 필드값을 넣어준다.</li>
<li>command와 event를 이어준다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/96b8cecd-1a95-4bc9-a524-607ece4a6ea3/image.png" /></p>
<hr />
<h3 id="step5-event에-속성-동기화">step5. event에 속성 동기화</h3>
<ul>
<li>orderplaced, orcercancelled 는 속성 동기화를 해준다.</li>
<li>accepted, rejected 는 필요없는 속성foodid,status은 삭제해준다.</li>
<li>cookstarted, cookfinished 는 필요없는 속성foodid,status은 삭제해준다.</li>
<li>foodpicked, deliverycomfirme 은 속성 동기화를 해준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/eb1fb141-a84d-4821-8659-06291839fb2f/image.png" /></li>
</ul>
<hr />
<h3 id="step6-command에-따른-http-메서드-매핑">step6. command에 따른 HTTP 메서드 매핑</h3>
<blockquote>
<p>command 유형에 따라 적절한 HTTP Method를 지정</p>
</blockquote>
<ul>
<li>Create : order(POST) -&gt; orderplaced(post presist) = load order info
주문의 정보를 가져와서 주문 정보를 만든다.</li>
<li>Delete : cancel(DELETE) -&gt; ordercancelled(pre remove)</li>
<li>Update : isaccept(PUT) -&gt; accepted/rejected
엄격한 restful에서의 제한된 동사를 확장해서 작성한다. <strong>좁은 범위</strong>의 정보를 PUT 때린다. 어떤 정보를 줄지 요청 데이터에 적어준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/6813ffb7-084d-466b-a6b7-0c36457cd63d/image.png" /></li>
<li>Update : start(PUT) -&gt; cookstarted
요청 데이터를 넣어주지 않아도 된다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/6b08ac9d-8646-4ec3-810b-6f5a9c637058/image.png" /></li>
</ul>
<h3 id="step7-read-model-설계">step7. read model 설계</h3>
<blockquote>
<p>비동기 이벤트 기반으로 <strong>조회 전용 모델(read model)</strong>을 구성한다. (CQRS 적용)
서비스 간의 직접 요청-응답(REST)를 피하고,
*<em>필요한 데이터를 이벤트로 받아 저장한다. *</em></p>
</blockquote>
<p>address를 rider가 얻어오는 방법..
store에는 address 정보가 없어서 rider에게 줄 수 없음
policy에 order에서 address 를 가져오도록 해야한다. </p>
<p>read model</p>
<ul>
<li><p>Read : Query for Aggregate 로 단순 get를 해서 load delivery info에서 가져온다.
load delivery info -&gt; getAddress(read model) requset와 response의 관계로 이어지게 된다. 서비스가 중간에 죽으면 가져올 수 없게 되어 문제가 발생한다. (res/req를 많이 사용하지 않도록 지양한다.)</p>
</li>
<li><p>Create : orderplaced -&gt; load delivery info</p>
</li>
<li><p>Update : cookstart -&gt; load delivery info
위의 2과정으로 비동기할 수 있다.</p>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7726a22f-38e8-47a4-b8bb-edd5e1b4fe0a/image.png" />
📌 Rider가 address를 얻어오려면,
→ OrderPlaced 이벤트에 address 포함 → DeliveryReadModel에 저장됨</p>
<hr />
<p><a href="https://www.gitpod.io/">https://www.gitpod.io/</a></p>
<p>온라인에서 코드 실행 가능한 환경이다. </p>
<p>gitpod classic &gt; 원격환경 사용</p>
