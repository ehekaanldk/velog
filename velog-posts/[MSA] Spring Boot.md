---
title: "[MSA] Spring Boot"
date: "2025-05-29"
link: "https://velog.io/@ehekaanldk/MSA-Spring-Boot"
series: "Uncategorized"
---

<p>전체흐름</p>
<ul>
<li><ol>
<li>클라이언트: 브라우저나 앱을 통해 사용자가 요청</li>
</ol>
</li>
<li><ol start="2">
<li>웹서버: 요청을 받아 스프링부트 애플리케이션으로 전달</li>
</ol>
</li>
<li><ol start="3">
<li>스프링부트: 요청 처리 (Controller → Service → Repository)</li>
</ol>
</li>
<li><ol start="4">
<li>DB: 데이터 읽기/쓰기</li>
</ol>
</li>
<li><ol start="5">
<li>스프링부트: 처리 결과를 View 또는 JSON으로 생성</li>
</ol>
</li>
<li><ol start="6">
<li>웹서버: 응답 전달</li>
</ol>
</li>
<li><ol start="7">
<li>클라이언트: 화면에 결과 표시</li>
</ol>
</li>
</ul>
<p>응답흐름</p>
<ol>
<li><p>DB → Repository로 결과 반환</p>
</li>
<li><p>Repository → Service</p>
</li>
<li><p>Service → Controller</p>
</li>
<li><p>Controller → HTTP 응답 생성</p>
</li>
</ol>
<ul>
<li>JSON (API)</li>
<li>HTML (Thymeleaf, JSP)</li>
</ul>
<ol start="5">
<li><p>스프링부트 → 웹서버로 전달</p>
</li>
<li><p>웹서버 → 클라이언트에게 응답</p>
</li>
<li><p>클라이언트 → 브라우저에서 결과 출력</p>
</li>
</ol>
<h2 id="스프링과-스프링-부트">스프링과 스프링 부트</h2>
<ul>
<li><p><strong>spring</strong>은 프레임워크로 java 기반의 웹 애플리케이션을 만들 수 있도록 도와주는 도구이다. </p>
</li>
<li><p><strong>spring boot</strong>는 spring을 기반으로 내장형 톰캣을 포함한 실행 가능한 서버 환경(jar)을 제공한다. 마치 서버처럼 실행이 가능하다. </p>
</li>
</ul>
<h3 id="기존의-spring과-spring-boot의-차이">기존의 spring과 spring boot의 차이</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>기존 Spring Framework</th>
<th>Spring Boot</th>
</tr>
</thead>
<tbody><tr>
<td><strong>설정 방식</strong></td>
<td>XML 또는 Java 설정 파일을 수동 작성해야 함</td>
<td>자동 설정(Auto Configuration) 제공</td>
</tr>
<tr>
<td><strong>서버 구동</strong></td>
<td>외부 WAS(Web Application Server) 필요 (예: Tomcat 설치 필요)</td>
<td>내장형 톰캣 제공 → <code>jar</code> 실행만으로 서버 구동 가능</td>
</tr>
<tr>
<td><strong>개발 편의성</strong></td>
<td>복잡한 설정 필요</td>
<td>의존성 자동 관리, 기본 구조 제공</td>
</tr>
<tr>
<td><strong>프로젝트 초기 구성</strong></td>
<td>복잡하고 시간이 오래 걸림</td>
<td>Spring Initializr로 간단하게 시작 가능</td>
</tr>
</tbody></table>
<ul>
<li><p>spring에서는 설정을 XML로 많이 작성했다. 
객체를 수동으로 등록하고 관리했다. </p>
</li>
<li><p>spring boot에서는 어노테이션 방식을 사용한다. 
@component, @service,@configuration
XML 설정이 거의 없고, Java기반의 설정이나 application.properies로 간단하게 처리가 가능하다.</p>
</li>
</ul>
<ul>
<li><p>기존의 스프링은 구동을 위해서 외부의 WAS인 tomcat를 설치해야한다. </p>
</li>
<li><p>스프링 부트는 내장형 톰캣을 제공해 jar실행만으로 서버 구동이 가능하다.</p>
</li>
<li><p>기존의 스프링은 여러 war 중에 하나가 치명적인 오류가 있다면?
하나의 어플리케이션이 오류가 나도 tomcat 전체가 오류가 날 수 있다. =&gt; scale-out이 권장</p>
</li>
<li><p>스프링 부트로 만든 결과물이 단독으로 실행이 가능하다. </p>
</li>
<li><p>프로그램 내부에 tomcat이 존재해서 프로그램하나가 온전한 웹 서버의 역할을 한다. </p>
</li>
</ul>
<blockquote>
<p>스프링 기반의 애플리케이션을 개발하기 쉽도록 설정의 많은 부분을 자동화하여 사용자가 편하게 스프링을 활용할 수 있다.</p>
</blockquote>
<h3 id="특징">특징</h3>
<ul>
<li>스프링은 설정이 매우 복잡</li>
<li>빠르게 스프링 부트 프로젝트 설정가능</li>
<li>의존성 세트라고 불리는 starter 를 사용해서 간편하게 의존성을 사용하ㅏ거나 관리할 수 있다.</li>
<li>내장형 tomcat 이 있어서 웹서버로써도 동작이 가능하다.</li>
<li>tomcat에게 프로그램을 실행시키기 위해서는 war가 필요하지만 내장되어 있음 =&gt; jar</li>
<li>war로 감싸서 따로 배포없이, 바로 jar파일만 실행하면 웹 서버도 같이 실행된다.</li>
</ul>
<h3 id="starter">starter</h3>
<ul>
<li><p><strong>빌드</strong> : 개발한 소스코드(.java) 를 실행 가능한 형태(.jar/.war) 로 만드는 과정이다. </p>
</li>
<li><p><strong>배포</strong> : 빌드된 실행 파일(.jar/.war)를 실제 서버에 올려서 구동시키는 과정이다.</p>
</li>
<li><ol>
<li>개발 단계에서 controller, service, repository로 자바 코드를 작성하고,</li>
</ol>
</li>
<li><ol start="2">
<li>빌드 단계에서 .jar 파일이 생성된다.</li>
</ol>
</li>
<li><ol start="3">
<li>배포 단계에서 생성된 .jar 파일을 서버에 복사하고, 서버에서 java -jar 로 실행하면, 앱이 내장 톰캣으로 서버처럼 동작한다. </li>
</ol>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/fc9c1023-e845-485d-8626-1a84f6518486/image.png" /></p>
<h4 id="dependencies">dependencies</h4>
<p>initialize에서 의존성 dependencies를 미리 추가할 수 있다.</p>
<ul>
<li>Spring Boot DevTools : 개발하고 디버깅하는데 도움울 주는 기능</li>
<li>Lombok : @getter/@setter등을 자동 생성해서 코드를 간결하게 만들어주는 기능</li>
<li>Spring Web : 웹 애플리케이션을 만들기 위한 기본 프레임워크<ul>
<li>spring MVC : Controller, Service, View구성</li>
<li>REST API 생성</li>
</ul>
</li>
<li>H2 Database : 메모리 기반의 가벼운 테스트용 RDBMS<ul>
<li>서버 리부트 시 데이터 사라짐</li>
<li>설치없이 내장으로 동작</li>
</ul>
</li>
</ul>
<h4 id="템플릿-엔진">템플릿 엔진</h4>
<blockquote>
<p>서버에서 <strong>동적으로 HTML을 생성하기 위해</strong> 사용하는 기술이다. 
HTML 파일 안에 ${변수} 같은 자바변수를 끼워넣는 기능이다. </p>
</blockquote>
<ul>
<li>Mustache 는 템플릿 엔진의 일종으로 {{변수명}} 형태로 데이터를 바인딩하는 간단한 템플릿이다. </li>
</ul>
<p><strong>Mustache</strong>
{{변수명}} 형식으로 데이터를 넣어준다. </p>
<pre><code>//main/resourece/templates/hello.mustache
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;&lt;title&gt;Hello&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;안녕하세요, {{name}}님!&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre><p>컨트롤러에서 데이터 전달</p>
<pre><code>//main/java/com.first.mvc/controller/helloController.java
@Controller
public class HelloController {
    @GetMapping(&quot;/hello&quot;)
    public String hello(Model model) {
        model.addAttribute(&quot;name&quot;, &quot;홍길동&quot;);
        return &quot;hello&quot;; // hello.mustache를 렌더링
    }
}</code></pre><ul>
<li>Model model은 View에 데이터를 전달할 때 사용하는 바구니 역할</li>
<li>addAttribute에서 name이라는 이름의 변수에 &quot;홍길동&quot; 값을 담아서 템플릿 엔진에게 전달한다.</li>
<li>model에 <code>name=&quot;홍길동&quot;</code>을 저장한다.</li>
<li>템플릿 안에서 {{name}} -&gt; 홍길동 으로 치환한다. </li>
</ul>
<h2 id="spring-boot-프로젝트">spring boot 프로젝트</h2>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/60a85a9c-19b7-4d3e-88c8-3e61c85aa885/image.png" /></p>
<p>project에서 우클릭&gt; open module settings &gt; project에서 SDK 17 확인</p>
<h3 id="기본적인-디렉토리의-구조">기본적인 디렉토리의 구조</h3>
<pre><code>📦 my-springboot-project
├── 📁 src
│   ├── 📁 main
│   │   ├── 📁 java                ← 💡 Java 코드 (Controller, Service 등)
│   │   │   └── com.example.demo   ← 패키지 경로 (루트 패키지)
│   │   │       └── HelloController.java
│   │   ├── 📁 resources           ← 💡 설정파일, 템플릿, 정적 파일
│   │   │   ├── 📁 static          ← 정적 자원 (HTML, CSS, JS, 이미지 등)
│   │   │   ├── 📁 templates       ← 템플릿 엔진(Mustache, Thymeleaf) 파일
│   │   │   └── 📄 application.properties 또는 application.yml
│   └── 📁 test                   ← 테스트 코드
├── 📄 build.gradle 또는 pom.xml  ← 💡 빌드 설정 파일
</code></pre><ul>
<li><p><code>com.example.demo</code> 디렉토리 아래에 자바 클래스 파일들을 위치시켜줘야 한다. </p>
</li>
<li><p>controller, servicem, repository, model 등을 <code>com.example.demo</code> 패키지 하위에 두어야 자동인식이 된다.</p>
</li>
<li><p>자바 파일을 제외한 HTML, CSS, JavaScript, 환경파일 등은 📁 resources에 저장된다. </p>
</li>
<li><p>📁 templates에는 HTML형식 파일로 템플릿 파일을 저장한다. </p>
</li>
<li><p>📁 static에는 정적인 파일인 이미지, CSS, JavaScript 파일 등이 저장된다.</p>
</li>
<li><p>📄 application.properties 또는 application.yml 는 스프링 애플리케이션 환경을 설정한다. </p>
</li>
</ul>
<p>어노테이션을 확인하고 싶을 때 =&gt; ctrl 눌러서 내용 확인 가능</p>
<p>기본으로 생성되는 파일명Application.java 에는 3개의 어노테이션이 존재한다. </p>
<ul>
<li>@SpringBootConfiguration : 자동구성 활성화</li>
<li>@EnableAutoConfiguration : 현재 패키지 이하에서 어노테이션이 붙은 클래스를 찾아서 빈 등록</li>
<li>@ComponentScan : 빈을 생성하는 configuration 파일임을 명시</li>
</ul>
<p>3개의 어노테이션은 @SpringBootApplication 이라는 1개의 어노테이션이 한번에 처리한다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/3039637a-ebce-457a-985e-54304fd473c1/image.png" /></p>
<p>스프링부트 기반의 test하기 위한 부분
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/0153da08-a599-4da7-a548-8be6d2a175c9/image.png" /></p>
<p>// implementation : 빌드, 개발에 모두 사용(잘 모르면 그냥 다 이거로 설정)
// compileOnly : 컴파일할 때만 사용, 실행 시에는 사용x
// developmentOnly : 개발할 때만 사용
// runtimeOnly : 실행할 때만 사용</p>
<p>gradle로 다운받은 라이브러리를 어디에 어떻게 다운 받았는가? =&gt; external libraries
어떤 버전을 받을지는 어떻게 하는가? pugin에 적은 버전들과 호환이 되는 버전을 것을 자동으로 가져온다.</p>
<p>뭐 때문에 뭘 가져왔다는 구성을 알 수 없다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/f8651465-f719-4b69-acf9-39553fe35953/image.png" /></p>
<p>gradle로 하여금 다운받은 것들이 dependecies에 존재하고 tasks에는 프로젝트에서 실행할 수 있는 작업들을 가진다.</p>
<ul>
<li>dependencies : 필요한 라이브러리 목록</li>
<li>task : gradle이 해줄 수 있는 일 목록
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/83c86458-c24c-4aff-b650-68fdae381e12/image.png" /></li>
</ul>
<p>build.gradle 파일에서 의존성을 추가할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/2e0a2cff-2172-4657-ba1f-4fbb5a4be3c6/image.png" /></p>
<p>main&gt;TestAppApplication 파일을 실행해서 서버동작을 확인한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/9449f7f9-2e3d-4993-bd25-65af3c04c2f4/image.png" /></p>
<p>localhost:8080으로 서버의 동작을 No static resource . 로 나오면 html파일이 없어서 나오는 문제이다. =&gt; index.html을 만들어준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/053698f7-5e2d-4397-a048-6fd3df43e836/image.png" /></p>
<p>수정사항을 입력하고 아래 버튼을 통해서 조작을 하는 것을 권장한다. 코드의 실행 파일을 다시 실행하게 되면 2개가 실행될 수도 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7471b9a2-0d4b-4769-a135-6a6414b8e8a1/image.png" /></p>
<p>F12에서 elements, console, network 에서 request를 잘 받았는지 확인할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/0ddbf774-0047-4d1f-82c2-f6545856424a/image.png" /></p>
<h2 id="mvc-디자인-패턴">MVC 디자인 패턴</h2>
<h3 id="디자인-패턴">디자인 패턴</h3>
<blockquote>
<p>디자인 패턴은 일종의 해답지와 같이 설계의 노하우를 축적하여 방법을 만들고, 이름을 붙여서 규약을 만들어 정리한 것</p>
</blockquote>
<h3 id="🌈-mvc란">🌈 MVC란?</h3>
<p>model - view - controller</p>
<blockquote>
<p>웹 애플리케이션을 3가지 역할로 구분해서 개발하는 디자인패턴이다. </p>
</blockquote>
<h4 id="model">model</h4>
<ul>
<li>데이터를 관리하고 처리하는 계층(DB와 직접연동)</li>
<li>도메인객체(Entity) + 비즈니스로직(Service) + Repository(JPA)</li>
<li>view 나 controller 와 독립적으로 설계할 수 있다.</li>
<li>도메인 데이터나 비즈니스 규칙, 연속성 처리</li>
<li>모델 + 로직을 가지고 있으며, 원론적으로 설명하는 부분으로 기술과 떨어짐</li>
</ul>
<pre><code>@Entity
public class User {
    @Id @GeneratedValue
    private Long id;
    private String name;
}
</code></pre><h4 id="view">view</h4>
<ul>
<li>사용자에게 데이터를 보여주는 역할(UI)를 한다. </li>
<li>모델로 부터 받은 데이터를 시각적으로 표현한다. </li>
<li>HTML, CSS, 템플릿 엔진 등이 포함된다.</li>
<li>view이름은 템플릿 파일이름과 일치해야한다.</li>
<li>사용자의 입력을 직접 처리하지 않고, 모델이 넘긴 데이터만 보여주는 데 집중<pre><code>&lt;!-- templates/hello.mustache 또는 hello.html --&gt;
&lt;h1&gt;안녕하세요, {{name}}님!&lt;/h1&gt;</code></pre></li>
</ul>
<h4 id="controller">controller</h4>
<ul>
<li>사용자 요청(Requset)를 받아서 처리하고, 적절한 View 또는 JSON을 반환한다.</li>
<li>Model &lt;-&gt; View 사이의 중개자 역할</li>
<li>로직은 Service에게 위임해야 한다. 
@Controller, @RestController</li>
</ul>
<pre><code>@Controller
public class HelloController {
    @GetMapping(&quot;/hello&quot;)
    public String helloUser(Model model) {
        model.addAttribute(&quot;name&quot;, &quot;홍길동&quot;);
        return &quot;hello&quot;; // → templates/hello.mustache
    }
}</code></pre><ul>
<li>MVC는 관심사를 분리해서 코드의 의존성을 낮추고, 유지보수성과 재사용성을 향상시킵니다.</li>
<li>프로젝트의 규모가 작을 떄는 복잡성이 증가하는 단점이 있다.</li>
<li>controller로 중간에서 중개하는 사람이 힘들기 마련이다. 중간의 controller가 비대해진다.</li>
<li>request가 오면 제일 먼저 처리해줘야 하는 부분이 controller이다. </li>
</ul>
<p>ctrl + space 를 눌러서 자동완성을 한다. </p>
<hr />
<p>실습</p>
<ol>
<li>@controller
@controller 는 controller 역할을 부여한다. </li>
</ol>
<p>사용자의 요청(/hello)를 받아서 처리하고, 어떤 뷰(template)을 보여줄지 결정하는 역할이다. </p>
<ol start="2">
<li>@GetMapping(&quot;/hello&quot;)
@GetMapping(&quot;/hello&quot;)는 웹 브라우저에서 <a href="http://localhost:%ED%8F%AC%ED%8A%B8%EB%B2%88%ED%98%B8/hello">http://localhost:포트번호/hello</a> 로 접속했을 때 실행되는 코드이다. </li>
</ol>
<p>helloUser() 메서드는 뷰이름 &quot;helloUser&quot;를 리턴한다. </p>
<ol start="3">
<li>return &quot;helloUser&quot;
&quot;templates/helloUser.mustache&quot; 파일을 찾아서 브라우저에 HTML로 보여줘라&quot; 는 뜻이다. 
뷰 이름과 파일 이름은 완전히 일치해야 한다. </li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7a87beb4-ef02-40a7-989b-d2e17d5563d6/image.png" /></p>
<hr />
<p>뷰 템플릿에서 {{}} 안에 변수명을 적어서 구멍을 만들어준다.
컨트롤러의 메소드에서 모델을 매개변수로 받아올 수 있도록 한다. 
컨트롤러가 중간에서 view를 뿌리는 형태이다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/37c72513-fc7e-475b-a5bf-d4fa85cf63fc/image.png" /></p>
<p>모델을 추가한다. </p>
<table>
<thead>
<tr>
<th>대상</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>Model</code></td>
<td>Spring에서 제공하는 인터페이스로, <strong>뷰로 데이터를 전달할 때 사용하는 객체</strong></td>
</tr>
<tr>
<td><code>Model.addAttribute(&quot;키&quot;, 값)</code></td>
<td>데이터를 <code>key-value</code> 형태로 View에 넘겨줌</td>
</tr>
</tbody></table>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d700a85e-3adb-4faa-a1c6-f8218dfd6a0b/image.png" /></p>
<p>모델을 계속 넣어서 실행한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/868f38c3-87b3-4011-9e79-43cfd3687218/image.png" /></p>
<blockquote>
<p>보통 MCV 패턴에서는 Model -&gt; Controller -&gt; View 순으로 파일을 작성한다. </p>
</blockquote>
<ol>
<li>어떤 데이터를 다룰지 정의 (예: Book, User 등)한다. </li>
<li>어떤 요청을 처리할지, 어떤 데이터를 뷰로 전달할지 결정한다.</li>
<li>전달받은 모델 데이터를 화면에 표시한다.</li>
</ol>
<ul>
<li>모델이 있을 떄는 모-&gt;컨-&gt;뷰</li>
<li>모델이 없을 때는 컨-&gt;뷰</li>
</ul>
<p>DispatcherServlet</p>
<ol>
<li>클라이언트의 요청을 DispatcherServlet이 받는다.</li>
<li>DispatcherServlet은 Hander Mapping을 </li>
</ol>
<hr />
<h2 id="persistance-영속성">Persistance: 영속성</h2>
<p>Spring Boot에서 &quot;영속성(Persistence)&quot;이란?
<strong>영속성(Persistence)</strong>이란
데이터를 <strong>일시적인 메모리가 아닌 영구 저장소(보통 DB)</strong>에 지속적으로 저장하고 관리하는 특성을 말합니다.</p>
<p>=&gt; 영속성은 파일 시스템과 관계형 데이터베이스(RDB) 등을 통해서 구현할 수 있다.</p>
<p>=&gt; JAVA에서는 JDBC (Java Database Connectivity) 를 통해 이루어진다. </p>
<h3 id="jdbc">JDBC</h3>
<blockquote>
<p>Java가 데이터베이스에 직접 연결해서 SQL을 실행할 수 있도록 해주는 표준 API</p>
</blockquote>
<ul>
<li><p>JDBC는 SQL을 자동으로 만들어주거나 추상화해주지 않기 때문에 개발자가 직접 SQL을 작성해야 한다.</p>
</li>
<li><p>DB마다 SQL 문법이 다르므로, 데이터베이스 변경 시 SQL도 수정이 필요하다.</p>
<h3 id="jdbc-template">JDBC Template</h3>
<blockquote>
<p>Spring이 제공하는 JDBC 도우미 클래스로, JDBC 사용을 간소화한 버전</p>
</blockquote>
</li>
<li><p>SQL은 여전히 직접 작성하지만, 중복 코드 제거, 예외 처리 자동화 등으로 생산성이 향상된다.</p>
</li>
<li><p>서로 다른 DB라도 일관된 방식으로 접근 가능하도록 템플릿 구조 제공한다.</p>
</li>
<li><p>SQL에서 변하는 값은 ?로 지정하고, setXxx() 메서드로 값을 바인딩한다.</p>
</li>
<li><p>별도의 ORM 없이도 간단한 CRUD 처리에 적합</p>
</li>
</ul>
<h3 id="jpa">JPA</h3>
<blockquote>
<p>Java Presistence API로, 자바에서의 ORM을 구현하기 위한 표준 규칙이다.</p>
</blockquote>
<ul>
<li>ORM은 (Object-Relational Mapping) 객체와 관계형 데이터베이스 간의 매핑을 제공한다. </li>
<li>JPA는 규칙만 정의합니다 (@Entity, @Id, EntityManager 등)</li>
</ul>
<p><strong>구현체(Provider)</strong>가 필요합니다:</p>
<ul>
<li>Hibernate (스프링 부트 기본)</li>
<li>EclipseLink</li>
</ul>
<p>JPA 규칙에 따라 코드가 작성되며, 실제로 SQL을 만들어서 실행하는 것은 hiberate가 수행한다.</p>
<p><strong>hibernate 구현체가 DB가 되는 것은 아니다!!!!!!!</strong></p>
<blockquote>
<ul>
<li>[자바 객체(Entity)]
 ⇅      (JPA)</li>
</ul>
</blockquote>
<ul>
<li>[JPA 인터페이스]
 ⇅      (구현체)</li>
<li>[Hibernate]
 ⇅      (JDBC를 통해 SQL 실행)</li>
<li>[DBMS: MySQL / PostgreSQL / Oracle 등]</li>
</ul>
<p>Spring Boot에서는 </p>
<ul>
<li>build.gradle 에 hibernate가 자동 포함</li>
<li>application.yml 또는 application.propertire에 DB 설정만 하면된다.</li>
<li>show-sql: true → Hibernate가 생성한 SQL을 콘솔에 출력<pre><code>spring:
datasource:
  driver-class-name : org.h2.Driver
  url: jdbc:h2:~/demodb
  username: sa
  password: 1234
h2:
  console:
    enabled: true
    path: /h2-console
jpa:
  hibernate:
    ddl-auto: update
    show-sql: true</code></pre></li>
</ul>
<p>JPA(자바 표준 ORM 인터페이스) 를 사용하는 구조 + Hibernate + DB</p>
<pre><code>@Repository
public interface BookRepository extends JpaRepository&lt;Book, Long&gt; {
}</code></pre><p><strong>JPA 사용중!</strong></p>
<ul>
<li>JpaRepository는 CRUD를 자동으로 생성해주고, &lt;엔티티 클래스명, 클래스의 PK필드 타입&gt; 으로 상속받는다. </li>
<li>Book는 @Entity로 지정된 클래스</li>
<li>Long은 Book의 PK(기본키 @Id)의 타입</li>
<li><em>구현체Hibernate 는 spring이 자동 동작중!*</em></li>
<li>Spring Boot + Spring Data JPA를 쓰면</li>
<li>Spring이 SimpleJpaRepository 기반으로 런타임에 자동 구현</li>
<li>내부적으로 Hiberate가 SQL을 생성하고 실행</li>
<li><em>Hibernate는 의존성 포함중*</em></li>
<li><code>build.gradle</code>에서</li>
<li><code>implementation 'org.springframework.boot:spring-boot-starter-data-jpa'</code></li>
</ul>
<h3 id="jdbc-기반-vs-jpa-비교">JDBC 기반 VS JPA 비교</h3>
<table>
<thead>
<tr>
<th>기술</th>
<th>SQL 직접 작성?</th>
<th>SQL 자동 생성?</th>
<th>특징</th>
</tr>
</thead>
<tbody><tr>
<td><strong>JDBC</strong></td>
<td>✅ 직접 작성</td>
<td>❌ 없음</td>
<td>가장 기본, 모든 SQL 수동 작성</td>
</tr>
<tr>
<td><strong>JdbcTemplate</strong></td>
<td>✅ 직접 작성</td>
<td>❌ 없음</td>
<td>JDBC를 간편하게 사용</td>
</tr>
<tr>
<td><strong>MyBatis</strong></td>
<td>✅ 직접 작성 (XML or 어노테이션)</td>
<td>❌ 없음</td>
<td>SQL은 내가, 매핑은 프레임워크가</td>
</tr>
<tr>
<td><strong>JPA</strong></td>
<td>❌ 직접 작성 안 해도 됨</td>
<td>✅ 자동 생성됨</td>
<td>객체 중심, SQL을 거의 안 씀 (필요하면 JPQL 사용)</td>
</tr>
<tr>
<td>- mybatis와 JDBC는 대표적인 SQL중심으로 SQL쿼리문을 코드에 직접 작성하면 DBMS에종속적인 문제점이 있다.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody></table>
<h3 id="객체-중심-어노테이션">객체 중심: 어노테이션</h3>
<blockquote>
<p>객체 (Entity) 중심으로 SQL을 자동으로 생성하려면,
ORM 매핑을 위한 핵심 역할인 어노테이션을 해야한다. </p>
</blockquote>
<ul>
<li>@Entity → 이 클래스는 DB 테이블이다!</li>
<li>@Id, @GeneratedValue → 기본키 설정</li>
<li>@Column → 컬럼 이름, 제약조건 등 지정</li>
<li>관계 설정에는 @OneToMany, @JoinColumn 등 사용</li>
</ul>
<blockquote>
<p>&quot;자바 클래스는 설계도 📦, 어노테이션은 DB와 연결해주는 주소표 📌&quot;</p>
</blockquote>
<h3 id="orm이란">ORM이란</h3>
<ul>
<li>ORM은 (Object-Relational Mapping) 객체와 관계형 데이터베이스 간의 매핑을 제공한다.</li>
<li>객체지향 언어(Java)의 객체와, 관계형 데이터베이스(DB)의 테이블을 자동으로 매핑(mapping) 해주는 기술</li>
<li>쉽게 말하면, &quot;객체(Entity) 1개 ↔ 테이블(Table) 1개&quot; </li>
<li>불일치를 자동으로 매칭해주는 기술이 ORM이다.<table>
<thead>
<tr>
<th>불일치 유형</th>
<th>설명</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><strong>상속 불일치</strong></td>
<td>자바는 클래스 상속이 자연스럽지만, RDB는 테이블 상속 없음</td>
<td><code>User</code>와 <code>Admin</code> 클래스가 상속일 때 테이블은 나눌지 합칠지 선택해야 함</td>
</tr>
<tr>
<td><strong>관계 표현의 불일치</strong></td>
<td>객체는 참조로 연결하지만, DB는 외래키로 연결</td>
<td><code>user.getDepartment()</code> vs. <code>user.dept_id</code></td>
</tr>
<tr>
<td><strong>컬렉션 처리의 차이</strong></td>
<td>객체는 List, Set 등 컬렉션을 직접 사용</td>
<td>DB는 조인으로 표현해야 함 (<code>1:N 관계</code>)</td>
</tr>
<tr>
<td><strong>식별 방식의 차이</strong></td>
<td>객체는 메모리 주소로 구분, DB는 기본키(PK)로 구분</td>
<td>객체는 <code>==</code>, DB는 <code>id</code></td>
</tr>
<tr>
<td><strong>데이터 변경 감지</strong></td>
<td>객체는 메모리 내에서 추적, DB는 트랜잭션 로그 사용</td>
<td>Java는 equals/hashCode, DB는 쿼리 비교</td>
</tr>
</tbody></table>
</li>
</ul>
<blockquote>
<ul>
<li>자바 관점에서는 클래스,객체</li>
</ul>
</blockquote>
<ul>
<li>DB 관점에서는 테이블</li>
<li>스프링+JPA 관점에서는 @entity</li>
<li>Model은 데이터 그 자체 or 데이터를 담은 객체</li>
</ul>
<h4 id="orm의-장점">ORM의 장점</h4>
<ul>
<li>전체 구조 일관 유지</li>
<li>query보다 객체 자체에 집중</li>
<li>코드의 가독성이 높다</li>
<li>DBMS에 대한 종속성 감소</li>
</ul>
<p>=&gt; 객체 간의 관계를 바탕으로 SQL를 자동으로 생성,
객체의 자료형 타입까지 사용가능해서 
RDBMS의 데이터 구조와 객체 지향 모델 사이의 간격을 좁힌다.</p>
<p>추상적으로 소스코드 부르듯이 CURD 다 만들어준다. </p>
<h3 id="영속성-컨텍스트persistence-context">영속성 컨텍스트(Persistence Context)</h3>
<blockquote>
<p>JPA가 엔티티(객체)를 저장하고 추적하는 1차 캐시 공간이다. </p>
</blockquote>
<ul>
<li>객체와 DB가 연결된 상태로 JPA는 DB에 바로 저장하지 않고, 먼저 메모장에 써두고 관리한다. </li>
<li>이 메모장이 영속성 컨텍스트로 애플리케이션(JPA)와 DB 사이의 객체를 보관하는 <strong>가상의 DB(캐시)역할</strong>을 한다.</li>
</ul>
<h4 id="영속-상태">영속 상태</h4>
<blockquote>
<p>메모장에 적혀서 JPA가 관리 중인 객체</p>
</blockquote>
<p>사용하는 이유</p>
<ul>
<li>기억해두고, SQL을 다시 안 날림</li>
<li>감시하면서, 값이 바뀌면 알아서 UPDATE</li>
<li>지연처리하면서, 쿼리를 모아두고 트랜잭션 끝날 때 한번에 처리</li>
</ul>
<p>1차 캐시는 Map&lt;엔티티의 ID, 엔티티 객체&gt; 으로
<strong>ID(PK)</strong>를 <strong>Key</strong>, <strong>Entity 객체</strong>를 <strong>Value</strong>로 저장하는
<strong>Map 형태의 캐시 저장소</strong>입니다.</p>
<h4 id="엔티티-매니저">엔티티 매니저</h4>
<blockquote>
<p>영속성 컨텍스트를 관리하는 JPA의 핵심 객체
👉 즉, 엔티티(자바 객체)를 <strong>저장, 조회, 수정, 삭제하는 모든 JPA 작업</strong>은 <strong>EntityManager가 처리한다.</strong></p>
</blockquote>
<table>
<thead>
<tr>
<th>기능</th>
<th>설명</th>
<th>예시 메서드</th>
</tr>
</thead>
<tbody><tr>
<td>📦 <strong>영속성 컨텍스트 관리</strong></td>
<td>객체를 등록, 추적, 삭제</td>
<td><code>persist()</code>, <code>detach()</code>, <code>clear()</code></td>
</tr>
<tr>
<td>🔍 <strong>데이터 조회 (SELECT)</strong></td>
<td>PK로 엔티티 찾기</td>
<td><code>find()</code></td>
</tr>
<tr>
<td>💾 <strong>데이터 저장 (INSERT)</strong></td>
<td>객체를 DB에 저장 (쓰기 지연 적용됨)</td>
<td><code>persist()</code></td>
</tr>
<tr>
<td>✏️ <strong>데이터 수정 (UPDATE)</strong></td>
<td>엔티티 값이 바뀌면 자동 감지</td>
<td>(변경 감지 + 트랜잭션 commit 시 반영)</td>
</tr>
<tr>
<td>🗑 <strong>데이터 삭제 (DELETE)</strong></td>
<td>영속 상태의 객체를 삭제 예약</td>
<td><code>remove()</code></td>
</tr>
<tr>
<td>🔄 <strong>플러시(쿼리 실행)</strong></td>
<td>쿼리 실행 시점 제어</td>
<td><code>flush()</code></td>
</tr>
<tr>
<td>🧹 <strong>캐시 초기화</strong></td>
<td>1차 캐시(영속성 컨텍스트) 제거</td>
<td><code>clear()</code>, <code>detach()</code></td>
</tr>
</tbody></table>
<p><strong>jpa.find() ==  SELECT</strong>
<code>News news = entityManager.find(News.class, newsId);</code></p>
<ul>
<li>같은 트랜잭션 내에 해당 엔티티가 존재하면 DB쿼리 없이 반환(영속성 컨텍스트에서 확인)</li>
<li>없으면 Hibernate가 SQL문 자동생성 후 JDBC를 통해 DB에 날림
<code>SELECT * FROM news_table WHERE news_id = :newsId;</code></li>
<li>DB에서 조회된 결과를 기반으로 <code>News</code> 객체를 <code>new</code> 안하고 영속 객체로 만들어 반환</li>
<li>이 <code>News</code> 객체는 영속 상태로 전환됨(영속성 컨텍스트에 등록-관리대상)</li>
</ul>
<h4 id="쓰기-지연-sql-저장소">쓰기 지연 SQL 저장소</h4>
<blockquote>
<p>persist() 했을 때 바로 DB에 INSERT SQL 을 보내지 않고, 트랜잭션이 commit되지 전까지 SQL을 모아두는 공간</p>
</blockquote>
<p>INSERT는 초기 등록으로 DB에 없던 새로운 데이터로 언제 넣을지 타이밍을 정할 수 있다..!!</p>
<ul>
<li>아직 DB에 없는 새 데이터</li>
<li>순서와 즉시성 중요하지 않음 -&gt; 즉시 SQL을 날리지 않고 모아두면 성능 최적화, 트랜잭션 안정성</li>
<li>다른 SELECT, UPDATE, DELETE는 타이밍이 매우 중요해서 지연에 넣지 않음</li>
</ul>
<p>persist()는 영속성 컨텍스트에 객체를 등록하라는 명령이다. 
트랜잭션은 하나의 작업 단위를 DB에 반영하려는 논리적 묶음</p>
<p>[em.persist()] 
  → 영속성 컨텍스트 등록 (1차 캐시에 추가)
  → 쓰기 지연 저장소(INSERT SQL 보류 상태)에 저장</p>
<p>[트랜잭션 commit() 호출 시]
  → flush()
  → 쓰기 지연 저장소의 SQL 생성
  → JDBC를 통해 DB에 실제 INSERT</p>
<h4 id="엔티티-생명-주기">엔티티 생명 주기</h4>
<ul>
<li>비영속 : 객체 생성 후 영속성 컨텍스트와 관계가 없는 상태(em은 모름)
<code>Book book = new Book();</code></li>
<li>영속 : 객체 생성 후 em.persist(엔티티)로 영속성 컨텍스트에 들어간 상태 (DB table과 매핑되어 추적 가능)
<code>Book book = new Book();</code>와 <code>em.persist(book);</code></li>
<li>준영속 : 영속성 컨텍스트에 저장되었다가 분리되어 나온 상태(관리 해제)
<code>Book book = new Book();</code>와 <code>em.detach(book);</code></li>
<li>삭제 : 객체를 삭제한 상태
<code>Book book = new Book();</code>와 <code>em.remove(book);</code> 으로 반드시 영속상태에서만 가능</li>
</ul>
<hr />
<h2 id="실습">실습</h2>
<p>h2를 사용하는 것은 JDBC driver도 함께 다운받는 것과 같다. </p>
<p>파일의 이름을 application.yml 로 변경하거나 지우고 다시 생성한다. 
shift+tab 들여쓰기 앞으로 이동
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/24621353-fbf2-4c9f-97de-4fc5104e9045/image.png" /></p>
<p>스프링부트에서 H2 database와 JPA 사용을 위한 설정을 yml파일로 해준다.</p>
<pre><code>spring:
  datasource:
    driver-class-name : org.h2.Driver
    url: jdbc:h2:~/demodb
    username: sa
    password: 1234
  h2:
    console:
      enabled: true
      path: /h2-console
  jpa:
    hibernate:
      ddl-auto: update
      show-sql: true</code></pre><ul>
<li><p>driver-class-name: H2 데이터베이스에 연결하기 위한 드라이버 클래스.</p>
</li>
<li><p>url: H2 데이터베이스의 주소</p>
</li>
<li><p>enabled: true: H2 콘솔 기능을 켜짐 상태로 설정</p>
</li>
<li><p>path: /h2-console: 웹에서 접속할 때 <a href="http://localhost:%ED%8F%AC%ED%8A%B8%EB%B2%88%ED%98%B8/h2-console">http://localhost:포트번호/h2-console</a> 경로로 접속 가능</p>
</li>
<li><p>ddl-auto: update: 애플리케이션 실행 시 엔티티 클래스(Entity)에 맞춰 DB 테이블을 자동 생성 및 수정</p>
</li>
</ul>
<p><code>http://localhost:8080/h2-console</code> 으로 h2 database에 들어갈 수 있는 콘솔에 접속한다. 
<code>C:\Users\User</code> 가 경로에서 ~ 이다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/05122e11-2272-4068-942e-421214c37da4/image.png" /></p>
<p>DB table이랑 entity class를 매핑해줘야 한다. entity class를 먼저 만든다.</p>
<pre><code>@Entity // 영속성과 관련된 content
@NoArgsConstructor // 기본 생성자를 만든다.
@AllArgsConstructor // 모든 args를 받는 생성자를 만든다.
@Getter
@Setter // 클래스 안에 모든 필드들을 set할 수 있다. setter()함수 막 선언 안해도 된다.
public class News { // 엔티티이다. 엔티티이면 jpa에서 테이블로 만든다.

    @Id // 뉴스클래스를 뉴스테이블로 만들 때 PK로 만들어준다. 엔티티는 ID가 없으면 오류가 난다.
    @GeneratedValue(strategy = GenerationType.IDENTITY) // ID를 자동으로 만들어준다. 전략으로 자동으로 어떻게 만들지 선택한다.
    private Long newsId; // 고유식별 번호, 숫자가 들어간다.

    // ID를 제외하면 일반 컬럼
    @Column(name =&quot;new_title&quot;, nullable = false, length = 255) // 컬럼으로 변환할 때 제약을 주고 싶을때(자바와 실제
    private String title; // 문자가 들어가는 것을 알 수 있다.

    // 테이블 설계에 도움을 준다. auto ddl에서 사용된다.
    @Column(nullable = false) // nullable=false로 데이터가 무조건 들어와야 되는 필수값으로 지정
    private String content;

}</code></pre><p>News 테이블이 만들어진 것을 확인할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/f4d179d7-98f6-48e0-8a50-c9e7885ff339/image.png" /></p>
<ul>
<li><p>@NoArgsConstructor</p>
</li>
<li><p>@AllArgsConstructor</p>
</li>
<li><p>@Getter/ @Setter</p>
</li>
<li><p>@Enumerated </p>
</li>
</ul>
<h2 id="과거-jdbc-코드">과거 JDBC 코드</h2>
<p>과거에는 코드에 SQL도 쓰고, 연결하고 등등의 코드가 길게 작성하였다. </p>
<pre><code>Connection conn = ...
PreparedStatement stmt = conn.prepareStatement(&quot;INSERT INTO news ...&quot;);
stmt.setString(1, &quot;제목&quot;);
stmt.executeUpdate();
</code></pre><h2 id="jpa-1">JPA</h2>
<blockquote>
<p>JPA는 자바 객체를 데이터베이스에 쉽게 저장하고 꺼내기 위한 표준기술이다. </p>
</blockquote>
<ul>
<li>자바 클래스 = DB 테이블</li>
<li>자바 객체 = DB 행(ROW)</li>
<li>SQL를 안써도 자바 코드로 DB 조작이 가능하다!</li>
</ul>
<pre><code>@Entity
public class News {
    @Id
    private Long id;
    private String title;
}</code></pre><p>em은 entityManager 로 JPA의 도구이다. persist는 영속성을 부여한다. </p>
<pre><code>em.persist(news); // news 객체를 DB에 저장해줘</code></pre><p>entityManager를 사용하는 것도 복잡해서 spring data jpa와 jparepository를 사용한다. </p>
<h2 id="repository">Repository</h2>
<p>스프링에서 repository 는 데이터베이스와 직접 통신하는 계층이다. 
데이터를 저장하거나 꺼낼 떄 사용하는 역할이다. </p>
<h3 id="jparepository란">JpaRepository란?</h3>
<p>JpaRepository는 Spring Data JPA에서 제공하는 인터페이스이다.</p>
<p>👉 쉽게 말해: 데이터베이스 작업(CRUD)을 자동으로 해주는 도구예요.</p>
<hr />
<p>DB 서버
domain 에서 book을 만든다.
repository 에서 interface로 만든다.
controller 통신
DTO </p>
<ul>
<li>controller가 repos 구현체가 필요하다. =&gt; 요청을 해주어야 한다.</li>
<li>DI 의존성 주입으로 controller가 repository가 필요하다~!</li>
</ul>
<ol>
<li><p>필드에 직접 넣어주세요</p>
<pre><code>public class BookController {
 @Autowired
 private BookRepository bookRepository; // +bookRepository.findAll()

 @GetMapping(&quot;/books&quot;)
 public List&lt;Book&gt; getBooks(){
     return bookRepository.findAll();
 }
}</code></pre></li>
</ol>
<ul>
<li>BookController는 사용자의 요청을 받아서 응답을 처리한다. (MVC에서 Controller)</li>
<li>의존성 주입으로 @Autowired 로 스프링이 필요한 객체를 자동으로 주입</li>
<li>BookRepository 라는 인터페이스의 구현체를 찾아서 자동으로 필드에 넣어준다.</li>
<li>BookController가 직접 BookRepository(데이터베이스)에 접근한다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/17f79703-1637-4520-8849-8031f60715ff/image.png" /></p>
<p>Postman으로 확인할 수도 있다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/8dd183f2-8e6f-408b-a7f4-8cef870a12f0/image.png" /></p>
<p>POST로 컬렉션 리소스(books)에 새 자원을 생성해달라는 요청을 보낸다.</p>
<ul>
<li>현재 값을 아무것도 주지 않고 POST해서 nullable=false로 값을 넣어주지 않아서 400 error가 발생한다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/f647c499-4e08-4df1-bbae-7c3c29e51ba8/image.png" /></p>
<p>Body: POST 패킷의 본체</p>
<ul>
<li>POST 요청은 데이터를 HTTP 요청의 <strong>Body(본문)</strong>에 담아 전송한다.</li>
<li>Postman 등의 도구에서 raw + JSON 타입으로 원문 데이터를 직접 작성한다.</li>
</ul>
<pre><code>{
  &quot;title&quot;: &quot;book title&quot;,
  &quot;subTitle&quot;: &quot;book sub title&quot;
}</code></pre><p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/0d0533be-2e94-4435-a6da-7a454583b4f9/image.png" /></p>
<blockquote>
<p>컬렉션 리소스란?
books는 책의 모음을 의미한다. 
POST/books 는 books 컬랙션의 새 항목을 추가해줘의 의미이다. </p>
</blockquote>
<p>현재는 books를 전체 다 확인한다. 
@PostMapping(&quot;/books&quot;) 처리했기 때문에 JSON을 Book 객체로 매핑한다. </p>
<p>book을 하나씩 확인하기 위해서는 
@GetMapping(&quot;/books/{id}&quot;) 으로 경로 변수로 id를 받는 GET 요청을 처리한다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/385a2c1f-4a8e-4aae-8cc5-c06df9db8258/image.png" /></p>
<ul>
<li>{id}로 URL 경로 중에 변하는 부분이다. 책의 고유한 번호</li>
<li><code>bookRepository.findById(id)</code> 으로 해당 ID의 BOOK을 데이터베이스에서 조회</li>
</ul>
<p><code>books</code> 경로가 계속 동일하게 사용되는 것을 컨트롤러의 상위로 꺼내서 정의한다. 
모든 request에 대한 mapping을 <code>/books</code> 로 해준다.</p>
<p>*<em>도메인 객체를 컨트롤러에서 그대로 사용하는 것은 사실 권장하지 않는다. *</em></p>
<ul>
<li>도메인 객체 = @Entity가 붙은 클래스로 DB와 연결된 모델</li>
</ul>
<p>DPO를 사용한다. </p>
<h2 id="dpo">DPO</h2>
<blockquote>
<p>DTO는 data를 전송하기 위해서 순수 데이터만 담는 객체이다. </p>
</blockquote>
<ul>
<li>entity와 분리해서 <strong>입력/출력 전용</strong>으로 사용한다. </li>
</ul>
<p>객체들이 json으로 직렬화된다.</p>
<blockquote>
<p>계층 간의 데이터 전달을 위해서 controller &lt;-&gt; service &lt;-&gt; DB 사이에서 데이터를 안전하게 전달하고, 필요한 데이터만 추려서 보낸다.</p>
</blockquote>
<p>🧾 Entity: 실제 문서 원본 (모든 정보 포함)
📬 DTO: 고객에게 보내는 요약본 (필요한 정보만 간추림)</p>
<p>순수 데이터 전달용으로 getter, setter만 가지고 있다. </p>
<p>도메인 객체와 통신을 위한 객체를 분리한다.</p>
<p>클라이언트에게 받을 때 id 필요없음
순수 데이터만 받는다는 규격을 정해준다. </p>
<ul>
<li>신규책이 들어오면 항상 대출 가능한 상태를 만들어준다. </li>
<li>POST로 책을 하나씩 넣어주고</li>
<li>GET으로 전체를 모두 가져와서 읽어준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/c552c46d-57be-412d-91e5-db782bf38371/image.png" /></li>
</ul>
