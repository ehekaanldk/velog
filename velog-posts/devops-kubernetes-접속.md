---
title: "[DevOps] Kubernetes 접속"
date: "2025-06-17"
link: "https://velog.io/@ehekaanldk/DevOps-Kubernetes-%EC%A0%91%EC%86%8D"
series: "Uncategorized"
---

<h2 id="azure-cli-tasks">Azure CLI Tasks</h2>
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
<h2 id="git">git</h2>
<p>git add .
git commit -m &quot;설명하기&quot;
git push origin main</p>
