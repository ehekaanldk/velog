---
title: "[MSA] Event pub/sub"
date: "2025-06-11"
link: "https://velog.io/@ehekaanldk/MSA-Event-pubsub"
series: "Uncategorized"
---

<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/e7eb081c-1b67-4add-a1ce-423f7b98899d/image.png" /></p>
<h1 id="이벤트-publish--subscribe">이벤트 publish &amp; subscribe</h1>
<p>현재 실습은 인벤토리가 없는데도 일단 주문을 받는다. 있는지 없는지 어쩌구는 나중에 할 일이 된다.
(원래는 인벤토리에 재고량을 stock=10 이렇게 넣고 시작했는데-&gt; 현재는 그냥 product를 여러개 먼저 order를 보낼 수 있다.) </p>
<blockquote>
<p>목표</p>
</blockquote>
<ul>
<li>인벤토리 확인 없이 주문(Order)을 Producer가 보내고,</li>
<li>Kafka를 통해 Consumer가 그 주문 이벤트를 수신,</li>
<li>Consumer가 수신한 메시지를 확인하는 것</li>
</ul>
<ol>
<li><p>producer(order)는 뒤에 상황은 모르겠고, 주문을 일단 보낸다. 
터미널1 : 8082 점유 Order</p>
<pre><code>cd order
mvn spring-boot:run</code></pre><p>터미널2 : http 주문보냄</p>
<pre><code>http POST :8082/orders productId=1 qty=3 customerId=hong productName=TV</code></pre></li>
<li><p>새터미널 추가, kafka를 켜서
터미널3 : kafka</p>
<pre><code>cd kafka
docker-compose exec -it kafka /bin/bash
cd /bin</code></pre></li>
<li><p>consumer를 연결해서 주문이 잘 왔는지 확인한다. 
터미널3</p>
<pre><code>./kafka-console-consumer --bootstrap-server localhost:9092 --topic labshoppubsub  --from-beginning</code></pre></li>
</ol>
<ul>
<li>주문 이벤트 확인 가능
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/1b5cf768-29b6-454f-b7a7-9214c7d79985/image.png" /></li>
</ul>
<hr />
<p>domain (비즈니스 로직을 담당하는 곳)</p>
<ul>
<li>Entity : aggregate에 넣은 값들</li>
<li>event 로 식별한 것들 (DTO)(POJO)</li>
<li>repository : entity와 한몸임</li>
</ul>
<p>제외하고는 전부 infra에 위치한다 
inbound, outbound는 infra에 위치</p>
<p>@RepositoryRestResource 를 통해서 Order라는 spring resourse를 Rest 로 변경한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/1ea7725c-2ff0-4111-8b5a-7e05acbe8e9a/image.png" />
덕분에 http :8082/orders 처럼 orders를 controller로 주지 않아도 resoure를 rest의 path로 변경되어 들어간다. 
infra의 controller 부분에 동시에 추가하면 controller가 우선순위가 높다. </p>
<hr />
<h2 id="이벤트를-kafka로-publish하는-흐름">이벤트를 kafka로 publish하는 흐름</h2>
<p>하나의 주문(Order)을 생성할 때 kafka로 이벤트가 발행되는 객체의 흐름이다. </p>
<h3 id="1-order-객체가-db에-저장된다">1. Order 객체가 DB에 저장된다.</h3>
<pre><code>orderRepository.save(order);</code></pre><h3 id="2-postpersist-가-호출된다">2. @PostPersist 가 호출된다.</h3>
<pre><code>/Order.java
@PostPersist
public void onPostPersist() {
    OrderPlaced orderPlaced = new OrderPlaced(this); // 1. 이벤트 객체 초기화
    orderPlaced.publishAfterCommit();                // 2. 커밋 후 publish 예약
}</code></pre><ul>
<li>Order 엔티티를 기반으로 이벤트 객체를 생성한다</li>
<li>이벤트 객체 OrderPlaced 를 생성한다. </li>
<li>OrderPlaced는 AbstractEvent를 상속받은 클래스이다. </li>
</ul>
<h3 id="3-orderpalced-객체가-초기화된다">3. OrderPalced 객체가 초기화된다.</h3>
<pre><code>/AbstractEvent.java
public class AbstractEvent {

    String eventType;
    Long timestamp;

    public AbstractEvent(Object aggregate) {
        this();
        BeanUtils.copyProperties(aggregate, this);
    }

    public AbstractEvent() {
        this.setEventType(this.getClass().getSimpleName());
        this.timestamp = System.currentTimeMillis();
    }</code></pre><p>이벤트 객체의 초기화 단계를 정의한 부분이다. </p>
<ul>
<li>eventType: 이벤트의 종류를 구분할 수 있는 이름 (예: OrderPlaced)</li>
<li>timestamp: 이벤트가 생성된 시각 (Unix Time, 밀리초)</li>
<li>Order의 필드를 복사해서 이벤트 객체 안에 데이터를 담는다.</li>
</ul>
<h3 id="4-publishaftercommit-이-호출된다">4. publishAfterCommit() 이 호출된다.</h3>
<pre><code>/AbstractEvent.java
    public void publishAfterCommit() {
        TransactionSynchronizationManager.registerSynchronization(
            new TransactionSynchronizationAdapter() {
                @Override
                public void afterCompletion(int status) {
                    AbstractEvent.this.publish();
                }
            }
        );
    }
</code></pre><ul>
<li>바로 kafka에 이벤트를 보내는 것이 아니라, 트랙잭션 커밋 후 실행해달라고 spring에게 예약한다. </li>
<li>spring의 <code>TransactionSynchronizationAdapter</code>가 내부적으로 이 요청을 기억한다. </li>
<li>트랜잭션 커밋 이후에 이벤트를 안전하게 발행하는 코드</li>
</ul>
<h3 id="5-트랜잭션이-커밋된다">5. 트랜잭션이 커밋된다.</h3>
<ul>
<li>DB에 주문 정보가 완전히 저장되며, spring의 트랜잭션이 커밋된다. </li>
<li>커밋 직후, 위에서 예약한 afterCompletion() 메서드가 실행된다.</li>
</ul>
<h3 id="6-publish-가-호출되고-kafka로-이벤트-전송">6. publish() 가 호출되고 kafka로 이벤트 전송</h3>
<pre><code>
    public void publish() {
        /**
         * spring streams 방식
         */
        KafkaProcessor processor = OrderApplication.applicationContext.getBean(
            KafkaProcessor.class
        );
        MessageChannel outputChannel = processor.outboundTopic();

        outputChannel.send(
            MessageBuilder
                .withPayload(this)
                .setHeader(
                    MessageHeaders.CONTENT_TYPE,
                    MimeTypeUtils.APPLICATION_JSON
                )
                .setHeader(&quot;type&quot;, getEventType())
                .build()
        );
    }</code></pre><p>🔵여기부터 다시 보기</p>
<ul>
<li><p>Spring에서 미리 Bean으로 등록된 KafkaProcessor를 받아옵니다.</p>
</li>
<li><p>outboundTopic() 채널을 통해 Kafka에 메시지를 전송합니다.</p>
</li>
<li><p>이때 Kafka로 전송되는 메시지는 JSON 형태입니다.</p>
<p>왜 이렇게 구성하는가?</p>
<table>
<thead>
<tr>
<th>이유</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>DB 트랜잭션 성공 후에만 Kafka에 이벤트를 보내기 위해</strong></td>
<td>만약 DB가 실패했는데 Kafka 이벤트가 먼저 나가면 시스템 간 <strong>데이터 불일치</strong> 문제가 발생합니다.</td>
</tr>
<tr>
<td><strong>Spring이 만든 Bean(KafkaProcessor)을 쓰기 위해</strong></td>
<td>Kafka 채널은 Spring Cloud Stream이 자동으로 구성해 주므로, new 하지 않고 <code>getBean()</code>으로 가져와야 함</td>
</tr>
</tbody></table>
</li>
</ul>
<hr />
<p>spring에서 계속 new해서 만들 수 없음. bean
kafka에서 사용할 수 있도록 spring에서 이미 만들어놓고 이거를 달라고한다....</p>
<pre><code>        KafkaProcessor processor = OrderApplication.applicationContext.getBean(
            KafkaProcessor.class
        );</code></pre><ul>
<li><p>KafkaProcessor는 Spring Cloud Stream에서 바인딩 인터페이스입니다.</p>
</li>
<li><p>이 객체는 Spring이 자동으로 Bean으로 등록해 주기 때문에 직접 new하지 않고, ApplicationContext에서 주입받는다.</p>
</li>
<li><p>직접 생성하지 않고 스프링이 만들어준 것을 주입받아서 사용한다. </p>
</li>
</ul>
<p>application.yml의 destination, brokers, group 설정으로 구성한다.
| 설정 위치                                               | 의미                              |
| --------------------------------------------------- | ------------------------------- |
| <code>spring.profiles.active</code>                            | 현재 실행중인 프로파일 (예: default)       |
| <code>spring.cloud.stream.bindings.eventOut.destination</code> | Kafka 토픽 이름 (producer용)         |
| <code>spring.cloud.stream.bindings.eventIn.destination</code>  | Kafka 토픽 이름 (consumer용)         |
| <code>spring.cloud.stream.bindings.eventIn.group</code>        | Kafka consumer group 설정         |
| <code>spring.cloud.stream.kafka.binder.brokers</code>          | Kafka 브로커 주소 (<code>localhost:9092</code>) |</p>
<p>코드 설명</p>
<pre><code>AbstractEvent.java
    public void publishAfterCommit() {
        TransactionSynchronizationManager.registerSynchronization(
            new TransactionSynchronizationAdapter() {
                @Override
                public void afterCompletion(int status) {
                    AbstractEvent.this.publish();
                }
            }
        );
    }
</code></pre><ul>
<li>트랜잭션 커밋 이후에 이벤트를 안전하게 발행하는 코드</li>
</ul>
<p>Inventory.java</p>
<pre><code>/PolicyHandler.java


</code></pre><h2 id="orderplaced-이벤트-수신--재고-감소-처리">OrderPlaced 이벤트 수신 &amp; 재고 감소 처리</h2>
<p>decrease stock 이란느 Policy를 어디서 관리하는지 알아야한다. 
트리거를 누가가지는가!! =&gt; kafka의 policyhandler</p>
<h3 id="1-kafka로부터-메시지를-수신consumer역할">1. kafka로부터 메시지를 수신(consumer역할)</h3>
<pre><code>/PolicyHandler.java
@StreamListener(
    value = KafkaProcessor.INPUT,
    condition = &quot;headers['type']=='OrderPlaced'&quot;
)
public void wheneverOrderPlaced_DecreaseStock(@Payload OrderPlaced orderPlaced) {
</code></pre><ul>
<li><p>KafkaProcessor.INPUT은 application.yml의 eventIn 토픽에 해당</p>
</li>
<li><p>headers['type']=='OrderPlaced'는 이벤트의 eventType 헤더를 기준으로 필터링</p>
<ul>
<li>즉, OrderPlaced 이벤트일 때만 이 리스너가 반응</li>
</ul>
</li>
<li><p>@Payload OrderPlaced orderPlaced는 Kafka에서 받은 JSON 메시지를 OrderPlaced 객체로 변환해줌</p>
</li>
</ul>
<p>orderplaced라는 이벤트를 쓰기 위해서 inven 안에소ㅗ는 orderplaced와 모양이 같은 객체 하나를 가져야 한다....
좋던 실던 이벤트의 값이 뭔지 알아야 하기 때문에 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d7ad51c0-769d-4899-b951-34fc19d90157/image.png" /></p>
<h3 id="2-이벤트-내부-데이터를-이용해서-inventory-처리">2. 이벤트 내부 데이터를 이용해서 Inventory 처리</h3>
<pre><code>Inventory.decreaseStock(event);</code></pre><ul>
<li>OrderPlaced 안에 있는 productId, qty 등의 값을 기반으로,</li>
<li>Inventory 클래스에 있는 decreaseStock() 메서드를 호출함</li>
<li>이것은 위임(delegate)으로 policyHandler는 이벤트를 받아서 Inventory에게 작업을 전가한 것</li>
</ul>
<h3 id="3-inventory에서-재고-차감-처리">3. Inventory에서 재고 차감 처리</h3>
<p>기존의 코드</p>
<pre><code>// Inventory/java
        /** Example 2:  finding and process**/

        repository().findById(orderPlaced.get???()).ifPresent(inventory-&gt;{

            inventory // do something
            repository().save(inventory);


         });
        /**/</code></pre><ul>
<li>??? 부분에 inventory에서 product에 접근할 때, </li>
<li>getProducetID() 로 productId를 Inventory 테이블에서 재고 정보를 찾는다. </li>
</ul>
<pre><code>/Inventory.java
public static void decreaseStock(OrderPlaced orderPlaced) {
    repository().findById(Long.valueOf(orderPlaced.getProductId())) // ① 상품 ID로 재고 조회
        .ifPresent(inventory -&gt; {
            inventory.setStock(                                   // ② 현재 재고에서 주문 수량 차감
                inventory.getStock() - orderPlaced.getQty()
            );
            repository().save(inventory);                         // ③ 재고 DB에 저장
        });
}</code></pre><ul>
<li>인벤토리 내부에서의 수행과정</li>
<li>현재 재고에서 stock찾고 -&gt; 주문한 stock를 빼고 -&gt; stock를 저장</li>
</ul>
<hr />
<h2 id="inventory-실행">inventory 실행</h2>
<p>Inventory 도 실행해준다. 
터미널4 : Inventory</p>
<pre><code>cd inventory
mvn spring-boot:run
</code></pre><ul>
<li>inventory는 PolicyHandler를 통해 Kafka 메시지를 자동으로 수신하고 처리</li>
</ul>
<p>--</p>
<h2 id="전체-이벤트-흐름">전체 이벤트 흐름</h2>
<pre><code>[터미널2] http POST /orders
         ↓
[터미널1] Order 서비스
         ↓ Kafka에 JSON 이벤트 발행 (topic: labshoppubsub)
         ↓
[터미널3] kafka-console-consumer (확인용)
         ↓
[터미널4] Inventory 서비스
         └── @StreamListener → decreaseStock() 실행
</code></pre><ul>
<li><p>Order와 Inventory는 서로 연결되지 않고, kafka만 각자 바라보고 있다. </p>
</li>
<li><p>각 마이크로서비스가 독립된 bounded context로 동작하며,
충돌 방지를 위해 application.yml에 서로 다른 포트를 지정한다.</p>
</li>
<li><p>배정된 값은 application.yml에 tool에서 써준것이다. </p>
</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/462cd7f2-20ce-421a-876a-11cbf71e5e26/image.png" /></p>
<p>domain 부터 본다. </p>
<p>entity, domain event, repository</p>
<p>order</p>
<p>delivery</p>
<p>stock</p>
<ul>
<li>kafka키기<pre><code>cd infra
docker-compose exec -it kafka /bin/bash
</code></pre></li>
</ul>
<p>cd /bin</p>
<p>./kafka-console-consumer --bootstrap-server localhost:9092 --topic &lt;&gt; --from-beginning</p>
<pre><code>
- order키기</code></pre><p>cd order
mvn spring-boot:run</p>
<pre><code></code></pre><p>//Order.java
    @PrePersist
    public void onPrePersist(){
        setStatus(&quot;ORDER PLACED&quot;);
    }</p>
<pre><code>- 영속화 상태 되기 전에 실행되는 @PrePersist를 통해서 setStatus로 해당값을 설정하고 나서 영속화하도록 한다. 
&lt;p align=&quot;center&quot;&gt;
  &lt;img src=&quot;https://velog.velcdn.com/images/ehekaanldk/post/0a109d8c-d999-412b-90a5-97114d292095/image.png&quot; width=&quot;45%&quot; /&gt;
  &lt;img src=&quot;https://velog.velcdn.com/images/ehekaanldk/post/545d4c63-6313-4400-bfa0-26ed2f91649f/image.png&quot; width=&quot;45%&quot; /&gt;
&lt;/p&gt;

- delivery 띄우기</code></pre><p>cd delivery
mvn spring-boot:run</p>
<pre><code>
#### start delivery 로직 구성(코딩)

delivery 서버 구성 요소 파악
start delivery policy 파악
start delivery 로직 구성(코딩)
delivery completed 이벤트 발행
</code></pre><pre><code>    /** Example 1:  new item **/
    Delivery delivery = new Delivery(); // delivery 객체를 만들어서
    delivery.setOrderId(orderPlaced.getId());
    delivery.setCustomId(orderPlaced.getCustomId());
    delivery.setItemId(orderPlaced.getItemId());
    delivery.setQty(orderPlaced.getQty());
    delivery.setAddress(orderPlaced.getAddress());
    delivery.setStatus(&quot;DELIVERY STARTED&quot;);
    repository().save(delivery); // 저장(영속상태)한다. (이걸로 충분한가? =&gt; 아마도 빈배송건이 된다.=&gt; 배송건을 담아줘야한다.)

    DeliveryCompleted deliveryCompleted = new DeliveryCompleted(delivery); // deliverycompleted 객체를 만들어서 이벤트를 발생한다.
    deliveryCompleted.publishAfterCommit();
    /**/</code></pre><pre><code>기본값으로는 배송건이 비어있게 됨으로 주문건에 배송건의 필드에 get, set 해줘야 한다. 



- 터미널 bash</code></pre><p>http :8082/orders customerId=&quot;hong&quot; itemId=1 qty=5 address=&quot;서울&quot;
http :8083/deliveries</p>
<pre><code>- 터미널 infra&gt;docker-compose
확인가능
![](https://velog.velcdn.com/images/ehekaanldk/post/413f6226-8eac-42bb-90ec-b0aa5aa006d3/image.png)

#### decrease stock 로직 구성
product 서버 띄우기
product 서버 구성 요소 파악
product stock policy 파악
product stock 로직 구성
stockDecreased 이벤트 발행

**product : 8084 점유**</code></pre><p>cd product
mvn spring-boot run</p>
<pre><code>
새 인벤토리를 만드는 부분은 생략한다. 
이 부분은 inventoryRepository.java에서 만들어준다.

**Inventory부분에 product stock 로직을 작성**</code></pre><p>/inventory.java
    public static void decreaseStock(DeliveryCompleted deliveryCompleted) {</p>
<pre><code> repository().findById(Long.valueOf(deliveryCompleted.getItemId())).ifPresent(inventory-&gt;{

        inventory.setStock(inventory.getStock() - deliveryCompleted.getQty()); // do something
        repository().save(inventory);

     });
}</code></pre><pre><code>
**stockedDecreased 이벤트를 발생**</code></pre><p>StockDecreased stockDecreased = new StockDecreased(inventory);
            stockDecreased.publishAfterCommit();</p>
<pre><code>
- 터미널 bash</code></pre><p>http :8084/inventories name=&quot;TV&quot; stock=10
http :8082/orders customerId=&quot;yun&quot; itemId=1 qty=5 address=&quot;경기도&quot;
http :8083/deliveries
http :8084/inventories</p>
<pre><code>
- 터미널 infra&gt;docker-compose
확인가능


## 정리
지금은 order와 delivery, inventory가 다 같은  Kafka topic을 바라본다.
모든 서비스가 이벤트를 broadcast로 수신하지만,
각 서비스는  @StreamListener + condition을 통해 자신이 원하는 이벤트(policy)만 골라 처리한다.



---

## 보상 트랜잭션(Compensating Transaction)
![](https://velog.velcdn.com/images/ehekaanldk/post/9cf252a2-91db-4d0d-9473-4fbfed775dbb/image.png)

stock decrease가 불가능한 경우에는 어떻게 하는가?
재고가 부족할 때 발생하는 실패 상황에 대해서, 이전 상태를 보상하고 정리해주는 흐름을 이벤트 기반으로 설계한다. 

하나의 DB일 때는 

**Inventory Bounded Context**
![](https://velog.velcdn.com/images/ehekaanldk/post/b1a48533-6acc-4591-900b-c7edfec0136f/image.png)
- 속성 동기화 후 Long 타입의 orderId를 추가한다.
- decrease stock이 발생하지 못하는 경우의 상태로 Outofstock이기에 연결해준다. 

**Order Bounded Context**
![](https://velog.velcdn.com/images/ehekaanldk/post/165efd32-cf27-43b5-a425-3994a9300bd9/image.png)
- update Status&quot;라는 Policy 스티커를 생성한다.


### Decrease stock 로직 구성
</code></pre><p>/inventory.java</p>
<pre><code>public static void decreaseStock(OrderPlaced orderPlaced) {

    /** Example 2:  finding and process**/


    // 재고량과 주문 수량을 비교해서 로직을 처리한다
    repository().findById(Long.valueOf(orderPlaced.getProductId())).ifPresent(inventory-&gt;{

        // do something
        if(inventory.getStock() - OrderPlaced.getStock() &lt;0) { // decrease 불가한 상황황
            // 인벤토리의 stock고치지 않아도 됨
            // outOfStock에서 id,stock은 잘가져오지만, orderId는 넣어줘야한다.
            OutofStock outofStock = new OutofStock(inventory); 
            outofStock.setOrderId(orderPlaced.getId()); //orderId는 넣어주는 부분분
            outofStock.publishAfterCommit();
        }
        else{ // 정상 decrease됨
            inventory.getStock(inventory.getStock() - OrderPlaced.getStock());
            repository().save(inventory);

            StockDecreased stockDecreased = new StockDecreased(inventory);
            stockDecreased.publishAfterCommit();
        }


     });
    /**/

}</code></pre><pre><code>
### Update status 로직 구성
재고없음에 따른 order팀의 policy를 작성한다. 
order의 status를 바꿔서 policy
</code></pre><p>/order.java</p>
<pre><code>public static void updateStatus(OutofStock outofStock){

    //implement business logic here:

    /** Example 1:  new item 
    Order order = new Order();
    repository().save(order);

    */

    /** Example 2:  finding and process


    repository().findById(outofStock.getOrderId()).ifPresent(order-&gt;{

        order.setstatus(&quot;ORDER CANCELLED&quot;); // do something
        repository().save(order);


     });
    */


}</code></pre><pre><code>- 만들어놓은 주문을 찾아야 update status로 주문의 상태를 변경할 수 있다. 
- OrderId를 outOfStock에 넣은 이유가 된다. 
- setStatus()로 상태를 변경해준다. 


추가적으로 OrderCancelled 이벤트부분에 
사용자가 cancel한건지
decrease로 cancel된건지 
나누어서 잘 작성해야 한다. 

![](https://velog.velcdn.com/images/ehekaanldk/post/404740e4-ad48-401b-888c-496f693f588f/image.png)


## 정리 
- controller에
- 영속화가 된 다음에 값 객체를 만들어서 this를 매개변수로 받아서 객체의 값을 카피 받아온다. 
- 이벤트로써 카피해서 초기화하는 기능, kafka 채널에게 이벤트를 보내는 기능
- 어떠한 이벤트도 상관없이 가지는 값 eventType, timeStep
- AbstratEvent 클래스로 이벤트의 기능이 구현되는 부분을 따로 작성한다. 
- policyhandler에서 시작한다. @StreamListener 는 whatever로 일단 다 받는다. 
보상 트랜잭션 처리
- decrease stock에서 stockdecreased 나 outofstock으로 간다. 
- outofstock은 order의 status를 주문 취소로 바꾸게 된다. 

- 이벤트를 만드는 쪽은 누가 가져가는지 신경쓰지 않아도 된다. 


## 중복실행 방지
![](https://velog.velcdn.com/images/ehekaanldk/post/a2f2773f-b153-4467-8058-7c7e7a53bcbb/image.png)

kafka는 데이터를 적어도 한번은 실행한다. 2번 줄 수 있다고 말한다. 
서버가 어디까지 실행되었는지, 어디까지 받았는지 알아야 한다. 

프로세스 처리 중에 실패를 하게 되면 reject에 따라 보상 처리가 이루어진다.
보상처리가 한번 이상 벌어져도, 같은 건에 대해서 또 취소가 되면 안된다. 

주문을 확정하지 않고 주문을 생성만 한다. (가주문상태 : OrderCreated)
배송 신청을 한다. (policy : start delivery)

배송 불가한 지역의 경우 DeliveryFailed 에서 reject된다. 
재고가 부족한 경우 StockDecreaseFailed 에서 reject된다. 

재고가 잘 줄어든 경우는 StockDecreased 에서 approve된다. 


### 중복 실행이 발생하는 경우
인프라 level에서 2번 
카프카에서 파티션의 수가 변하거나
카프카 내에서 리밸런싱이 발생하면, Offset이 처리되지 않은 파티션에 Consumer가 재할당 되어 메시지를 재수신하는 일이 벌어진다.
카프카는 큐의 형태이고, 한번만 보내준다!(한번만 보냈는지 확인하기 위해 추적! 느림!) vs 한번은 보낸준다! (카프카의 형태)
consumer group

트랜잭션이라는 entity를 만들어서(코드로) orderId와 stockOrderd 특정 주문 아이디를 검토하고 처리했다고 하면 이후에는 무시하도록 한다. 
한번 처리된 메시지는 중복처리 되지 않는다 - 멱등성 관리

### 실습
- product(8083)의 inventory에 2개의 상품 데이터를 넣는다. </code></pre><p>http :8083/inventories productName=TV stock=1000   # id=1
http :8083/inventories productName=RADIO stock=1000  # id=2</p>
<pre><code>- 주문(Order:8081)을 발행하고, 카프카 토픽과 상품 재고를 모니터링</code></pre><p>http :8081/orders customerId=1 productId=1 productName=TV qty=10</p>
<pre><code>pendding 상태가 된다. 
![](https://velog.velcdn.com/images/ehekaanldk/post/b2d1b77e-07e1-479b-bcf9-3332fe0a7beb/image.png)
주문이 잘 생성되고, 배달되고, 재고가 감소하고, orderplaced 가 생성됨
![](https://velog.velcdn.com/images/ehekaanldk/post/9af727dc-024b-49f3-9e77-d1fdd264e370/image.png)
- 재고량을 초과하는 상품번호로 주문을 발행하고, 모니터링</code></pre><p>http :8081/orders customerId=1 productId=2 productName=TV qty=200</p>
<pre><code>pendding 상태가 된다.
![](https://velog.velcdn.com/images/ehekaanldk/post/c8113a86-8559-4f02-970c-80d798779e1d/image.png)
주문이 잘 생성되고, 배달 시작되었지만 =&gt; 재고 감소가 실패 =&gt; reject된다.
![](https://velog.velcdn.com/images/ehekaanldk/post/12bf8927-fdc1-4a05-8f3a-f8808d05d5ba/image.png)
추가로 중복 실행되면서 fail이 되었는데 reject이 되면서 OrderRejected 되면서 DeliveryCancelled가 된다. DeliveryCancelled 이 되면서 increase와 decrease가 둘 다 실행되게 된다.

- 멱등성
&gt;멱등성(幂等性, 영어: idempotency)은 특정 연산을 여러 번 수행하더라도 결과가 달라지지 않는 성질을 의미

- Delivery
배송건 id와 주문건 id를 같이 한다. 
delivery가 order당 하나임
OrderCreated에서 start delivery로 Delivery를 CREATE 하는 것과 같아서 orderId를 추가해서 넣을 수 있다. 

- Inventory (멱등성)
Transaction.java로 처리의 로그를 담도록한다. 
orderId를 기반으로 내용을 가지고 있을 수 있도록 클래스를 하나 만드는 것이다. 
**TransactionRepository.java**
    - stockDecrease() 함수에서 TransactionRepository로 id를 찾아보고 있으면 return 처리하고 stockDecrease를 뒤에 더 처리하지 않는다. </code></pre><p>if(Transaction.repository().findById(Long.valueOf(deliveryStarted.getOrderId())).isPresent())
         return;</p>
<pre><code>stockDecrease() 함수에서 트랜잭션을 new로 객체를 (서버의 코드형태임) 만들어서, 
정상적으로 stock이 줄어들면 transaction을 만들어서 저장해둔다.
이후에 저장된 것과 같은 id가 있으면 멱등성 관리로 더 처리하지 않는다. </code></pre><pre><code>            Transaction transaction = new Transaction();
            transaction.setOrderId(Long.valueOf(deliveryStarted.getOrderId()));
            transaction.setStockOrdered(deliveryStarted.getQty());
            transaction.setCustomerId(deliveryStarted.getCustomerId());
            Transaction.repository().save(transaction);</code></pre><pre><code>    - increase가 되지 않도록 compensate() 함수에서 멱등성 관리를 해준다. 
deliveryCancelled이 들어오면 보상처리를 해야는 조건이다. 
transaction 에서 기존의 처리된 건을 찾아보고 id가 있다면 stock을 이미 dacrease 했다는 것이다 .
```        Transaction.repository().findById(Long.valueOf(deliveryCancelled.getOrderId())).ifPresentOrElse(tx -&gt;{</code></pre><p>stock의 재고가 부족하면 transaction을 만들지 않고 stockDecreaseFailed 이라고 소문을 내고 deliveryCancelled 때문에 compensate()이 실행된다. 
compensate() 함수에서는 transaction에서 찾을 때 만들지 않았기 때문에 사실은 비어있을 것이다. </p>
<pre><code>    public static void compensate(DeliveryCancelled deliveryCancelled){
        Transaction.repository().findById(Long.valueOf(deliveryCancelled.getOrderId())).ifPresentOrElse(tx -&gt;{
            repository().findById(Long.valueOf(deliveryCancelled.getProductId())).ifPresent(inventory-&gt;{

                inventory.setStock(inventory.getStock() + deliveryCancelled.getQty()); // do something
                repository().save(inventory);

                Transaction.repository().delete(tx); //FOCUS: 멱등성 관리를 위해 두번 보상 처리되는 것을 막기 위해 트랜잭션 이력 삭제, (플래그로 처리해도 되긴 함).  handle idempotent. delete to prevent to process twice
                new StockIncreased(inventory).publish();

            });
        }
         ,()-&gt;{
             throw new RuntimeException(&quot;Compensation failed due to stock&quot;);
         }
        );
    }</code></pre><ul>
<li>상품 등록 -&gt; 주문 발행하고 -&gt; 재고량 초과되는 주문 발행 으로 테스트한다. 
reject 이후에 deliverycancelled에서 추가로 increase가 발생하지 않도록 보상처리가 잘 적용된 것을 확인할 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/5aa47b12-4fb1-483d-a50d-37a477667960/image.png" /></li>
</ul>
<hr />
<h2 id="데드라인-추가">데드라인 추가</h2>
<p>시간에 대한 처리임
시간 내 주문건이 최종 처리되어야 하는 시나리오를 추가한다. </p>
<p>OrderCreated (가주문)으로 부터 delivery와 product까지 거치고 OrderPlaced로 올 때까지의 시간을 체크하고, 시간 내 처리하지 못한 주문 것은 유효하지 않은 대상으로 보상처리 한다. </p>
<p>OrderCreated 로 가주문을 생성할 때, 제3자가 해당 시간을 적어둔다.
제 3자의 서버가 deadline이라는 서비스를 만든다. </p>
<p>command나 policy는 주기적으로 실행하지 않아도 된다. 
일반적인 서버에서는 필요없었는데 deadline이라는 서비스는 스케줄러에 넣어두고 주기적으로 검사해야한다. </p>
<p>데드라인 서비스는 주문이 발생되면, 주문번호와 주문시간, 만기시간을 스케줄링한다. 
policyhandler 에 5초 주기로 체크한다. fixedRate
실제 취소된 주문 건에 대해서는 가주문이 취소되면 볼 필요없음으로 레코드에서 지워준다. </p>
<h3 id="실습">실습</h3>
<p><strong>Deadline.java</strong>
schedule() 함수에서 
orderCreated 안에 timestemp를 보고 이벤트 생성 시간을 기록한다. 
schedul에 의해서 관리할 deadline를 다 넣어준다. </p>
<pre><code>    public static void schedule(OrderCreated orderCreated){
        Deadline deadline = new Deadline();
        deadline.setOrderId(orderCreated.getId());
        deadline.setStartedTime(new Date(orderCreated.getTimestamp()));

        Date deadlineDate = new Date(deadline.getStartedTime().getTime() + deadlineDurationInMS);
        deadline.setDeadline(deadlineDate);

        repository().save(deadline);
    }</code></pre><p>지났는지 지나지 않았는지 주기적으로 확인한다. 
<strong>DeadlineScheduler.java</strong>
@Scheduled(fixedRate = 5000) 으로 5초에 한번씩 함수가 동작하도록 한다. </p>
<p><strong>Deadline.java</strong>
현재 지금 시간을 하나 따서 그 시간과 만기 시간을 비교해서 현재가 만기보다 지났으면 저장소에서 해당 만기 시간을 지우고 publish한다.</p>
<pre><code>    public static void sendDeadlineEvents(){
        repository().findAll().forEach(deadline -&gt;{
            Date now = new Date();

            if(now.after(deadline.getDeadline())){
                repository().delete(deadline);   
                new DeadlineReached(deadline).publishAfterCommit();
            }
        });
    }</code></pre><p><strong>Delivery.java</strong>
10초를 강제로 기다리게 한다. </p>
<pre><code>        if(&quot;1&quot;.equals(orderCreated.getProductId()))
        try{
            Thread.sleep(10000);
        }catch(Exception e){}</code></pre><p>gitpod.yml을 보면 init.sh을 실행해주도록 해준다. </p>
<pre><code>./init.sh 
A</code></pre><p>했던 내용을 가져올 수 있다. 
docker-compose.yml</p>
<pre><code></code></pre><pre><code>http :8083/inventories productName=TV stock=1000   # id=1
http :8083/inventories productName=RADIO stock=1000  # id=2
http :8081/orders customerId=1 productId=1 productName=TV qty=1001</code></pre><p>제품을 인벤토리에 담아두고 초과하는 주문을 보낸다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/98c1ba0e-c278-48c1-b9ed-3e65945cf7fc/image.png" /></p>
