---
title: "[Cloud] CSP 클라우드 서비스"
date: "2025-05-15"
link: "https://velog.io/@ehekaanldk/Cloud-CSP-%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EC%84%9C%EB%B9%84%EC%8A%A4"
series: "Uncategorized"
---

<h2 id="1-가상화-개요">1. 가상화 개요</h2>
<h3 id="11-가상화">1.1. 가상화</h3>
<p><strong>가상화</strong> : 물리적인 IT 자원을 논리적으로 분리하여, 여러 자원인 것 처험 사용할 수 있게 해주는 기술</p>
<p>가상화의 <strong>리소스</strong>는 대표적으로 <strong>CPU, Memory, Storage, Network</strong> 가 있다. </p>
<p><strong>가상화의 특징</strong></p>
<ul>
<li>자원의 효율적인 활용</li>
<li>격리성 보장</li>
<li>유연한 확장성 제공</li>
<li>중앙 집중화된 관리와 자동화</li>
<li>플랫폼과 운영체제의 독립성</li>
<li>비용 절감 및 유지보수 효율성 증가</li>
<li>클라우드와 컨테이너와의 높은 연계성</li>
</ul>
<p><strong>온프레미스 VS 클라우드</strong></p>
<ul>
<li><p>클라우드 : 클라우드는 회사에서 HW를 제공한다. HW를 빌려서 사용하는 경우</p>
</li>
<li><p>온프레미스 : 회사에서 서비스하기 위한 HW를 자체적으로 다 가지고 있는 경우이다.</p>
</li>
</ul>
<blockquote>
<p>가상화를 통해서 모든 IT자산을 가성화해서 동적이고 유연한 업무 인프라를구축한다.</p>
</blockquote>
<h3 id="12-컴퓨팅-환경의-발전사">1.2. 컴퓨팅 환경의 발전사</h3>
<ul>
<li><p><strong>서버</strong> : 서비스를 해주는 HW, SW, 사람, 머신 (테이블 담당서버)</p>
</li>
<li><p>베어메탈 : 물리 서버(HW) 위에 직접 애플리케이션을 실행하는 방식</p>
</li>
<li><p><strong>가상머신</strong> : 하나의 물리서버에서 <strong>하이퍼바이저</strong>를 이용해서 <strong>여러 개의 가상머신(VM)</strong>을 실행하는 방식</p>
</li>
<li><p>서버리스 : <strong>서버를 직접 관리하지 않고</strong>, 특정 이벤트가 발생하여 필요할 때 리소스를 가져와서 사용하고 반납하면서 <strong>코드만 실행</strong></p>
</li>
</ul>
<h3 id="13-하이퍼바이저">1.3. 하이퍼바이저</h3>
<p>전체적으로 물리적인 서버가 필요하다. 
<strong>하이퍼바이저</strong>는 <strong>1대의 물리 서버</strong>에서 여<strong>러 대의 가상머신을 실행</strong>할 수 있게 해주는 가상화 소프트웨어이다. </p>
<h4 id="하이퍼바이저의-역할">하이퍼바이저의 역할</h4>
<ul>
<li><p><strong>가상화</strong> : 가상머신(VM)을 만들어서 여러 Guest OS를 동시에 운영이 가능</p>
</li>
<li><p><strong>자원 할당</strong> : CPU, Memory, Disk 등 물리자원을 나누어 VM에 할당</p>
</li>
<li><p><strong>물리 자원 공유</strong> : 하나의 Host에서 동작하는 VM들은 <strong>Host의 물리 자원을 공유</strong>해서 사용</p>
</li>
<li><p><strong>가상 네트워크 구성</strong> : <strong>가상의 스위치를 만들어서</strong> VM 간 통신, VM &lt;-&gt; 외부 통신 을 위해서 네트워크 구성을 지원한다.</p>
</li>
<li><p><strong>마이그레이션</strong> : 가상머신(VM)을 하나의 Host에서 다른 Host로 이동(한 물리서버에서 다른 서버로 이동)</p>
<ul>
<li>VM을 옮기기 위해서는 <strong>shutdown 으로 중단 후</strong>에 HW 자원 file들을 다른 서버에 옮겨준다. </li>
<li><strong>라이브마이그레이션</strong> : VM을 종료하지 않고 실행 중인 상태 그대로 다른 서버에 옮겨준다. 
HW 자원을 두 서버가 공유하고 있어야 한다.</li>
</ul>
</li>
</ul>
<p><strong>하이퍼바이저의 종류</strong></p>
<h4 id="type-1--bare-metal">Type 1 : Bare-metal</h4>
<blockquote>
<p>운영체제 없이 물리적 서버(하드웨어) 위에 직접 설치되는 하이퍼바이저</p>
</blockquote>
<ul>
<li><p>물리적인 자원(CPU, RAM 등)을 가상의 자원(vCPU, vRAM)으로 나누어서 각 VM에 할당된다.</p>
</li>
<li><p>하이퍼바이저가 직접 하드웨어를 제어하여 가상의 자원으로 나눈다.</p>
</li>
<li><p>가상의 자원들로 이루어진 VM마다 자기만의 Guset OS를 가진다.</p>
</li>
<li><p><strong>자원 나누기(가상화)</strong> + <strong>자원 제어(CPU스케줄링, 메모리관리, I/O제어)</strong> : <strong>하이퍼바이저가 직접</strong></p>
</li>
</ul>
<h4 id="type-2--hosted">Type 2 : Hosted</h4>
<blockquote>
<p>기존의 컴퓨터의 운영체제 위에서 설치하는 하이퍼바이저</p>
</blockquote>
<ul>
<li><p>물리적인 서버 위에 Host OS를 올리고, 그 위에 애플리케이션처럼 하이퍼바이저를 올린다. </p>
</li>
<li><p>하이퍼바이저가 물리적인 자원을 가상자원으로 나누고 가상 머신 마다  Guset OS를 가진다.  </p>
</li>
<li><p><strong>자원 나누기(가상화)</strong> : <strong>하이퍼바이저가 수행</strong></p>
</li>
<li><p><strong>자원 제어</strong>(CPU스케줄링, 메모리관리, I/O제어) : <strong>Host OS가 수행</strong></p>
</li>
</ul>
<hr />
<h2 id="2-가상화-유형">2. 가상화 유형</h2>
<h3 id="21-가상화의-종류">2.1. 가상화의 종류</h3>
<ul>
<li>서버 가상화</li>
<li>스토리지 가상화</li>
<li>네트워크 가상화</li>
<li>데스크톱 가상화 </li>
</ul>
<h4 id="서버-가상화">서버 가상화</h4>
<blockquote>
<p>서버 가상화란, <strong>한 대의 물리서버</strong>에서 <strong>여러 개의 서버</strong>를 동시에 <strong>동작</strong>시키는 기술</p>
</blockquote>
<p><strong>하이퍼바이저 소프트웨어</strong>를 사용해서 물리서버의 자원(리소스)를 나누어서 여러 가상서버로 분할</p>
<p>커다란 색종이를 4개로 나누어서 4명이 색종이로 서로다른 학, 곰, 개구리, 토끼를 만드는 것이다. </p>
<ul>
<li>커다란 색종이 : 물리적인 서버 한 대</li>
<li>조각을 나누는 것 : 서버를 가상으로 나누는 것</li>
<li>각 사람들이 동물을 만드는 것 : 각 가상의 VM에서 다른 역할을 수행</li>
</ul>
<p>💡 EC2는 서버 가상화 기술을 활용하여 만든 AWS의 가상 서버 서비스</p>
<h4 id="스토리지-가상화">스토리지 가상화</h4>
<blockquote>
<p><strong>다수의 물리 스토리지</strong>를 <strong>논리적으로 통합</strong>하여 스토리지의 가용성과 편리성을 향상 시키는 기술</p>
</blockquote>
<p>여러 개의 물리적 스토리지를 묶어서 하나의 논리적 스토리 풀로 구성한다. </p>
<p>서버나 사용자에게는** 하나의 저장소**처럼 보여진다.</p>
<p>💡 EBS는 스토리지 가상화 기술을 기반으로 만들어진 AWS의 블록 스토리지 서비스</p>
<h4 id="네트워크-가상화">네트워크 가상화</h4>
<blockquote>
<p>실제 물리적인 네트워크 장비(케이블, 스위치, 라우터) 없이도, 가상의 네트워크 환경을 만드는 기술</p>
</blockquote>
<ul>
<li>가상 스위치 : VM 간의 통신을 위한 가상의 스위치</li>
<li>가상 네트워크 인터페이스(vnic) : VN에 설치된 가상의 랜카드처럼 작동하는 네트워크 장비</li>
</ul>
<p>사물실 내 1개의 인터넷 회선을 각 팀별로 따로 가상회선으로 나누어 사용한다. </p>
<p>💡 VPC는 네트워크 가상화를 활용하여 만든 AWS의 가상 네트워크 서비스</p>
<h4 id="데스크톱-가상화">데스크톱 가상화</h4>
<blockquote>
<p>내 컴퓨터 화면을 가상으로 만들어서, 다른 기기에서 원격으로 사용할 수 있게 하는 기술</p>
</blockquote>
<p>서버에서 여러 개의 가상 데스크톱 환경을 만들어두고, 사용자들은 각자의 데스크톱처럼 원격으로 접속해서 사용할 수 있다.</p>
<p>사용자 입장에서는 마치 자기 컴퓨터처럼 사용하지만, 실제로는 클라우드나 서버 안에서 돌아가는 가상 컴퓨터에 접속하는 것이다. </p>
<h2 id="3-가상-머신">3. 가상 머신</h2>
<h3 id="31-가상머신이란">3.1. 가상머신이란?</h3>
<blockquote>
<p>가상머신은 하이퍼바이저를 통해 만들어진 가상의 서버이다. </p>
</blockquote>
<h4 id="가상머신의-특징">가상머신의 특징</h4>
<ul>
<li>독립된 컴퓨터처럼 동작한다.</li>
<li>각 가상머신에서 OS도 설치할 수 있다. </li>
<li>유연하게 복사, 삭제, 중지, 이동이 쉽다.</li>
<li>하나가 꺼져도 다른 VM에 영향이 없어 안전하다.</li>
</ul>
<h2 id="4-컨테이너">4. 컨테이너</h2>
<h3 id="41-컨테이너란">4.1. 컨테이너란?</h3>
<blockquote>
<p>애플리케이션 실행에 필요한 모든 요소를 컨테이너라는 하나의 상자에 담아 배포, 실행하는 기술</p>
</blockquote>
<p>운영체제 수준의 가상화로 <strong>Host OS의 커널을 공유</strong>하여 <strong>애플리케이션 실행 환경</strong>을 가볍게 격리한다. </p>
<h4 id="컨테이너-vs-가상머신">컨테이너 VS 가상머신</h4>
<ul>
<li><p>컨테이너와 가상머신은 &quot;가상화를 한다&quot;는 점에서 같은 계열이다.</p>
</li>
<li><p>컨테이너는 운영체제 수준의 가상화 (Host OS의 커널을 공유)</p>
</li>
<li><p>가상머신은 운영체제가지 통제로 가상화</p>
</li>
</ul>
<p><strong>컨테이너 == 요리키트</strong>
냄비, 재료, 레시피까지 다 들어있어서 어디에 가든지 <strong>그대로 꺼내서 요리</strong>가 가능하다.</p>
<p><strong>가상머신 == 주방 전체</strong>
냉장고, 가스레인지, 조리도구, 싱크대까지 요리하기 위한 전체 주방 세트를 통으로 옮겨야 해서, 무겁고 크지만 완전히 독립적이다.</p>
<ul>
<li>가상머신의 구조<pre><code>[하드웨어]
 ↓
[하이퍼바이저]
 ↓
[ VM 1 ]     [ VM 2 ]
Guest OS     Guest OS
App          App
</code></pre></li>
</ul>
<pre><code>
- 컨테이너의 구조</code></pre><p>[하드웨어]
   ↓
[Host OS + 컨테이너 엔진(Docker)]
   ↓
[컨테이너 1]   [컨테이너 2]
 App + Libs     App + Libs</p>
<p>```</p>
<table>
<thead>
<tr>
<th>항목</th>
<th>컨테이너</th>
<th>가상머신</th>
</tr>
</thead>
<tbody><tr>
<td>가상화 수준</td>
<td>운영체제(OS) 수준</td>
<td>하드웨어 수준</td>
</tr>
<tr>
<td>커널</td>
<td>Host OS 커널 공유</td>
<td>Guest OS 커널 포함</td>
</tr>
<tr>
<td>무게</td>
<td>가볍고 빠름</td>
<td>무겁고 느림</td>
</tr>
<tr>
<td>분리성</td>
<td>비교적 약함 (커널 공유)</td>
<td>완전 분리 (OS 포함)</td>
</tr>
</tbody></table>
<h3 id="42-컨테이너-엔진">4.2. 컨테이너 엔진</h3>
<blockquote>
<p>컨테이너를 생성, 실행, 중지, 삭제하고, 컨테이너 이미지를 관리할 수 있는 도구</p>
</blockquote>
<p>컨테이너의 종류 =&gt; docker, podman ...</p>
<h4 id="docker">Docker</h4>
<blockquote>
<p>컨테이너 기반 가상화 기술을 제공하는 플랫폼
애플리케이션과 실행환경을 패키징하고, 배포, 실행</p>
</blockquote>
<p>*<em>1. 도커 이미지 *</em></p>
<ul>
<li>서비스 운영(애플리케이션 구동)에 필요한 프로그램, 소스코드, 라이브러리 등을 묶어 놓은 패키지 형태</li>
<li>이미지를 기반으로 실제 컨테이너가 실행된다.</li>
</ul>
<p><strong>2. 도커 허브</strong>
도커 허브에서 컨테이너에서 구동하고 싶은 애플리케이션의 이미지를 다운받는다. </p>
<p><strong>3. 커스터마이징</strong>
다운받은 이미지를 커스터마이징 하려면 <strong>도커 파일(Docker file)</strong>을 사용한다. </p>
<p><strong>4. 도커 파일</strong>
이미지를 만들기 위한 레시피(설명서)로 어떤 OS를 쓸지, 어떤 프로그램을 설치할지, 어떻게 실행할지를 적어둔다.</p>
<ul>
<li><p><strong>build</strong>는 docker file -&gt; image</p>
</li>
<li><p><strong>run</strong>는 image -&gt; container</p>
</li>
<li><p><strong>pull</strong>은 docker hub -&gt; image 다운</p>
</li>
<li><p>도커 이미지 URL 형식 : <code>&lt;namespace&gt;/&lt;imageName&gt;:&lt;tag&gt;</code>
주소 / 이미지이름 : 태그 
의 형태로 태크의 기본값은 latest로 이미지들 중에서 최신을 디폴드로 가진다.</p>
</li>
</ul>
<h4 id="kubernetes">Kubernetes</h4>
<p>Docker : container 를 구동하느 가장 유명한 표준 엔진 도구
Kubernetes : container orchestration 환경을 구현해주는 가장 유명한 표준 오케스트레이션 도구</p>
<ul>
<li><p>수천 수만 개의 컨테이너가 운영되는 대규모 환경에서 각각의 컨테이너를 사람이 일일이 관리하기 어려우므로 쿠버네티스가 대신 알아서 운영해주는 역할</p>
</li>
<li><p>docker가 1인분 요리를 직접 만드는 도구(도시락 하나 만드는 도구)</p>
</li>
<li><p>kubernetes는 수백-수천 개의 도시락을 자동으로 만들고, 배달하고, 고장나면 새로 만드는 시스템</p>
</li>
</ul>
<hr />
