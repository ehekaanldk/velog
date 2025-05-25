---
title: "[Spring] POJO"
date: "2025-05-24"
link: "https://velog.io/@ehekaanldk/Spring-POJO"
series: "Uncategorized"
---

<p>스프링에서의 POJO는 스프링프레임워크의 근간의 기본이 되는 개념이다. </p>
<h2 id="pojo">POJO</h2>
<p>특별한 규칙이나 상속 없이 만든 평범한 자바 객체</p>
<p>인터페이스나 클래스의 상속을 받지 않고, 단순히 필드와 메서드만 갖는 객체</p>
<pre><code>public class Member {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}</code></pre><ul>
<li>개발자가 특정 API에 종속되지 않게 해준다.</li>
<li>비즈니스 로직에 집중할 수 있게 해준다. </li>
</ul>
<h2 id="pojo와-iocdi">POJO와 IoC/DI</h2>
<p><strong>IoC</strong>는 제어의 역전으로 개발자가 했던 객체 생성을 스프링 컨테이너에게 맡긴다. </p>
<p><strong>DI</strong>는 의존성 주입으로 객체 간의 의존 관계를 개발자가 직접 연결했었던 것을 스프링이 주입해준다.</p>
<table>
<thead>
<tr>
<th>개념</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>IoC (Inversion of Control)</td>
<td>객체 생성/관리를 개발자가 아닌 스프링 컨테이너에게 맡김</td>
</tr>
<tr>
<td>DI (Dependency Injection)</td>
<td>객체 간 의존 관계를 직접 연결하지 않고 스프링이 주입해줌</td>
</tr>
</tbody></table>
<ul>
<li>POJO 기반의 클래스 구성으로 프레임워크 코드와 분리된다.</li>
<li>스프링이 내부에서 객체를 만들고 주입하기 쉽다.</li>
</ul>
<pre><code>@Component
public class OrderService {
    private final PaymentService paymentService;

    public OrderService(PaymentService paymentService) {
        this.paymentService = paymentService; // DI를 통한 주입
    }
}</code></pre><h2 id="pojo와-aop">POJO와 AOP</h2>
<p>AOP는 로깅, 트랜잭션, 보안 등의 공통 기능을 POJO에 끼워넣을 수 있도록 한다. </p>
<ul>
<li>POJO 클래스에 @Transactional 과 @LogExecutionTime 같은 어노테이션을 붙이기만 하면된다.</li>
<li>AOP는 대리객체를 이용해서 POJO 기능을 확장한다.</li>
</ul>
<pre><code>@Service
public class MemberService {
    @Transactional
    public void joinMember(Member m) { ... } // 트랜잭션이 자동 처리됨
}
</code></pre><h2 id="pojo와-psa">POJO와 PSA</h2>
<p>PSA는 '멀티 어댑터' 와 같이 개발자는 콘센트의 모양에 신경을 쓰지 않아도, 스프링에서 일관된 방식으로 서비스를 사용하게 해주는 것이다.</p>
<ul>
<li>데이터베이스 연동(JDBC)<ul>
<li>원래는 데이터베이스마다 드라이버, 연결 방식, 예외 처리 등이 다 다르다.</li>
<li>스프링에서는 <code>JdbvTemplate</code> 이라는 PSA를 통해서 코드를 단순화하고 표준화<pre><code>@Autowired
private JdbcTemplate jdbcTemplate;
</code></pre></li>
</ul>
</li>
</ul>
<p>public List findAll() {
    return jdbcTemplate.query(&quot;SELECT * FROM members&quot;, new MemberRowMapper());
}</p>
<pre><code>
- 트랜잭션 처리
    - 여러 벤더(Oracle, MySQL, JPA 구현체 등)에 따라서 트랜잭션 처리 방식이 다르다.
    - 스프링은 ```@Transactional``` 으로 추상화 해준다.</code></pre><p>@Transactional
public void join(Member m) {
    memberRepository.save(m);
}</p>
<pre><code>
PSA 덕분에 개발자는 POJO 형태의 코드만 작성하면 된다. 스프링이 그 위에 기술 적응 레이어를 붙여준다.


---

## SOLID
spring 프레임워크는 객체 지향 설계의 핵심 원칙인 SOLID 원칙을 매우 잘 반영한다.

### 1. SRP
단일 책임 원칙으로 하나의 클래스에는 하나의 책임만 가져야 한다. 

- 하나의 pay 클래스에 pay 메소드와 order 메소드가 필드로 가진다.
- pay 메서드 로직이 변하면 order 메서드도 변경 가능성이 있다. 
- 하나의 pay 클래스와 하나의 order 클래스로 나누어 구현한다.

spring은 Controller - Service - Repository 구초로 단일 책임 원칙을 실현한다. 

- @Controller : 요청 처리
- @Service : 비즈니스 로직
- @Repository : DB 접근

### 2. OCP
개방 폐쇠 원칙으로 확장을 열려있고, 변경은 닫혀있어야 한다. 

자주 변화하는 부분은 추상화(interface)하고, 상속을 통해서 확장한다. 

spring의 의존성 주입으로 OCP를 쉽게 실현한다.
새 정책을 추가 시 기존 코드를 수정할 필요없이 구현체만 추가한다. 


### 3. LSP
리스코프 치환 원칙으로 상위타입을 하위타입으로 교체해도 프로그램이 정상 동작한다.

상속을 하면 하위타입이 상위타입의 특성을 가지고 확장한다.

- Rectangle 부모 클래스에서 너비와 높이를 독립적으로 설정
- Square 자식 클래스에서 너비와 높이를 항상 같게 override 하여 정의
=&gt; 자식이 부모를 대신할 수 없음 (ISP 위반)

spring에서는 @Autowired 를 통해 인터페이스 타입으로 주입 시, 어떤 구현체를 넣어도 문제가 없어야 한다. 

### 4. ISP
인터페이스 분리 원칙으로 인터페이스를 잘게 잘라서 목적과 용도에 적합한 인터페이스를 제공한다.

클래스가 사용하지 않는 함수여도 인터페이스 내 함수는 억지라도 구현해야한다. 

spring에서는 Spring Data JPA 의 Repository 설계에서 확인이 가능하다.


### 5. DIP
의존관계 역전 원칙으로 사용자가 상속관계로 이루어진무튤을 가져올 때,
하위모듈의 인터페이스를 직접 사용하지 않고, 상위 인터페이스 타입의 객체를 사용해야 한다.

- 고수준의 모듈인 Huni 클래스, 저수준의 모듈인 Galaxy, Ipad 클래스, 추상화의 Tablet 인터페이스

- Huni 클래스에서 Galaxy 클래스를 필드로 가져와 의존한다. =&gt; Ipad를 바꾸려면 고수준 필드를 수정해야한다.

- Huni 클래스에서 Tablet 인터페이스를 필드로 가져와 의존하면, 고수준의 필드를 변경 안해도 된다.

spring에서는 핵심이 IoC가 의존관계 역전 원칙을 구현한다.


### spring에서의 SOLID
| 원칙 (SOLID)                    | 의미                                   | Spring에서의 적용 방식                                     | 적용 예시                                                      |
| ----------------------------- | ------------------------------------ | --------------------------------------------------- | ---------------------------------------------------------- |
| **S**&lt;br&gt;SRP&lt;br&gt;(단일 책임 원칙)    | 클래스는 하나의 책임만 가져야 한다                  | Controller, Service, Repository를 나누어 각 계층에 단일 책임 부여 | `@Controller`, `@Service`, `@Repository` 분리                |
| **O**&lt;br&gt;OCP&lt;br&gt;(개방-폐쇄 원칙)    | 확장에는 열려 있고 변경에는 닫혀 있어야 한다            | 인터페이스 기반 설계 + DI를 통해 새로운 구현체 추가 가능                  | `PaymentService` 인터페이스와 여러 구현체 등록                          |
| **L**&lt;br&gt;LSP&lt;br&gt;(리스코프 치환 원칙)  | 자식 클래스는 부모 클래스를 대체할 수 있어야 한다         | 인터페이스를 구현한 모든 클래스는 동일한 계약(contract)을 지켜야 함          | `JpaRepository` 구현체들은 동일한 방식으로 동작                          |
| **I**&lt;br&gt;ISP&lt;br&gt;(인터페이스 분리 원칙) | 불필요한 의존성을 피하기 위해 인터페이스는 작게 나눠야 한다    | 필요한 기능만 갖는 인터페이스로 분리                                | `CrudRepository`, `PagingAndSortingRepository` 등 기능별 인터페이스 |
| **D**&lt;br&gt;DIP&lt;br&gt;(의존 역전 원칙)    | 고수준 모듈이 저수준 모듈에 의존하지 않고, 추상화에 의존해야 함 | 인터페이스를 의존하고, Spring의 DI로 구현체를 주입받음                  | `@Autowired` 또는 생성자 주입을 통해 인터페이스 타입으로 주입                   |</code></pre>
