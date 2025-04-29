---
title: "[JAVA] Generic collection"
date: "2025-04-15"
link: "https://velog.io/@ehekaanldk/Java-Generic-collection"
series: "Uncategorized"
---

<p>자바에서 배열(Array)와 ArrayList의 차이점을 확인하면서 ArrayList에 대해서 자세히 알아본다. </p>
<p>컬렉션은 객체들만 요소(elements)로 다룬다. 
기본 타입의 값은 wrapper 클래스로 객체화하여 삽입한다. 
<code>v.add(Intger.valueOf(4))</code>
자동 박싱</p>
<p>자동 언박싱</p>
<h2 id="vectore">Vector&lt;E&gt;</h2>
<p>Vector&lt;E&gt; 배열을 가변 크기로 다룰 수 있게 하고, 객체의 삽입, 삭제, 이동이 쉽도록 구성한 컬렉션 클래스이다. </p>
<ul>
<li>삽입되는 요소의 개수에 따라 자동으로 크기를 조절한다. </li>
<li>요소의 삽입과 삭제에 따라 자동으로 요소들의 자리를 이동한다. </li>
</ul>
<p>&lt;E&gt; 에 요소로 사용할 클래스 타입을 지정한다. 
<code>Vector&lt;Integer&gt; v = new Vector&lt;Integer&gt;()</code> 
기본 타입의 int, char, double 등을 사용할 수 없다.</p>
<p>벡터에 요소 접근</p>
<ul>
<li>요소 삽입 : <code>v.add()</code></li>
<li>요소 확인 : <code>v.get()</code> 이나 <code>v.elementAt()</code></li>
<li>벡터 크기 : 벡터의 요소 개수 <code>v.size()</code></li>
<li>벡터 용량 : 벡터가 수용가능한 크기 <code>v.capacity()</code></li>
<li>요소 삭제 : <code>v.remove()</code></li>
<li>모든 요소 삭제 : <code>v.removeAllElements()</code></li>
</ul>
<h2 id="arrayliste">ArrayList&lt;E&gt;</h2>
<p>ArrayList&lt;E&gt;는 가변 크기의 배열을 구현한 컬랙션으로 vector클래스와 거의 동일하다. 
다른 점은 ArrayList는 스레드 간에 동기화를 지원하지 않아 , 다수의 스레드가 동시에 ArrayList에 요소를 삽입하거나 삭제할 때 충돌이 발생할 수 있다.</p>
<p><code>ArrayList&lt;String&gt; a = new ArrayList&lt;String&gt;();</code></p>
<p>ArrayList에 요소 접근</p>
<ul>
<li>요소 삽입 : <code>a.add()</code></li>
<li>요소 확인 : <code>a.get()</code> 이나 <code>a.elementAt()</code></li>
<li>벡터 크기 : 벡터의 요소 개수 <code>a.size()</code></li>
<li>요소 삭제 : <code>a.remove()</code></li>
<li>모든 요소 삭제 : <code>a.removeAllElements()</code></li>
</ul>
<h2 id="iterator">Iterator</h2>
<p>Vector, ArrayList, LinkedList, Set 컬렉션은 순차적으로 요소에 검색할 때 Iterator&lt;E&gt; 인터페이스를 사용한다.</p>
<p><code>Iterator&lt;Integer&gt; it = v.iterator();</code></p>
<ul>
<li>Iterator&lt;E&gt;에서의 컬렉션의 매개 변수와 동일한 타입을 설정한다. </li>
</ul>
<p>iterator 인터페이스 메소드</p>
<ul>
<li>boolean hasNext() : 다음 반복에서 사용될 요소가 있으면 true리턴</li>
<li>E next() : 다음 요소 리턴</li>
<li>void remove() : 마지막으로 리턴된 요소 제거</li>
</ul>
