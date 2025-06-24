---
title: "[CI/CD] Istio"
date: "2025-06-24"
link: "https://velog.io/@ehekaanldk/CICD"
series: "Uncategorized"
---

<p>ACR
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ec50ce0d-f7ed-49d0-962f-10b06a1530e3/image.png" /></p>
<p><strong>ACR와 AKS 바인딩</strong>
<code>az aks update -n (Cluster-NAME) -g (RESOURCE-GROUP-NAME) --attach-acr (REGISTRY_NAME)</code></p>
<ul>
<li>AKS는 이미지가 실행되는 런타임 쿠버네티스</li>
<li>ACR은 클러스터 배포 전에 이미지가 저장되는 저장소</li>
</ul>
<p><strong>현재 context의 위치를 확인</strong>
<code>kubectl config current-context</code></p>
<p>AKS를 바라보고록 context switching해서..??뭐여?</p>
<p>쿠버네티스 내부에서 클러스터 데이터베이스가 있어서 </p>
<p>order&gt;application.yaml 에서 
profile, docker, co</p>
<p>configmap?</p>
<blockquote>
<p>ConfigMap은 쿠버네티스(Kubernetes)에서 <strong>설정 파일(configuration)</strong>을 관리하기 위한 리소스</p>
</blockquote>
<p>컨피그맵(Configmap)은 쿠버네티스가 컨테이너에서 필요한 환경설정 내용을 컨테이너와 분리해 저장하고 제공해 주기 위해 사용한다.</p>
<p>애플리케이션을 개발하고 배포할 때, 보통 코드와는 별도로 설정값이 필요하다.</p>
<ol>
<li>imperative한 방식? =&gt; command로 보낸다. 
<code>kubectl create configmap my-config --from-literal=class=MSA --from-literal=Lab=ConfigMap</code></li>
</ol>
<p><code>kubectl get configmap</code>
<code>kubectl get cm -n default</code>
namespace 설정 안해주면 default</p>
<p><code>kubectl get configmap my-config -o yaml</code>
데이터라고 하는 ?? 데이터가 보여진다.
리소스들은 타입별로 달라진다? 뭔소리?</p>
<ol start="2">
<li>yaml 파일로 만드는 방식<pre><code>kubectl apply -f - &lt;&lt;EOF
apiVersion: v1
kind: ConfigMap
metadata:
name: config-dev
namespace: default
data:
ORDER_DB_URL: jdbc:mysql://mysql:3306/connectdb1?serverTimezone=Asia/Seoul&amp;useSSL=false
ORDER_DB_USER: myuser
ORDER_DB_PASS: mypass
ORDER_LOG_LEVEL: DEBUG
EOF</code></pre></li>
</ol>
<p>configmap 예제코드 다운로드
<code>git clone https://github.com/msa-school/lab-shop-configmap.git</code></p>
<p>deployment 하위에 배포 spec 들이 작성된다. 
env: 환경변수인 configmap과 관련된 정보를 넣는다. 
환경변수 ORDER_LOG_LEVEL 은 configmapkeyref을 참조한다. 
yaml </p>
<p>docker 대신에 acr을 사용한다. 
컨테이너가 될때 env 환경변수 설정이 들어가게 되는 것이다. </p>
<p>/lab-shop-configmap/order 에서 
order 를 클러스터에 배포한다.
<code>mvn package -B -DskipTests</code> =&gt; jar 파일 만들기
<code>docker build -t [acr이름].azurecr.io/order:v1 .</code>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c503715a-1f10-4c08-997e-e9a2ca29d9d4/image.png" /></p>
<p>저장소에 푸시한다.
<code>docker push username/order:v1</code></p>
<p>UNAUTHORIZED 로 로그인을 하지 않아서 보낼 수 없다. 
docker에 로그인이 필요하다. ACR도 마찬가지로 로그인을 해줘야한다. </p>
<p><code>az acr login --name [registry_name]</code> 하고 다시 push하면 된다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ab05782a-e4a7-409b-9c8c-b4902053a8b7/image.png" /></p>
<p>이미지를 배포할 때마다 태그가 달라야한다. 
버전관리를 위해서 rollback으로 돌아갈 수 있어서 
태그가 같으면 반영이 안된다.</p>
<p>yaml로 배포한다. 
yaml의 배포하는 이미지를 위에서 만든 것의 이름으로 넣어준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/dc08874e-4690-4bd8-8836-bbcc56465c52/image.png" /></p>
<ul>
<li>ORDER_LOG_LEVEL은 configmap에서 작성한 config-dev를 debug모드로..? <code>kubectl logs -l app=order</code></li>
</ul>
<p><code>kubectl apply -f kubernetes/deployment.yaml</code></p>
<p>쿠버네티스로 부터 받아서 전달하고 있는??
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/56318e0b-dc9e-409d-9a76-b90d9f2b21a1/image.png" /></p>
<p>설정값 중 ORDER_LOG_LEVEL=DEBUG 값을 → INFO로 수정</p>
<blockquote>
<p>ORDER_LOG_LEVEL
ORDER_LOG_LEVEL은 애플리케이션이 로그(기록)를 어떤 수준까지 출력할지 정하는 설정값</p>
</blockquote>
<p>kubectl delete pod -l app=order
kubectl logs -l app=order
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/83592201-cec1-439a-acc7-63ea1fd5bc9e/image.png" /></p>
<ul>
<li>exec는 실행되는 컨테이너 내부의 로그들을 확인하는 코드?
kubectl exec pod/order-7966866f79-2tpfp -- env
쿠버네티스가 실행 중인 주문 서비스 안에 env라는 커맨드를 실행한다. 
주문 os에 env라는 shellsrpit를 돌려서 
컨테이너의 환경 정보를 쥐고 있다가 넘겨주었다??
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/534433d3-8224-4448-8d64-b9f0a556578f/image.png" /></li>
</ul>
<h2 id="github-gitlab-gittea">GitHub, GitLab, GitTea</h2>
<p>github 이미지 저장소의 도커 허브의 준한다. 
gitlab 도 비슷?
gittea 국내 공공 클라우드 시장에서는 많이 사용한다. </p>
<p>mvn package
yaml로 말아서 배포
하는 파이프라인</p>
<p>Service Mesh</p>
<p>파이프라인이 자동으로 무정지 배포되어서?</p>
<h2 id="lstio-로-클라우드-네이티브-피처-확장">lstio 로 클라우드 네이티브 피처 확장</h2>
<h3 id="service-mesh">Service Mesh</h3>
<blockquote>
<p>클러스터에서 워킹하고 있는 마이크로서비스들 간의 통신을 관리해주는 인프라 레이어</p>
</blockquote>
<p>많은 서비스들이 서로 얽히고설킨 통신 구조로 망 Mesh의 의미를 가진다. Mesh 자체는 마이크로서비스(MSA)들이 서로 통신하는 구조이다. 서비스 A ↔ B ↔ C ↔ D처럼 서로 연결되어 얽히고설킨 네트워크 구조가 된 것이라고 생각하자!</p>
<p>마이크로서비스들끼리 통신은 가능하지만...</p>
<ul>
<li>장애 나면?</li>
<li>어디로 트래픽 보낼까?</li>
<li>보안은 어떻게?</li>
<li>로그는 어떻게 수집?</li>
</ul>
<p>이걸 <strong>자동으로 해주는 시스템</strong>이 바로** Service Mesh이**다.</p>
<p><strong>sidecar</strong> : 비서실?의 개념으로 보조 컨테이너</p>
<ul>
<li>마이크로서비스에 sidecar라는 개념이 자동으로 붙는다. </li>
<li>sidecar가 마이크로서비스 사이에 트래픽을 관리한다. </li>
<li>pod 내 동일한 네임스페이스와 volume, network 를 공유한다. </li>
</ul>
<p>sidecar를 붙이는 주체는 mesh 플랫폼으로, Service Mesh 플랫폼이 자동으로 붙인다. Istio는 서비스를 배포할 때마다, 각 서비스 Pod 옆에 자동으로 Envoy Proxy를 붙여서 같이 배포한다. </p>
<p>mesh 네트워크 중의 하나가 isto 이다. lstio는 쿠버네티스를 조력해주는 작은 배라는 개념이다. pod는 고래의 그물? azure 는 쪽빛? </p>
<p><strong>Fault Isolation</strong></p>
<p>Hashcorp, Consul</p>
<p>Inner Archi와 Outer Archi 사이에서 service mesh는 Inner를 제외한 나머지에 모두 영향을 미친다. </p>
<p>A 서비스가 B 서비스를 호출할 때 B가 응답이 없으면 B에 대한 트래픽 원천 차단?</p>
<p>페인트 클라이언트?</p>
<p>사이드카 프록시는 service mesh에 활동하는 방향
라이브러리는 코드 레벨</p>
<h3 id="lstio-service-mesh">lstio Service Mesh</h3>
<p>Service가 트래픽을 배분한다. Pod가 3개이면 기본적인 라운드로빈으로 트래픽을 배분한다. </p>
<p>v1이 실행 중이고, v2를 추가하게 되면 무정지 배포가 이뤄진다. </p>
<p>lstio를 사용하면 rolling update가 아니라 카나리 배포를 한다. 
이는 쿠버네티스는 불가능한 전력이다. 
lstio 가 카나리 배포를 지원한다. </p>
<h2 id="배포-전략">배포 전략</h2>
<p>recreate : 금융도메인에서 사용하는 전략으로, Downtime이 존재한다. </p>
<p>ramped : 새 배포 버전을 점차적으로 rollout한다. 쿠버네티스의 전략이다. </p>
<p>canary : 특정 유저 집단에게만 배포가 가능한 전략이다. 베타 오픈이나 알파오픈으로 점진적으로 확장한다. </p>
<h3 id="실습--lstion">실습 : lstion</h3>
<p><code>kubectl version</code>
문제 생기면 clinet version을 고쳐준다.
Server Version: v1.31.8</p>
<p><code>export ISTIO_VERSION=1.24.6</code>
lstio와 kubectl의 server version을 맞춘다. </p>
<p><code>curl -L https://istio.io/downloadIstio | ISTIO_VERSION=$ISTIO_VERSION TARGET_ARCH=x86_64 sh -</code>
Istio 설치 스크립트를 자동으로 내려받아서 실행한다. </p>
<p><code>istioctl install --set profile=demo --set hub=gcr.io/istio-release</code>
Istio는 <strong>Sidecar Proxy(Envoy)</strong> 를 자동으로 각 Pod 옆에 붙여줍니다. 이 프록시는 이미지 형태로 컨테이너로 설치한다. 
sidercar로 생성되는 이미지가 저장되는 위치가 <code>gcr.io/istio-release</code> 이다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7813fb1a-4c58-45e0-852d-a7d28a7f1230/image.png" /></p>
<p><code>kubectl get namespace</code>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/602c3fe2-c498-4d2e-b0a2-3d38668392eb/image.png" /></p>
<p>해당 pod안에 들어와야하는 총 값이 분수로 나타난다.
istio 관련 pod들이 다 running 중이다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/bb0571e7-1775-404c-b409-fede588fa336/image.png" /></p>
<p><code>mv samples/addons/loki.yaml samples/addons/loki.yaml.old</code></p>
<p><code>curl -o samples/addons/loki.yaml https://raw.githubusercontent.com/msa-school/Lab-required-Materials/main/Ops/loki.yaml</code></p>
<p><code>kubectl apply -f samples/addons</code></p>
<p>.....?&gt;??
서비스 메시 모니터(kiali) 접속</p>
<p>sidecar까지 붙었을 때 pod가 2개 떠야한다. sidecar가 injection 되어야 한다. 
<code>istioctl</code></p>
<pre><code>/istio-1.24.6/deployment.yaml 에 생성
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-nginx
  template:
    metadata:
      labels:
        app: hello-nginx
    spec:
      containers:
        - name: hello-nginx
          image: nginx:latest
          ports:
            - containerPort: 80</code></pre><p>sidecar를 addon하고 output.yaml로 받는다. 
<code>istioctl kube-inject -f deployment.yaml &gt; output.yaml</code></p>
<p><code>kubectl create ns tutorial</code> 로 namespace를 만들고 안에 <code>kubectl label namespace tutorial istio-injection=enabled</code> </p>
<p><code>kubectl apply -f deployment.yaml -n tutorial</code> tutorial 이라는 이름의 namespace에 deployment.yaml 을 배포한다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/dd492212-3926-4549-9008-ace6bd9c467e/image.png" /></p>
<ul>
<li>상세조회 시 namespace도 포함시켜야 한다.
<code>kubectl describe pod/hello-nginx-5464f686dc-d7t8g -n tutorial</code></li>
</ul>
<hr />
<h2 id="트래픽-배분관리와-카나리-배포">트래픽 배분관리와 카나리 배포</h2>
<p>게이트워이가 서비스로 보내고, 엑티베이션 되어 있는 pod의 개수에 맞게 서비스가 라운드로빈으로 트래픽을 차례대로 분배한다. 
서비스는 라운드로인으로 pod들에게 동등하게 배분한다. 
istio에서는 라운드로빈이 아닐 수 있다. traffic mgmt</p>
<p><strong>setting</strong></p>
<ul>
<li>kubcectl get all -n istio-system</li>
<li>kubectl get ing -n istio-system (ingress )
tracing IP
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b54c4190-9ac4-44b3-a292-d83e7c4b09fc/image.png" /></li>
</ul>
<p>ingress IP
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/9719cfea-dc2b-44f7-af5e-387fc9a78539/image.png" /></p>
<blockquote>
<p>확인코드</p>
</blockquote>
<ul>
<li>kubectl get ns</li>
<li>kubectl get all -n ingress basic</li>
</ul>
<blockquote>
<p>label 확인코드
kubectl get ns --show-labels</p>
</blockquote>
<p>kubectl get ns
kubectl get all -n tutorial
kubectl delete deploy hello-nginx -n tutorial (삭제할 때 객체의 타입과 ns 붙여줘야 함)</p>
<p>kubectl create namespace tutorial 
kubectl label namespace tutorial istio-injection=enabled</p>
<p>istio 설치</p>
<ul>
<li>export ISTIO_VERSION=1.24.6</li>
<li>curl -L <a href="https://istio.io/downloadIstio">https://istio.io/downloadIstio</a> | ISTIO_VERSION=$ISTIO_VERSION TARGET_ARCH=x86_64 sh -</li>
</ul>
<p>istio 설치 폴더로 이동</p>
<ul>
<li>cd istion-1.24.6/</li>
<li>kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml -n tutorial (istio를 설치할 때 dev로 설치함 이거 배포!)</li>
</ul>
<p>쿠버네티스가 컨테이너의 health check 에서 liveness probe</p>
<p>게이트웨이
main이 productpage(컨텐츠의 진입정)
main하위에 detail, 
main 하위에 review1,2,3</p>
<p>게이트웨이 (main: productpage)</p>
<ul>
<li>kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml -n tutorial</li>
<li>kubectl get svc istio-ingressgateway -n istio-system (확인)
게이트웨이의 external ip/productpage
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ef91bcee-10d4-4a3f-91a4-a8d0658753da/image.png" />
detail과 review가 결합되어 있음
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/9cb2ede3-59a4-459e-94c8-0bb2d884bf84/image.png" /></li>
</ul>
<p>mesh 설치하고 
책과 관련된 페이지 들
브라우저에서 로딩을 함
컨테이너에서 
cpu, 등의 요청 정보를 proxy가 보내고 있고,
통신이 필요할 떄 제대로 워킹하고 있음</p>
<blockquote>
<p>Kiali
Kiali는 Istio 기반의 Service Mesh를 시각화하고 관리하기 위한 대시보드 도구입니다.
즉, Service Mesh의 &quot;감시탑&quot; 역할을 해주는 모니터링/관찰(Observability) 스택</p>
</blockquote>
<p>kiali는 기본 모니터링 서비스 중 하나이고 ...? 뭐하는 스택이다?</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/988ee323-c1ba-4d94-83af-0f4a8b923a29/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/faf57bfd-057e-43e2-837b-83b0a7b86843/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/8ca5fd75-4092-4c59-959c-bf93021d2fa4/image.png" /></p>
<h3 id="istio-동적-트래픽-제어">istio 동적 트래픽 제어</h3>
<p>Sidecar Proxy는 트래픽을 제어할 수 있지만, 
어떻게 제어할지는 별도로 알려줘야 한다. 
각 pod의 사이드카가 
컨트롤 플레인</p>
<p>사이드카의 정책 관리를 위해서는 추가적인 리소스가 필욯다. 
deploy와 같은 객체 타입니다. 
해당 객체 타입들이 있어서 
추가적인 객체 타입(crd)을 설치해서 사용하낟. </p>
<ol>
<li><p>VirtualService
트래픽 라우팅에 대한 가중치 기반으로 제어하는 데 관여한느 서비스</p>
</li>
<li><p>DestinationRule
도달하는 목적지
백엔드 컨테이너들을 그룹핑하거나 목적지를 어떨게 관여하는 서비스</p>
</li>
</ol>
<p>DestinationRule 을 실행
컨테이너의 레이블을 가지고 ....? 뭐가 재정의?</p>
<ul>
<li><p>kubectl apply -f samples/bookinfo/networking/destination-rule-reviews.yaml -n tutorial</p>
</li>
<li><p>vi samples/bookinfo/networking/destination-rule-reviews.yaml (내부 내용 확인가능)</p>
</li>
</ul>
<p>VirtualService 로 
subset은 DR에서 식별한 레이블을 가진 컨테이너로 </p>
<ul>
<li>kubectl apply -f samples/bookinfo/networking/virtual-service-reviews-80-20.yaml -n tutorial</li>
</ul>
<p>트래픽의 유입을 가중치로 줄 수 있다. </p>
<pre><code>kubectl apply -f - &lt;&lt;EOF
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
  namespace: tutorial
spec:
  hosts:
    - reviews
  http:
  - route:
    - destination:
        host: reviews
        subset: v1
      weight: 30
    - destination:
        host: reviews
        subset: v2
      weight: 70
EOF</code></pre><pre><code>kubectl apply -f - &lt;&lt;EOF
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
  namespace: tutorial
spec:
  hosts:
    - reviews
  http:
  - route:
    - destination:
        host: reviews
        subset: v2
      weight: 100
EOF</code></pre><h3 id="웹-요청정보-기반-스마트-라우팅">웹 요청정보 기반 스마트 라우팅</h3>
<p>http 헤더를 가지고 분석한다. 유입되는 http 클라이언트 요청이 v2에 잇는 레이블을 가진 신규서비스로 보내고 그렇지 않으면 .....??
if than else route</p>
<p>브라우저 기반으로...
유입되는 http 헤더 조건에 따라서 분류?</p>
<pre><code>kubectl apply -f - &lt;&lt;EOF
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
  namespace: tutorial
spec:
  hosts:
  - reviews
  http:
  - match:
    - headers:
        baggage-user-agent:
          regex: .*Firefox.*
    route:
    - destination:
        host: reviews
        subset: v2
  - route:
    - destination:
        host: reviews
        subset: v1
EOF</code></pre><ul>
<li>v1은 별점이 없음</li>
<li>v2는 별점이 검은색</li>
<li>v3는 별점이 빨간색</li>
</ul>
<hr />
<h2 id="istio-timeout--retry">Istio timeout &amp; Retry</h2>
<p>서킷 브레이커 
istio는 배포 운영 단계이기에 컨테이너 ...</p>
<p>kubectl delete deployment,service --all -n tutorial</p>
<p>kubectl get dr -n tutorial
kubectl get vs -n tutorial</p>
<p>주문 서비스에서 응답시간 임계치에 따라 타임 아웃을 처리한다. 
스팩은 deploy, ns는 tutorail, replica는 1개</p>
<p>order 배포</p>
<ul>
<li>kubectl expose deploy order --port=8080 -n tutorial</li>
</ul>
<p>order 서비스의 타입아웃은 3초라고 정해준다. </p>
<pre><code>kubectl apply -f - &lt;&lt;EOF
    apiVersion: networking.istio.io/v1alpha3
    kind: VirtualService
    metadata:
      name: vs-order-network-rule
      namespace: tutorial
    spec:
      hosts:
      - order
      http:
      - route:
        - destination:
            host: order
        timeout: 3s
EOF</code></pre><ul>
<li>kubectl exec -it siege -c siege -n tutorial -- /bin/bash</li>
<li>siege -c1 -t4S -v --content-type &quot;application/json&quot; '<a href="http://order:8080/orders">http://order:8080/orders</a> POST {&quot;productId&quot;: &quot;1001&quot;, &quot;qty&quot;:5}'</li>
</ul>
<p>siege pod를 설치하고 해당 파드에 붙여서 </p>
<p>pod seige에서 order service에 보내고, pod order에 돌아온다?
시즈가 사이드카가 보내고, 줒문서비스의 타입아웃은                                                                                                                    ㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍㅍ                                                                                                                                                                                                                                                                                                                                                        </p>
<h3 id="retry">Retry</h3>
<p>retries: 부분을 추가해주면 된다. </p>
<pre><code>kubectl apply -f - &lt;&lt;EOF
  apiVersion: networking.istio.io/v1alpha3
  kind: VirtualService
  metadata:
    name: vs-order-network-rule
    namespace: tutorial
  spec:
    hosts:
    - order
    http:
    - route:
      - destination:
          host: order
      timeout: 3s
      retries:
        attempts: 3
        perTryTimeout: 2s
        retryOn: 5xx,retriable-4xx,gateway-error,connect-failure,refused-stream
EOF</code></pre><hr />
<p>kubectl top node
kubectl top pod</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/942a42c2-6d7c-40bb-8d5a-e039697fb3ac/image.png" /></p>
<h3 id="istio-서킷브레이커">istio: 서킷브레이커</h3>
<p>서킷브레이커에서 배송 서비스를 만들고
DR서비스 타입으로 내부에서 워킹하느</p>
<p>서브셋을 규정하고, vs에서 weight기반으로 트래픽을 보냄
DR은 백엔드 쪽에서...</p>
<p>배송 서비스에 대해서 controller plane에서 yaml로 실행하게 되면 각 pod의 sidecar 들이 policy 하나의 정보를 모두 전파 받는다. 
배송과 관련된 policy 이지만 모든 sidecar들이 다 지배를 받는다. </p>
<pre><code>kubectl apply -f - &lt;&lt; EOF
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: dr-delivery
  namespace: tutorial
spec:
  host: delivery
  trafficPolicy:
    loadBalancer:
      simple: ROUND_ROBIN
      localityLbSetting:
        enabled: false
    outlierDetection:
      interval: 10s
      consecutive5xxErrors: 1
      baseEjectionTime: 3m
      maxEjectionPercent: 100
EOF</code></pre><p>outlierDetection 이상감지를 해서 
3분동안 해당 대상 pool에서 ejection(잠깐 빼둔다) baseEjectionTime
해당 컨테이너은 제외하고 라운드로빈을 돌린다. </p>
<p>환경 정보를 컨테이너로 부터 독립시킴 : configmap</p>
<p>이미지 불변의 법칙 </p>
<p>2개의 컨테이너인 pod = siege, istio 에서 해당 컨테이너를 작성해주고, 안에 ns를 지정해주고, -- /bin/bash 커멘드를 마지막에 넣어준다. </p>
<p>siege 는 해당 리전에 들어가서 안에 만든 컨테이너 안으로 들어오게 해주다. 
http <a href="http://delivery:8080/actuator/echo">http://delivery:8080/actuator/echo</a> 로 요청을 보낸다. </p>
<p>첫번쨰 컨테이너의 해당 배송 컨테이너의 host이름/클러스터 IP가 출력된다. 
동일한 명령어를 보내면 replica 2로 설정한 두 컨테이너의 번호를 알 수 있다. 
10.244.2.77 , 10.244.3.209
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b6085321-85b5-4278-acea-059efe0c374a/image.png" /></p>
<p>pod ip에 직접 접근한다. 
보통은 게이트웨이를 통해서 접근하는게 정석이다. </p>
<p>http PUT <a href="http://10.244.3.209:8080/actuator/down">http://10.244.3.209:8080/actuator/down</a> 로 하나의 컨테이너를 정해서 다운시킨다. 이제 500 에러를 내게 될 것이다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/dd017019-4a16-41d7-88e8-2c5c2ee8e97f/image.png" /></p>
<p>http GET <a href="http://delivery:8080/actuator/health">http://delivery:8080/actuator/health</a> 으로 확인한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b8227a0f-35d5-489c-865a-12eaa2677bbd/image.png" /></p>
<p>500 에러를 내렸을 떄 3분간 퇴장한 것을 확인한다. 
http <a href="http://delivery:8080/actuator/echo">http://delivery:8080/actuator/echo</a> 로 확인하면 해당 209 번은 퇴장되어서 등장하지 않는다. 77 번 컨테이너만 계속 나오게 된다.
3분 이후에는 209번이 다시 보이게 된다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/4e63d661-ad82-4a4e-ae72-c6fb936dbd04/image.png" /></p>
<p>kiali 에서 확인할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c0e677e2-e852-427a-b591-0a88c870c5c6/image.png" /></p>
<h2 id="모니터링-istio-addon-grafana">모니터링 istio addon grafana</h2>
<p>ns 지우기</p>
<ul>
<li>kubectl delete ns [tutorial]</li>
</ul>
<p>ingress 지우기</p>
<ul>
<li>kubectl get ingress -n [ingress-basic]</li>
</ul>
<p>kubectl create ns shop
kubectl label namespace shop istio-injection=enabled</p>
<p>kubectl apply -f <a href="https://raw.githubusercontent.com/acmexii/demo/master/edu/order-liveness.yaml">https://raw.githubusercontent.com/acmexii/demo/master/edu/order-liveness.yaml</a> -n shop
kubectl expose deploy order --port=8080 -n shop
kubectl apply -f <a href="https://raw.githubusercontent.com/acmexii/demo/master/edu/delivery-rediness-v1.yaml">https://raw.githubusercontent.com/acmexii/demo/master/edu/delivery-rediness-v1.yaml</a> -n shop
kubectl expose deploy delivery --port=8080 -n shop</p>
<p>observablity의 promatheus 를 사용한다. 
모니터링이 아니라 왜 observablity를 사용하는가?</p>
<ul>
<li>모니터링은 직접 코드 스택에 agent를 심거나 빨대를 꽂아서 사용하는 것이다.</li>
<li>observablity는 옵저버(관찰자)는 외부에 들어나는 상태 정보값을 가지고 내부 속마음을 유추하는 것이다.</li>
<li>observablity는 뭔가 저장소에 설치를 하거나 시각화의 정보를 가져오는 것이 아니라 sidecar에 의해서 working한 정보들을 모으는 한 층이 더 있는 것이고 chart tool이 이 층을 바라보고 있는 것이고 이르 거쳐서 한 호흡을 더 가진다.</li>
</ul>
<p>서비스 조회</p>
<ul>
<li>kubectl get svc -n istio-system 를 통해서 내부에 grafana와 promatheus가 있는지 확인한다. </li>
</ul>
<p>서비스의 tracing의 타입을 Cluster IP 타입으로 변경하도록 수정한다. tracing은 ELB이였던 것을 Cluster IP 으로 변경하면서 External IP가 사라진다. 
kubectl patch svc kiali -n istio-system -p '{&quot;spec&quot;: {&quot;type&quot;: &quot;ClusterIP&quot;}}'
kubectl patch svc tracing -n istio-system -p '{&quot;spec&quot;: {&quot;type&quot;: &quot;ClusterIP&quot;}}'
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b5ec9358-9bed-446f-aef8-3488d31abb7d/image.png" /></p>
<p>promatheus 를 ELB으로 타입을 변경한다. promatheus는 모니터링 스택이다.
kubectl patch service/prometheus -n istio-system -p '{&quot;spec&quot;: {&quot;type&quot;: &quot;LoadBalancer&quot;}}'
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/fe38860e-df2a-42b6-b9ee-615baabcc798/image.png" /></p>
<p>해당 promatheus의 external IP를 이용해서 <a href="http://20.249.162.176:9090/">http://20.249.162.176:9090/</a> 으로 접속한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/07729670-df77-47be-afb2-fcab69ae10fd/image.png" /></p>
<p>kubectl get all -n shop
워크로드 생성기인 Siege Pod를 생성한다</p>
<pre><code>kubectl apply -f - &lt;&lt;EOF
apiVersion: v1
kind: Pod
metadata:
  name: siege
  namespace: shop
spec:
  containers:
  - name: siege
    image: apexacme/siege-nginx
EOF</code></pre><p>kubectl exec -it pod/siege -n shop -- /bin/bash
http GET <a href="http://order:8080">http://order:8080</a>
http GET <a href="http://order:8080/orders">http://order:8080/orders</a></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/e2ac8b89-f43f-4a15-8fd7-9f4c91f98af7/image.png" /></p>
<p>엑셀의 수식처럼 request total에서 end 조건으로 들어간다. 
app=order 라는 타겟에 대해서 responde 코드가 500대가 아닌 것에 대해서 수행한다. </p>
<p>order 서비스에 30명이 40초 동안 부하를 넣어본다. </p>
<ul>
<li>siege -c30 -t40S -v <a href="http://order:8080">http://order:8080</a></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/86b0db4a-7080-46e0-ac9d-fbd0c0a5780d/image.png" /></p>
<p><a href="https://istio.io/latest/docs/reference/config/metrics/">https://istio.io/latest/docs/reference/config/metrics/</a> 에서 지금까지의 ision_requset_total 과 다양한 피쳐들을 메트릭을 사용할 수 있다.</p>
<p>동일 ns에 있는 </p>
<p>레이블이다. 컨테이너에 다 붙어있는 것</p>
<p>app=order 는 컨테이너가 가지는 레이블이다. 
쿠버네티스에서는 왠만한 것들이 레이블 단위이다. 
request total 로 </p>
<h2 id="grafana">Grafana</h2>
<p>grafana는 대시보드..스택?</p>
<p>grafana를 ELB로 타입을 설정해준다. 
kubectl patch service/grafana -n istio-system -p '{&quot;spec&quot;: {&quot;type&quot;: &quot;LoadBalancer&quot;}}'</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/f8752b73-0c07-4a77-b7a4-66fbe6979bac/image.png" /></p>
<p>kafka 시간에 나이트메어??</p>
<p>Dashboard에서 6417 을 입력해서 차트를 로딩한다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/548d0b51-062b-411a-b8b9-9c1651ff3ecb/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d3134ae6-701f-4c5b-b6c6-702a57f5cc9c/image.png" /></p>
<p>Dashboard에서 315 을 입력해서 차트를 로딩한다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/3d3c1bce-126a-4237-b521-afb4ffd88cce/image.png" /></p>
<p>내 클러스터를 반영해주는 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/15b49145-257c-4a0f-bb9b-10196f132d36/image.png" /></p>
<h3 id="dashboard-customizing">Dashboard Customizing</h3>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/88adae5b-b64c-46ed-ab68-434eca09e792/image.png" /></p>
<p>길이를 기반으로  뭐를 하겠다는 query를 넣어줄 수 있다.</p>
<ul>
<li>rate(istio_requests_total{app=&quot;order&quot;,destination_service=&quot;order.shop.svc.cluster.local&quot;}[5m])
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/fbdfb732-ffae-4b7a-b2b0-1926c6ffa7a8/image.png" /></li>
</ul>
<p>대시보드를 확인할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/e2904d16-4bd3-4c57-8a9d-3a1ea153b408/image.png" /></p>
<p>siege에서 부하를 주게되면 그래프가 변화하는 것을 볼 수 있다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/524f4a4f-b53c-4898-ae01-caea7b57d6bd/image.png" /></p>
<p><a href="https://grafana.com/grafana/dashboards/">https://grafana.com/grafana/dashboards/</a></p>
<p>사용 후 ELB로 변경했던 것을 다시 ClusterIP로 되돌려 놓는다. 금액 사용 안하게 됨.?</p>
<ul>
<li>kubectl patch svc grafana -n istio-system -p '{&quot;spec&quot;: {&quot;type&quot;: &quot;ClusterIP&quot;}}'</li>
<li>kubectl patch svc prometheus -n istio-system -p '{&quot;spec&quot;: {&quot;type&quot;: &quot;ClusterIP&quot;}}'</li>
</ul>
<h2 id="loggregation">loggregation</h2>
<p>log를 aggregation한다. </p>
<h2 id="rollout">rollout</h2>
<h3 id="blue-green-배포--canary-배포">blue-green 배포 &amp; canary 배포</h3>
<p>기본 쿠버네티스는 불가한 방법이다. 
mesh 지원이 가능해야 가능한 배포들이다. </p>
<p><strong>canary</strong>
신규 서비스에 대한 범위를 늘려가는 것이 canary 배포이다. 
점진적으로 스케일인이 가능하다.
사용자를 서브셋으로 나눈다.</p>
<p><strong>blue-green</strong>
blue는 older를 말하고 green은 신규를 의미한다. 
cloud cost가 높은 특징을 가진다. 
문제가 없으면 기존의 서비스 레벨이 신규 서비스를 바라보는 전략이다. 
롤백이 상대적으로 빠르다.</p>
<h3 id="실습1--argo-rollout---canary">실습1 : argo rollout -&gt; Canary</h3>
<p>CRD는 ?</p>
<p>argo rollout 는 rollout 전략과 관련된 스택이다. </p>
<p>웹 상에 있는 argo rollout 에 관여하는 것을 배포한다. </p>
<ul>
<li><code>kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml</code></li>
<li>kubectl get all -n argo-rollouts (확인코드)</li>
</ul>
<p>yaml을 가지고 <strong>Rollout 배포 타입</strong>을 가진다.</p>
<ul>
<li>한 yaml 안에 다양하게 넣어줄 때 ---으로 페이지를 구분한다.</li>
<li>서비스를 ELB 타입으로 </li>
<li>상위의 스팩은 기본스팩과 같다. (deployment)</li>
<li>추가적인 스팩에는 canary가 있다 (strategy)</li>
<li>setWeight 신규 서비스에 대한 비율을 나타낸다.<pre><code>apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
name: example-rollout
spec:
replicas: 10
selector:
  matchLabels:
    app: nginx
template:
  metadata:
    labels:
      app: nginx
  spec:
    containers:
    - name: nginx
      image: nginx:1.19.10
      ports:
      - containerPort: 80
minReadySeconds: 30
revisionHistoryLimit: 3
strategy:
  canary:                     # Canary 배포 전략 적용
    maxSurge: &quot;25%&quot;
    maxUnavailable: 0
    steps:
    - setWeight: 10           # 트래픽 10%만 신규 Pod로 전달 
    - pause:
        duration: 10s         # 10초 동안 현 상태 유지
    - setWeight: 20
    - pause:
        duration: 10s 
    - setWeight: 30
    - pause:
        duration: 10s 
    - setWeight: 40
    - pause:
        duration: 10s </code></pre></li>
</ul>
<hr />
<p>  apiVersion: &quot;v1&quot;
  kind: &quot;Service&quot;
  metadata: 
    name: &quot;nginx&quot;
    labels: 
      app: &quot;nginx&quot;
  spec: 
    ports: 
      - 
        port: 80
        targetPort: 80
    selector: 
      app: &quot;nginx&quot;
    type: &quot;LoadBalancer&quot;</p>
<pre><code>
rollout 을 배포해준다.
- kubectl apply -f rollout.yaml
- kubectl get rollout (확인)
![](https://velog.velcdn.com/images/ehekaanldk/post/8c886706-53f9-4cb5-b1cc-6797d46f348b/image.png)


argo rollout이 제공해주는 dashboard가 따로 있다. dashboard를 설치해준다. 
- ```curl -LO https://github.com/argoproj/argo-rollouts/releases/latest/download/kubectl-argo-rollouts-linux-amd64```
- ```chmod +x ./kubectl-argo-rollouts-linux-amd64```
- ```sudo mv ./kubectl-argo-rollouts-linux-amd64 /usr/local/bin/kubectl-argo-rollouts``` (권한부여)

3100 으로 rollouts 의 dashboard가 할당된다.
- kubectl argo rollouts dashboard
![](https://velog.velcdn.com/images/ehekaanldk/post/80f29d37-cb03-4395-a777-203b5bfced8a/image.png)


카나리 배포를 확인하기 위해서 ELB 타입의 nginx로 만들어 두었던 것을 조회한다. </code></pre><p>  spec: 
    ports: 
      - 
        port: 80
        targetPort: 80
    selector: 
      app: &quot;nginx&quot;
    type: &quot;LoadBalancer&quot;</p>
<pre><code>```kubectl get svc```
![](https://velog.velcdn.com/images/ehekaanldk/post/d9883e66-1fc4-42b2-8b4f-e85143582723/image.png)
해당 external ip로 접근할 수 있다. 
![](https://velog.velcdn.com/images/ehekaanldk/post/595319d9-d3e2-4801-ba51-7b8ecc7ee79e/image.png)


yaml 에서 acr 안에 있는 image로 바꾸어주던지 한다. 
새 버전으로 해서 배포를 해주면서 점진적으로 rollout되도록 한다. 


**이미지를 실시간으로 치환한다.**
yaml의 image에서 nginx:1.19.10 으로 작성된 부분을 jinyoung/app:blue 으로 치환한다.
- kubectl argo rollouts set image example-rollout nginx=jinyoung/app:blue
- revision1에서 revision2로 점진적으로 10개가 다 배포된다.
![](https://velog.velcdn.com/images/ehekaanldk/post/42c848bb-05b5-42ad-8cd6-54abacabd0b9/image.png)


![](https://velog.velcdn.com/images/ehekaanldk/post/d8c881dd-d933-44c2-9763-586d69db1899/image.png)
전이가 다 이루어지면 ```jinyoung/app:blue``` 의 파란화면이 나온다.
![](https://velog.velcdn.com/images/ehekaanldk/post/1acf7f73-fec9-4809-89d5-a2770d24cd09/image.png)


### 실습2 : argo rollout -&gt; Blue/Green 

Blue/Green 배포를 위한 yaml 파일을 만든다. 
</code></pre><p>apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: example-rollout
spec:
  replicas: 10
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.19.10
        ports:
        - containerPort: 80
  strategy:
    blueGreen:
      activeService: nginx-active
      previewService: nginx-preview
      autoPromotionEnabled: false  # 수동 승인을 위해 false
      previewReplicaCount: 2</p>
<pre><code>서비스 부분에도 넣어준다.</code></pre><h1 id="액티브-서비스-사용자-트래픽이-전달되는-곳">액티브 서비스 (사용자 트래픽이 전달되는 곳)</h1>
<p>  apiVersion: v1
  kind: Service
  metadata:
    name: nginx-active
  spec:
    selector:
      app: nginx
    ports:
    - port: 80
      targetPort: 80</p>
<hr />
<h1 id="프리뷰-서비스-새-버전만-연결됨">프리뷰 서비스 (새 버전만 연결됨)</h1>
<p>  apiVersion: v1
  kind: Service
  metadata:
    name: nginx-preview
  spec:
    selector:
      app: nginx
    ports:
    - port: 80
      targetPort: 80</p>
<pre><code>
kubectl get rollout 로 조회해서 나오는 rollout을 삭제한다. 
- kubectl delete rollout example-rollout
- kubectl delete service/nginx

yaml에서 strategy를 blueGreen로 바꾼 후에 배포를 한다.
- kubectl apply -f rollout.yaml

배포하게되면 nginx-active에 nginx-preview에 대해서 걸린다?
서비스가 2개이다. 

새 버전 승인
- ```kubectl argo rollouts promote example-rollout```
- nginx-preview 신규 버전에 문제가 없으면 nginx-active 서비스의 제어가 한번에 바뀐다.


### 실습3 : istio 에 기반한 canary 배포
</code></pre>
