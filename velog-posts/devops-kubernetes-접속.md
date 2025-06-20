---
title: "[DevOps] Kubernetes 접속"
date: "2025-06-17"
link: "https://velog.io/@ehekaanldk/DevOps-Kubernetes-%EC%A0%91%EC%86%8D"
series: "Uncategorized"
---

<h2 id="azure-cli-tasks">Azure CLI Tasks</h2>
<blockquote>
<p>Azure에 로그인 후 리소스 그룹과 AKS 연결하기</p>
</blockquote>
<p>curl -sL <a href="https://aka.ms/InstallAzureCLIDeb">https://aka.ms/InstallAzureCLIDeb</a> | sudo bash </p>
<h3 id="azure-client-sso-설정">Azure Client SSO 설정</h3>
<p>az login --use-device-code
(az 로그인처리)</p>
<p>=&gt; To sign in, use a web browser to open the page <a href="https://microsoft.com/devicelogin">https://microsoft.com/devicelogin</a> and enter the code RQ92TVHGC to authenticate.
링크 누르고 코드 입력란에 코드 넣기</p>
<h3 id="kubernetes-client-설정">Kubernetes Client 설정</h3>
<p>az aks get-credentials --resource-group [RESOURCE-GROUP-NAME] --name [Cluster-NAME]</p>
<p>kubectl get all</p>
<p>kubectl get node</p>
<h2 id="클러스터-안에-kafka-설치">클러스터 안에 kafka 설치</h2>
<p>AKS 클러스터 안에 필요한 구성 요소를 배포하는 과정이다.</p>
<blockquote>
<p>Helm 
: Kubernetes용 <strong>패키지 매니저(apt/yum처럼)</strong>입니다.</p>
</blockquote>
<ul>
<li><p>Helm을 사용하면 복잡한 리소스 정의 없이 하나의 명령어로 Kafka 같은 오픈소스를 쉽게 설치</p>
</li>
<li><p>Helm(패키지 인스톨러) 설치 (1회만 수행)
curl <a href="https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3">https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3</a> &gt; get_helm.sh</p>
</li>
</ul>
<p>chmod 700 get_helm.sh</p>
<p>./get_helm.sh</p>
<ul>
<li>helm으로 Kafka 설치
helm repo add bitnami <a href="https://charts.bitnami.com/bitnami">https://charts.bitnami.com/bitnami</a></li>
</ul>
<p>helm repo update</p>
<p>helm install my-kafka bitnami/kafka --version 23.0.5</p>
<h2 id="app서비스를-클러스터에-올리고-실행하기">App서비스를 클러스터에 올리고 실행하기</h2>
<blockquote>
<p>AKS는 쿠버네티스 클러스터</p>
</blockquote>
<ul>
<li>APP을 올리기 위해서는 도커 이미지를 기반으로 Pod를 실행한다. </li>
<li>Deployment 는 Pod를 자동 생성한다.</li>
<li>Service 는 Pod에 접근할 수 있는 가상 객체로 노출한다.<ul>
<li>내부 통신: ClusterIP</li>
<li>외부 노출: LoadBalancer, NodePort</li>
</ul>
</li>
</ul>
<p>order, delivery, product, gateway 각각 수행
/order/kubernetes/deployment.yaml 에 배포한 이미지 적용
image : [도커허브아이디]/order:20250617 (이미지명:태그)</p>
<p>cd order
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml</p>
<p>frontend/kubernetes/deployment.yaml 에서 동일하게 배포한 이미지 적용하고, containerPort 아래부분은 삭제해준다. </p>
<ul>
<li>확인
kubectl get all</li>
<li>부가정보 포함 조회
kubectl get pod -o wide
조회되는 IP는 Pod에 자동으로 할당된 Cluster 내부 IP 주소이다. </li>
</ul>
<p>kubectl apply -f deploy.yaml
kubectl get pod -w</p>
<h2 id="git">git</h2>
<p>git add .
git commit -m &quot;설명하기&quot;
git push origin main</p>
