---
title: "Docker"
date: "2025-06-12"
link: "https://velog.io/@ehekaanldk/Docker"
series: "Uncategorized"
---

<h2 id="container">Container</h2>
<blockquote>
<p>컨테이너는 프로그램 실행에 필요한 환경(코드, 라이브러리, 설정 등)을 하나로 묶어
독립적으로 실행할 수 있게 만든 가상화된 실행 환경</p>
</blockquote>
<ul>
<li>전체 운영체제를 포함하지 않아서 가볍고 빠르다.</li>
<li>host 와 OS 커널을 공유한다.</li>
<li>가상화된 개발/실행 환경</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7b2ea075-d3ee-4b90-b028-ea5780b0111d/image.png" /></p>
<p>container 만들기 위한 준비물</p>
<ul>
<li>docker file</li>
<li>docker image</li>
</ul>
<h2 id="docker">Docker</h2>
<blockquote>
<p>컨테이너를 만들고 실행하고 관리하는 플랫폼</p>
</blockquote>
<ul>
<li>컨테이너 이미지를 만들 수 있게 도와주는 컨테이너 엔진</li>
<li>어느 OS에서도 동일한 컨테이너를 실행할 수 있다. </li>
<li>컨테이너는 파일 시스템, 네트워크, 프로세스 공간만 격리되고, 운영체제 커널은 호스트와 공유된다.</li>
<li>docker image를 기반으로 커널 기능??? 을 활용해서 실시간으로 격리된 실행 환경(컨테이너)를 만들어낸다. </li>
</ul>
<h2 id="docker-image">Docker Image</h2>
<blockquote>
<p>docker file을 기반으로 생성된 실행 환경 압축 패키지(정적 파일)</p>
</blockquote>
<ul>
<li>애플리케이션과 필요한 라이브러리, 실행 환경이 포함된 “컨테이너의 설계도”</li>
<li>직접 실행되지 않고, 컨테이너 생성의 기반이 된다. </li>
<li>구동되고 있는 application의 내용을 갭쳐해서 이미지로 두는 것이다. </li>
</ul>
<table>
<thead>
<tr>
<th>개념</th>
<th>비유</th>
</tr>
</thead>
<tbody><tr>
<td>Docker Image</td>
<td>클래스(class), 붕어빵 틀, 게임 설치 파일</td>
</tr>
<tr>
<td>Container</td>
<td>인스턴스(instance), 붕어빵 하나, 실행 중인 게임 프로세스</td>
</tr>
</tbody></table>
<h2 id="docker-file">Docker file</h2>
<blockquote>
<p>컨테이너 이미지를 만들기 위한 실행 환경을 구성하는 방법이 적힌 설정 파일</p>
</blockquote>
<ul>
<li>어떤 OS를 기반으로 할지</li>
<li>어떤 패키지를 설치할지</li>
<li>어떤 환경변수를 사용할지</li>
<li>어떻게 실행할지
명령어가 text로 작성</li>
</ul>
<pre><code># 어떤 OS를 기반으로 할지
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY requirements.txt .

# 패키지 설치
RUN pip install -r requirements.txt

# 전체 소스 코드 복사
COPY . .

# 실행할 명령어
CMD [&quot;python&quot;, &quot;main.py&quot;]</code></pre><ul>
<li>환경을 수정하거나</li>
<li>라이브러리를 추가할 수 있다.</li>
</ul>
<h2 id="docker-흐름">Docker 흐름</h2>
<p>Dockerfile ⟶ (docker build) ⟶ Docker Image ⟶ (docker run) ⟶ Container</p>
<h2 id="docker-compose">docker-compose</h2>
<blockquote>
<p>여러개의 컨테이너를 한꺼번에 사용하는 Application을 실행하거나 관리할 수 있도록 해주는 도구</p>
</blockquote>
<p>기존의 <code>docker run</code>은 서비스별로 실행 순서를 맞춰야 하고, 환경 변수도 붙여줘야 한다. 
docker 자체로 여러 컨테이너를 동시에 실행할 수 있지만 <code>docker run</code> 명령어는 한번에 하나의 컨테이너만 실행하는 명령이다.</p>
<table>
<thead>
<tr>
<th>서비스</th>
<th>역할</th>
<th>컨테이너</th>
</tr>
</thead>
<tbody><tr>
<td>FastAPI</td>
<td>API 서버</td>
<td>fastapi-container</td>
</tr>
<tr>
<td>MySQL</td>
<td>데이터베이스</td>
<td>mysql-container</td>
</tr>
<tr>
<td>Redis</td>
<td>캐시 서버</td>
<td>redis-container</td>
</tr>
</tbody></table>
<p><code>docker-compose.yml</code> 파일을 사용해서 터미널에 <code>docker-compose up</code> 으로 여러 개의 컨테이너가 동시에 실행되어 하나의 시스템처럼 보이게 한다. </p>
<pre><code>version: '3'
services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: example

  redis:
    image: redis:latest

  web:
    build: .
    ports:
      - &quot;8000:8000&quot;
    depends_on:
      - db
      - redis</code></pre>
