---
title: "[DevOps]"
date: "2025-06-18"
link: "https://velog.io/@ehekaanldk/DevOps"
series: "Uncategorized"
---

<h2 id="label">label</h2>
<blockquote>
<p>label 은 쿠버네티스 리소스에 붙이는 key-value형태의 태그</p>
</blockquote>
<p>kubernetes의 객체라면 모두 label을 붙일 수 있다. </p>
<ul>
<li>Pod</li>
<li>Service</li>
<li>Deployment</li>
<li>ReplicaSet</li>
<li>Node</li>
</ul>
<p>label을 붙이는 목적</p>
<ul>
<li>요구사항에 맞춰 객체의 하위 집합을 구성하고 선택하기 위해 사용한다. </li>
<li>env=dev 라벨이 붙은 pod만 모아서 보기, 관리하기 등</li>
</ul>
<h2 id="label-selector">label selector</h2>
<blockquote>
<p>label이 붙은 객체들을 조건에 맞춰서 필터링하는 방법</p>
</blockquote>
<p>label selector는 객체들의 집합을 선택한다.</p>
<ul>
<li>라벨이 app=nginx인 것만 골라줘!&quot;
→ 이걸 Label Selector라고 한다.</li>
</ul>
<p>selector의 결과는 주로 Pod의 묶음 단위가 된다. </p>
<ul>
<li>Service가 label selector를 통해서 app=web인 pod를 골랐다면,</li>
<li>이 서비스는 그 pod들에만 트래픽을 전달한다. </li>
</ul>
<h2 id="replication-controllerrc">Replication Controller(RC)</h2>
<p>지정한 Pod의 개수를 유지하고, 
Pod가 죽으면 새로 만들어주고,
많으면 줄여주는 역할을 한다. </p>
<p>master node의 controller manager 중의 하나이다. </p>
<h3 id="추가controller-manager">[추가]controller manager??</h3>
<blockquote>
<p>쿠버네티스 내부에서 각종 컨트롤러들을 실행하고 관리하는 프로그램</p>
</blockquote>
<ul>
<li>ReplicaSet Controller</li>
<li>Node Controller</li>
<li>Job Controller</li>
<li>Endpoint Controller
이 모든 컨트롤러들이 돌아가는 실행 엔진이 controller manager이다.</li>
</ul>
<p>기존에 Deployment → ReplicaSet → Pod → Container 라고 이해했는데 
ReplicaSet도 동일하게 지정된 Pod의 개수를 유지해주는 것이다. </p>
<p>RC는 단순히 pod의 수를 유지하는 역할
deployment는 replicaset을 감싸서 버전 업데이트, 배포, 롤백 등을 하기 위해서 Deployment + ReplicaSet 구조를 사용한다. </p>
<h3 id="추가-deployment">[추가] Deployment</h3>
<blockquote>
<p>쿠버네티스에서 배포하겠다는 설명서!
Pods와 ReplicaSets 에 대한 선언적 업데이트를 제공한다. </p>
</blockquote>
<p>&quot;nginx 컨테이너를 3개 돌리고 싶어요.
pod가 죽으면 다시 만들고, 버전 바꾸고 싶을 땐 자연스럽게 바꿔줘요.&quot;
=&gt; yaml 파일로 작성해서 kubectl apply -f xxx.yaml로 배포한다. 
=&gt; 쿠버네티스가 해석해서 실제로 배포해주는 대상 =&gt; <strong></strong></p>
<h3 id="replicaset--pod의-생명-관리자">ReplicaSet : Pod의 생명 관리자</h3>
<blockquote>
<p>ReplicaSet은 지정한 수만큼 Pod를 유지시키러는 controller</p>
</blockquote>
<p>&quot;Pod가 3개 있어야 해!&quot; 하면
→ 실제로 그 pod 수를 유지시켜주는 게 ReplicaSet이다. </p>
<p>pod들의 복제본을 관리하는 부분이다. 
deployment없이 pod를 실습이나 학습 목적으로 유지할 때 사용한다. 
거의 replicaset이 독립적으로 사용되는 경우는 없으며 deployment가 대신한다. </p>
<pre><code>/replicaset.yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-replicaset  # ReplicaSet의 이름
spec:
  replicas: 3              # Pod 몇 개 만들지
  selector:                # 어떤 Pod를 관리할지 라벨 조건
    matchLabels:
      app: nginx
  template:                # ↓ 실제 Pod의 설계도
    metadata:
      labels:
        app: nginx         # ↑ 이 라벨이 selector와 일치해야 함
    spec:
      containers:          # ↓ 이 안이 실제 컨테이너 정의
        - name: nginx
          image: nginx:1.21
          ports:
            - containerPort: 80
</code></pre><ul>
<li>replicaset.yaml 안에는 replicaset 의 메타정보가 들어있다. </li>
<li>또한 pod 템플릿으로 Pod 안에 들어갈 컨테이너 정의가 적혀있다. </li>
</ul>
<h3 id="deployment와-replicaset">Deployment와 ReplicaSet</h3>
<pre><code>/kubernetes/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
spec:
  replicas: 3
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
          image: nginx:1.21
</code></pre><p>Deployment를 만들면</p>
<ul>
<li>쿠버네티스가 Deployment 내용을 바탕으로 ReplicaSet을 생성한다. </li>
<li>ReplicaSet이 Pod 3개를 생성한다. </li>
<li>Pod 안에서 <code>nginx:1.21</code> 컨테이너가 실행된다.</li>
</ul>
<p><strong>Deployment rollout</strong>
업데이트가 발생해 nginx:1.21 -&gt; nginx:1.22가 되면(pod template이 바뀌면)</p>
<ul>
<li>Deployment가 알아서 새 ReplicaSet을 생성하고,</li>
<li>새 ReplicaSet은 새로운 Pod를 생성하고,</li>
<li>예전 ReplicaSet의 Pod는 점점 삭제됨
=&gt; scaling 작업에서는 replicaset을 새로 생성하지 않는다.
=&gt; rollback 으로 문제 발생시 되돌릴 수 있다.</li>
</ul>
<p>결론적으로 
<strong>deployment</strong>는 <strong>사용자</strong>가 직접 만들고
Pod 개수 유지하는 <strong>replicaset</strong>은 <strong>Deployment가 자동 생성</strong>하고,
실제 컨테이너가 돌아가는 최소 단위인 <strong>Pod</strong>는 <strong>ReplicaSet이 생성</strong>한다.</p>
<h3 id="pod에-접속">Pod에 접속</h3>
<blockquote>
<p>컨테이너 안에 들어가서 확인하는 방법</p>
</blockquote>
<p><code>kubectl exec -it [pod이름] -- /bin/bash</code></p>
<p>실행하면 
<code>root@[pod이름]:/#</code> 으로 변경되어 리눅스로 명령어 입력이 가능하다. </p>
<h3 id="실습--label과-annotation-으로-객체-관리">실습 : label과 annotation 으로 객체 관리</h3>
<ul>
<li>pod 인스턴스에 label을 추가한다.
kubectl edit po [pod이름]</li>
</ul>
<p>kubectl get pods -l env=test
kubectl get pods --selector env=test</p>
<ul>
<li><p>replicaset을 확인할 수 있다.
kubectl get rs
kubectl describe rs</p>
</li>
<li><p>repliacset을 삭제할 수 있다. 
kubectl delete rs</p>
</li>
<li><p>deployment를 파일기반으로 배포한다. 
kubectl create -f deployment.yaml
kubectl apply -f deployment.yaml (해당 배포가 있으면 업데이트, 없으면 새배포)
kubectl describe deployment deployment.yaml (생성 확인)</p>
</li>
<li><p>deployment의 replicaset의 개수확인한다. 
kubectl get pods</p>
</li>
<li><p>deployment의 scale 수를 수동 조정한다. 
kubectl scale deployments [deployments 이름] --replicas=3</p>
</li>
</ul>
<p><strong>rolling update</strong>
kubectl apply -f deployment.yaml</p>
<ul>
<li><p>기존 Deployment에 정의된 컨테이너의 이미지를 새 버전으로 변경 (롤링 업데이트의 트리거 역할)
kubectl set image [리소스종류]/[이름] [컨테이너이름]=[새로운 이미지]</p>
</li>
<li><p>롤링 업데이트의 진행 상태를 보여준다. 
kubectl rollout status deployment/nginx-deployment</p>
</li>
</ul>
<p><strong>rollback</strong></p>
<ul>
<li><p>객체를 image 버전도 나오게 자세히 확인
kubectl get deployments -o wide</p>
</li>
<li><p>객체를 롤백 처리한다. 
kubectl rollout undo deployment/nginx-deployment</p>
</li>
</ul>
<hr />
<h2 id="namespaces--리소스의-논리적-부분">Namespaces : 리소스의 논리적 부분</h2>
<p>AKS 클러스터를 가상으로 여러개 나누어 이 나누어진 가상의 클러스터를 namespace라고 한다. </p>
<p>하나의 클러스터는 노드로 구성되어 있다. 
노드는 pod들이 올라가는 컴퓨터의 모음이다. </p>
<p>물리적으로는 하나이지만,
논리적으로 공간을 나눠둬야 여러팀과 환경이 완전히 분리된 공간처럼 사용할 수 있다. </p>
<pre><code>AKS 클러스터
├── Namespace: dev
│   └── Pod, Service, ConfigMap (개발팀)
├── Namespace: prod
│   └── Pod, Service, ConfigMap (운영팀)
├── Namespace: data-team
│   └── 분석 관련 리소스</code></pre><p>kubernetes는 생성 시에 4개의 namespace를 제공한다. </p>
<ul>
<li>default</li>
<li>kube-node-lease</li>
<li>kube-public</li>
<li>kube-system</li>
</ul>
<h2 id="service">Service</h2>
<p>Service가 필요한 이유</p>
<ul>
<li><p>Pod 안에 들어 있는 컨테이너가 실제 어플리케이션이다. 
pod는 컨테이너를 실행하기 위한 포장지/껍데기라고 생각한다.</p>
</li>
<li><p>어플리케이션에 접근하기 위해서 사용자가 pod에 직접 접근할 수 없다. </p>
</li>
<li><p>pod에 고정 IP로 사용자가 접근을 하게 되면,
pod가 죽거나 새로 생기면 그때마다 조치를 해줘야 한다. </p>
</li>
</ul>
<h3 id="service-1">Service</h3>
<blockquote>
<p>추상화된 객체인 Service를 통해서 
pod들의 논리적인 집단을 만들어서 규칙을 설정하고 
사용자는 service를 통해서 접속하도록 한다.</p>
</blockquote>
<ul>
<li>selector로 pod들을 논리적인 그룹으로 나누고 service ip를 연결해서,</li>
<li><strong>사용자</strong>가 <strong>service ip에 접속</strong>하면 selector로 묶인 <strong>pod들에 접근</strong>한다. </li>
<li>service는 각 pod들에 대해서 load balancing(트래픽 균등)을 자동 수행한다. </li>
</ul>
<pre><code>/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx               # 이 라벨을 가진 Pod에 연결
  ports:
    - protocol: TCP
      port: 80              # 서비스 포트
      targetPort: 80        # 실제 Pod(컨테이너)의 포트
  type: ClusterIP           # 서비스 타입 (내부 접근만 허용)</code></pre><ul>
<li>사용자는 service ip 주소를 통해서 pod에 접속한다. </li>
<li><strong>각 service 에 부여된 IP</strong>를 <strong>cluster IP</strong>라고 한다. </li>
</ul>
<h3 id="kube-proxy-데몬">kube-proxy 데몬</h3>
<p>Service는 가상의 객체로 사용자에게 
고정 cluster IP를 제공하는 트래픽 라우터 역할을 한다.</p>
<blockquote>
<p>Service 자체에서는 트래픽을 처리하지 않고, 실제 트래픽을 전달하는 것이 kube-porxy이다. 
Service의 ClusterIP로 들어오는 트래픽을 해당 pod로 전달한다. </p>
</blockquote>
<p><strong>kube-proxy의 역할</strong></p>
<ul>
<li>각 node(서버)에 설치되어 있는 데몬(백그라운드 프로세스)</li>
<li>API Server로부터 다음 리소스를 감시(watch):<ul>
<li>Service 정보</li>
<li>Endpoints 정보 (어떤 Pod들이 연결되어 있는지)</li>
</ul>
</li>
<li>service가 제거되면 iptable이 사라져서 해당 clusterip로 접근할 수 없다. </li>
</ul>
<h2 id="service-discovery">Service Discovery</h2>
<p>service가 동적으로 생기고 사라질 때 이를 자동으로 찾고 연결해주는 시스템 자체를 의미한다.</p>
<blockquote>
<p>Pod나 Service의 IP/주소가 계속 바뀌어도
애플리케이션이 자동으로 상대 서비스의 위치를 찾아낼 수 있게 하는 메커니즘</p>
</blockquote>
<p>쿠버네티스에서의 service discovery 방법</p>
<h3 id="1-dns-기반-service-discovery-🔄-내부에서-내부로">1. DNS 기반 Service Discovery (🔄 내부에서 내부로)</h3>
<blockquote>
<p>AKS 안에서 Pod 간 통신이나 Service 간 통신을 할 때,
Service IP를 기억할 필요없이, Service 이름만으로 자동 연결된다.</p>
</blockquote>
<p><code>[서비스명][네임스페이스명].svc.cluster.loacal</code> 
고정된 DNS를 통해서 서비스의 이름 =&gt; ClusterIP로 자동 변환해준다. </p>
<h3 id="2-external-ip-지정-방식-🌐-외부에서-내부로">2. External IP 지정 방식 (🌐 외부에서 내부로)</h3>
<blockquote>
<p>외부 사용자, 인터넷 사용자가 쿠버네티스 내부 서비스에 접근할 수 있게 하기 위한 방법이다.</p>
</blockquote>
<p>회사 내부에 쿠버네티스가 있으면,
쿠버네티스는 외부 IP를 알아서 만들어주지 않기 때문에,
spec.externalIPs 항목을 직접 명시적으로 설정해야 한다.</p>
<p>그렇지 않은 경우는 클라우드환경에서는,
Service 의 타입을 loadbalancer 로 설정한다.
벤터 사에서 퍼플릭IP를 자동으로 생성해서 할당한다.</p>
<h2 id="servicetype">ServiceType</h2>
<p>쿠버네티스 service의 접근 범위</p>
<p>service를 생성할 때,
yaml파일에서 IP주소할당 방식과 서비스 연계에 따라서 4가지로 구분한다. 
| 유형             | 설명                  | 접근 범위       |
| -------------- | ------------------- | ----------- |
| <code>ClusterIP</code>    | 기본값. 내부 IP만 생성      | ❗ 클러스터 내부   |
| <code>NodePort</code>     | 외부에서 노드 IP + 포트로 접근 | ✅ 외부 접근 가능  |
| <code>LoadBalancer</code> | 클라우드에서 외부 IP 자동 할당  | ✅ 외부 접근 가능  |
| <code>ExternalName</code> | 클러스터 밖의 DNS 주소로 연결  | ✅ 외부 대상 연결용 |</p>
<h3 id="클러스터-내에서만-접근이-가능--clusterip">클러스터 내에서만 접근이 가능 : ClusterIP</h3>
<ul>
<li><p>ClusterIP는 내부에서만 접근이 가능하다. </p>
</li>
<li><p>Pod → Service 통신만 할 거면 ClusterIP만으로 충분하다.</p>
</li>
<li><p>외부의 인터넷 브라우저나 사용자에서는 절대 접근이 불가능하다.</p>
</li>
</ul>
<h3 id="클러스터-내와-외부에서-접근이-가능--nodeport-loadbalancer">클러스터 내와 외부에서 접근이 가능 : NodePort, LoadBalancer</h3>
<p><strong>NodePort</strong>
<code>[노드 IP]:[포트]</code></p>
<ul>
<li>NodePort는 각 노드의 IP에 지정된 포트로 접근한다. </li>
<li>일종의 비상용으로 실무에서는 테스트용으로 사용한다. </li>
</ul>
<p>Service의 일종으로 요청은 외부에서 <code>[노드 IP]:[포트]</code> 으로 들어오지만,
kube-proxy가 트래픽을 받아서 service의 clusterip -&gt; 연결된 pod들로 포워딩한다. </p>
<blockquote>
<p>외부 접근용 고정 포트를 열어주는 service이다. </p>
</blockquote>
<pre><code>사용자 브라우저
    ↓
[노드의 IP:NodePort 포트]      ← 외부에서 접근
    ↓
[Service: my-service]         ← type: NodePort
    ↓
[Pod A, Pod B, Pod C]         ← app=nginx 라벨 기준으로 선택됨
</code></pre><p>노드가 여러개 있어도 NodePort는 모든 Node에 동일한 포트를 열어둔다. </p>
<table>
<thead>
<tr>
<th>Node 이름</th>
<th>외부 IP</th>
<th>열린 포트 (NodePort)</th>
</tr>
</thead>
<tbody><tr>
<td>node-1</td>
<td><code>203.0.113.10</code></td>
<td><code>30080</code></td>
</tr>
<tr>
<td>node-2</td>
<td><code>203.0.113.11</code></td>
<td><code>30080</code></td>
</tr>
<tr>
<td>node-3</td>
<td><code>203.0.113.12</code></td>
<td><code>30080</code></td>
</tr>
</tbody></table>
<p><strong>LoadBalancer</strong></p>
<ul>
<li>LoadBalancer는 퍼블릭 IP가 자동 할당된다.</li>
<li>일반적으로 실무 외부 노출 방식이다.</li>
<li>LoadBalancer는 service의 타입이다.</li>
</ul>
<p>사용자는 이 퍼블릭 IP만 알면 됨
→ 노드가 몇 개인지, 어디에 있는지 몰라도 접근 가능!</p>
<ul>
<li>LoadBalancer는 AKS 내부에 있어서 노드들의 IP, 포트를 알고 있어서 연결이 가능하다.</li>
</ul>
<blockquote>
<p>LoadBalancer 타입은 실제로는 NodePort 위에 클라우드 로드밸런서를 얹은 구조이다.</p>
</blockquote>
<pre><code>[브라우저 사용자]
       ↓
[클라우드 Load Balancer (퍼블릭 IP)]  ← type: LoadBalancer
       ↓
[각 Node의 NodePort 포트 (예: 31234)] ← 자동 생성됨
       ↓
[kube-proxy]
       ↓
[ClusterIP Service]
       ↓
[Label로 선택된 Pod들] ← Pod가 어느 Node에 있어도 OK</code></pre><ul>
<li>nodeport와 clusterip 타입의 service는 쿠버네티스에 의해 자동생성</li>
<li>사용자가 해당 nodeport를 알기만 하면 강제로 LB을 안거치고 접속이 가능하긴 하다.</li>
</ul>
<h3 id="클러스터-밖의-리소스에-대한-map을-가짐--externalname">클러스터 밖의 리소스에 대한 map을 가짐 : ExternalName</h3>
<p>클러스터 외부에 존재하는 서비스 이름을 클러스터 내부 서비스처럼 사용이 가능한 타입이다.</p>
<h3 id="추가-service">[추가] Service</h3>
<p>특정 label을 기준으로 묶인 Pod 그룹의 짝꿍이 service라고 생각한다. </p>
<h3 id="네트워킹과-로드밸런싱">네트워킹과 로드밸런싱</h3>
<h3 id="스케일링과-배포-전략">스케일링과 배포 전략</h3>
<p>서비스라는 가상의 객체</p>
<p>실제로 동작하는 과정을 알아본다. </p>
<p>워커 노드들은 내부적으로 kube-proxy 라는 데몬을 실행한다. 
서비스나 엔드포인트 객체의 추가/삭제를 위해서 마스터 노드의 API 서버를 모니터링한다. </p>
<p>워커 노드의 kube-proxy는 </p>
<ul>
<li>새로운 서비스에 대한 IPtable 규칙,</li>
<li>서비스 ClusterIP의 트래픽을 캡쳐</li>
<li>해당 트래픽을 서비스의 백엔드 pod 중 하나로 라다이랙트한다. </li>
</ul>
