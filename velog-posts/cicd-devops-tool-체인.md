---
title: "[CI/CD] DevOps tool 체인"
date: "2025-06-24"
link: "https://velog.io/@ehekaanldk/CICD-DevOps-tool-%EC%B2%B4%EC%9D%B8"
series: "Uncategorized"
---

<h2 id="cicd">CI/CD</h2>
<p>CI/CD는 DevOps의 핵심 개념으로, <strong>지속적인 소프트웨어 개발 생명주기</strong>를 의미한다.</p>
<p>개발자가 코드를 지속적으로 배포할 수 있어야 하며, 이 요구를 충족시키기 위한 자동화된 절차가 CI/CD 파이프라인이다.</p>
<p>CI/CD 파이프라인은 새로운 소프트웨어 버전이 사용자에게 전달되기까지의 일련의 단계를 정의한다.</p>
<p>축구 경기CI는 전반전과 같고, CD는 후반전의 경기와 같다. </p>
<table>
<thead>
<tr>
<th>구분</th>
<th>설명</th>
<th>최종 단계</th>
</tr>
</thead>
<tbody><tr>
<td>CI (지속적 통합)</td>
<td>코드를 자동으로 빌드하고 테스트하여 컨테이너 이미지로 만드는 과정</td>
<td>이미지 저장소</td>
</tr>
<tr>
<td>CD (지속적 배포)</td>
<td>이미지 저장소의 이미지를 운영 클러스터에 자동 배포하는 과정</td>
<td>쿠버네티스</td>
</tr>
</tbody></table>
<h3 id="ci-continuous-integration-지속적인-통합">CI (Continuous Integration, 지속적인 통합)</h3>
<p>CI는 개발자가 작성한 코드를 통합하고 검증하는 단계이다.</p>
<ul>
<li>git 저장소에 코드를 push하면 자동으로 시작한다.</li>
<li>build, test, 정적 분석, 보안 검사를 수앻한다. </li>
<li>CI의 최종 산출물은 컨테이너 이미지이다. </li>
<li>이미지는 이미지 저장소(DockerHub, Amazon ECR 등)에 업로드 된다. </li>
</ul>
<blockquote>
<p>즉, CI는 코드 -&gt; 이미지 -&gt; 이미지 저장소 등록 까지를 자동화하는 과정이다. </p>
</blockquote>
<h3 id="cd-continuous-delivery--deployment-지속적인-배포">CD (Continuous Delivery / Deployment, 지속적인 배포)</h3>
<p>CD는 CI를 통해 생성된 이미지를 배포 환경까지 자동으로 전달하는 과정이다.</p>
<ul>
<li>일반적으로 운영 클러스터 (kubernetes) 등에 배포된다. </li>
<li>배포 대상은 preview 환경일 수 있고, 실서비스 환경일 수 있다. </li>
<li>kubectl apply, Helm, Argo CD 등의 도구를 통해 이미지가 쿠버네티스에 배포된다.</li>
</ul>
<blockquote>
<p>즉, CD는 이미지 저장소 -&gt; 대상 클러스터(kubernets)까지를 다룬다. </p>
</blockquote>
<h2 id="pipelines-settings">pipelines settings</h2>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/5e9451e2-c179-4c5d-a443-2f1c1c1070f4/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/912b5239-410b-41ab-8379-a9b7059457e6/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/21a59df5-a579-4a0f-b57c-916e7fd1dda0/image.png" /></p>
<p>해당 소스 레포를 포크한다. </p>
<p>deploy.yaml에 [ACR 이름].azurecr.io/product:latest 로 이미지를 변경해준다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/226c3b1d-2cbe-46c8-9a56-6ea53f9cd82e/image.png" /></p>
<h2 id="pipelines-ci">pipelines CI</h2>
<h3 id="step-1-ci-파이프라인-생성--템플릿-없이-제작">Step 1. CI 파이프라인 생성 : 템플릿 없이 제작</h3>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/29c6da3d-86c6-494b-a6f3-24a880dfc1e6/image.png" /></p>
<p>포크한 레포의 계정명/포크레포명 으로 넣어준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/cb872680-3074-4c4d-a53e-1ea72d9b6a73/image.png" /></p>
<p>empty job&gt; 미리 정의된 템플릿 없이 완전히 수동으로 CI 파이프라인을 구성할 수 있다.</p>
<h3 id="step-2-agent-선택">Step 2. Agent 선택</h3>
<p>파이프라인을 만드는데 대상 소스 코드를 전 단계에서 가져오고 세세한 task를 설정한다. 파이프라인을 설정하고 파이프라인을 구동할 OS를 선택한다. (azure에서의 agent는 VM과 같다.)
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/2390af5b-4a5d-4ee4-90bf-7972daf91ca5/image.png" /></p>
<h3 id="step-3-주요-task-추가--maven">Step 3. 주요 Task 추가 : Maven</h3>
<p>필요한 task를 추가해준다. 
fork한 프로젝트는 maven으로 구성되어서 패키징하고 도커파일로 빌드한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c6831318-e80f-4f5a-8f69-1a2a83ad0e20/image.png" /></p>
<p>maven에서의 package를 실행하겠다
mvn package는 아카이브.jar파일을 만든다. 
마이크로서비스의 모든 서비스가 jar파일로 압축된다. </p>
<p>jar를 도커라이징한다. 
이미지는 .jar파일로 만드는 것이 일반적이다. 
자바 기반의 이미지를 만들 때 jar를 만드는 이유는 dockerfile을 만들기 위함이다. 
jar인 이유는 자바에서 runnable jar 로 실행 가능한 파일로 만들어야지
컨테이너가 되고 req요청이 폭주하면 auto scaling 하는 과정처럼 애자일하게 빨리 하기 위해서이다. (순간 성능 확장을 위함이다.)</p>
<p>mvn spring-boot run 도 실행 가능하다. 
이는 maven을 거쳐서 실행하는 것이다. </p>
<p>maven을 거치지 않고, java -jar order.jar를 통해서 바로 실행할 수 있다. 
jdk만 가져도 가능하다는 말이다??</p>
<p>가장 빨리 컨테이너화하기 위해서 이다. </p>
<h3 id="step-4-주요-task-추가--docker">Step 4. 주요 Task 추가 : Docker</h3>
<p>docker의 이미지를 acr에 저장하도록 하기 위해서 acr를 정의한다. 
docker가 acr에 push할 때 로그인 성공이 표시되도록 체크해준다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/abd4e5c8-5991-4c24-b753-c768d618b119/image.png" /></p>
<p>container repo의 이름을 product로 설정해준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/91f639a4-7f6b-4510-a1d1-8dc58282463b/image.png" /></p>
<p>azure의 acr에서 각 마이크로서비스가  레포지토리 (마이크로서비스 이름) 를 가지고 안에 한번 더 배포하게 되면 v1, v2 와 같이 이미지가 태그로 이력이 남는다. 
ACR에 동일한 이름의 이미지가 다시 푸시되면, 태그를 달아서 버전 관리한다.</p>
<hr />
<h3 id="step-5-주요-task-추가--copy-files-to--publish-artifactdrop">Step 5. 주요 Task 추가 : copy files to &amp; publish artifact:drop</h3>
<p><strong>Kubernetes 배포를 위한 Manifest 파일 준비</strong></p>
<p>CD 단계에서는 manifast가 필요하다. yaml을 CI가 복사해서 토스해주기 위해서 
publish artifact:drop는 폴더 이름을 지정하는 기능이다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/5e4b9196-92b8-41f3-97bd-916f10c6d4f7/image.png" /></p>
<p>리눅스 agent가 소스코드를 내려받고, 소스폴더가 해당 위치 아래의 kubernetes 폴더 아래에 있는 yaml 파일2개를 복사하겠다 라고 설정해주는 부분이다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/efa026b3-f04c-4a16-a515-3b39b2ecd11b/image.png" /></p>
<pre><code>Source Folder : $(system.defaultworkingdirectory)
Contents : kubernetes/*
Target Folder : $(build.artifactstagingdirectory)</code></pre><p>파이프라인 메뉴&gt;product:ci&gt;edit 로 내부 작업 수정 가능하다.</p>
<h3 id="step-6-ci-트리거-설정">Step 6. CI 트리거 설정</h3>
<p>CI (Continuous Integration) Trigger, 즉 코드가 변경되었을 때 자동으로 파이프라인을 실행할지 여부를 설정하는 부분이다. 체크를 해제하면 파이프라인 실행을 수동으로 해줘야 한다. 
코드의 변화감지가 일어나면 파이프라인이 기동되겠다는 확인이다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/2832ce1d-f934-49db-97dc-28bfb96d9c97/image.png" /></p>
<p>소스코드가 변하면 기능 수정이 되고 파이프라인이 실행된다.</p>
<p>구지 파이프라인을 돌려야하는 리소스가 있고, 그렇지 아니한 리소스가 있다. 
코드 저장소에서 해당 부분이 바뀌면 파이프라인을 다시 돌리고, 다른 부분에서는 파이프라인을 돌릴 필요가 없다를 보여줄 수 있다.</p>
<p>arc에서 product가 만들어지고 태그가 만들어지면  CI는 잘 수행된 것이다. </p>
<h3 id="step-7-ci-run">Step 7. CI run</h3>
<p>run pipeline&gt; run 
billing환경을 설정하고 돌려라 라는 경고가 발생한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c1b9152f-1d85-43f6-8b3a-2c4646fa0930/image.png" /></p>
<p>organization settings &gt; billing &gt; set up billing &gt; save
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/9b7b765d-451a-4a01-8978-32c9a456e2a3/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/6f61c784-746f-4d2c-9fa3-9cc9ea9ca040/image.png" /></p>
<p>다시 run pipeline을 하면 작동한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/53d38320-f04c-46f0-999b-6ebd5da677d0/image.png" /></p>
<blockquote>
<p>run 실패시 
<a href="https://aka.ms/azpipelines-parallelism-request">https://aka.ms/azpipelines-parallelism-request</a> 에서 병렬처리 요청서 작성
private으로 설정한다. </p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/0c75e4e4-165f-4208-b069-32f979096022/image.png" /></p>
<h3 id="step-8-ci-확인">Step 8. CI 확인</h3>
<ul>
<li><p>arc에 생성한 이미지가 잘 생겼는지 확인한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/fb4085ed-005e-4f3e-a725-b320ee295e04/image.png" /></p>
</li>
<li><p>실행한 detail에서 <code>1 published; 1 consumed</code> 를 확인한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/585c1073-f636-4dd3-a9ba-05bb8fc47ce6/image.png" /></p>
</li>
</ul>
<h2 id="pipelines-cd">pipelines CD</h2>
<h3 id="step-1-cd-파이프라인release-생성">Step 1. CD 파이프라인(Release) 생성</h3>
<p>CD는 pipelines &gt; Releases 로 접근한다. </p>
<p><strong>Artifact 연결</strong>
이전 CI에서 생성된 아티팩트(drop/kubernetes/)를 연결한다.
CI를 승계해서 이동함으로 Artifacts를 눌러서 CI다음에 연결되도록 눌러준다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/aec276a4-80f7-4a01-ae1d-13188b19c15b/image.png" /></p>
<h3 id="step-2-release-이름-및-trigger-설정">Step 2. Release 이름 및 Trigger 설정</h3>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c6fae839-f7a9-425c-954a-3eb90d9fb262/image.png" /></p>
<p>CD의 트리거 이벤트를 설정한다. 
CI가 깃허브하고 트리거를 잡았듯이 CD는 CD와 releases 시켜야 한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d0586e64-942f-458f-a316-2b7a8e402ff3/image.png" /></p>
<h3 id="step-3-stage예-dev-생성-및-agent-설정">Step 3. Stage(예: Dev) 생성 및 Agent 설정</h3>
<p>오른쪽 부분의 CD 단계의 주요 task를 설정해준다. 
empty-job &gt; stage name : Dev 설정 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/2fc8f7e9-c0c8-4a17-88c8-8fd88513de51/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/5133184f-72d9-466d-8961-f93f66fae532/image.png" /></p>
<h3 id="step-4-주요-task-추가--kubernetes-연동-설정-kubectl">Step 4. 주요 task 추가 : Kubernetes 연동 설정 (kubectl)</h3>
<p>azure piplines과 ubuntu로 agent job의 설정을 해준다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/da5775ac-e2f0-4a96-bc22-6651c7f776e9/image.png" /></p>
<p>주요 task에 kubectl를 추가한다. Kubernetes service connection &gt; new
CI에서는 arc와 연결하여 이미지를 저장하도록 하였고,
CD에서는 aks의 target context 정보를 azure cluster를 넣어준다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a668f79b-0459-47f3-9387-db6840e58b76/image.png" /></p>
<h3 id="step-5-배포용-yaml-파일-처리">Step 5. 배포용 yaml 파일 처리</h3>
<p><strong>kubectl apply Task 추가 – deploy.yaml 적용</strong>
CI 단계에서 yaml들을 가져와서 kubectl 안에 넣어준다. 
command 에 apply 하면 kubectl apply 와 같은 작업이다. file path로 접근한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ddc8b86e-4247-4a59-a389-6d3e77d88d67/image.png" /></p>
<p>(aks는 최초 하나만 해주면 된다. 같은 deploy와 cluster의 target이 구지 다를 필요가 없음.)
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/db656480-60bc-4ff6-9b6e-c7dcda2ad60d/image.png" /></p>
<p><strong>kubectl apply Task 추가 – service.yaml 적용</strong></p>
<p>service.yaml을 받기 위해 kubectl 을 하나 더 add해서 기존의 Kubernetes service connection는 만들었던 aks를 선택해준다. 동일하게 path file로 추가한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c53132a4-0edb-4db9-813c-7a9ed5693f8d/image.png" /></p>
<p>** bash Task: deploy.yaml의 이미지 태그 수정**</p>
<p>bash script를 task에 추가한다. 
속성 창에서 inline에 script에 아래를 추가해준다.
kubectl 의 deploy를 추가해 얻은 경로 : <code>$(System.DefaultWorkingDirectory)/_Product-CI/drop/kubernetes/deploy.yaml</code> 를 아래 $ 이후에 붙여준다.</p>
<pre><code>sed -i &quot;s/latest/$(Build.BuildId)/g&quot; $(System.DefaultWorkingDirectory)/_Product-CI/drop/kubernetes/deploy.yaml</code></pre><p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/64beeaa4-0d2e-48a6-a406-6aa37504d78a/image.png" /></p>
<ul>
<li>sed는 리눅스 command이다. agent를 리눅스로 설정한 이유이다. </li>
<li>yaml에 대해서 <code>&quot;s/latest/$(Build.BuildId)/g&quot;</code> 는
해당 파일(yaml)에서 latest를 Build.BuildId 로 변경하도록 수정하는 명령이다. </li>
</ul>
<p>빌드 번호(Build.BuildId) 는 이미지 태그이고, 매번 진행할 때마다 태그가 달리되어서 해당 이미지로 배포가 되고 이미지가 올라간다.
빌드 번호가 매번 같으니까 해당 yaml을 kubectl 로 apply 배포하면 동일함 이름의 태그를 맞는 이미지로 치환해서 pool과 이름을 맞춰준다. </p>
<h3 id="step-6-실행-순서-정리">Step 6. 실행 순서 정리</h3>
<p>bash가 먼저 실행 이후에 kubectl apply 를 순서를 맞춰준다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/35351a62-c5d1-456a-ac5e-e4bbfdad8be3/image.png" /></p>
<h3 id="step-7-release-실행">Step 7. Release 실행</h3>
<p>save 이후에 releases 를 실행해준다. </p>
<p>create a release &gt; releases 를 그대로 눌러준다. 
Dev가 활성화 된다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a3f5a02e-00c7-4bd7-bd6c-a337b71887b6/image.png" /></p>
<p>agent job이 진행중이고, 
artifacts를 다운로드하고,
bash가 샐행되고,
deploy.yaml이 잘 실행되고, 
service.yaml도 잘 실행된다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/af0c1baf-f038-4497-a4bf-ff67972728b0/image.png" /></p>
<h3 id="step-8-결과-확인">Step 8. 결과 확인</h3>
<ul>
<li><p>CI와 CD가 잘 된 것을 확인할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/f6ffcdb4-14c3-4feb-a384-4b42f7c08883/image.png" /></p>
</li>
<li><p>codespace나 gitpod에서 aks에 잘 배포되었는지 확인이 가능하다. 
해당 과정은 파이프라인으로 배포한 결과이다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/54cc4148-ad71-43e7-b0e2-bd8dda6314c4/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/faf6cbd7-d84a-407f-9d86-e14f185cc733/image.png" /></p>
</li>
</ul>
<p>CD에 옮겨주기 위해서 yaml을 drop폴더에 복사해서 넘겨준다. 
CD가 이어받아서 DEV 단계에서 job이 중간에 같이 참조하는 
bash에서 arc와 deploy에서 동일한 이름의 이미지 빌드번호를 맞춰준다. </p>
<hr />
<h2 id="추가-디벨롭">추가 디벨롭</h2>
<h3 id="특정-디렉터리-변화에만-ci-작동시키기-trigger-범위-제한">특정 디렉터리 변화에만 CI 작동시키기 (Trigger 범위 제한)</h3>
<p>product 팀에서 코드 변화로 파이프라인이 변경될</p>
<ul>
<li>전체 코드 변경이 아닌, 특정 디렉터리(ex. src/)만 변경되었을 때만 파이프라인 작동시키기</li>
<li>예: README.md만 변경된 경우에는 파이프라인 작동 ❌</li>
</ul>
<p>src 아래 코드가 변경되면 배포하라고 파이프라인에게 특정 스코핑을 정해줄 때 </p>
<p>triggers 부분에서 include 의 src만 추가해주면 된다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/fb8e662d-2a86-4682-ad29-f2f77940b85c/image.png" /></p>
<h3 id="ci는-하나-cd는-여러-환경stage로-분기">CI는 하나, CD는 여러 환경(Stage)로 분기</h3>
<p>변화되는 환경마다 이미지로 하나씩 가져가고 동일한 이미지를 사용해서 배포를 나누어서 한다.</p>
<ul>
<li>CI 파이프라인은 단일로 구성 (이미지 빌드 및 publish까지 수행)</li>
<li>CD는 <strong>다양한 환경(dev, prod 등)</strong>으로 나뉜 멀티 스테이지 파이프라인 구성</li>
</ul>
<p>dev아래에 + 버튼으로 새로운 Stage(prod) 생성 후 dev 단계와 동일한 구조로 설정 </p>
<p>해당 이미지 빌드가 끝나면 개발환경에서 돌려보고 운영환경에서 돌려볼 수 있다. 운영환경prod 안에는 동일하게 내부 세팅을 해줘야 한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ab12ca3d-31c4-4f9e-a2bd-0294f402e0d1/image.png" /></p>
<h3 id="권한-제어">권한 제어</h3>
<p>Azure DevOps의 각 환경(Stage)에 대해 접근 권한을 설정할 수 있다. </p>
<ul>
<li>dev 환경은 누구나 접근 가능</li>
<li>prod는 관리자 승인 후만 접근 가능</li>
</ul>
<p>내부의 사용자에게 권한을 줄 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ba5f6748-c8a4-418f-afa0-da510a6e1c9f/image.png" /></p>
<hr />
<h2 id="삭제">삭제</h2>
<p>project를 삭제한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/373b4bb0-892c-40aa-864b-bcd71a0a719f/image.png" /></p>
<p>organization도 삭제한다.</p>
