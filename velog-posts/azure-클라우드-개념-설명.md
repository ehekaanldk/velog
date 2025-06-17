---
title: "[Azure] 클라우드 개념 설명"
date: "2025-06-10"
link: "https://velog.io/@ehekaanldk/Azure-%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EA%B0%9C%EB%85%90-%EC%84%A4%EB%AA%85"
series: "Uncategorized"
---

<h1 id="azure-자격증-목표">Azure 자격증 목표</h1>
<p>▶ Fundamental
  └ AZ-900 (기초) ✅</p>
<p>▶ Associate (중급)
  ├ AZ-104 (운영) 
  ├ AZ-204 (개발) ✅
  ├ AZ-500 (보안)
  ├ DP-203 (데이터 엔지니어)
  └ AI-102 (AI 엔지니어) ✅</p>
<p>▶ Expert (고급)
  ├ AZ-305 (솔루션 아키텍트)
  └ AZ-400 (DevOps 전문가) ✅</p>
<h1 id="클라우드-배포-유형">클라우드 배포 유형</h1>
<table>
<thead>
<tr>
<th>배포 유형</th>
<th>설명</th>
<th>사용 예시</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Public Cloud</strong> (공용 클라우드)</td>
<td>클라우드 제공자가 모든 인프라를 소유/운영하며, 다수의 고객이 공유하여 사용하는 환경</td>
<td>Microsoft Azure, AWS, Google Cloud 등</td>
</tr>
<tr>
<td><strong>Private Cloud</strong> (전용 클라우드)</td>
<td>특정 조직만을 위해 사용되는 클라우드. 자체 데이터 센터에서 운영하거나 타사에 위탁할 수 있음</td>
<td>금융기관, 보안 민감 기관</td>
</tr>
<tr>
<td><strong>Hybrid Cloud</strong> (하이브리드 클라우드)</td>
<td>Public과 Private Cloud를 <strong>혼합</strong>해서 사용하는 구조. 보안, 유연성, 기존 자산 활용 목적</td>
<td>On-Prem 시스템 + Azure 연동</td>
</tr>
<tr>
<td><strong>Multi-cloud</strong> (멀티 클라우드)</td>
<td>여러 개의 클라우드 공급자(Azure, AWS, GCP 등)를 함께 사용하는 전략</td>
<td>장애 대응, 비용 최적화 목적 등</td>
</tr>
</tbody></table>
<ul>
<li><strong>public cloud</strong>는 리소스를 <strong>Azure, AWS 같은 공급자의 Data Center</strong>에 배포한다. </li>
<li><strong>private cloud</strong>는 리소스를 <strong>회사 자체의 Data Center나 전용 server</strong>에 배포한다. </li>
<li><strong>hybrid cloud</strong>는 리소스를 <strong>일부는 사내에</strong> (온프레미스), <strong>일부는 퍼블릭 클라우드</strong>에 배포한다. </li>
<li><strong>Multi-cloud</strong>는 리소스를 <strong>Azure, AWS, GCP 등 여러 클라우드 공급자에 분산 배포</strong>한다.</li>
</ul>
<h3 id="azure-arc">Azure Arc</h3>
<p>Azure Arc-enabled services 으로 </p>
<blockquote>
<p>&quot;클라우드가 아닌 환경도 Azure에서 관리하고 싶다&quot; → 하이브리드 &amp; 멀티클라우드 관리용</p>
</blockquote>
<p>Azure 외부에 있는 자원(온프레미스, 다른 클라우드의 VM, 쿠버네틱스, DB 등) 을 Azure portal 에서 직접 관리할 수 있게 한다. </p>
<h3 id="azure-vmware-solution-avs">Azure VMware Solution (AVS)</h3>
<blockquote>
<p>&quot;프라이빗 클라우드를 Azure로 옮기고 싶다&quot; → 마이그레이션, 확장성 확보용</p>
</blockquote>
<ul>
<li>기존에 온프레미스에 있던 VMware 인프라를 그대로 Azure에 호스팅한다. </li>
<li>코드 수정없이 클라우드 전환 가능하다.</li>
<li>마이그레이션은 기존 시스템이나 데이터를 다른 환경으로 이전하는 것이다.</li>
</ul>
<h2 id="사용량-기반-모델pay-as-you-go">사용량 기반 모델(Pay-as-you-go)</h2>
<blockquote>
<p>클라우드에서 가장 기본적인 요금 모델
사용한 만큼만 요금 지불하는 방식이다.</p>
</blockquote>
<ul>
<li>정해진 요금 없음</li>
<li>리소스 사용 시점에만 과금 발생</li>
<li>테스트/개발/비정기적 서비스에 적합</li>
</ul>
<h3 id="capex">CapEx</h3>
<blockquote>
<p>일회성 선불 지출이다.
한번에 큰 비용을 지출하여 인프라를 구축한다.</p>
</blockquote>
<ul>
<li>서버, 스토리지, 데이터센터 등 자산을 직접 구매하고 보유한다.</li>
</ul>
<h3 id="opex">OpEx</h3>
<blockquote>
<p>시간이 지남에 따라 서비스나 제품에 쓰는 비용
운영하면서 발생하는 반복적인 비용이다.</p>
</blockquote>
<ul>
<li>사용량 기반의 탄력적인 비용 구조</li>
</ul>
<h3 id="클라우드-컴퓨팅--opex">클라우드 컴퓨팅 : OpEx</h3>
<ul>
<li><p>물리적 인프라인 전기,보안 ,데이터 센터의 비용이 들지 않고, </p>
</li>
<li><p>필요한 리소스만 사용하고 사용한 IT 리소스 비용만을 지불한다. </p>
</li>
<li><p>클라우드 기반 모델에서는 리소스의 요구사항을 올바르게 얻지 않아도 된다. </p>
</li>
<li><p>vm을 유연하게 추가하고, 제거하기 때문에 </p>
</li>
</ul>
<blockquote>
<p>클라우드 컴퓨팅은 다른 사람의 데이터센터에 컴퓨팅 파워와 스토리지를 빌리는 방법이다.</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c421571c-c832-41a6-b3a7-75227bb33c56/image.png" /></p>
<hr />
<h1 id="클라우드-서비스-사용-이점">클라우드 서비스 사용 이점</h1>
<h2 id="고가용성-및-스케일링">고가용성 및 스케일링</h2>
<h3 id="고가용성">고가용성</h3>
<blockquote>
<p>시스템이나 서비스가 장애 없이 지속적으로 동작할 수 있는 능력</p>
</blockquote>
<ul>
<li>목표 : 시스템 중단 없이 항상 사용 가능하게 만들기</li>
<li>하나의 데이터 센터가 문제가 생겨도 다른 지역이나 영역에서 서비스가 계속 유지되는 구조</li>
</ul>
<h3 id="sla">SLA</h3>
<blockquote>
<p>서비스 수준의 약정
서비스 또는 애플리케이션의 가용성과 관련된 백분율로 나타낸다. </p>
</blockquote>
<ul>
<li>SLA 99.9% → 한 달 기준 최대 허용 중단 시간 약 43.8분</li>
<li>각 Azure 서비스에는 고유한 SLA가 있다.</li>
<li>SLA은 고가용성 설계 여부에 따라 달라질 수 있다.</li>
</ul>
<h3 id="확장성">확장성</h3>
<blockquote>
<p>수요에 따라서 IT 자원의 크기나 수량을 조정하는 능력</p>
</blockquote>
<ul>
<li>스케일링 성능은 수요에 맞게 리소스를 조정하는 기능</li>
<li>서비스에 대해 초과 지불하지 않는다 : 사용한 것에서만 비용 지불</li>
</ul>
<h4 id="스케일링의-종류">스케일링의 종류</h4>
<ul>
<li><ol>
<li>수직 스케일링 : <strong>리소스의 기능</strong>을 늘리거나 줄이기
CPU, RAM을 더 추가 또는 다운</li>
</ol>
</li>
<li><ol start="2">
<li>수평 스케일링 : <strong>리소스의 수</strong>를 추가하거나 빼기
추가 가상 머신(VM) 또는 컨테이너를 추가</li>
</ol>
</li>
<li><p>Auto scaling은 Azure에서 조건에 따라서 스케일 업/다운을 수행할 수 있도록 지원</p>
</li>
</ul>
<h2 id="안정성-및-예측-가능성">안정성 및 예측 가능성</h2>
<h3 id="신뢰도">신뢰도</h3>
<p><strong>안정성 : 오류로부터 복구하고 계속 작동하는 시스템의 기능</strong>
Azure Well-Architected Framework
분산된 디자인 =&gt; 전 세계 지역에 리소스 배포 가능</p>
<h3 id="azure-well-architected-framework">Azure Well-Architected Framework</h3>
<blockquote>
<p>MS Azure에서 클라우드 기반 시스템을 잘 설계하고 운영하기 위해 만든 공식 가이드라인이다. </p>
</blockquote>
<ul>
<li>이 프레임워크는 “좋은 클라우드 아키텍처란 무엇인가?”라는 질문에 대한 기준을 제시한다.</li>
<li>안정적이고, 보안에 강하고, 성능이 뛰어나고, 비용이 효율적이고, 지속 가능한 시스템</li>
</ul>
<p>Azure가 안정성을 제공하는 방법</p>
<h3 id="예측">예측</h3>
<ol>
<li>성능 예측가능성</li>
</ol>
<ul>
<li>고객에게 긍정적인 환경을 제공하는 데 필요한 리소스를 예측하는 데 중점을 둔다. </li>
<li>자동 크기 조정 : 수요 충족을 위한 추가 리소스 배포, 수요 감소시 축소</li>
<li>부하 분산 및 고가용성 : 일부 오버로드를 덜 스트레스 가 많은 영역으로 리디렉션</li>
</ul>
<ol start="2">
<li>비용 예측가능성 </li>
</ol>
<ul>
<li>클라우드 지출 비용을 에측하거나 예측하는 데 중점을 둔다. </li>
<li>리소스 실시간 추적</li>
<li>리소스 모니터링</li>
<li>TCO(총 소유비용) 등으로 잠재적인 클라우드 지출 예측가능</li>
</ul>
<h2 id="보안-및-거버넌스">보안 및 거버넌스</h2>
<p>클라우드는 인터넷을 통한 IT 리소스 전달을 목적으로 하기 때문에, 클라우드 공급자가 일반적으로 DDoS(분산 서비스 거부) 공격과 같은 작업을 처리하는 데 특화되있다.</p>
<h3 id="거버넌스">거버넌스</h3>
<blockquote>
<p>조직의 자원(클라우드 자원)을 잘 통제하고, 규칙과 기준에 따라 운영되도록 관리하는 체계이다.</p>
</blockquote>
<p>&quot;이 시스템은 누가, 무엇을, 어떻게, 어디까지 사용할 수 있는가?&quot;
&quot;우리 회사 기준에 맞게 안전하게 잘 운영되고 있는가?&quot;
를 정의하고 감시한다. </p>
<h3 id="보안">보안</h3>
<blockquote>
<p>외부나 내부의 위협으로부터 시스템을 보호하는 것</p>
</blockquote>
<p>보안은 &quot;안전하게 막는것&quot;
거버넌스는 &quot;정해진 규칙에 따라 관리하는 것&quot;</p>
<h2 id="관리-효율성">관리 효율성</h2>
<p>클라우드 컴퓨팅에 대한 관리 효율성에는 두 가지 유형이 있다. </p>
<h3 id="클라우드-관리">클라우드 관리</h3>
<p>클라우드 리소스 관리에 관한 내용
클라우드에서 수행한다.</p>
<ul>
<li>필요에 따라 리소스 배포 크기를 자동 스케일링</li>
<li>미리 구성된 템플릿을 기반으로 리소스를 배포하여 수동 구성의 필요성 제거</li>
<li>리소스의 상태를 모니터링하고 실패한 리소스를 자동으로 바꿈</li>
<li>구성된 메트릭에 따라 자동 경고를 수신하므로 실시간으로 성능을 인식</li>
</ul>
<h3 id="클라우드에서의-관리">클라우드에서의 관리</h3>
<p>클라우드 환경 및 리소스를 관리하는 방법</p>
<ul>
<li>웹 포털을 통해서</li>
<li>CLI(명령줄 인터페이스) 사용</li>
<li>API 사용</li>
<li>PowerShell 사용</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/67563308-b62b-49c9-9a57-e78328d65f0a/image.png" /></p>
<h1 id="클라우드-서비스-유형">클라우드 서비스 유형</h1>
<h2 id="iaas--데이터-센터에서의-공간-임대">IaaS : 데이터 센터에서의 공간 임대</h2>
<p>IaaS(Infrastructure as a Service) 는 <strong>사용자에게 클라우드 리소스에 대한 최대 제어량</strong>을 제공한다. 
클라우드 서비스의 <strong>가장 유연한 범주</strong>이다. 
클라우드 공급자는 물리적 인프라와 인터넷에 대한 엑세스 유지하며, 사용자는 OS부터 애플리케이션까지 직접 관리한다. </p>
<table>
<thead>
<tr>
<th>주체</th>
<th>책임 영역</th>
</tr>
</thead>
<tbody><tr>
<td><strong>클라우드 공급자</strong></td>
<td>하드웨어, 네트워크 연결, 물리적 보안, 인터넷 연결 유지 관리</td>
</tr>
<tr>
<td><strong>사용자</strong></td>
<td><strong>운영체제 설치</strong>, 네트워크 구성, 애플리케이션 설치, 데이터베이스 및 스토리지 구성</td>
</tr>
</tbody></table>
<ul>
<li>예 : Azure의 가상머신</li>
</ul>
<p>IaaS의 일반적인 시나리오</p>
<ul>
<li>리프트 앤 시프트 방식 마이그레이션 : 기존에 On-premise(내부 서버실)에서 사용하던 시스템을 비슷한 형태로 클라우드로 옮기는 전략</li>
<li>테스트 및 개발 : 빠르게 개발하거나 테스트하기 위한 인프라 환경을 만들 때</li>
</ul>
<h2 id="paas--중간">PaaS : 중간</h2>
<p>PaaS(Platform as a Service) 는 <strong>사용자와 클라우드 공급자 간에 책임을 분할</strong>한다. 
운영체제 및 데이터베이스에 대한 라이선스, 패치는 걱정하지 않아도 된다. </p>
<ul>
<li>클라우드 공급자 : (물리적 인프라, 물리적 보안 및 인터넷 연결 유지 관리)+(운영체제, 미들웨어, 데이터베이스, 개발도구 및 비즈니스 인텔리전스 서비스 유지 관리)</li>
<li>사용자 : 애플리케이션 데이터와 코드만 관리</li>
</ul>
<table>
<thead>
<tr>
<th>주체</th>
<th>책임 영역</th>
</tr>
</thead>
<tbody><tr>
<td><strong>클라우드 공급자</strong></td>
<td>물리적 인프라, 보안, 인터넷 연결, <strong>운영체제</strong>, 미들웨어, <strong>데이터베이스</strong>, <strong>개발 도구</strong>, BI 서비스 등</td>
</tr>
<tr>
<td><strong>사용자</strong></td>
<td>*<em>데이터, 애플리케이션 코드 *</em></td>
</tr>
</tbody></table>
<ul>
<li>예 : Azure App Service, Azure SQL Database, Azure Logic Apps</li>
</ul>
<p>PaaS의 일반적인 시나리오</p>
<ul>
<li>개발 프레임워크 : 백엔드 설정 없이 빠르게 애플리케이션을 개발하고 배포 가능</li>
<li>분석 또는 비즈니스 인텔리전스 : 내장된 분석 도구와 AI 기능을 통해 데이터를 분석/마이닝 하고, 패턴을 찾고 결과를 예측하면서 비즈니스 의사 결정을 개선</li>
</ul>
<h2 id="saas--완전히-배포된-솔루션에-대한-비용을-지불">SaaS : 완전히 배포된 솔루션에 대한 비용을 지불</h2>
<p>SaaS(Software as a Service) 는 완전히 개발되고 운영되는 <strong>소프트웨어를 구독 형태</strong>로 사용하는 모델이다. 
제품 관점에서 가장 완벽한 클라우드 서비스 모델이다. 
기본적으로 완전히 개발된 애플리케이션을 임대하거나 사용한다. </p>
<p>사용자는 설치나 유지관리 걱정 없이 웹이나 앱을 통해서 서비스를 즉시 사용할 수 있다. 
클라우드 공급자는 모든 기술적 운영을 책임진다. </p>
<p>클라우드 공급자의 책임이 가장 크고, <strong>사용자에게는 최소한의 책임</strong>을 지는 모델이다.</p>
<table>
<thead>
<tr>
<th>주체</th>
<th>책임 영역</th>
</tr>
</thead>
<tbody><tr>
<td><strong>클라우드 공급자</strong></td>
<td>데이터 센터, 전원, 네트워크 연결, 물리적 보안, 애플리케이션 개발 및 유지관리</td>
</tr>
<tr>
<td><strong>사용자</strong></td>
<td>애플리케이션 사용, <strong>데이터 입력, 디바이스 권한 설정</strong> 등 최소한의 관리</td>
</tr>
</tbody></table>
<ul>
<li>예 : Microsoft 365
메일, 금융 SW, 메시징 애플리케이션 은 모두 SaaS 구현의 예이다. </li>
</ul>
<p>SaaS의 일반적인 시나리오</p>
<ul>
<li>메일 및 메시징</li>
<li>비즈니스 생산성 애플리케이션</li>
<li>재무 및 비용 추적</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a15b14b0-ab9e-48db-a0a6-59369b153bd6/image.png" /></p>
