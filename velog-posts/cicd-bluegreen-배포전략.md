---
title: "[CI/CD] blue/green 배포전략"
date: "2025-06-24"
link: "https://velog.io/@ehekaanldk/CICD-8961m8z5"
series: "Uncategorized"
---

<p>gitpod에 </p>
<p>kubectl 이 관리되는 </p>
<p>vi /home/codespace/.kube/config</p>
<p>context </p>
<p>config 파일</p>
<p>aks </p>
<p>kubectl config get-contexts</p>
<p>빅프에서는 msa할때 mesh 써야함</p>
<h3 id="istio-설치-과정">istio 설치 과정</h3>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/85aed3d6-d50a-44d0-ab99-4f23a80a52f4/image.png" /></p>
<p>예거는 추적하는 tracing이였는데 
demo 프로파일을 기반으로 Istio를 설치부분 아래로 업데이트 됨</p>
<pre><code>istioctl install --set profile=demo --set hub=gcr.io/istio-release \
  --set values.pilot.traceSampling=100.0 \
  --set meshConfig.extensionProviders[0].name=jaeger \
  --set meshConfig.extensionProviders[0].zipkin.service=jaeger-collector.istio-system.svc.cluster.local \
  --set meshConfig.extensionProviders[0].zipkin.port=9411 \
  --set meshConfig.defaultProviders.tracing[0]=jaeger</code></pre><h3 id="rollout--canary--bluegreen">rollout &amp; canary &amp; blue/green</h3>
<p>CRD 는 기본 get all에 포함되어서 보여지지 않는다. 
동일하게 ingress, rollout은 보이지 않는다. </p>
<ul>
<li>rollout 객체 삭제
kubectl delete rollout --all -n default</li>
</ul>
<p>rollout은 추가로 설치해서 기본 deploy와 동일하고 strategy에 배포를 위한 전략을 추가한다.</p>
<p><strong>blue/green</strong>
두 개의 환경(서비스 버전)을 유지하면서, 새로운 버전을 안전하게 배포하고 전환하는 전략이다.</p>
<ul>
<li>service/nginx-active → blue 버전의 Pod들을 바라봄 (유저가 사용하는 서비스)</li>
<li>service/nginx-preview → green 버전의 Pod들을 바라봄 (QA 테스트용)
둘 다 동시에 존재하지만, 실제 유저 트래픽은 active만 사용</li>
</ul>
<p>서비스가 만들어져야 pod가 만들어진다. </p>
<table>
<thead>
<tr>
<th>구분</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Blue</strong></td>
<td>현재 운영 중인 <strong>Stable 버전</strong> (유저들이 사용 중)</td>
</tr>
<tr>
<td><strong>Green</strong></td>
<td>새로 배포한 <strong>Preview 버전</strong> (QA 팀이 테스트)</td>
</tr>
<tr>
<td><strong>Service 객체</strong></td>
<td>유저 트래픽을 어느 Pod로 보낼지 결정 (Pod들을 selector로 관리)</td>
</tr>
</tbody></table>
<p>현재 배포된 이미지의 서비스로, 신규 배포된 서비스가 따로 있다. 
쿠버네티스의 서비스가 2가지가 되고, 일반 유저들이 사용하는 서비스가 현재 배포된 서비스가 된다. 신규 배포된 버전은 preview 에서 관리가 된다. Q/A 팀에서 문제가 없다고 판단되면 현재 배포된 서비스가 신규 배포된 서비스의 pod를 바라보게 된다.</p>
<p><strong>bluegreen.yaml</strong></p>
<pre><code>apiVersion: argoproj.io/v1alpha1
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
      previewReplicaCount: 2

---

# 액티브 서비스 (사용자 트래픽이 전달되는 곳)
apiVersion: v1
kind: Service
metadata:
  name: nginx-active
spec:
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
  type: &quot;LoadBalancer&quot;    

---

# 프리뷰 서비스 (새 버전만 연결됨)
apiVersion: v1
kind: Service
metadata:
  name: nginx-preview
spec:
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
  type: &quot;LoadBalancer&quot;        </code></pre><ul>
<li><p>배포된 2개의 서비스를 확인한다.
service/nginx-active    LoadBalancer   10.0.118.205   20.214.116.23   80:31408/TCP   96s
service/nginx-preview   LoadBalancer   10.0.116.148   20.214.97.209   80:30934/TCP   95s</p>
</li>
<li><p>rollout 배포
kubectl apply -f bluegreen.yaml</p>
</li>
<li><p>rollout 객체 조회
kubectl get rollout (metadata 에 </p>
</li>
<li><p>yaml의 rollout의 이미지를 신규버전의 이미지로 변경
kubectl argo rollouts set image example-rollout nginx=jinyoung/app:blue</p>
</li>
</ul>
<blockquote>
<p>argo 설치 방법
Argo rollout Plug-in을 설치</p>
</blockquote>
<ul>
<li><p>kubectl create ns argo-rollouts</p>
</li>
<li><p>kubectl apply -n argo-rollouts -f <a href="https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml">https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml</a>
argo CLI kubectl Plugin 설치</p>
</li>
<li><p>curl -LO <a href="https://github.com/argoproj/argo-rollouts/releases/latest/download/kubectl-argo-rollouts-linux-amd64">https://github.com/argoproj/argo-rollouts/releases/latest/download/kubectl-argo-rollouts-linux-amd64</a></p>
</li>
<li><p>chmod +x ./kubectl-argo-rollouts-linux-amd64</p>
</li>
<li><p>sudo mv ./kubectl-argo-rollouts-linux-amd64 /usr/local/bin/kubectl-argo-rollouts</p>
</li>
<li><p>QA 팀이 green에 대해 테스트 수행하고, 오류 없으면 새버전 승인
kubectl argo rollouts promote example-rollout</p>
</li>
</ul>
<ul>
<li>pod와 service 삭제</li>
<li>rollout 삭제
kubectl delete rollout,svc --all -n default</li>
</ul>
