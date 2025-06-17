---
title: "[DevOps] Docker&Kubernetes"
date: "2025-06-16"
link: "https://velog.io/@ehekaanldk/DevOps-Docker"
series: "Uncategorized"
---

<h3 id="리눅스-배포판">리눅스 배포판</h3>
<ul>
<li>리눅스는 커널(핵심)과 기타 구성요소(도구, 라이브러리) 로 구성된다. </li>
<li>동일한 커널 위에서 어떤 도구와 설정을 얹느냐에 따라서 배포판이 달라진다. 
   Debian, red hat, ubuntu</li>
</ul>
<blockquote>
<p>리눅스는 <strong>커널은 같고</strong>, <strong>생태계는 다양한</strong> 구조이다. 
패키지나 라이브러리에 따라서 배포반의 종류가 다양하다. </p>
</blockquote>
<h3 id="os-는-왜-리눅스로-고정되는가">OS 는 왜 리눅스로 고정되는가?</h3>
<ul>
<li>리눅스는 오픈소스, 경량, 안정성, 확장성 덕분에 다양한 환경에서 표준</li>
<li>도커 등의 컨테이너 환경은 리눅스 커널을 공유하기 떄문에 니눅스에 최적화 되어 있어 있다. </li>
<li>리눅스는 &quot;동일한 커널 위에 다양한 생태계와 목적에 맞게 맞춤화할 수 있어서&quot;</li>
<li>OS 선택 시 특히 서버, 개발, 클라우드, IoT에서는 리눅스가 사실상 표준처럼 사용된다. </li>
</ul>
<h3 id="소프트웨어app-는-os에-종속된다">소프트웨어(App) 는 OS에 종속된다.</h3>
<p>도커에서 격리라는 개념에서 
OS는 하드웨어를 관장하는 부분(커널: 안정성에 관한 부분으로 업데이트 관련 크지 않음)과 소프트웨어를 관장하는 부분(여러 라이브러리, 도구 등으로 확장판) 으로 나눈다.</p>
<p>그위에 APP를 동작시키면 어떤 OS인가에 따라서 종속된다. 
(jenkins 는 리눅스 배포판 별로 설치환경에 따라서 설정값과 라이브러리가 다 다르다. ) 
=&gt; App는 주변환경에 영향을 받는다. </p>
<h3 id="과거의-해결방법--가상머신-vm">과거의 해결방법 : 가상머신 (VM)</h3>
<blockquote>
<p>과거에 App에 OS까지 묶어서 배포를 하자. =&gt; VM</p>
</blockquote>
<p><strong>가상머신의 특징</strong></p>
<ul>
<li><p>앱 + OS + 필요한 도구까지 전부 포함하여 격리된 가상 환경에서 실행</p>
</li>
<li><p>Hypervisor가 하드웨어를 가상으로 분리해 여러 개의 OS를 동시에 실행</p>
</li>
<li><p>VM 위에 올라간 OS: Guest OS, 실제 OS: Host OS</p>
</li>
<li><p>App입장에서는 현재 운영되고 있는 환경이 가상인지 실제인지 알 수 없다.</p>
</li>
<li><p>독립된 공간에서 혼자 돌고 있어서 오류가 없다. </p>
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
<td>완전 격리, 안정성, 보안</td>
<td>느림, 용량 큼, 중복 많음 (OS 전체 포함)</td>
</tr>
</tbody></table>
<h3 id="현재의-해결방법--docker">현재의 해결방법 : Docker</h3>
<blockquote>
<p>OS의 커널은 공유하고, OS의 실행환경(lib, bin)은 컨테이너마다 격리한다. 
Docker는 컨테이너 기반 가상화 도구이다. </p>
</blockquote>
<table>
<thead>
<tr>
<th>비교</th>
<th>가상머신</th>
<th>Docker 컨테이너</th>
</tr>
</thead>
<tbody><tr>
<td>커널</td>
<td>Guest OS 포함 (별도)</td>
<td>Host OS 커널 공유</td>
</tr>
<tr>
<td>실행 속도</td>
<td>느림</td>
<td>빠름</td>
</tr>
<tr>
<td>용량</td>
<td>큼 (GB 단위)</td>
<td>작음 (MB 단위)</td>
</tr>
<tr>
<td>부팅 시간</td>
<td>수십 초</td>
<td>수 초 내외</td>
</tr>
<tr>
<td>격리 방식</td>
<td>하드웨어 수준</td>
<td>운영체제 수준 (namespace, cgroup 등)</td>
</tr>
</tbody></table>
<ul>
<li>격리하면 특정 App이 돌아가도록 하기 좋음</li>
<li>보안상 좋음</li>
<li>문제 생기면 통채로 날려버리면 좋음</li>
</ul>
<p><strong>격리와 가상화</strong>
완전한 가상화를 위해서 docker가 host os를 공유해서 쓴다.
도커는 커널은 공유하고 바이너리와 라이브러리는 각자 격리한다.</p>
<ul>
<li>os 는 커널은 하드웨어와 컨트롤을 담당한다.</li>
<li>os의 bin와 lib (배포판) 에서 바이너리와 라이브러리에 영향을 많이 받는다. </li>
<li>os의 커널을 모두 공유해서 다 같아야 한다. </li>
</ul>
<h3 id="도커는-리눅스에서만-사용-가능한가">도커는 리눅스에서만 사용 가능한가?</h3>
<p>docker는 리눅스 커널을 사용해야 하기 때문에 </p>
<p>Window/macOS 에서는 내부적으로 리눅스 커널이 없다. 
docker를 사용하기 위해서는 가상 리눅스 환경(WSL)을 만들어서 docker를 구동해야한다. </p>
<h2 id="도커-이미지">도커 이미지</h2>
<blockquote>
<p>컨테이너를 실행하기 위한 실행 환경의 설계도</p>
</blockquote>
<ul>
<li>ISO와 유사한 개념</li>
<li>.iso 는 가상 CD으로  읽기 전용</li>
</ul>
<p>docker image는 레이어로 이루어져 있다. 
잘 만들어 놓은 읽기 전용이고 여러 개의 층을 위에 올려서 구성한다. </p>
<blockquote>
<p>도커 이미지를 저장하고 있는 저장소 : 레지스트리 (대표적으로 도커 허브)</p>
</blockquote>
<p><code>도메인 주소 / 저장소 이름 / 이미지 이름 : 이미지 버전</code></p>
<ul>
<li>도메인 주소는 생략 가능하고, 기본값은 Docker Hub로 인식</li>
<li>이미지 이름을 생략 불가</li>
<li>이미지 버전은 생략 가능하고, 기본값 latest 인식</li>
</ul>
<p>Docker.io/library 는 도커이미지의 공식 이미지 Namespace이다. 
Azure에서 받으려면 gdhong.azurecr.io/order:1.0 </p>
<h2 id="도커-컨테이너">도커 컨테이너</h2>
<blockquote>
<p>도커 이미지를 실행한 인스턴스</p>
</blockquote>
<ul>
<li>읽기 전용 이미지 + 읽기/쓰기 계층(RW Layer)로 구성</li>
<li>가상의 OS의 환경(bin/lib) 에 App을 올려서 구동한다. </li>
<li>컨테이너는 이미지를 구동하는 구조이다. 일회성으로 한번 만들어 놓고, 안좋으면 날려버리고 다시 만든다. </li>
</ul>
<p>실행 컴퓨터에서는 pull로 도커 이미지를 다운로드 받아서 하드디스크에 저장된다. 
가상 CD를 CD룸에 넣는 것 처럼 run으로 이미지를 메모리에 올려서 구동한다. </p>
<h3 id="도커의-레이어-구조-요약">도커의 레이어 구조 요약</h3>
<p>기존의 만들어진 것을 재활용하는 관점
차이점을 기록하는 형태로 레이어링을 한다. </p>
<p>Base layer</p>
<ul>
<li><p>Custom layer</p>
</li>
<li><p>어떤 파일을 추가했는지, 삭제했는지를 기록한다. 
=&gt;     ubuntu + nginx</p>
</li>
<li><p>여러 레이어들을이후에 재활용하는 컨셉으로 운영된다. </p>
</li>
<li><p>도커 이미지가 층층이 쌓여서 도커 컨테이너로 이미지 중에 하나를 컨테이너화 하는데 읽기 전용 - layers을 그대로 가져오고, read/write layer 붙인다. </p>
</li>
<li><p>만들어진 컨테이너 자체를 이미지로 바꿀 수도 있다. </p>
</li>
</ul>
<h2 id="도커-파일">도커 파일</h2>
<blockquote>
<p>레이어를 만들어서 이미지를 만드는 스크립트
<strong>하나의 명령어가 하나의 레이어로 추가된다.</strong> </p>
</blockquote>
<ul>
<li><p>FROM : 사용할 기본 이미지(베이스 이미지)</p>
</li>
<li><p>RUN : 읽기 전용 이미지 위에 올릴 추가 레이어 (RUN 당 하나의 레이어 추가)</p>
</li>
<li><p>WOEKDIR : 작업할 디렉토리 지정</p>
</li>
<li><p>COPY : 로컬 파일/폴더를 이미지로 복사(앞에 있는 것을 뒤에 있는 것으로 복사한다. )</p>
</li>
<li><p>ENTRYPOINT : 아무 조건을 안주고 이미지를 컨테이너화 시킬 때 구동할 명령어</p>
</li>
</ul>
<h2 id="도커-이미지-명령어">도커 이미지 명령어</h2>
<p>Docker는 백그라우드에서 도는 데몬(서버) 와 사용자가 명령을 보내느 CLI(도커 명령줄 도구) 로 구성된다. </p>
<p>사용자가 <code>docker image</code> 을 입력하면, CLI가 데몬에게 명령을 전달해 작업을 처리한다. </p>
<table>
<thead>
<tr>
<th>명령어</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>docker images</code></td>
<td>로컬 PC에 다운로드된 이미지 목록 확인</td>
</tr>
<tr>
<td><code>docker pull 이미지명</code></td>
<td>Docker Hub에서 이미지 다운로드</td>
</tr>
<tr>
<td><code>docker rmi 이미지명</code></td>
<td>이미지 삭제 (<code>rmi = remove image</code>)</td>
</tr>
<tr>
<td><code>docker image rm 이미지명</code></td>
<td>위 명령과 동일 (권장 사용 방식)</td>
</tr>
</tbody></table>
<p><strong>컨테이너 제어 : docker run</strong>
container run 으로 컨테이너 실행
<code>docker run [옵션] [이미지명] [명령어]</code></p>
<p>--name :  컨테이너 이름을 지정한다. 
-d : 백그라운드 실행한다. 
-p 8080:80 : 호스트(8080)와 컨테이너(80)를 연결한다. </p>
<p><code>docker run --name my-nginx -d -p 8080:80 nginx</code></p>
<ul>
<li><p>컨테이너는 메모리에 올라가 실행됨</p>
</li>
<li><p>실행 중인 컨테이너는 docker ps로 확인 가능</p>
</li>
<li><p>중지된 컨테이너는 docker ps -a로 확인 가능</p>
</li>
</ul>
<p>컨테이너를 완전히 제거해야 해당 이미지도 안전하게 삭제 가능함</p>
<p><strong>이미지 빌드 : docker build</strong>
도커 빌드는 도커 파일을 이용해서 이미지를 만드는 행위를 bulid라고 한다. </p>
<p><code>docker build --tag[생성할 이미지의 이름]:[태그 이름].</code>
. 은 도커 파일의 위치이다. 
. 만 작성할 경우 해당 명령어를 터미널에서 입력할 때 터미널의 위치가 dockerfile이 있는 위치여야 한다. </p>
<p><strong>이미지 푸시 : docker push</strong>
image push는 하드 안에 저장된 이미지를 만천하에 공개하고 싶으면 push한다. 
push를 하려면 권한이 있어야 한다. </p>
<ol>
<li>docker login</li>
<li>docker tag myapp:1.0 [도커허브 아이디]/myapp:1.0</li>
<li>docker push [도커허브 아이디]/myapp:1.0</li>
</ol>
<h2 id="도커-전체-흐름-요약">도커 전체 흐름 요약</h2>
<ol>
<li>Dockerfile 작성 ← 이미지 설계도</li>
<li>docker build    ← 이미지 생성</li>
<li>docker run      ← 컨테이너로 실행</li>
<li>docker ps       ← 컨테이너 상태 확인</li>
<li>docker stop/rm  ← 정지 및 삭제</li>
<li>docker push     ← 이미지 업로드 (Docker Hub 등)</li>
</ol>
<h2 id="실습1--docker-다루기">실습1 : docker 다루기</h2>
<p><code>docker image pull nginx:latest</code>
도커 이미지 nginx:latest를 하드디스크에 다운받는다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/2b93637d-353a-4941-ab25-4d11225baf70/image.png" /></p>
<p><code>docker run --name my-nginx -d -p 8080:80 nginx:latest</code>
-d 는 데몬으로 백그라운드에서 실행
-p 는 container 내에 실행(80)할 때 내 서버의 포트(8080)와 연결해주는 역할(서버포트와 컨테이너 안에 포트와 연결한다.) -&gt; 8080 -&gt; 80 으로 컨테이너에 들어온다.</p>
<p><code>docker run --name my-new-nginx -d -p 8081:80 nginx:latest</code>
다른 nginx 컨테이너 페이지를 열어서 동시에 실행 가능하다. </p>
<p><code>docker container ls</code>로 실행 중인 모든 컨테이너의 목록을 확인할 수 있다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/5211e0e7-c9ea-4060-9fff-4a36e44974bb/image.png" /></p>
<p>pip install httpie
http GET <a href="http://localhost:8080">http://localhost:8080</a>
http GET <a href="http://localhost:8081">http://localhost:8081</a>
으로 서로 다른 것을 확인할 수 있다. </p>
<h3 id="도커-이미지-삭제하기">도커 이미지 삭제하기</h3>
<p>docker 이미지를 삭제할 때는 해당 이미지를 사용하는 컨테이너를 먼저 정리 해야한다. </p>
<p><code>docker container stop [컨테이너명]</code>
<code>docker container ls -a</code> 으로 stop된 결과를 확인할 수 있다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/af6371f5-21c4-4790-bbab-4e945416c8ee/image.png" /></p>
<p><code>docker container rm [컨테이너명]</code>
<code>docker image rm [이미지명]</code>
컨테이너 이름이나 컨테이너 ID을 넣어서 정지할 수 있다. </p>
<h3 id="도커-이미지-만들기">도커 이미지 만들기</h3>
<p>/Docker/index.html</p>
<pre><code>&lt;html&gt;
&lt;body&gt;
&lt;center&gt;
&lt;br/&gt;&lt;/br&gt;
&lt;img src=&quot;https://raw.githubusercontent.com/acmexii/demo/master/materials/smile.jpg&quot;&gt;
&lt;br/&gt;&lt;/br&gt;
&lt;h1&gt; Hi~ My name is Hong Gil-Dong...~~~ &lt;/h1&gt;
&lt;/center&gt;
&lt;/body&gt;
&lt;/html&gt;
&lt;/center&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre><p>/Docker/Dockerfile</p>
<pre><code>FROM nginx
COPY index.html /usr/share/nginx/html/</code></pre><p>만든 도커 이미지를 빌드한다. 
<code>docker build -t [도커허브 아이디]/welcome:v1 .</code>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/4846d495-2775-4601-86ed-de37f54c7c1f/image.png" /></p>
<p>도커허브에 만든 도커이미지를 push한다. 
<code>docker login</code>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/63cccfd7-bd98-47ec-a819-99414111fb07/image.png" /></p>
<p><code>docker push [도커허브아이디]/welcome:v1</code>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/85d1b953-1bd1-42d4-bfd8-cc19b44cfae6/image.png" /></p>
<p><code>docker run --name=welcome -d -p 8080:80 [도커허브아이디]/welcome:v1</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a66106a1-dcdd-4df1-ae7a-f8cff52a002a/image.png" /></p>
<hr />
<h2 id="실습2--spring-boot의-app을-docker-image로-만들기">실습2 : spring boot의 app을 docker image로 만들기</h2>
<h3 id="애플리케이션-빌드--mvn-package">애플리케이션 빌드 : mvn package</h3>
<p>mvn spring-boot:run 했던거를 mvn package 으로 해서 
<code>컴파일 -&gt; test 코드 컴파일 -&gt; 실제 test -&gt; jar로 만들기</code> 을 자동으로 수행한다. 
해당 과정의 결과가 <strong>target/</strong> 폴더에 들어가게 된다. </p>
<p>실제 실행을 할 수 있다. 
✅ 결과
<code>java -jar target/inventory-0.0.1-SNAPSHOT.jar</code> 으로 동일하게 mvn spring-boot:run 처럼 실행된다. </p>
<ul>
<li><code>.jar</code> 는 독립 실행 가능한 spring-boot의 앱이다. </li>
<li>snapshot을 개발중인 버전을 의미한다. </li>
</ul>
<h3 id="도커-이미지-생성">도커 이미지 생성</h3>
<p>/inventory/Dockerfile</p>
<pre><code>FROM openjdk:15-jdk-alpine
COPY target/*SNAPSHOT.jar app.jar
EXPOSE 8080
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime &amp;&amp; echo $TZ &gt; /etc/timezone
ENTRYPOINT [&quot;java&quot;,&quot;-Xmx400M&quot;,&quot;-Djava.security.egd=file:/dev/./urandom&quot;,&quot;-jar&quot;,&quot;/app.jar&quot;,&quot;--spring.profiles.active=docker&quot;]</code></pre><ul>
<li>FROM 아래에는 베이스 이미지를 작성한다. </li>
<li>COPY 뒤에는 target/*SNAPSHOT.jar 를 복사해서 app.jar 에 붙인다. =&gt; layer 하나 생성되어 붙음</li>
<li>이 이미지는 Spring Boot 앱이 포함된 경량 자바 실행 환경이 된다.</li>
</ul>
<p>터미널에서 order, gateway 폴더로 이동해서 
각각의 Dockerfile이 있는 위치에서 아래를 실행한다. (cd order, cd gateway 각각에서 실행)</p>
<pre><code>mvn package 
docker build -t [dockerhub ID]/inventory:[오늘날짜] .     
docker push [dockerhub ID]/inventory:[오늘날짜]  
</code></pre><p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/fdd2c32f-b052-4d86-a6e3-c267fc52c830/image.png" /></p>
<hr />
<h2 id="쿠버네티스-kubernetes">쿠버네티스 (kubernetes)</h2>
<blockquote>
<p>컨테이너 오케스트레이션 도구 중의 하나이다. 
컨테이너화된 애플리케이션을 자동으로 배포, 조정, 관리할 수 있는 오픈소스 플랫폼이다. </p>
</blockquote>
<ul>
<li>nginx, spring, mysql 등을 Docker로 만들었을 때</li>
<li>서버가 많아지고, 컨테이너가 수십~수백 개가 되면</li>
<li>자동 배포/확장/장애 복구/트래픽 분산이 필요함
→ 이걸 자동화하는 것이 Kubernetes</li>
</ul>
<h3 id="cncf--cloud-native-computing-foundation">CNCF  (Cloud Native Computing Foundation)</h3>
<p>클라우드 네이티브 기술을 표준화하고 발전시키는 재단
쿠버네티스를 비롯한 다양한 오픈소스 인프라 기술을 관리/지원하는 조직</p>
<ul>
<li>한 기업이 소유하면 독점적 방향으로 가기 쉬움</li>
<li>중립적으로 여러 기술을 공동 관리한다. </li>
</ul>
<p>대표적인 프로젝트</p>
<ul>
<li>Kubernetes (컨테이너 오케스트레이션)</li>
</ul>
<h3 id="container-orchestration의-기능">Container Orchestration의 기능</h3>
<p><strong>자가 치유</strong></p>
<blockquote>
<p>원하는 상태 (desired) 을 유지하도록 노력하는 것이다. </p>
</blockquote>
<p>desired(4) &lt;- actual(3) 로 하도록 노력하는 것</p>
<ul>
<li>예: 사용자가 4개 컨테이너를 원하면 (desired = 4)</li>
<li>실제 컨테이너가 3개면 (actual = 3) → 1개를 자동으로 생성</li>
<li>비어있는 곳에 생성하거나 사용하지 않지만 pool에서 가져온 곳에 생성한다.</li>
</ul>
<p><strong>확장</strong></p>
<blockquote>
<p>요청이 많아지면 컨테이너 수를 늘린다.</p>
</blockquote>
<p>need to scale out 으로 desired == actual일 떄 더 필요하다고 보낸다. </p>
<p><strong>무중단 배포</strong></p>
<blockquote>
<p>앱을 중단하지 않고, 점진적으로 새 버전으로 교체한다. </p>
</blockquote>
<ul>
<li>기존의 컨테이너를 하나씩 내리고, </li>
<li>새 버전을 하나씩 올린다. </li>
</ul>
<ul>
<li>새로운 업데이트에 대해서 찰나에 순간에 서비스가 중단될 수 있다. (ex 게임)
정기점검, 임시점검, 연장점검, 긴급점검 =&gt; 쿠버네티스가 이걸 막아준다. </li>
</ul>
<h3 id="aksazure-kubernetes-service">AKS(Azure Kubernetes Service)</h3>
<p>MS azure에서 쿠버네티스를 쉽게 쓸 수 있게 도와주는 서비스이다 </p>
<blockquote>
<p>복잡하게 직접 쿠버네티스를 설치하지 않아도, ASK를 사용해서 버튼 몇 번 클릭으로 구버네티스를 자동으로 설치해준다. </p>
</blockquote>
<ul>
<li>azure에서는 계정관리 azure ad(active directory) 로 관리한다. </li>
<li><strong>user, groups, apps 을 이용해서 권한 인증</strong>을 한다. </li>
<li><strong>구독(Azure Subscriptions)</strong> 이라는 단위(돈을내는 단위)로 여러 리소스를 
여러 리소스를 묶여서 <strong>리소스 그룹</strong>이라고 한다. </li>
<li><strong>리소스들 중에서 쿠버네티스 서비스</strong>를 사용한다. 
acr registry 로 컨테이너 저장소</li>
</ul>
<blockquote>
<ul>
<li>전체 흐름</li>
</ul>
</blockquote>
<ol>
<li>Azure <strong>로그인(users)</strong></li>
<li><strong>구독(Azure Subscriptions)</strong> 확인 (어떤 요금제 쓸지)</li>
<li><strong>리소스 그룹</strong> 만들기 (리소스들을 묶는 바구니)</li>
<li><strong>AKS 클러스터</strong> 만들기 (쿠버네티스 서버)</li>
<li>연결해서 내 앱 배포하기</li>
</ol>
<ol>
<li>리소스 그룹 만들기<blockquote>
<p>Azure 리소스들을 묶어서 관리하는 논리적 컨테이너</p>
</blockquote>
</li>
</ol>
<ul>
<li>리소스 그룹명 예시: a071212-rsrcgrp</li>
<li>영역(Region): Korea Central (한국 서울 리전)</li>
<li>이 그룹 안에 쿠버네티스 클러스터, 노드, 네트워크, 디스크 등이 함께 배치됨</li>
</ul>
<ol start="2">
<li>쿠버네티스 서비스 생성<blockquote>
<p>Azure에서 제공하는 완전관리형 Kubernetes 클러스터 서비스</p>
</blockquote>
</li>
</ol>
<ul>
<li>클러스터 이름 예시: a071212-aks</li>
<li>클러스터 유형: 개발/테스트용 선택 (비용 낮고 구성 단순)</li>
<li>Production 클러스터는 고가용성, 보안, 로깅 등이 추가되어 복잡하고 비쌈</li>
</ul>
<ol start="3">
<li>agent pool <blockquote>
<p>실제 컨테이너(Pod)를 실행시키는 <strong>워커 노드(Worker Node)</strong> 들이 포함된 풀</p>
</blockquote>
</li>
</ol>
<p><strong>워커 노드</strong></p>
<ul>
<li>쿠버네티스 클러스터에서 컨테이너를 실제로 실행하는 VM</li>
<li>Azure는 마스터 노드는 무료로 제공한다 </li>
<li>워커 노드 비용만 사용자가 지불한다. </li>
</ul>
<p><strong>노드 사양 예시</strong></p>
<ul>
<li>DS2_v2: 2 vCPU / 7GB RAM</li>
<li>테스트/개발 환경에 적합</li>
<li>여러 개의 워커 노드를 묶은 것이 노드 풀(Node Pool)</li>
</ul>
<ol start="4">
<li>도커 로그인과 Azure CLI 연동</li>
</ol>
<ul>
<li>보통 AKS는 도커 이미지 기반 앱을 실행하기 때문에 docker login이 필요</li>
</ul>
<pre><code>az</code></pre><ol start="5">
<li>kubectl : 쿠버네티스 제어툴<blockquote>
<p>쿠버네티스를 제어하는 대표 CLI 도구</p>
</blockquote>
</li>
</ol>
<ul>
<li>쿠버네티스 자체에 손을 대려면 <code>kubectl</code>을 사용한다. </li>
<li>쿠버네티스를 다루는 tool 에게 azure 로그인 이후에 접속 정보를 받아서 넣어줘야 한다. </li>
</ul>
<h2 id="실습3--azure에서-쿠버네티스">실습3 : Azure에서 쿠버네티스</h2>
<p><strong>구독확인</strong></p>
<p><strong>리소스 그룹</strong>
만들기 &gt; 구독누르고 &gt; 리소스그룹 이름 설정
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/10f745e6-aecd-42d8-9178-255d43feebb9/image.png" /></p>
<p><strong>Azure Kubernetes Service 생성</strong>
만들기 &gt; 쿠버네티스 클러스터 &gt; 구독 &gt; 리소스그룹(생성했던거) &gt; 클러스터 세부 정보(반드시 개발/테스트) &gt; 쿠버네티스 이름 설정
다음 &gt; 노드 풀(worker node 모음) &gt; 크기 선택 DS2_v2 , 최소2 최대2 설정 &gt; 업데이트 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/1965eb80-e7ae-44bd-a9d3-29f29b2ffd3b/image.png" /></p>
<p><strong>설치 확인</strong>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/4b008234-dab9-412b-a0c0-794433a9cde8/image.png" /></p>
<p><strong>초기 세팅</strong>
/init.sh 을 터미널에 입력하면 초기 세팅을 해준다. </p>
<pre><code>sudo apt-get update
sudo apt-get install net-tools
sudo apt install iputils-ping
pip install httpie

curl -LO &quot;https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl&quot;
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/microsoft.gpg &gt; /dev/null
echo &quot;deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ jammy main&quot; | sudo tee /etc/apt/sources.list.d/azure-cli.list
sudo apt update
sudo apt install azure-cli
</code></pre><ul>
<li>kubectl : 쿠버네티스를 다루기 위함</li>
<li>azure-cli : azure 다루기</li>
</ul>
<p>터미널에서 <code>az</code>와 <code>kubectl</code> 으로 확인한다. </p>
<p><strong>클라이언트의 CLI 환경을 준비</strong>
<code>curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash</code> 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/907d1c93-2547-4d66-ae9e-0a759d21661e/image.png" /></p>
<hr />
<p><code>az aks get-credentials --resource-group (RESOURCE-GROUP-NAME) --name (Cluster-NAME)</code> 
어디 클러스트에 붙는지에 따라서 </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7a51e8a7-f779-4573-bac4-1d5cb90cbf2c/image.png" /></p>
<p><code>kubectl get all</code> 으로 쿠버네티스의 서비스 객체를 확인할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/875b807a-7f43-4f2d-a55f-84d9324ad468/image.png" /></p>
<p><code>kubectl get node</code> 으로 워커 노드들의 목록을 확인할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/514bef8c-fb1e-4406-8aed-8764ff209047/image.png" /></p>
