---
title: "[Cloud] 클라우드 인프라 가상화"
date: "2025-05-14"
link: "https://velog.io/@ehekaanldk/Cloud-%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EC%9D%B8%ED%94%84%EB%9D%BC-%EA%B0%80%EC%83%81%ED%99%94"
series: "Uncategorized"
---

<h2 id="가상화">가상화</h2>
<p>물리적인 IT자원을 논리적으로 분리하여, 여러 자원인 것처럼 사용할 수 있게 해주는 기술
PC(물리적인 자원)를 4개의 PC(논리적)으로 분리하여 사용할 수 있게 한다. </p>
<h4 id="특징"><strong>특징</strong></h4>
<ul>
<li>자원의 효율적인 활용 
: PC의 리소스(cpu, memory, storage, network =&gt; 사용측정 가능)를 나누어서 가상의 PC에게 나누어서 사용</li>
<li>격리성 보장
: 나눈 가상의 PC들이 독립적으로 실행</li>
<li>유연한 확장성
: 서버를 물리적으로 추가하지 않아도, 추가 , 삭제 가능, 유연하게 확장하고 필요시 줄일 수 있다.</li>
<li>중앙 집중화 관리 및 자동화
: 중앙의 물리적인 머신에서 모든 가상머신을 관리</li>
<li>플랫폼과 운영체제의 독립성
: 가상머신에 OS와 플랫폼을 독립적으로 설치 가능</li>
<li>비용 절감, 유지 보수 효율성 증가
: 서버의 대수가 필요할 경우나 기업에서의 온프레미스 형태로 관리하고, 가상화</li>
<li>클라우드와 컨테이너와의 높은 연계성
: 가상화 관리를 위한 개념인 컨터이네, 클라우드 회사도 인프라 자원을 가상화 처리를 해야 한다.</li>
</ul>
<p>문제점을 해결하는 방법이 가상화이다.
모든 IT 자산을 가상화한다. 
가상화 플랫폼으로 동적이고 유연한 업무 인프라를 구축한다. 
데이터 센서의 모든 리소스를 가상화 한다. </p>
<h4 id="컴퓨팅-환경-발전사">컴퓨팅 환경 발전사</h4>
<p>서버 : 서비스를 해주는 하드웨어, 소프트웨어, 머신, 사람 (테이블 담당 서버)</p>
<ul>
<li>베어메탈 : 물리적인 서버 위에서 직집 애플리케이션(주문, 메뉴, 배송)을 실행하는 방식</li>
<li>가상머신 : 하나의 서버에서 여러 개의 가상 서버들에 </li>
<li>컨테이너 : 가상머신보다 가벼워서 애플리케이션을 더 많이 담기 가능</li>
<li>서버리스 : 서버가 없진 않고, 직접 관리하지 않고 특정 이벤트(사용자 폭등) 발생 시 필요 코드(VM 증설)만 실행
코드 저장 코드와 코드 실행 코드가 필요했지만, 서버에서 관리하지 않고 리소스만 빌려서 사용하고 반납한다. 
베어메탈과 가상머신, 컨테이너는 pyshical machine이 필요하고 이를 통해 관리한다. </li>
</ul>
<h4 id="하이퍼바이저">하이퍼바이저</h4>
<blockquote>
<p>자원 관리자 + 가상 머신 실행기
여러 개의 가상머신을 실행할 수 있게 해주는 가상화 소프트웨어</p>
</blockquote>
<p>하이퍼바이저의 종류</p>
<ul>
<li><p>type 1 : Bare-metal
물리서버는 반드시 있어야 한다. 물리서버 위에 가상머신이 올라가는 것이다. 
시스템을 운영하기 위해서는 OS가 필요하다. 
OS 대신에 소프트웨어인 하이퍼바이저도 자원을 운영해주는 역할이다. 
하이퍼바이저도 OS이고 기존의 OS와는 달리 스페셜한 OS로 
하드웨어 위에 OS를 설치하고, 그 위에 사용자로써의 애플리케이션을 설치, 서비스를 해주기 위한 서버로써의 역할을 하는 애플리케이션
하나의 하드웨어에서 하나의 애플리케이션, 서버로 사용하는 것이 일반적이다. 
하이퍼바이저로 기존의 리소스를 가상머신으로 리소스를 나눈다. 
기존에 있는 하드웨어 서버도 운영이 되어야 하기에 최소 메모리나 cpu등의 리소스가 남아있어야 한다. 
vCPU, vMemory 로 나누고 VM마다 vCPU, vMemory등을 가지고, VM의 OS인 Guset OS가 이를 관리한다. 
하이퍼바이저는 host OS로 
가상화 환경에서 만들어지는 새로운 OS
하이퍼바이저 위에 바로 VM을 설치할 수 있도록 서버를 구축해준다.</p>
</li>
<li><p>type 2 : Hosted
type2에서의 하이퍼바이저는 애플리케이션이다. 그 위에 나누어진 리소스 위에 VM을 만들고 </p>
</li>
<li><p>물리자원 공유 : 아래 있는 HW의 물리적 자원을 가상 자원으로 나누어서 사용한다. </p>
</li>
<li><p>가상 네트워킹 : 공유기가 스위치 역할도 한다. 하이퍼바이저 내에 가상 스위치를 만들어서 사용
데이터를 주고 받기 위해서 연결이 되어 있어야 한다. 인터넷으로 연결이 되어 있다. pc는 통신을 위한 포트(lan port)가 있고 PC의 네트워크 인ㅌ페이스 카드에 위치하고 있다. 
스위치는 포트가 여러개 있어서 pc들과 각각 연결해서 스위치에서 관리한다. 스위치의 예인 공유기는 와이파이나 선으로 인터넷과의 연결을 해준다. 
하이퍼바이저가 물리적인 자원</p>
</li>
<li><p>가상 머신 마이그레이션</p>
</li>
</ul>
<h2 id="가상화-유형">가상화 유형</h2>
<h2 id="가상-머신">가상 머신</h2>
<p>하이퍼바이저를 통해서 만든 가상의 서버</p>
<p>os의 이미지를 다운받아준다. IOS만 다운받기를 누른다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/5a99e10f-c8f5-45f4-811f-a809ad3ba483/image.png" /></p>
<p>ubuntu.ova를 불러와서 ubuntu이름의 vm을 설정에서 cpu의 코어를 2개로 추가한다. 프로세서 2개로 만들기</p>
<p><code>ip a</code>을 통해서 가상머신의 ip를 확인한다. vm에서 접속해서 확인 =&gt; 10.0.2.15
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/16a79aa5-0a0c-4caf-b579-f85c9d88feb2/image.png" /></p>
<p>PC의 cmd창에서 <code>ipconfig /all</code> 으로 PC의 ip를 확인 =&gt; 192.168.56.1</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/61107590-59a1-41f9-835a-fb4c160e4455/image.png" /></p>
<p>네트워크의 포트 포워딩에서 호스트IP에 pc의 ip를 22포트로 연결하고, 게스트IP에 vm의 ip를 22포트로 연결한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7b50b9c5-2b6c-4d70-b31b-cee6cdebba61/image.png" />
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/1ec2a84f-28a9-49a7-87b4-482d22709664/image.png" /></p>
<hr />
<h4 id="putty">putty</h4>
<p>putty는 리눅스나 유닉스 기반의 서버에 원격 접속을 위한 tool이다. 윈도우는 불가능하며, SSH와 Serial만 가능하다.</p>
<p>putty에서 host name를 pc의 ip를 작성해서 open해준다. =&gt; accept
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/93f0944c-423f-4a2b-9307-1e01d6121106/image.png" /></p>
<p>putty로 oracle에서의 화면조정과 커서가 보이지 않았던 것을 putty를 통해서 할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/4e68bf2b-7a6c-429b-a909-1743742c0f67/image.png" /></p>
<p>이제 putty를 통해서 리눅스 서버에 원격 접속으로 컨트롤 할 수 있다. </p>
<hr />
<h4 id="리눅스-기본-명령어">리눅스 기본 명령어</h4>
<p><code>ls</code> 현재 디렉토리 아래의 파일을 모두 보여줌</p>
<ul>
<li>ls는 명령어로 리눅스에서 명령어는 대문자로 입력하면 안됨</li>
<li>ls 뒤에 (-) 옵션은 대문자/소문자 가능
<code>pwd</code> 명령어는 <strong>현재 디렉토리의 위치</strong>를 보여줌</li>
<li>root 디렉토리는 / 로 최상위를 나타냄
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/1c15a94f-1910-4874-b841-bc706cba6a83/image.png" /></li>
</ul>
<hr />
<ul>
<li><code>ls -a</code> 는 . 으로 시작하는 숨긴 파일들을 보여준다. .으로 시작하는 파일은 숨긴 파일을 의미한다. </li>
<li><code>ls -l</code> 은 파일의 상세 정보를 보여준다. 시간, 파일크기, 이름, 소유자, 그룹 등등</li>
<li><code>ls -al</code> 로 숨긴파일과 상세 정보 모두 보기도 가능하다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/17de3780-e315-4c26-828b-a1ed48edea54/image.png" /></li>
</ul>
<ul>
<li>파일의 유형
일반 파일은 흰색 파일
파란 파일은 디렉토리(폴더)
drwx는 디렉토리 파일임을 알려준다. </li>
<li>명령어에서 옵셥(-)을 사용할 때는 &quot; &quot;공백으로 명령어와 옵션을 구분해주어야 한다. </li>
</ul>
<hr />
<ul>
<li><p><code>history</code> 명령어는 터미널에서 사용한 명령어들의 목록과 번호
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/bf5970e5-6333-4692-857c-e39d16b4a834/image.png" /></p>
</li>
<li><p><code>echo</code> 명령어는 텍스트를 출력해준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/3ad697a8-2411-4ced-9b04-c64f15756a87/image.png" /></p>
</li>
<li><p><code>cd</code> 명렁어는 디렉토리를 이동한다. </p>
</li>
<li><p><code>mkdir</code> 명렁어는 <strong>디렉토리를 생성</strong>해준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/871903aa-0094-424a-a6b5-9f326337e355/image.png" /></p>
</li>
<li><p><code>touch</code> 명렁어는 <strong>파일을 생성</strong>해준다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/f983b309-8276-4b9f-a00a-fe92fe1f9dce/image.png" /></p>
</li>
<li><p><code>rm</code>명령어는 파일을 삭제해준다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/8127fdd3-9021-4817-a4e2-360d8431900e/image.png" /></p>
</li>
<li><p><code>rmdir</code> 명렁어는 디렉토리를 삭제해준다. 
삭제하고자하는 디렉토리는 비어있어야 한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/898a87b2-560c-4d3d-a374-96b44612d948/image.png" />
옵션으로 <code>-rf</code> 를 하면 강제로 지울 수 있다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b120e4e4-f76d-4e0a-87f3-4c4a8efb5dc3/image.png" /></p>
</li>
<li><p><code>cat</code> 명령어는 파일의 이름을 읽고 한번에 출력해준다. 내용이 길면 내용의 마지막만 출력이된다
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/28b97159-bd77-4c79-960e-cbed07844916/image.png" /></p>
</li>
<li><p><code>more</code> 명령어는 스크롤 가능한 형태로 한 화면씩 출력한다. =&gt; space나 enter로 이동가능
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/8bf0390e-a509-4fad-8059-98c6c27840f7/image.png" /></p>
</li>
</ul>
<hr />
<p>도커 
<code>docker login -u username</code> 로 도커로 본인의 username을 입력해서 로그인한다.
현재 도커 비번 설정해주고 입력</p>
<h2 id="컨테이너">컨테이너</h2>
