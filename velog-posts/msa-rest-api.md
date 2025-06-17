---
title: "[MSA] REST API"
date: "2025-06-01"
link: "https://velog.io/@ehekaanldk/MSA-REST-API"
series: "Uncategorized"
---

<h2 id="rest">REST</h2>
<p>Representational State Transfer API 으로 <strong>자원</strong>을 웹상에서 제공하려고 하는 규격이다. </p>
<p>자원은 데이터 정보를 규격화해서 해당 정보를 넘고 받으며, json을 기반으로 한다. 
json 형태로 데이터를 송수신한다. </p>
<p><strong>JSON이 선호되는 이유</strong></p>
<ul>
<li><p>브라우저입장에서 rest로 서버에 데이터를 요청하는 것은 브라우저의 특성에 데이터를 맞춘다. </p>
</li>
<li><p>xml은 쓸데없는 데이터가 많아서 오버헤드가 크다. 태그의 열고 닫힘으로 키가 2배로 발생하고 파싱이 어렵다.</p>
</li>
<li><p>JS가 다루는 객체와 구조가 유사한 JSON을 사용한다.</p>
</li>
</ul>
<p>자원 resource : URL로 표현되는 대상
행위 method : HTTP 메서드로 표현
표현 representation : 자원의 데이터표현 JSON, XML </p>
<p>json으로 직렬된 형태로, {} 중괄호 하나로 데이터가 하나이다.</p>
<pre><code>{
  &quot;book_id&quot;: 1,
  &quot;title&quot;: &quot;REST API 입문&quot;,
  &quot;author&quot;: &quot;홍길동&quot;
}</code></pre><p><strong>REST의 특징</strong></p>
<ul>
<li>인터페이스 일관성
HTTP method를 사용해서 균일하게 인터페이스를 정의하고 구현한다. </li>
<li>무상태성<ul>
<li>한번의 응답을 하면서 이후에는 기억하지 않는다. </li>
<li>작업을 위한 상태 정보를 따로 저장하고 관리하기 않아서 client가 관리한다.</li>
<li>api서버는 들어오는 요청만 단순히 처리한다.</li>
<li><strong>로그인</strong> 정보조차도 저장하지 않아서 token을 통해서 <strong>requset header에 token을 붙여서 매번 requset 할 때마다 들고 다닌다.</strong></li>
<li>브라우저가 모든 것을 알고 있어야 한다.</li>
</ul>
</li>
<li>캐싱<ul>
<li>웹에서 사용하는 기존 인프라를 그대로 활용할 수 있다.</li>
</ul>
</li>
<li>서버-클라이언트 구조<ul>
<li>UI를 처리하는 부분과 UI와 통신하는 부분과, 데이터와 통신하는 부분을 나누어서 관리한다.</li>
</ul>
</li>
<li>계층형 구조<ul>
<li>rest 서버는 다중 계층으로 구성되면서 구조상의 유연성을 가진다.</li>
</ul>
</li>
</ul>
<p><strong>장점</strong></p>
<ul>
<li>HTTP 프로토콜 인프라를 그대로 사용</li>
<li>서버와 클라이언트의 역할을 명확하게 분리한다.</li>
</ul>
<p><strong>단점</strong></p>
<ul>
<li>표준 자체가 존재하지 않아서 </li>
<li>구현을 할 때의 표준, 정의할 때의 표준과 같은 기준이 없다.</li>
<li>HTTP Method의 형태가 제한적이다.
실제로 서비스를 하면 세부적인 method가 없고 개발자가 작성하는데 영향이 크다.</li>
<li>header값 수정이 여려움 =&gt; postman사용</li>
</ul>
<br />

<h2 id="rest-api">REST API</h2>
<h3 id="api">API</h3>
<p>프로그램들을 위한 인터페이스가 API이다. 
프로그램들이 상호작용하는 것을 도와주는 매개이다.
코드를 작성하는 방법을 표준화</p>
<h3 id="rest-api-1">REST API</h3>
<p>REST의 특징을 기반으로 서비스 API를 구현한 것이다. 
각 요청이 어떤 동작이나 정보를 위한 것인지를 요청 그 자체로 추론이 가능하다.</p>
<p><strong>REST API의 규칙</strong></p>
<h4 id="1-url는-특정한-자원의-위치를-나타낸다">1. URL는 특정한 자원의 위치를 나타낸다.</h4>
<ul>
<li><p>동사보다는 명사!</p>
</li>
<li><p>대문자보다는 소문자!</p>
</li>
<li><p>일반적으로 복수 명사!</p>
</li>
<li><p>❌ /getUser, /deleteBook</p>
</li>
<li><p>✅ /users, /books</p>
</li>
</ul>
<p>데이터가 모여있는 곳으로 컬렉션은 복수를 의미한다. </p>
<h4 id="2-고유한-객체를-가지고-올-때는-리소스-옆에-path-상에-id를-나타낸다">2. 고유한 객체를 가지고 올 때는 리소스 옆에 path 상에 id를 나타낸다.</h4>
<ul>
<li>컬렉션의 값들 중에서 하나의 객체를 가져올 때</li>
<li>✅ /books/123 → ID가 123인 책 정보</li>
</ul>
<h4 id="3-마지막에-슬래시를-포함하지-않는다">3. 마지막에 슬래시를 포함하지 않는다.</h4>
<ul>
<li>✅ /books</li>
<li>❌ /books/</li>
</ul>
<h4 id="4-단어-구분은-언더바-대신에-하이픈-을-사용한다">4. 단어 구분은 언더바 대신에 하이픈(-)을 사용한다.</h4>
<ul>
<li>✅ /user-profile</li>
<li>❌ /user_profile</li>
</ul>
<h4 id="5-조인된-결과를-url상에서-나타낼-때는-계층적인-구조에서-명확하게-표현해야-한다">5. 조인된 결과를 URL상에서 나타낼 때는 계층적인 구조에서 명확하게 표현해야 한다.</h4>
<ul>
<li>컬렉션/단수/컬렉션</li>
<li>고유한 값이 리소스 뒤에 나와야 한다.</li>
<li>✅ /users/123/books → 사용자 123이 등록한 책 목록</li>
</ul>
<h4 id="6-url에-파일-확장자를-포함하지-않는다">6. URL에 파일 확장자를 포함하지 않는다.</h4>
<ul>
<li>❌ /users.json, /books.xml</li>
<li>✅ /users, /books</li>
</ul>
<h4 id="7-span-stylecolor-red행위동사를-포함하지-않는다span-url이-아닌-http-메소드를-통해서-나타낸다">7. <span style="color: red;"><strong>행위(동사)를 포함하지 않는다.</strong></span> URL이 아닌 HTTP 메소드를 통해서 나타낸다.</h4>
<ul>
<li>✅ GET /books → 도서 목록 조회</li>
<li>✅ POST /books → 도서 등록</li>
<li>✅ PUT /books/1 → ID 1 도서 수정</li>
<li>✅ DELETE /books/1 → ID 1 도서 삭제</li>
</ul>
<h2 id="rest-api-동작">REST API 동작</h2>
<p>REST API는 <strong>서버가 클라이언트의 요청에 대한 응답으로 화면(view)가 아닌 데이터(data)</strong>를 전송한다.
응답 데이터는 <strong>JSON, XML</strong>이 있다.</p>
<p><strong>JSON (JavaScript Object Notation)</strong>
JSON은 객체를 JS로 표현하기 위한 표기법으로 데이터를 쉽게 교환하고 저장하기 위한 텍스트 기반의 데이터 교환 표준이다. </p>
<ul>
<li>객체는 {} 중괄호로 표현한다. </li>
<li>배열은 [] 대괄호로 표현한다. 배열에 여러 객체들을 넣어서 표현할 수 있다.</li>
</ul>
<p>요청/응답 과정
CSR으로 client의 브라우저에 구멍을 내서 해당 위치에 데이터를 넣는다. 
하지만 데이터가 다른곳에서 가져오게 된 오염된 데이터일 경우에는 문제가 생김!
브라우저의 정보를 그대로 배껴서 데이터의 도움을 안받고 배길 수 있음.
페이지의 Ajax로 가져오게 되면 CORS 
데이터를 주는 서버와 --서버가 origin이 다르면 보안상 막아주는 ..?
단순히 데이터를 요청하고 응답하는 것에는 문제없이 가능하다. </p>
<h3 id="클라이언트---서버--요청-http-requset">클라이언트 -&gt; 서버 : 요청 HTTP requset</h3>
<p>클라이언트는 서버에게 요청을 보낼 때, 다음과 같은 3가지 주요 구성 요소로 HTTP 요청 메시지를 구성한다.</p>
<p><strong>요청라인</strong></p>
<blockquote>
<p><code>HTTP 메서드 + URL + HTTP 버전</code>
HTTP 메서드는 자원에 대해 어떤 동작을 수행할지 나타낸다.</p>
</blockquote>
<ul>
<li>GET  : 자원 조회 (본문 없음)</li>
<li>POST : 자원 생성 (본문 포함)</li>
<li>PUT  : 자원 전체 수정 (본문 포함)</li>
<li>PATCH : 자원 일부 수정 (본문 포함)</li>
<li>DELETE: 자원 삭제 (본문 없음)</li>
</ul>
<p><strong>헤더</strong></p>
<blockquote>
<p>요청에 대한 부가 정보를 담는 부분</p>
</blockquote>
<ul>
<li>HOST: 내가 누구인가</li>
<li>User-agent: 클라이언트의 정보를 준다.</li>
<li>Authorization: 인증 토큰을 서버로 보낼 때 사용한다. 사전에 token을 받아서 헤더에 계속 넣어준다.</li>
<li>Cookie : 쿠키 값이 key-value값으로 표현된다.</li>
</ul>
<p><strong>본문</strong></p>
<blockquote>
<p>클라이언트가 서버에게 전달하고자 하는 데이터
데이터를 클라이언트가 들고 있고 서버쪽에게 데이터를 넘겨줘야 한다. </p>
</blockquote>
<table>
<thead>
<tr>
<th>메서드</th>
<th>본문 사용 여부</th>
<th>용도</th>
</tr>
</thead>
<tbody><tr>
<td><code>GET</code> / <code>DELETE</code></td>
<td>❌ 없음</td>
<td>자원 조회 / 삭제 요청만 전달</td>
</tr>
<tr>
<td><code>POST</code> / <code>PUT</code> / <code>PATCH</code></td>
<td>✅ 있음</td>
<td>새로운 데이터 전달, 수정 요청 시 데이터 포함</td>
</tr>
</tbody></table>
<h3 id="서버---클라이언트--응답-http-response">서버 -&gt; 클라이언트 : 응답 HTTP Response</h3>
<p>서버가 클라이언트에게 응답을 보낼 때, 다음과 같은 3가지 주요 구성 요소로 HTTP 응답 메시지를 구성한다.</p>
<p><strong>상태라인</strong></p>
<blockquote>
<p><code>HTTP/1.1 [상태 코드] [상태 메시지]</code>
응답 메시지의 첫줄로, 요청에 대한 처리 결과를 나타낸다. </p>
</blockquote>
<ul>
<li>200 =&gt; &quot;OK&quot;</li>
<li>404 =&gt; &quot;Not Found&quot;<pre><code>HTTP/1.1 200 OK
HTTP/1.1 404 Not Found
HTTP/1.1 500 Internal Server Error
</code></pre></li>
</ul>
<pre><code>
**헤더**
&gt; 응답에 대한 부가 정보를 포함한다. 

| 헤더 항목                         | 설명                                                 |
| ----------------------------- | -------------------------------------------------- |
| `Content-Type`                | 응답 본문의 데이터 형식 (예: `application/json`, `text/html`) |
| `Set-Cookie`                  | 클라이언트에 저장할 쿠키 데이터 전송                               |
| `Cache-Control`               | 캐시 저장 관련 정보                                        |
| `Access-Control-Allow-Origin` | CORS 정책 허용 출처 설정                                   |


**본문**
&gt; 클라이언트에게 전달하고자 하는 실제 데이터를 담는다. 

response 응답의 본문이 비어잇는 경우는 
POST에서는 있을 수도 있고, 없을 수도 있다. 로그인이 잘 되어서 정보를 다시 주는 경우
저장된 정보를 클라이언트에게 다시 주는 경우는 POST로 뉴스를 담았을 때 response에 담아주지 않으면 클라이언트가 뉴스의 번호를 알 수 없어서 다시 넘겨주면 좋음

✅ 본문이 있는 경우
클라이언트가 요청한 데이터를 전달해야 할 때

- 예: 로그인 성공 후 사용자 정보나 토큰을 반환할 때
- 예: 새로운 글을 등록한 후, 저장된 글의 ID 또는 전체 정보를 다시 돌려줄 때

클라이언트가 ```news_id``` 와 같은 고유값을 알아야 이후에 상세 조회나 수정 등 추가 작업을 할 수 있다.

❌ 본문이 없는 경우
처리 결과만 알려주면 되는 경우
- 예: 단순한 삭제 요청 (DELETE /news/17)

또는 저장은 했지만, 클라이언트가 추가 정보가 필요 없는 경우

이럴 땐 상태 코드만으로 충분하고, 본문은 비워둘 수 있습니다.
- 204 No Content 상태 코드도 주로 이럴 때 사용합니다.


## REST API 어노테이션
@Entity : 해당 클래스가 엔티티임을 나타낸다.
@Data : geeter, setter, equals, hashcode, tostring 등 메소드를 자동으로 생성
@Id : DB 테이블의 기본키
@Column : DB 에티블의 열
    - nullable = false : null값을 허용하지 않음
    - 비워두면 안되는 필드
@Enumerated : 열거형 타입

## RestController
&gt;@RestController는 @Controller + @ResponseBody를 합친 어노테이션으로, 
웹 요청을 받는 Spring MVC의 Controller이고 리턴되는 값은 View가 아닌 JSON 데이터로 자동 변환되어 응답한다.

컨트롤러가 모델을 가져와서 잘 만든 후에 view의 이름 (string) 을 리턴한다. 
rest컨트롤러는 view의 힘을 빌리지 않고 body를 다 채워서 리턴한다. 컨트롤러가 온전히 다 한다.
mvc 패턴은 view가 json형태로 바뀐 것이다. 
@GetMapping 
함수에 리턴에 해당하는 객체가 body에 채워진다.

DB 연동을 위해서 repository를 사용하려면 DB 컨트롤러 객체인 repository를 사용한다. repository 구현체를 DI로 의존성 주입을 받는다. 

필드주입 : @Autowired
private BookRepository bookRepository;

생성자주입 : 

## Repository
SELECT : findAll(), findById(), findBy필드명()
INSERT : save(entity), saveAll
DELETE : delete(entity), deleteById(ID id), deleteAll()


## DTO
&gt; 계층 간 데이터 교환을 하기 위해 사용하는 객체
로직을 갖지 않는 순수한 데이터 객체로 getter/ setter만 가진 클래스

클라이언트에서 서버 쪽으로 전송하는 요청 데이터를 전달 받을 때,
서버에서 클라이언트 쪽으로 전송하는 응답 데이터를 전송할 때,

보여지면 안되는 필드 데이터가 담겨있는 경우
DB의 구조가 바뀌어서 URL의 데이터가 바뀌는 경우
=&gt; 도메인 객체를 그대로 컨트롤러에 사용하면 좋지 않다.
=&gt; **통신을 위해서** 사용하는 별도의 클래스인 DTO를 사용한다.
=&gt; 도메인 객체와 통신을 위한 객체를 분리한다.

id를 제외하고 상대편에서 주고 받는 필드의 모양을 작성한다.
함수에 static을 붙여주면 new로 생성하지 않아도 사용이 가능하다.


**DTO 클래스**는 HTTP 메서드를 직접 구현하는 것이 아니라, 각 HTTP 요청/응답의 **데이터 구조**만을 분리해서 정의하는 방식</code></pre><p>public class BookDTO {
    public static class Post {
        private String title;
        private String author;
        // ... 요청에 필요한 데이터
    }</p>
<pre><code>public static class Put {
    private String title;
    private String author;
    private Book.Status status;
}

public static class Response {
    private String title;
    private String author;
    private Book.Status status;
}</code></pre><p>}</p>
<pre><code>

BookDTO.Post, BookDTO.Put 등으로 **데이터만 전달** 하면서 controller에서 사용자 요청에 대한 작업을 수행한다.

**Controller에서는 DTO를 매개변수 또는 반환값으로 사용**

- 화면에 필요한 데이터를 선별한다.
- 순환 참조를 예방한다.
- DTO에서 validation이 가능하다.(잘못된 값을 전달받았을 때 걸러낼 수 있다.)
- DTO만 사용하면 DB와의 연동은 불가능하다.

## Mapper
Mapper 없이도 DTO만 사용하는 것은 가능하다!

하지만 DTO는 DB에 직접 저장할 수 없기 때문에,
→ 반드시 DTO 데이터를 기반으로 Entity 객체를 새로 만들어서 저장해야 한다.

Entity로의 변환 작업이 반복되거나 복잡해지면 Mapper를 사용하는 것이 효율적이다.

&gt;Mapper는 DTO ↔ Entity 간의 변환 로직을 담당하는 클래스이다.
즉, DTO → Entity 또는 Entity → DTO로 바꿔주는 작업을 Controller나 Service에서 따로 하지 않고,
하나의 Mapper 클래스에 모아서 명확하게 분리한다.

수동 mapper와 자동 mapper를 통해서 구현한다. 
- 수동 mapper는 개발자가 변환 메서드를 직접 구현한다. 
- 자동 mapper는 mapstruct로 어노테이션 기반 인터페이스 작성 → 구현은 자동 생성

## Service

&gt; Service 레이어 단이 없는 것은 conotroller -&gt; repository(DB) 로 접근하는 것과 같다.
화면단(프리젠테이션 계층)이 DB 계층과 직접 연결되어 있어 설계 원칙인 계층 분리를 깨뜨린다.
그럼으로 Controller → Service → Repository(DB) 의 흐름을 지켜야한다. 

controller는 요청과 응답의 입출력 처리하는 부분이다.
controller는 service를 호출하는 부분이다. 
service는 요청에 대한 실질적인 작업(로직) 수행

&gt;- 📮 Controller = 프론트 데스크 (접수창구)
고객의 요청을 받아서 → 처리부서에 넘기고 → 결과를 받아 다시 전달
- 🛠 Service = 실무 담당 부서
실제로 로직을 처리하고, 필요한 데이터를 가공해서 반환

### Service의 특징 및 구조
- Controller는 사용자의 **요청(Request)**을 받고, 서비스에게 작업을 시키고, 그 **결과(Response)**를 사용자에게 응답하는 입출구(인터페이스) 역할

- Service는 실제 **작업(비즈니스 로직)**을 처리하고, data access layer와의 상호작용을 수행하는 핵심 처리 계층
repository를 생성자 주입으로 DI 필요!!!!

=&gt; Controller와 Service는 &quot;구현하고자 하는 기능&quot;은 같을 수 있지만, 각 계층은 그 기능을 구현하는 &quot;책임과 역할&quot;이 다르기 때문에 분리

### 주요 어노테이션
- @Transactional 은 함수를 하나의 트랙잭션으로 묶어서, 중간에 문제가 생기면 전부 롤백한다. 

- @Service 는 비즈니스 로직을 처리하는 서비스 클래스에 적용되며, 해당 클래스는 스프링 빈(bean) 으로 등록하는 역할을 한다. 



### Service 작성 팁
- service는** repository를 반드시** 가져오고, mapper를 가져올 수도 있다. 
- data access layer와의 상호작용을 담당하기에 **repository를 생성자 주입으로 DI** 해주어야 한다. 
- controller에서 service를 Autowird해주어야 한다. 
private final로 service(인터페이스)를 놓고 DI(의존성 주입) 한다. + @RequiredArgsConstructor
- DI 주입 방법
    - private final로 놓고, 생성자 주입한다.  
    - 또는 private final만 쓰고 @RequireArgsConstuctor 로 자동 주입을 해줄 수 있다.
    - 또는 @Autowird를 해줄 수 있다.

- service는 **순수 POJO**로 만드는 것을 선호한다. 
- 내부의 함수명은 서비스 행위와 연관 지어서 작성해야한다.
- **service의 스펙**을 **인터페이스**로 미리 정의을 하고, **serviceimpl**로 해당 비즈니스 로직을 **클래스** 내부에 작성한다. 
ctrl + i 를 통해서 인터페이스로 정의한 부분을 클래스에서 불러올 수 있다. </code></pre><p>/service/BookService
public interface Service{ // CRUD의 함수를 선언한다.
}</p>
<p>/service/BookServiceImpl
public class BookServiceImpl implements Service{ // CRUD의 함수 로직을 작성한다.
}</p>
<pre><code>
&gt;- service layer는 MCV 패턴에서 model로 볼 수 있다. 
- model안에 domain 객체도 들어가고, 도메인 객체를 컨트롤하는 service로 포함된다. 


### Repository 기본 메서드 
보통 INSERT 시에서는 ID가 필요하지 않음
Repository의 save() : 저장 또는 수정
Repository의 findeById() : 단건 조회
Repository의 findAll() : 전체 조회
Repository의 delete() : 삭제

---


## 계층 정리
**Model**은 시스템의 데이터 + 로직 임으로 **Domain + Service** 가 된다.
Controller → Presentation Layer (프리젠테이션 계층)
Repository → Data Access Layer (데이터 접근 계층)
Service → Business Logic Layer (비즈니스 로직 계층) (무엇을 할지)
Domain은 데이터의 핵심 데이터 구조
DTO는 controller와 service의 통신 사이에서의 데이터 구조(무엇을 주고 받을지)
Mapper는 DTO와 entity 간의 변환(선택사항) (수동or MapStruct자동)

---

## 계층별 책임 역할
✅ Controller는 HTTP 요청 메서드(GET, POST 등)에 따라
요청을 처리하고 응답을 반환하는 입출력(인터페이스) 역할을 담당합니다.
즉, 어떤 요청이 들어왔을 때 어떤 기능을 호출할지만 정의합니다.

✅ 실제로 요청을 처리하는 핵심 로직(CRUD 수행)은 Service 계층에서 수행됩니다.
예: save(), findAll(), delete() 등 비즈니스 로직 포함

✅ Repository는 DB에 접근하는 계층이며,
Service에서 호출하는 CRUD 메서드를 기반으로
Spring Data JPA가 적절한 SQL을 자동 생성하거나 실행하여
DB에서 데이터를 저장하고 불러오는 작업을 수행합니다

---
## 전체 구현 순서
1. domain 폴더에 entity 클래스를 만든다. 
 DB 구조이자 비즈니스 핵심 모델
2. repository 폴더에 repository 를 만든다. 
interface 생성하고 JpaRepository&lt;Entity, ID&gt; 상속
3. service 폴더에 service 를 만든다. 
서비스 클래스를 생성해서 비즈니스 로직을 구현
4. dto 폴더에 DTO 를 만든다. 
REST API의 HTTP 메서드 요청/응답에 대한 데이터구조만 정의하는 곳
5. controller 폴더에 controller 를 만든다. 
사용자의 요청 HTTP를 받아서 service 호출, 응답 반환


</code></pre>
