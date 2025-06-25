---
title: "[DevOps] Kubernetes"
date: "2025-06-24"
link: "https://velog.io/@ehekaanldk/DevOps-Kubernetes"
series: "Uncategorized"
---

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
<p>컨테이너 오케스트레이션의 특징</p>
<ul>
<li>컨테이너 자동 배치 및 복제 : ReplicaSet, Deployment</li>
<li>컨테이너 그룹에 대한 로드밸런싱 : Service, ClusterIP, LoadBalancer, Ingress</li>
<li>컨테이너 장애 복구 : Self-healing, LivenessProbe, ReadinessProbe, Deployment, ReplicaSet</li>
<li>클러스터 외부에 서비스 노출 : NodePort, LoadBalancer, Ingress</li>
<li>컨테이너 확장 및 축소 : Horizontal Pod Autoscaler (HPA)</li>
<li>컨테이너 서비스 간 인터페이스를 통한 연결 : Service, DNS</li>
</ul>
<h3 id="클러스터cluster">클러스터(Cluster)</h3>
<blockquote>
<p>여러 대의 컴퓨터(노드)를 하나처럼 묶어서 사용하는 시스템 구조이다. </p>
</blockquote>
<ul>
<li><p>쿠버네티스는 여러 개의 노드를 하나의 논리적인 그룹으로 구성해 앱을 안정적이고 자동화된 방식으로 운영한다. </p>
</li>
<li><p>Master node : 클러스터의 상태를 관리</p>
</li>
<li><p>Worker node : App 실행</p>
</li>
<li><p>Master 는 Azure 등에서 제공, Worker를 사용한 만큼만 돈을 냄</p>
</li>
<li><p>여러 노드들을 묶어서 앱을 자동으로 배포/관리한다. </p>
</li>
<li><p>카프카 클러스터도 여러 브로커(서버)를 묶어서 메시지를 안정적으로 송수신한다. </p>
</li>
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
<li>새로운 업데이트에 대해서 찰나에 순간에 서비스가 중단될 수 있다. (ex 게임)
정기점검, 임시점검, 연장점검, 긴급점검 =&gt; 쿠버네티스가 이걸 막아준다. </li>
</ul>
<h3 id="aksazure-kubernetes-service">AKS(Azure Kubernetes Service)</h3>
<p>MS azure에서 쿠버네티스를 쉽게 쓸 수 있게 도와주는 서비스이다 </p>
<blockquote>
<p>복잡하게 직접 쿠버네티스를 설치하지 않아도, ASK를 사용해서 버튼 몇 번 클릭으로 구버네티스를 자동으로 설치해준다. </p>
</blockquote>
<ul>
<li>azure에서는 <strong>계정관리 azure ad(active directory)</strong> 로 관리한다. </li>
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
<h2 id="실습1--azure에서-쿠버네티스">실습1 : Azure에서 쿠버네티스</h2>
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
<p><strong>클라이언트 Client 설정</strong>
<code>az aks get-credentials --resource-group (RESOURCE-GROUP-NAME) --name (Cluster-NAME)</code> 
어디 클러스트에 붙는지에 따라서 </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7a51e8a7-f779-4573-bac4-1d5cb90cbf2c/image.png" /></p>
<p><code>kubectl get all</code> 으로 쿠버네티스의 서비스 객체를 확인할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/875b807a-7f43-4f2d-a55f-84d9324ad468/image.png" /></p>
<p><code>kubectl get node</code> 으로 워커 노드들의 목록을 확인할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/514bef8c-fb1e-4406-8aed-8764ff209047/image.png" /></p>
<hr />
<h2 id="kubernetes-기본-구성-관계">Kubernetes 기본 구성 관계</h2>
<blockquote>
<p>[Deployment]
   ↓ (자동으로 생성)
[ReplicaSet]
   ↓ (자동으로 생성)
[Pod]
   ↓ (안에 포함)
[Container] ← Docker 이미지가 메모리에 올라가서 실행되는 단위</p>
</blockquote>
<p>Deployment는 가장 상위의 관리자이다. 
몇개의 pod를 만들지, 업데이트는 어떻게 할지 전체를 관리한다. </p>
<p>ReplicaSet 은 실제로 pod의 개수를 유지한다.
3개를 유지한다면, 죽으면 다시 만든다. </p>
<p>Pod는 컨테이너가 들어 있는 실행 단위이다. 
1개 또는 여러 컨테이너가 들어갈 수 있다. </p>
<p>Container 는 우리가 만든 이미지(jinyoung/monolith-order)가 메모리에 올라가서 실행되는 실제 앱</p>
<p><strong><code>kubectl create deploy order --image=...</code> 하면</strong></p>
<ul>
<li>Deployment 생성됨
  <code>deployment.apps/order</code> 생성된다.</li>
<li>Deployment가 자동으로 ReplicaSet 생성
  내부적으로 <code>replicaset.apps/order-86b7fd4f57</code> 생성된다. </li>
<li>ReplicaSet이 자동으로 Pod 생성
  그 안에 <code>pod/order-86b7fd4f57-xxxxx</code> 생성된다. </li>
<li>Pod 안에서 Container가 실행됨 (이미지가 메모리에 올라감)</li>
</ul>
<blockquote>
<p>Deployment를 만들면 자동으로 ReplicaSet이 생성되고, 
그 안에 Pod가 만들어지며, 
Pod 안에서 우리가 만든 Container(Image) 가 메모리에 올라가 실행된다.</p>
</blockquote>
<h3 id="pod">Pod</h3>
<blockquote>
<p>Pod는 Kubernetes의 가장 작은 배포 단위이다.</p>
</blockquote>
<p>이 경우, order라는 이름의 Pod 하나가 생성되어 실행(Running) 중입니다.
컨테이너는 Pod 내부에 존재하며, Pod는 실제로 애플리케이션이 실행되는 공간입니다.</p>
<p>Pod 이름 뒤의 -86b7fd4f57-...은 자동 생성된 ReplicaSet과 고유 식별자입니다.</p>
<p>💡 요약: 컨테이너를 메모리에 올리고 실행하는 실질적인 실행 단위가 Pod입니다.</p>
<p>pod는 휘발성임
이상이 생기거나 문제가 있으면 바로 내린다. </p>
<p>pod의 연속</p>
<h2 id="실습2--컨테이너-오케스트레이션">실습2 : 컨테이너 오케스트레이션</h2>
<p><code>kubectl create deploy order --image=jinyoung/monolith-order:v202105042</code>
deploy 는 개발하는 단위(배포하는 단위)
order 서비스를 배포단위로 배포한다. --image를 jinyoung/monolith-order:v202105042 으로 해서 해주세요
create 한거</p>
<p>접수만 한 상태이다. 확인 필요
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a08e2d78-18e5-40c7-991e-65f2430ff606/image.png" /></p>
<p>container가 서버 단위의 pod
pod는 이미지를 메모리에 올린 컨테이너 역할이다.
get all 만든 모든 객체를 다 가져오는 것
<code>kubectl get pod</code>
레플리카셋-pod의 고유id
컨테이너들은 여러개 생길 수 있고 고유한 아이디가 필요하다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a33d7eeb-883c-4e07-bc30-1e727e54692e/image.png" /></p>
<p><strong>pod의 자세한 정보 출력</strong>
<code>kubectl describe po [pod명]</code></p>
<ul>
<li>이벤트</li>
<li>상태</li>
<li>어떤 이미지인지</li>
<li>어떤 노드에 있는지
가운데 노드에 배치했다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/6ed89f07-d92c-4cfa-aa1f-61fab9088ff6/image.png" /></li>
</ul>
<p><strong>pod 안에 컨테이너에서 출력된 로그 실시간 확인</strong>
<code>kubectl logs -f order-86b7fd4f57-kmr67</code></p>
<p><code>kubectl exec -it order-86b7fd4f57-kmr67 -- bin/sh</code>
내부파일 확인 </p>
<p>pod 삭제
<code>kubectl delete pod order-86b7fd4f57-kmr67</code></p>
<p>pod를 아예 지우려면 deploy를 지워야한다. 
pod는 항상성? 되돌아가려는 성질이 있나.</p>
<h3 id="외부에서-app에-접근하는-방식">외부에서 App에 접근하는 방식</h3>
<p>2초에 한번씩 관측한다. 
<code>watch kubectl get pod</code></p>
<p><code>kubectl delete pod -l app=order</code>
를 하면 ID와 age가 바뀐다. 항상성을 유지하려는 특징이 있다. </p>
<p>** kubectl expose + LoadBalancer **</p>
<p>목적</p>
<blockquote>
<p>pod 들은 외부에서 바로 접근하기 어려워서, Service 객체를 통해 접근 가능하게 한다. 
클라우드 벤더에서 퍼블릭 IP를 자동 할당해서 외부에서도 직접 접근할 수 있게 해준다.</p>
</blockquote>
<ul>
<li>Deployment를 외부에 노출할 수 있는 Service를 생성한다. </li>
<li><code>LoadBalancer</code> 는 클라우드 환경에서 퍼블릭 IP를 자동으로 만들어서 외부에서 접속 가능하게 한다. </li>
</ul>
<p>service 객체를 붙여줘야 실행이 가능하다. </p>
<p>pod 5개는 각각다 별도의 ip 포트를 가지고 있다. 
외부에서 pod들에게 접속하려면 pod들의 포트들을 다 알아야한다. 
이게 싫어서 api gateway를 사용한다. </p>
<p>pod는 일회성이여서 5개에서 -&gt; 4개가 될 수도 이렇게 다이렉트로 pod를 가르킬 수 업음</p>
<p>서비스 디스커버리로 pod가 구동될 때 등록시키도록 하는 방법을 사용한다. 
컨테이너들의 정보를 kubernetes는 다 알고 있다. </p>
<p>가상의 객체(접속용 객체) service 객체를 연결하고 
여기에 pod들이 연결되어 있다. 
이 것을 로드밸런서 겸 서비스디스커버리이다. 
실제 pod와 상관없이 독립적으로 만들 수 있다. pod가 없어도 생성할 수 있다. </p>
<p>실물 세계를 pod., replica -set, </p>
<p><code>kubectl expose deploy order --type=LoadBalancer --port=8080</code>
order라는 서비스 객체를 만들어라!
벤더사의 
LoadBalancer 는 외부에서 바로 접속할 수 있는 ip를 벤더 사에서 제공한다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/85ae8737-8ade-460c-9cb8-f1883a668b35/image.png" /></p>
<p>로드밸런서는 ip 획득이 필요하고, ip획득에 따라서 비용이 발생한다. </p>
<p><strong>kubectl port-forward</strong></p>
<ul>
<li>Kubernetes 클러스터 안의 Pod(또는 Deployment)**에 직접 연결하는 임시 통신 터널을 만듦</li>
<li>현재 gitpod 컴퓨터에서 localhst:8080 -&gt; 클러스터 내부의 Pod : 8080 에 직접 연결
<code>kubectl port-forward deploy/order 8080:8080</code></li>
</ul>
<p>서버의 8080으로 데이터를 쏘면 클러스터 안에 서비스에 접속된다. </p>
<ul>
<li>kubectl이 터널을 열고 직접 통신</li>
<li>production에서는 비추 : 서버의 부하</li>
<li>test용으로 사용하는 것을 추천한다.</li>
</ul>
<h3 id="instance-확장">instance 확장</h3>
<p>레블리카 셋으로 pod를 확장 가능하다 </p>
<p>scale deploy order
deploy order 를 대상으로 스케일을 desired를 3으로 해줘</p>
<p><code>kubectl scale deploy order --replicas=3</code>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7e214229-bae6-4e2d-8793-ae178143b6c3/image.png" /></p>
<p>pod 3개가 살아잇어서 더 많은 요청을 담을 수 있다. </p>
<h3 id="rollback">rollback</h3>
<p>이전 버전으로 돌아가야 한다. 
<code>kubectl rollout udo deploy order</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/f8277579-8687-4cff-95e0-2d95671c8f58/image.png" /></p>
<h3 id="pod-깔쌈하게-지우기">pod 깔쌈하게 지우기</h3>
<p><strong>deployment 지우기</strong></p>
<p>kubectl delete deploy order</p>
<p>아예 배포되었던 사실을 없애야 한다. 
deploy order를 service 객체로 만든 사실을 살아있다. 
이는 별도의 가상 객체여서 </p>
<p>접속을 위한 가상 객체와 실제 객체 중에 실제 객체가 삭제된 것이다. 
이 둘은 독립된 성격을 가진다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/fc0c7345-99aa-447b-8bf9-eee274bb18bf/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ab068229-4f75-4fcd-a570-0ed62755d2a8/image.png" /></p>
<p><strong>service를 지우기</strong></p>
<p>kubectl delete service order</p>
<p>실제 azure의 로드밸런서를 지우는 것으로 
다시 ip를 반납해야 해서 시간이 좀 걸린다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ab068229-4f75-4fcd-a570-0ed62755d2a8/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b5874f87-d9d1-40c6-b2d7-19e2b2c5f144/image.png" /></p>
<p>** Deployment 선언 파일을 정의**</p>
<blockquote>
<p>Deployment 객체로 정의하고 Pod을 몇 개 배포할지, 어떤 이미지 쓸지를 지정</p>
</blockquote>
<p>Lab 폴더를 새로 만든다. 
/Lab/order.yml 
스팩을 정해줄 수 있다.
deployment를 배부해라..?</p>
<ul>
<li><p>apiversion : 타입에 따른 버전</p>
</li>
<li><p>type : 어떤 리소스 타입을 쓰냐에 따라서 다르다. </p>
</li>
<li><p>metadata : deployment에 정보를 넣는다. (이름과 검색을 위한 레이블)</p>
</li>
<li><p>spec : deployment를 배포할 때의 replicaset 영역이다. </p>
<ul>
<li>selector : pod까지의 연결고리를 정해주는 부분</li>
<li>template : deployment를 배포할 때의 pod의 영역이다.<ul>
<li>spec : pod의 스팩을 설정한다. 
pod 하나 안에 여러 개의 컨테이너를 넣을 수 있다. 
되도록이면 2개까지 권장한다. 
다수의 컨테이너가 하나의 pod안에 들어갈 수 있다. </li>
<li>image : 실제 컨테이너를 구성하는 주요 구성요소인 이미지(latest는 권장하지 않는다.)</li>
<li>ports : 8080로 컨테이너 내부에서 노출할 포트이다. </li>
</ul>
</li>
</ul>
</li>
</ul>
<p><code>cd Lab</code>
<code>kubectl apply -f order.yml</code></p>
<p>해당 파일을 적용할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/9b2a34a2-258b-4654-af32-344fff2b8e37/image.png" /></p>
<p>적용된 이름이 order-by-yaml 이기에 
<code>kubectl port-forward deploy/order-by-yaml 8080:8080</code> 해준다. </p>
<p><code>kubectl get deploy order-by-yaml -o yaml &gt; order2.yaml</code> 으로 조회한거를 뺄수도 있다. </p>
<hr />
<h2 id="실전-실습">실전 실습</h2>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a4acc2c6-fd1a-4b7b-9515-d3804a8af9dc/image.png" /></p>
<blockquote>
<p>kafka를 kubernetes 환경에 배포할 때, Helm 을 사용해 간편하게 설치하고, service로 연결하여 접근할 수 있도록 구성한다. </p>
</blockquote>
<h3 id="helm">Helm</h3>
<p>kubernetes 애플리케이션을 설치하고 관리하기 위한 패키지 매니저이다. </p>
<p>kafka는 기본적으로 <code>clusterIP</code> 서비스로 생성되어 내부 통신만 가능하지만, </p>
<p>kafka도 인프라로써 사용한다. 
service를 붙여서 동일하게 
my-kafka 이름이기만 하면 되고 다운로드 받아서 설치만 잘하면 된다. 
Helm 으로 설치파일이 이미 들어있다. 
Helm으로 kafkaf를 설치하기만 하면 9092로 띄우고 하지 않아도 ㄱ된다. </p>
<p>어디에 저장되어있ㄴ느 어플래키에션을 받아올지 등록을 해야한다. </p>
<p>*<em>기존의 앱을 모ㅓㄴ저 배포한다. *</em>
cd order
mvn package
target 폴더에 jar 파일이 생성이 되었는지 확인한다.
docker login (최초 1회 실행한다)
docker build -t [dockerhub ID]/order:[오늘날짜] .<br />docker push [dockerhub ID]/order:[오늘날짜]<br />Docker hub에서 image 확인
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b1f70db9-de45-4307-afe3-9f1e6086e1c1/image.png" /></p>
<p>*<em>클러스터를 배포한다. *</em>
az login --use-device-code
az aks get-credentials --resource-group [RESOURCE-GROUP-NAME] --name [Cluster-NAME]
kubectl get all</p>
<p><strong>helm 설치하기</strong>
curl <a href="https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3">https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3</a> &gt; get_helm.sh
chmod 700 get_helm.sh
./get_helm.sh</p>
<ul>
<li>Helm Chart 저장소(repository) 를 등록
bitnami 은 Kafka를 포함한 다양한 오픈소스 소프트웨어를 템플릿 형식으로 제공하는 대표적인 저장소이다.</li>
</ul>
<p>helm repo add bitnami <a href="https://charts.bitnami.com/bitnami">https://charts.bitnami.com/bitnami</a>
helm repo update</p>
<ul>
<li>카프카 설치하기 (이름 : my-kafka)
helm install my-kafka bitnami/kafka --version 23.0.5</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a213693b-9b1b-494f-9b79-d4e18bcab613/image.png" /></p>
<p><strong>폴더마다 kubernetes 폴더에 deployment.yaml</strong></p>
<p>deployment 타입으로 
order라는 이름으로 
replicaset은 1개로
image name에 이전에 도커허브에 push한 이미지의 이름을 적어줘야 한다. </p>
<p>kubectl apply -f [해당 폴더 경로까지 가줘야한다.]</p>
<p><code>kubectl apply -f kubernetes/deployment.yaml</code></p>
<p>deployment가 잘 생성되었고, 해당 deploy의 order가 running으로 잘 작동되고 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/5ddf4f01-3915-4f16-a656-e63cd755b914/image.png" /></p>
<p><strong>폴더마다 kubernetes 폴더에 service.yaml</strong>
targetport는 Pod 내부의 컨테이너가 실제로 열고 있는 포트 번호와 같아야한다. </p>
<pre><code>/kubernetes/deployment.yaml
containers:
- name: order-container
  image: jinyoung/order:v1
  ports:
    - containerPort: 8080</code></pre><pre><code>/kubernetes/service.yaml

apiVersion: v1
kind: Service
metadata:
  name: order
  labels:
    app: order
spec:
  ports:
    - port: 8080
      targetPort: 8080
  selector:
    app: order
</code></pre><ul>
<li><p><code>containerPort: 8080</code>이므로, <code>targetPort: 8080</code>으로 설정해야 맞다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/979ce7f1-e38b-465e-9d40-c76b801d4db9/image.png" /></p>
</li>
<li><p><code>kubectl apply -f kubernetes/deployment.yaml</code>
<code>kubectl apply -f kubernetes/service.yaml</code>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/1ad876d2-dfc0-43c7-ac95-3011247666f5/image.png" /></p>
</li>
</ul>
<p><strong>gateway의 external ip로 외부 요청을 통한 주문 생성</strong>
<code>http 20.249.162.162:8080/inventories id=1 stock=100</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/826cd6f9-1399-4259-a8a0-24ddfd6b1c03/image.png" /></p>
<p><strong>cluster ip로 내부에서 주고 받는다. (모든 서비스와 kafka 간의 통신)</strong></p>
<blockquote>
<p>kafka 클러스터 내부 통신 테스트용 <code>클라이언트 pod</code>를 하나 띄운다. 
해당 클라이언트 Pod 안에 kafka 메시지를 콘솔로 받아보는 consumer를 싱핸한다. </p>
</blockquote>
<ul>
<li><p>서비스들(order, product 등)은 kafka로 메시지를 주고 받는다. </p>
</li>
<li><p>pod -&gt; kafka 통신은 </p>
</li>
<li><p>클라이언트 Pod 를 생성한다. 
<code>kubectl run my-kafka-client --restart='Never' --image docker.io/bitnami/kafka:3.5.0-debian-11-r21 --namespace default --command -- sleep infinity</code></p>
</li>
<li><p>해당 pod에 접속한다. 
<code>kubectl exec --tty -i my-kafka-client --namespace default -- bash</code></p>
</li>
<li><p>Kafka 메시지 소비(Consumer 실행)
<code>kafka-console-consumer.sh --bootstrap-server my-kafka.default.svc.cluster.local:9092 --topic modelforops --from-beginning</code></p>
</li>
</ul>
<p><code>kafka delete po --all</code></p>
<hr />
<h2 id="frontend를-정적웹서버로-서빙">frontend를 정적웹서버로 서빙</h2>
<blockquote>
<p>frontend 앱을 docker이미지로 만들고, 웹서버 컨테이너로 배포하는 과정
정적 HTML/CSS/JS 를 웹서버로 서빙한다. </p>
</blockquote>
<p><strong>프론트엔드 앱 로컬 확인</strong>
<code>npm install</code>
<code>npm run serve</code>으로 서빙이 되는지 확인한다.</p>
<p><strong>빌드(정적 웹 페이지 생성)</strong>
<code>npm run build</code> ㅇ로 빌드의 결과이다.
<code>build</code>는 패키징한거를 dist에 담아둔다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/04136e1d-87dd-4266-914b-e383133b472f/image.png" /></p>
<ul>
<li>dist/ 폴더 안에 index.html, main.js, style.css 등 정적 파일 생성된다.</li>
<li>웹서버에 넣어서 사용이 가능하다.</li>
</ul>
<p>** Docker 이미지로 패키징**
<code>docker build -t ehekaanldk/frontend:20250617 .</code></p>
<ul>
<li>Dockerfile에서 dist 폴더의 내용을 웹서버(Nginx 등)에 복사해서 정적 파일을 서빙하는 이미지 생성</li>
</ul>
<p><strong>docker hub에 이미지 푸시</strong>
해당 폴더에서 docker build하면 된다. </p>
<p><code>docker push ehekaanldk/frontend:20250617</code></p>
<p>빌드를 하면 dist 폴더 내에 html, css, js 가 만들어진다. 
html, css, js를 웹서버에 원래는 가져가서 웹서버가 떠잇는 상태니까 브라우저가 요청?을 하면? 웹서버가 index.html을 넘겨주면서<br />이후에 브라우저는 모두 받아서 그걸 이용해서 cSR를 한다. </p>
<p>html, css, js파일들을 이용해서 웹서버에게 주고 contrainer가 되면 된다. 
웹서버게에 복사해서 주고 그거를 컨테이너로 띄우는 것이다. </p>
<p>빌드를 하고 정적 웹서비스에 올릴 수 있다. </p>
<p>*<em>gateway ip의 external 포트 : 8080 으로 접속할 수 있다. *</em></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/efea6a8d-393d-4911-86a0-1ad450227b3f/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/427002ce-a0b5-4764-be1c-f90b9f87e2e6/image.png" /></p>
<hr />
<h2 id="label">Label</h2>
<blockquote>
<p>쿠버네티스에서 객체를 식별하고 분류하기 위한 key-value 쌍의 메타데이터</p>
</blockquote>
<p>selectors 로 특정 리소스를 필터링한다.</p>
<p>레이블은 지정한 이후에 선택할 수 있다. </p>
<ul>
<li>env==dev</li>
<li>배포 환경(env=dev, env=prod), </li>
<li>앱 버전(version=v1), </li>
<li>역할(tier=frontend) 등을 식별한다.</li>
</ul>
<p>label</p>
<pre><code>kubectl delete deploy --all
kubectl delete svc --all</code></pre><p><strong>라벨을 달아서 deploy를 생성한다.</strong>
kubectl apply -f - &lt;&lt;EOF ... EOF 명령은 라벨(label)을 포함한 Deployment 객체를 생성하는 코드</p>
<pre><code>kubectl apply -f - &lt;&lt;EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: home
spec:
  replicas: 1
  selector:
    matchLabels:
      app: home
  template:
    metadata:
      labels:
        app: home
    spec:
      containers:
        - name: home
          image: apexacme/welcome:v1
          ports:
            - containerPort: 80
EOF</code></pre><p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/9de883b2-a7af-4be0-909a-fe7b0885adad/image.png" /></p>
<p>kubectl get pods -l app=home
kubectl get pods --selector app=home
kubectl delete pod -l app=home</p>
<p>kubectl get pods --selector 'app in (home, home1)'
kubectl get po --selector 'env in(home, home1), app in (home, home1)'</p>
<p>kubectl get deploy
kubectl label deploy home app=home
kubectl get deployment --show-labels
kubectl delete deploy --selector app=home
kubectl get all</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d5f83b7e-28ac-4f43-a932-17a908cec586/image.png" /></p>
<h3 id="서비스-롤백에-annotation-활용">서비스 롤백에 annotation 활용</h3>
<p><code>kubectl create deploy home --image=apexacme/welcome:v1</code></p>
<p>버전을 관리한다. 
<code>kubectl get deploy -o wide</code> 
원래꺼보다 더 많은 정보를 보여준다. </p>
<p>배포 주석으로 해당 home에 내용을 기록한다.
<code>kubectl annotate deploy home kubernetes.io/change-cause=&quot;v1 is The first deploy of My Homepage.&quot;</code></p>
<p>이미지를 set할 떄 어느 deploy를 할지 적어준다. home
<code>kubectl set image deploy home welcome=apexacme/welcome:v2</code></p>
<ul>
<li>deploy이름 container이름 순으로 작성해줘야 한다. </li>
</ul>
<p><strong>annotation을 모두 확인한다.</strong>
<code>kubectl rollout history deploy home</code></p>
<p><strong>rollback한다.</strong>
<code>kubectl rollout undo deploy home</code> </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/70d22966-4ffd-4620-b0c4-6f3bdd95bb37/image.png" /></p>
<p>ver1로 rollback되었다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/547191b3-64e3-435b-b07b-31a82b6964b0/image.png" /></p>
<h2 id="scale-out">Scale out</h2>
<ul>
<li>monolith 로 서비스를 배포한다. 
kubectl create deploy order --image=jinyoung/monolith-order:v20210504</li>
<li>expose 하면 서비스가 등록된다. 
kubectl expose deploy order --port=8080</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/6bdf0bc8-9191-4463-802e-6e18c1699cc9/image.png" /></p>
<ul>
<li>scale 하면 replicaset 를 늘릴 수 있다. 
<code>kubectl scale deploy order --replicas=3</code>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b03932c5-88e7-495b-8e4d-fea141ed6f2e/image.png" /></li>
</ul>
<h3 id="auto-scale-out">Auto scale out</h3>
<p>Pod로 부하를 준다. (시즈?)
siege 라고 하는 파트 안에 들어가서 /bin/bash로 들어갈 수 있다. 
kubectl exec -it siege -- /bin/bash</p>
<p>siege -c1 -t2s -v <a href="http://order:8080/orders">http://order:8080/orders</a></p>
<p>AKS 안에 oreder라는 서비스를 만들어서 배포를 했고, siege 라는 pod를 만들어서 배포했다. 모든 요청은 하나의 pod 안에 다 들어가도록 </p>
<p>어느정도 cpu를 사용하는지 측정
원래는 meteric을 설치해야하지만 이미 설치가 되어 있음
kubectl top pods
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/decdd409-b110-4f91-b6f8-d710d2ea50da/image.png" /></p>
<p>1개에서 3개 사이의 스케일  범위?&gt;? 준다?
<code>kubectl autoscale deployment order --cpu-percent=50 --min=1 --max=3</code></p>
<p>auto scaling은 절대적인 기준이 필요하다. 
order라는 서비스를 deploy할 때 기대하는 기준값이 있어야 이를 보고 50%인지 80%라고 할 수 있다. </p>
<p>/order-deploy.yaml </p>
<pre><code>apiVersion: apps/v1
kind: Deployment
metadata:
  name: order
  labels:
    app: order
spec:
  replicas: 1
  selector:
    matchLabels:
      app: order
  template:
    metadata:
      labels:
        app: order
    spec:
      containers:
        - name: order
          image: jinyoung/monolith-order:v20210602
          ports:
            - containerPort: 8080
          resources: 
            requests:
              cpu: &quot;200m&quot;            
          readinessProbe:
            httpGet:
              path: '/actuator/health'
              port: 8080
            initialDelaySeconds: 10
            timeoutSeconds: 2
            periodSeconds: 5
            failureThreshold: 10
          livenessProbe:
            httpGet:
              path: '/actuator/health'
              port: 8080
            initialDelaySeconds: 120
            timeoutSeconds: 2
            periodSeconds: 5
            failureThreshold: 5</code></pre><p>kubectl apply -f order-deploy.yaml </p>
<p>배포 파일에 기준에 대한 것을 작성해줘야 한다. 
limit , requset 를 보고 agent pool 에서 워커 노드들을 배치할지를 정한다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/300d4e7c-e197-4ebe-9c61-c747162b44ca/image.png" /></p>
<hr />
<h2 id="router-for-containers--service">Router for Containers : Service</h2>
<p>service scope</p>
<pre><code>  apiVersion: v1
  kind: Service
  metadata:
    name: my-service
  spec:
    selector:
      app: order
    ports:
      - protocol: TCP
        port: 8080
        targetPort: 8080
    type: ClusterIP/NodePort/LoadBalancer        </code></pre><ul>
<li>type을 생략하면 clusterIP가 된다. </li>
</ul>
<p>yaml파일을 사용(<code>kubectl apply -f kubernetes/service.yaml</code>
)해서 하거나 <code>kubectl expose deploy order --type=ClusterIP --port=8080 --target-port=8080</code> 를 사용해서 할 수 있다. </p>
<p>http <a href="http://10.0.66.31:8080">http://10.0.66.31:8080</a></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a821367b-832b-4b73-a4ad-264b271c5f88/image.png" /></p>
<p>order cluster는 실제 order pod를 가르키고 있다.</p>
<p>서비스를 얼마나 공개하고 싶은지에 대해서 3가지 방법 중에 선택할 수 있다. </p>
<p>kube-dns
서비스를 조회할 때 서비스의 이름으로 바로 조회해준다. </p>
<p>뭔소리고~</p>
