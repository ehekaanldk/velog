---
title: "Day1_IT프로젝트 관리도구(GIT)"
date: "2025-03-26"
link: "https://velog.io/@ehekaanldk/Day1IT%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B4%80%EB%A6%AC%EB%8F%84%EA%B5%ACGIT"
series: "Uncategorized"
---

<h3 id="버전관리가-무엇인가">버전관리가 무엇인가?</h3>
<p>작업.txt =&gt; 파일을 복사해서 작업.최종.txt</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/5b875c88-d353-4217-8d9c-a2238d867564/image.png" /></p>
<ul>
<li>파일 내 작업이 충분히 기술되어 있지 않다.</li>
<li>작업을 하다가 옛날 것으로 돌려야 하는 경우가 발생한다. </li>
</ul>
<p>버전을 안전하게 관리하기 위해서 백업을 한다. </p>
<p>버전관리를 사용하는 이유는 무엇일까? =&gt; 디버깅
버그를 잡는 것이 디버깅이다. </p>
<p>과거에는 버전관리가 유료화가 되면서 '리눅스 토발츠'라는 인물이 개발한 버전관리 시스템이 바로 Git이다. </p>
<p>모든 코드를 전수조사하기 VS 버전관리
버그가 발생하면 이전 버전으로 돌리면서 버그가 발생하지 않았던 과거의 버전을 찾아 바로 이후의 버전에서 버그를 찾아낸다. </p>
<p>극단적인 상상력!</p>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b349f4c3-939f-4544-89ab-9db3bdeff450/image.png" />
바탕화면에 폴더를 생성한다. 
해당 폴더로 vs code를 연다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/adedbb09-07ef-4fcd-9f12-f5c011121358/image.png" />
폴더 내에서 work1.txt 파일을 생성한다. </p>
<p>단위작업은 하나의 작업만 저장하는 것이 좋다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b3855f15-3ac1-4d79-ac54-6cf1b21aa237/image.png" />
현재 디렉토리를 git으로 버전관리하겠다는 의미이다. 버전관리를 프로젝트마다 하는 것으로 initialize respository이다. initialize respository는 vs code 내의 기능이 아닌 git의 기능이다. </p>
<p>ctrl+, 로 설정창을 키면 </p>
<p>누군가에게 프로젝트를 보낼 때는 프로젝트 자체를 압축해서 보내면 된다. 
모든 버전은 .git안에 저장된다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/dbb51f34-96e9-4002-be89-7c6d7a4bff0e/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/5772cc93-ab24-498f-a6dc-4c0f2879428e/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/9a9ea1d2-e689-47c5-aa92-a2bd4e06104e/image.png" />
각각의 버전은 이름 등의 정보가 담겨있는데 해당 설정을 하지 않은 경우에 나타나는 오류이다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a58c6fad-cc0a-4701-a22f-9b0c4701a5d3/image.png" />
해당 도움 로그를 보고 따라하면된다. 해당 코드는 terminial에서만 실행이 가능하다. 새터미널 창을 열어서 powershell로 나오는 것을 확인한다. powershell를 bash로 바꾸어야 한다. 아래는 따라한다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/61bdde29-145d-4f14-9dcc-49512be0ab04/image.png" />
select default profile &gt; git bash &gt; +버튼 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/0ad1671d-9cc3-4903-a96a-bc61ef605f2f/image.png" /></p>
<hr />
<pre><code>git config --global user.name &quot;Your Name&quot;
git config --global user.email &quot;you@example.com&quot;</code></pre><p>터미널에 respository의 정보를 설정해준다. git 사용자 설정은 최초의 1회만 수행하면 된다. 이후 commit을 통해서 버전을 만들면 된다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/e0bae50f-c5fe-4f35-a64f-62c01251078b/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/34d8ca74-2716-4ef5-803d-db26d2af7bf2/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a69d0705-003b-4e40-8d8a-901cbdeeb0fb/image.png" />
다음 git graph를 설치하고 우측 하단에 git graph를 클릭하여 확인할 수 있다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/8b4adf0c-1dc4-4bf6-ab5d-2801888dc922/image.png" /></p>
<p>하나의 버전이 여러개의 파일로 이루졌을 수도 있고, 커밋을 잊어버리고 여러 작업을 수행하였을 때는 파일을 쪼개서 버전을 만들어야 한다. </p>
<p>work1.txt에 2라고 적고 work2.txt
2번째 단위작업은 2개의 work1과 work2.txt 파일을 수정하는 것이다. 
3번째 단위작업은 work3.txt파일을 생성 후 작성
3번째 단위작업을 커밋하기 전에 2번째 단위작업을 잊어서 커밋하지 않음</p>
<p><strong>add는 커밋 대기 상태를 말한다.</strong>
<strong>커밋 대기 상태를 stage area라고 부른다.</strong></p>
<p>staged area에 담는 것을 장바구니라고 생각하고 담은 장바구니를 commit하면 된다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/6338fdb8-089d-40fc-acf0-0d8fbf343983/image.png" /><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/5ed40b1d-fa2e-4dba-a065-bbe92f68f728/image.png" />
새 버전으로 만들고 싶은 때는 add를 누르고 staged area로 옮기고 commit를 누른다. </p>
<blockquote>
<p><strong>커밋이란?</strong>
Git이 저장하는 한 시점의 스냅샷
수정한 파일들을 모아서 “지금 이 상태를 저장하자!” 할 때 커밋을 한다. 커밋마다 고유한 ID(해시값)가 있어서, 과거로 돌아가거나 변경사항을 추적할 수 있다.</p>
</blockquote>
<blockquote>
<p><strong>버전이란?</strong>
Git에서는 특정 시점의 코드 상태를 의미
커밋마다 하나의 버전이라고 보면 된다. Git에서는 파일을 전체 복사해서 저장하는 게 아니라, 변경된 부분만 저장하면서도 각 커밋을 고유하게 식별할 수 있는 버전 ID (해시값) 를 부여한다.</p>
</blockquote>
<hr />
<p>git의 원리에 대해서 알아본다.
수동으로 이해한 것을 자동화하였을 때 이해한다.... (개공감)</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/43a53a23-76b0-4f8a-80d7-1c983e45b539/image.png" /></p>
<p>하나의 텍스트로 만들고 텍스트를 해시값으로 만든다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/48dcbbd3-6564-4382-bfb6-203eb2e50a96/image.png" />
해시값은 40글자의 고유한 값으로 생성된다. SHA256 
이것이 commit의 ID가 된다. </p>
<p><strong>git은 내용을 기반으로 commit ID가 생성된다.</strong>
git과 비트코인은 유사한 방식?</p>
<p>git은 commit ID를 어딘가에 적어두고 가장 마지막에 한 것을 알려준다. </p>
<p><strong>main은 마지막 버전을 가리킨다</strong></p>
<p>head가 주인공이고 main가 조연이다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d8a01522-8dbd-4070-8a42-e2772d735f70/image.png" /></p>
<p>v2)
stage area에는 전체가 모두 들어있다. 시각적으로는 현재 넣은 것들만 보여주는 것이다. 본질적으로는 모두 들어있다.!..!
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/0cb0ffca-0ccd-4995-a033-911b6b564f77/image.png" />
현재 만든 버전의 부모 버전을 git은 main에 적혀있는 값을 현재 만든 버전의 parent로 기록한다. 수행한 내용으로 해시값을 생성해 commit ID 만들고 last commit을 나타내는 main에 기록된다. </p>
<p><strong>새로 만들어진 버전의 부모는 HEAD다.</strong></p>
<p>디버깅
working dir의 내용을 과거로 본다. 
현재로 돌아올 수 있다. </p>
<p><strong>HEAD는 현재 시간이다. main은 마지막 시간이다.</strong> </p>
<p>v1과 v2가 있을 때, working dir이 v1의 시점으로 돌아간다. 
git graph에서 돌아가고 싶은 버전을 누르고 checkout을 눌러준다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/8beebb77-c9aa-4f72-bcae-247eab0cd2ca/image.png" /></p>
<p>main을 더블클릭하면 v2의 시점으로 돌아올 수 있다. (checkout Branch와 같다.) 파란색 동그라미가 head이다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a6bb252b-9e8f-48f3-aa3d-4de4c55ed87f/image.png" /></p>
<p><strong>checkout은 head를 바꾼다.</strong></p>
<p>git checkout main
git checkout C</p>
<hr />
<p>4교시)</p>
<h4 id="head를-독자적으로-옮기는-법실험적인-작업">head를 독자적으로 옮기는 법(실험적인 작업)</h4>
<p>head-&gt; mian-&gt; v2이고
v2 checkout 하면 head-&gt; v2
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/60cea3fa-22d5-48d9-a884-cf92118a9400/image.png" /></p>
<p>exp commit하면
head-&gt; exp
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/06e9ec39-2d39-4913-9863-e64d0fecb36d/image.png" /></p>
<p>v2 checkout 하면 exp를 완벽하게 버릴 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a53926bb-4a10-4ff6-bb2c-2ca13a48e40d/image.png" /></p>
<pre><code># 터미널에서 아래 검색으로 한 과정을 확인할 수 있다. 
git relfog</code></pre><h4 id="실험적인-작업으로-되돌리기">실험적인 작업으로 되돌리기</h4>
<p>실험적인 작업에서 main으로 돌아올 때는 
실험적인 작업exp에 이름을 붙인다. 이렇게 붙인 이름을 <strong>branch</strong>라고 한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/f1e92461-b777-4de9-9737-5d30aa4929ae/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/08347ac7-97cf-498e-a577-f8835d6134f3/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ad8ef2e0-ae1b-4c53-a40d-18a15c01206f/image.png" />
새로운 파일 main.txt를 생성해 commit한다. </p>
<p><strong>reset은 main을 바꾼다.</strong>
<strong>reset은 head가 가르키는 branch를 바꾼다.</strong></p>
<hr />
<h4 id="merge">merge</h4>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d556241f-0c30-4e6f-9e33-b489085f816e/image.png" />
성공적인 작업을 한 후에는 exp 실험적인 작업을 main에 합쳐야 한다. 
main이 exp를 합침 -&gt; main을 더블클릭으로 checkout 후 exp에서 우클릭으로 merge 한다. (main이 움직임, exp1과 main1이 모두 부모임)
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/2573cdb5-a089-47ce-bd86-c179c3b03b3b/image.png" /></p>
<p>exp가 main을 합침 -&gt; exp를 더블클릭으로 checkout 후 exp에서 우클릭으로 merge한다. 결과적으로는 동일하고 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/88d36adc-3dab-41ca-a604-f8b22e19caf7/image.png" /></p>
<h3 id="서로다른-branch가-같은-파일의-같은-행을-다르게-수정한-경우">서로다른 branch가 같은 파일의 같은 행을 다르게 수정한 경우</h3>
<p>start (1,2,3,4)
start에서 exp brach생성
main에 테두리 상태에서 (1,m2,3,4)
m2 commit
exp brach checkout
exp에 테두리 상태에서 (1,2,e3,4)
e3 commit
exp에 테두리 상태에서 (1,2,e3,e4)
e4 commit
main 더블클릭 checkout
main에 테두리 상태에서 (1,m2,3,m4)
m4 commit</p>
<p>main에 테두리 상태에서 exp branch에 우클릭으로 merge
conflict</p>
<p>두 branch의 공통의 조상을 찾는다. 공통의 조상을 <strong>base</strong>라고 한다. 
base로 부터 어떻게 수정되었는지를 보고 자동으로 병합한다. 
자동 병합 후에 발생하는 <strong>충돌</strong>은 사람이 고쳐야 한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c1c6bc55-8f8b-4a6e-8890-31e72d26607e/image.png" /></p>
<p>conflict가 발생한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c839b2fe-06c9-4eef-8a53-d48774d8cb6a/image.png" /></p>
<p>merge는 brach와 branch 사이의 병합이 아닌, commit과 commit 사이의 병합이 맞다. </p>
<p>resolve in merge editor를 눌러서 어떻게 처리할지 물어본다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c3e5af53-b526-4c1d-a086-8c50d04300bb/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/61360ddf-ffb2-4be5-8501-7b8a62a71214/image.png" /> result의 수정 후 반영한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/bc574fba-ab96-434c-9951-7e7a63878337/image.png" /> 해당 파일이 staged changes에 올라가고 continue로 완료한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/a1aa5b3c-0628-42eb-a898-51a69c48e452/image.png" /></p>
<h3 id="협업">협업</h3>
<h4 id="1-로컬저장소를-먼저-만들고-원격저장소-연결하기">1. 로컬저장소를 먼저 만들고 원격저장소 연결하기</h4>
<p>서버를 구축한다. github</p>
<p>github에서 new repository 생성한다.
readme file 생성하지 말기!
내 컴퓨터의 저장된 저장소와 같이 github상에서 저장소를 만든 것이다. </p>
<p>내 컴퓨터의 저장된 저장소와 github.com의 저장소를 연결하준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/305fdddb-b507-4518-ab4f-1769f9467dcf/image.png" /></p>
<p>github.com의 주소를 add remote에 넣어준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d29fee60-5ef9-4f79-bfe4-16d1582bb9d8/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/15357be0-09ea-4089-9a87-f81789cc6c0f/image.png" /></p>
<p>remote name에 origin을 넣어서 연결하면 github인증이 뜬다.</p>
<p>push를 해서 main에 origin이 붙으면 성공이다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/88115e86-e022-422e-a4f4-6f0665de4644/image.png" /></p>
<p>와방 어렵따 진짜 머리 터져./......</p>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/378da05d-6703-4a4c-9dfd-7b71ef38d3ed/image.png" /></p>
<p>v5는 아직 내 컴퓨터에만 있고 원격저장소에는 올라가지 않았다. 
git commit --amend -m &quot;vv5&quot;로 커밋 메시지를 바꿀 수 있다. 이는 내 컴퓨터에만 있기 때문에 수정이 가능하고 공유된 상태에서 바꾸면 시말서 각임(주의)
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/63e5013a-a81d-4e89-ae73-86d5e2e59334/image.png" /></p>
<p>3세대 중앙집중버전관리 시스템commit이 곧 push
4세대 인터넷과 버전이 따로 가능</p>
<p>push하면 안정적으로 백업이 완료된다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/9b26f283-b53b-479b-b0e5-ab109ede49b6/image.png" /></p>
<p>지금까지는 로컬 저장소를 먼저 만들고 원격저장소를 만들었지만, 원격저장소부터 먼저 만들고 해도 상관없음</p>
<h4 id="2-원격저장소-만들고-복제해서-로컬에-저장해보기">2. 원격저장소 만들고 복제해서 로컬에 저장해보기</h4>
<p>이제는 원격저장소를 먼저 만들어서 복제한 후에 로컬에 저장한다. 
clone repository에 만든 원격저장소의 주소를 적어준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/cb58f87e-5eaf-4996-b1bf-460c060ab90b/image.png" /></p>
<p>저장될 위치를 정하고 폴더를 만들어주면 복제가 된다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/e6841b29-9df3-4bb1-b9ce-4b5e0b9b2374/image.png" /></p>
<h4 id="3-뭐ㅇ요">3. 뭐ㅇ요?</h4>
<p>left.txt 파일 content 1로 L1으로 commit
new window를 열어서 같은 링크를 붙여준다.</p>
<p>같은 원격저장소를 복제하여 2개의 로컬저장소에 각각 저장한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/77d41035-5298-4909-85a4-d792434ba1cd/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d91feb97-8644-4578-b286-b0231038622c/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ac1f5a53-bf5a-41a2-8f76-d405ff497caf/image.png" /></p>
<p>L1에서 push하고난 후에 R2를 push하면 실패한다.
이유는 두 branch가 main이고 원격저장소도 main이다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/adcc41df-e565-4bb9-946c-a2bff6b657b6/image.png" /></p>
<p>왼쪽이 c1를 생성하고 오른쪽은 C2를 생성했다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/49ba0b36-68a8-48cd-b5f2-a5563ab9fc10/image.png" /></p>
<p>왼쪽이 push를 하면 C1이 올라가고, C1의 부모는 B가 된다. 왼쪽의 origin/main이 C1을 가르킨다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/cbfd24e9-719a-4dc2-8722-4871a9bf9402/image.png" /></p>
<p>오른쪽이 push하면 C2가 올라가지만 반려된다. 반려되지 않으려면 원격저장소의 내용을 pull한다.
pull = fetch+merge
fetch는 원격저장소의 내용을 가져온다.
merge는 원격저장소에서 가져온 부분을 합친다.</p>
<p>fetch로 원격저장소의 내용을 가져온다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/1e7571b7-201f-4028-8eb7-43910311878f/image.png" /></p>
<p>merge는 원격저장소에서 가져온 부분을 합친다.
(origin/main과 main은 비슷할 뿐 완전히 다른 것이다. )
두 내용을 합쳐서 D를 만들고 main이 D을 가르킨다. 원격저장소에 올라가지 않은 c2와 D는 마음대로 조작이 가능하다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d9aa97a9-ced7-4d0d-8f4d-3a47c699fe12/image.png" /></p>
<p>오른쪽을 push하면 C2와 D가 올라가서 병합이 된다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/278723bc-a006-417b-8f85-135432038969/image.png" /></p>
<p>R2에서 pull
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/04d46a6b-75b8-4ded-b6ba-7e1838f42fd8/image.png" /></p>
<p>다시 R2를 push
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/3db947ce-c048-4762-938a-1a94f3870cc6/image.png" /></p>
<p>L1에서 pull
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/6404f292-7144-4a7b-adc1-44aacf74ef98/image.png" /></p>
<p>왼쪽에서 common.txt생성 후 push
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/8bf92404-e070-4a20-84ae-cc0377c694cd/image.png" /></p>
<p>오른쪽에서 pull
오른쪽에서 L2 add commit, L4 add commit</p>
<h3 id="복습-git78">복습 git7,8</h3>
<ol>
<li>github 저장소 만들기</li>
<li>저장소 복제하기(git7)</li>
<li>common.txt를 만들고 커밋</li>
<li>push</li>
<li>저장소 복제하기2(git8)</li>
<li>왼쪽(저장소1) =&gt; L2 커밋, L4 커밋</li>
<li>오른쪽(저장소2) =&gt; R3 커밋, R4 커밋</li>
<li>저장소1 push</li>
<li>저장소2 push =&gt; rejected 확인</li>
<li>저장소2 pull =&gt; conflict 수정 후 continue =&gt; merge commit 확인</li>
<li>저장소2 push</li>
<li>저장소1 pull
작업준비 완료!</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/1e7411ea-56de-45f2-a21f-dc94a67bca13/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b2b88644-ba8c-4fdf-9633-626edf30cdc1/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/57103713-159e-43bf-a537-d5786b2a8201/image.png" /></p>
<p>fetch는 원적 저장소에서 최신 상태를 로컬 저장소로 가져온다. 이는 충돌이 발생하지 않고, merge하는 과정에서 충돌이 일어나는 것이다. 기본적으로 fetch는 충돌이 일어나지 않는다. </p>
<p>충돌이 발생하는 순간들은 git merge, git pull이 있다.</p>
