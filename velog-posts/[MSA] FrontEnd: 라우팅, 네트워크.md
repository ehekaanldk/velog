---
title: "[MSA] FrontEnd: 라우팅, 네트워크"
date: "2025-05-28"
link: "https://velog.io/@ehekaanldk/MSA-FrontEnd-%EB%9D%BC%EC%9A%B0%ED%8C%85-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC"
series: "Uncategorized"
---

<p>새로운 프로젝트를 생성한다. </p>
<p>필요없는 데이터를 다 지운다. className 아래부분</p>
<ul>
<li>목록을 하나 만들어야 한다. </li>
<li>텍스트 입력창을 하나 만들어야 한다. </li>
</ul>
<p>new file로 Bucketlsit.jsx 파일을 생성한다. </p>
<p>new file로 WritForm.jsx 파일을 생성한다. </p>
<p>컴포넌트는 함수로 만들어야 한다. </p>
<pre><code>function WriteForm() {
}</code></pre><pre><code>const = WriteForm = () =&gt; {
    return (
        &lt;div&gt; 작성위치 &lt;/div&gt;
    )
}</code></pre><p>컴포넌트는 무조건 하나를 return하고 시작한다.
export default 파일명으로 내보내줘야한다. </p>
<p>App.js에서 
컴포넌트를 import해준다. </p>
<p>import BucketList from './BucketList'
import WriteFrom from './WriteFrom'

</p>
<p>가이드를 본다. </p>
<p>h1으로 버킷리스트 텍스트를 넣어준다. </p>
<p>목록을 감싸는 div를 만들어서 넣어준다.
div의 style을 작성해준다. 
border: &quot;1px solid #ccc&quot;
borderRadius : &quot;10px&quot;</p>
<p>BucketList.jsx에서 
BucketList 컴포넌트 안에 BucketList 목록을 넣어준다. </p>
<pre><code>const BucketList = () =&gt; {
    return (
        &lt;div&gt; 
            {BucketList.map((item, idex) =&gt; {
                console.log(item)
                return (
                    &lt;div style = {{
                        backgroud: &quot;aliceblue&quot;,
                        margin: &quot;10px&quot;,
                        padding: &quot;10px&quot;,
                        textAlign: &quot;left&quot;
                    }}&gt;
                        {item.item}
                    &lt;/div&gt;
                )
            })}
        &lt;/div&gt;
    )
}</code></pre><p>WriteFrom.jsx에서
WriteFrom를 작성해준다. </p>
<hr />이거나 style에서 borderTop을 사용할 수 있다. 
꽉 채우고 싶을 때는 display에서 grid를 해준다.
gridTemplateColumns로 앞에 몇칸을 주고 뒤에는 몇칸으로 준다고 설정할 수 있다.
em, rem 등의 px외의 단위도 있다. 
```
const WriteForm = () => {
    return (
        <div style={{
            borderTop: "1px solid #ccc",
            padding: "10px",
            displat: "grid",
            gridTemplateColumns: "3fr 1fr",
            gap: "0.5rem"

<pre><code>    }}&gt;

        &lt;input /&gt;
        &lt;button onClick={() =&gt;{
            console.log(&quot;안녕&quot;)
        }}&gt;추가하기&lt;/button&gt;

    &lt;/div&gt;
)</code></pre><p>}</p>
<pre><code>
onClick은 이벤트 핸들러로 유저가 행동을 했다고 알려주는 것이다. 
내부에 들어가는 함수가 눌렀을 때의 어떤 함수를 시행되는 함수이다. () =&gt; {}

버킷리스트의 아이템을 추가하고 싶다. 
버킷리스트의 아이템은 BucketList.jsx 안에 위치하고 있다.

부모의 APP에 자식 BucketList컴포넌트와 WriteForm컴포넌트가 연결되어 있고, 부모와 자식은 단방향임으로 WriteForm컴포넌트에서 BucketList컴포넌트를 접근할 수 없다. 

그럼으로 버킷리스트의 아이템을 BucketList컴포넌트에 작성하는 것이 잘못되었다. !!!!

App.js에 버킷리스트의 아이템을 옮겨준다. 
props로 App.js가 BucketList컴포넌트로 보내준다. 
App.js 에서 </code></pre><BucketList bucketList={bucketList} />
<WriteForm bucketList={bucketList} />
```

<p>props를 받아오도록 작성한다. </p>
<pre><code>const BucketList = (props) =&gt; {
    console.log(props)

    return (
        &lt;div&gt; 
            {props.bucketList.map((item, idex) =&gt; {
                console.log(item)
                return (
                    &lt;div style = {{
                        backgroud: &quot;aliceblue&quot;,
                        margin: &quot;10px&quot;,
                        padding: &quot;10px&quot;,
                        textAlign: &quot;left&quot;
                    }}&gt;
                        {item.item}
                    &lt;/div&gt;
                )
            })}
        &lt;/div&gt;
    )
}</code></pre><p>데이터의 위치가 app에 있기 때문에 WritemFrom 도 수정한다. 
props.bucketList=[] 를 넣어준다. =&gt; 오류가 발생한다. props로 받은 것은 변경이 불가능하기 때문에 오류가 난다.</p>
<pre><code>const WriteForm = () =&gt; {
    return (
        &lt;div style={{
            borderTop: &quot;1px solid #ccc&quot;,
            padding: &quot;10px&quot;,
            displat: &quot;grid&quot;,
            gridTemplateColumns: &quot;3fr 1fr&quot;,
            gap: &quot;0.5rem&quot;

        }}&gt;

            &lt;input /&gt;
            &lt;button onClick={() =&gt;{
                console.log(&quot;안녕&quot;)
                props.bucketList=[]
            }}&gt;추가하기&lt;/button&gt;

        &lt;/div&gt;
    )
}</code></pre><p>APP.js에서 
받아온 데이터를 수정하려면 <strong>수정할 수 있는 함수</strong>를 받아서 실행시켜야 한다. 
자식이 <strong>수정할 수 있는 함수</strong>를 가지고 호출하면 된다. 
<strong>수정할 수 있는 함수</strong>를 만들어준다.</p>
<pre><code>const changeBucketList() = () =&gt; {
    bucketList = [];  //빈배열로 만들기
}

&lt;BucketList bucketList={bucketList} /&gt;
&lt;WriteForm bucketList={bucketList} changeBucketList={changeBucketList}/&gt;</code></pre><p>WriteForm에서 
props.bucketList=[]를 props.changeBucketList() 으로 변경해주면 된다. 
부모가 바꾸도록 수정하는 함수를 넣어준다.</p>
<p>하지만 console에서는 바뀌지만 화면에서는 목록이 빈 상태가 안된다. 
=&gt; state가 아니여서 화면에서는 변경되지 않는다. </p>
<p>App.js에서
리엑트 hook 중에서 useState 를 사용해준다. </p>
<p>import {useState} from react</p>
<p>구조분해 할당으로 const[] 언에 리스트에 요소들이 받을 값을 각각 가져올 수 있다. 
_bucketList으로 데이터를 이름이 겹치지 않ㄷ록 한다. 
기존의 bucketList = []; 를 setBucketList([]) 로 바꿔서 리스트를 빈배열로 set해준다. state 상태값으로 관리하게 해준다. </p>
<pre><code>function App(){
    const [bucketList, setBucketList] = useState(_bucketList);
    const changeBucketList() = () =&gt; {
        setBucketList([]);  //빈배열로 만들기
        console.log(bucketList)
    }
}

</code></pre><h2 id="hook">Hook</h2>
<p>usetState : 상태 값 관리
useEffect : 컴포넌트의 라이브사이클에 따른 sideeffcet를 관리(생성, 수정, 삭제)하는 포인트를 알려준다. 
useCallback : 메모리의 함수가 어디에 초기화되었는지 위치를 기억해준다. 
userRef : 어떤 값이나 요소를 복사해서 .current해서 가져올 수 있도록 해준다.</p>
<p>Hook은 함수형 컴포넌트에만 사용이 가능하다. </p>
<hr>
<p>useEffect는 함수형 컴포넌트에서ㅓ만 사용이 가능하다.</p>
<blockquote>
<p>App() 컴포넌트 밖에서 Hook을 사용하는 것은 불가능!
리액트의 Hook은 함수형 컴포넌트 안쪽에서만 사용해야한다. </p>
</blockquote>
<p>생성, 수정, 삭제의 타이밍을 알려준다. 
삭제 되기 전에 정리 cleanUp
function App() 함수 안에 작성한다. 
어떤 값이 바뀌면 dependency array</p>
<pre><code>useEffect(() =&gt; {
    console.log('나 생성됨');
}, []); // []부분이 dependency array임

useEffect(() =&gt; {
    console.log('나 업데이트됨');
}, [bucketList]);</code></pre><p>dependency array 안에 있ㄴ느 값이 바뀌면 useEffect의 첫번쨰 인자가 수행된다. 
useEffect는 생성 시점에서는 모두 작동이된다. 
초기에 한번 수행, dependency array에 따라서 수행된다. </p>
<hr>
<p>useCallback은 함수의 고질적인 이슈때문에 사용한다. </p>
<p>변수(let)와 상수(cosnt)는 <code>선언</code>이라고 부른다. 선언을 하게 되면 메모리에 지정이 되고 초기화가 된 후에 값이 할당이 된다. </p>
<p>function App(){} 으로 선언하면 메모리에 초기화를 해준다. 함수는 만들어지면 무조건 초기화를 하게 되어 있다. 함수형 컴포넌트가 렌더링을 한다느 것은 함수 내 코드를 실행한다는 것으로 내부의 const 선언부분이 있으면 changeBucketList도 메모리에 초기화가 된다. </p>
<p>메모리의 입장에서 렌더링을 다시하면서 상태값이 바뀌면서 메모리에 다시 할당이 되면서 메모리가 어려워진다. </p>
<pre><code>useCallbeck(() =&gt; {
    console.log('여기 있어요!')
},[]);</code></pre><p>메모리에 위치를 기억하면서 다시 초기화가 되어도 수행되지 않도록 한다. 저장해놓은 위치를 까먹지 않도록 기억하는 것이다. 함수 내부의 console은 계속 실행이 되긴 하는 것이다. 함수의 위치만 기억하는것이고 함수 내 값을 기억하는 것이 아님!!!! (userMemo는 할달된 값도 저장이 되는 hook이다. 참고!)</p>
<hr>
<p>userRef는 도플갱어 박스로 어떤 값을 넣어주면 값을 얕은 복사로 가지고 있는다. </p>
<p><img src="https://velog.velcdn.com/images/ehekaanldk/post/091569d1-263d-465d-adbc-7829e254c02a/image.png" alt="">
input과 button을 만들어주다. </p>
<p>const inputRef = useRef(null); 로 초깃값을 넣어준다. </p>
<pre><code>&lt;input ref={inputRef}&gt;
&lt;button onClick={() =&gt;{
    console.log(&quot;누름&quot;)
    console.log(inputRef.current)
    console.log(inputRef.current.value)
    inputRef.current.value = &quot;고양이 귀여워&quot;
}}&gt;버튼&lt;/button&gt;</code></pre><ul>
<li>상태값은 무조건 useState로 한 것만 해당된다.
inputRef.current 까지가 input이고 value는 input창에 들어간 값이다. =는 할당으로 값 넣어주기를 의미한다. 
&lt;input value = {'aaaa'}&gt; 돔요소를 통해서 지정한다. 
inputRef.current.value = '고양이 귀여워' 는 JS를 사용해서 지정한다. </li>
</ul>
<pre><code>useEffect(() =&gt; {
    console.log('inputRef여기!')
    console.log(inputRef)
}, []);</code></pre><p>버킷리스트의 목록에 추가하려고자 하면?</p>
<p>순서 </p>
<ol>
<li>input에 접근이 가능해야한다. userRef사용</li>
<li>추가하기 버튼을 눌러서 값을 가져온다. onClick 이벤트 핸들러 사용</li>
<li>클릭했을 때 목록은 state로 관리되고 있음으로 state에 추가해준다. useState, setState</li>
</ol>
<p>배열의 값을 추가할 때는 append를 사용하지만
state에 직접 접근해서 append하면 안된다. 무조건 setState로 하기로 했음</p>
<p>...은 대괄호를 제거해주고 
console.log(bucketList)
console.log([...bucketList])</p>
<p>const newBucketList = [...bucketList, {
    id: 3,
    item: &quot;고양이 귀여워&quot;,
    completed: false,
},]</p>
<p>console.log(newBucketList)</p>
<p>setBucketList(newBucketList);</p>
<p>WriteForm에서 
useRef를 사용해서 사용자의 입력값을 목록에 넣도록한다. </p>
<p>스프레드 문법은 
a=[1,2,3] 이고 
...a 은 a -&gt; 1,2,3 으로 벗겨준다. 
객체도 가능하다.
object = {a:1, b:2}
...object 는 a:1, b:2 으로 된다. </p>
<p>const newBucketList = [...bucketList, {...newItem, id:buckerList.length}];</p>
<h2 id="라우팅">라우팅</h2>
<ul>
<li>npm install -g yarn </li>
<li>yarn add global create-react-app : 패키지들의 묶음인 react를 쉽게 만들어준다.</li>
<li>yarn create react-app route-ex</li>
<li>cd route-ex</li>
<li>yarn start</li>
</ul>
<h3 id="라우팅이란">라우팅이란?</h3>
<blockquote>
<p>페이지 이동을 위한 경로 설정하는 것이 라우팅이다. 
사용자가 요청한 <strong>URL 경로(path)</strong>에 따라 어떤 <strong>페이지(또는 컴포넌트)</strong>를 보여줄지 미리 약속해두는 것</p>
</blockquote>
<h3 id="왜-라우팅을-사용하는가">왜 라우팅을 사용하는가?</h3>
<ul>
<li>웹은 기본적으로 주소(경로)를 통해서 문서에 접근한다. </li>
<li>경로마다 다른 페이지를 보여줘야 하기 때문에, 경로와 컴포넌트를 연결해주는 것이 필요하다. </li>
</ul>
<p>자바에서는 어노테이션으로 라우팅을 하고, 예약어이다. </p>
<p>라우팅은 약속으로 naver.com/blog을 넣으면 blog을 보여주자고 정하는 것이다. </p>
<h3 id="라우저-라우터란">라우저 라우터란?</h3>
<p>BrowserRouter는 주소창(예: <a href="http://www.site.com/about)%EC%9D%98">www.site.com/about)의</a> 변경을 감지해서</p>
<p>라우트 정의에 따라 어떤 컴포넌트를 보여줄지 결정해주는 도구</p>
<p>/a 가 들어오면 A 컴포넌트를 보여주기로 약속한다. 
주소창에 뭐가 있는지 보는 것이 브라우저 라우터이다. </p>
<p>브라우저 라우터를 만들어서 주소창에 뭐가 있는지 보고, A 컴포넌트를 달라고 프로젝트에 요청한다. </p>
<p>브라우저 라우터에게 연결관계를 알려준다. </p>
<p>라우팅을 위한 브라우저 라우터의 버전을 설정해서 </p>
<ul>
<li>yarn add react-router-dom@^6.30.1</li>
</ul>
<h3 id="react에서의-라우팅">react에서의 라우팅</h3>
<p>react는 html이 1개이다. 
전통적인 방식에서는 html을 여러개를 가진다.</p>
<p>a.html 이 아니라 /a는 a 컴포넌트를 주세요이다. </p>
<blockquote>
<p>전체 앱은 하나의 HTML로 구성되며, 라우터가 브라우저의 주소를 감시하다가 필요한 컴포넌트만 바꿔서 보여줌 (SPA: Single Page Application)</p>
</blockquote>
<p>페이지 이동 시 새로고침이 없음</p>
<p>브라우저 라우터를 만들고 브라우저 라우터에게 라우터 설정 파일을 만든다.</p>
<p>컴포넌트로 만들어서 ..?</p>
<ol>
<li>브라우저 라우터를 import로 가져온다. </li>
<li>라우터 설정 파일을 만든다. </li>
</ol>
<h4 id="전체-흐름">전체 흐름</h4>
<blockquote>
<ol>
<li>router.js 에서 라우터 설정 →</li>
<li>App.js에서 RouterProvider로 라우터 주입 →</li>
<li>각 경로에 맞는 컴포넌트 작성</li>
</ol>
</blockquote>
<ul>
<li><ol>
<li>router.js 를 만든다. 
설정 파일은 다른 파일을 새로 마들어서 넣어주는 게 좋음\<br>설정에 들어가야 한느 내용은 
경로- 컴포넌트 매칭을 해준다. <pre><code>// 📁 src/router.js
import { createBrowserRouter } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
</code></pre></li>
</ol>
</li>
</ul>
<p>const router = createBrowserRouter([
  {
    path: '/',
    element: <Home></Home>,
  },
  {
    path: '/about',
    element: <About></About>,
  },
]);</p>
<p>export default router;</p>
<pre><code>
- 2. 만든 설정으로 브라우저 라우터를 만들자.</code></pre><p>// 📁 src/App.js
import { RouterProvider } from 'react-router-dom';
import router from './router';</p>
<p>function App() {
  return (
    <RouterProvider router={router} />
  );
}</p>
<p>export default App;</p>
<pre><code>

- 3. 브라우저 라우터랑 app을 연결을 해준다.
브라우저 라우터에서는 주입한다고 말한다. 
주입은 RR 주입기(주입하는 컴포넌트)를 사용한다. 

RR 주입기를 import한다. 
```import { RouterProvider } from 'react-router-dom';``` 

만들어준 라우터(다른파일임 router.js) 를 export , import한다. </code></pre><p>// 📁 src/pages/Home.js
function Home() {
  return <h1>홈 페이지입니다</h1>;
}
export default Home;</p>
<p>// 📁 src/pages/About.js
function About() {
  return <h1>소개 페이지입니다</h1>;
}
export default About;</p>
<pre><code>


---

### url 파라미터
/post-민여잉의 글 1번 : 이렇게 사용하기 보다는
/post/1 로 사용한다.

url 파라미터를 써서 어떤 값을 넘겨 받는다. 

path 뒤에 url 파라미터를 담아준다. 

브라우저 라우터가 url 파라미터를 읽어준다. 
변수명을 name으로 하면 
/cat/:name 으로 작성한다. :을 반드시 작성해주어야 한다. 

useParams 를 사용해서 파라미터를 가져올 수 있게 해주는 hook이다. 
</code></pre><p>// 📁 src/Cat.js
import { useParams } from &quot;react-router-dom&quot;;</p>
<p>const Cat = () =&gt; {</p>
<pre><code>const params = useParams();
console.log(params)


return (
    &lt;div&gt;
        &lt;h1&gt;{params.name}&lt;/h1&gt;
        고양이 컴포넌트입니다. 
    &lt;/div&gt;
)</code></pre><p>}</p>
<p>export default Cat;</p>
<pre><code>
![](https://velog.velcdn.com/images/ehekaanldk/post/7c484ab7-fc75-4060-8a6d-8b243e2f8413/image.png)

- /cat/:name 
: 뒤에 안적으면 404에러가 발생한다. 
- /cat/:name?
? 를 붙이면 url 을 /cat만 해줘도 오류가 나지  않는다. 

---

## Link로 누르면 cat도는 dog 페이지로 가는 것을 만들어보자

![](https://velog.velcdn.com/images/ehekaanldk/post/95594fef-a3b8-43f6-824f-7c98dfb8fc6b/image.png)

```import { Link } from &quot;react-router-dom&quot;;``` 으로 Link를 사용할 수 있게 해준다. 

</code></pre><p>import { Link } from &quot;react-router-dom&quot;;</p>
<p>const Home = () =&gt; {
    return (
        <div>
            홈 컴포넌트입니다. </p>
<pre><code>        &lt;Link to={&quot;/dog&quot;}&gt;
            dog으로 갈레요!
        &lt;/Link&gt;
    &lt;/div&gt;
)</code></pre><p>}</p>
<p>export default Home;</p>
<pre><code>
버튼을 넣어서 페이지가 이동할 수 있도록 한다. 
- 버튼을 누르면 새로고침이 이루어진다. 
- 이전의 url은 자연스럽게 페이지 이동이 된다.
- window.location.href 는 주소창에 아래 url을 담아달라는 요청이다. 
- react는 화면에서만 관리하다가 주소창에 넣어달라는 요청을 하게되는 것이다. </code></pre><pre><code>        &lt;button onClick={() =&gt; {
            window.location.href=&quot;http://localhost:3000/cat&quot;
        }}&gt;cat으로 가는 버튼&lt;/button&gt;</code></pre><pre><code>
새로고침이 되지 않도록 useNavigate를 사용한다. 
- const navigate = useNavigate(); 를 navigate에 함수객체를 할당한다. 
- 브라우저의 주소창에 갈아끼워 넣어달라고 부탁하는 역할이다. </code></pre><pre><code>        &lt;button onClick={() =&gt; {
            navigate('/cat');
        }}&gt;cat으로 가는 버튼&lt;/button&gt;</code></pre><pre><code>
---

## 중첩라우팅
&gt; 여러 페이지에서 **공통으로 포함되어야 하는 레이아웃(Header 등)**을 중복하지 않고, 한 번에 포함시키는 방식입니다.

React Router에서는 이를 위해 ```children```과 ```Outlet```을 사용합니다.

### 메뉴바는 어느 화면에서 다 위치한다. 
- header.jsx를 만들어서 모든 cat.jsx와 dog.jsx 에 다 넣어주어야 한다. 

**귀찮음!!**

- header를 매번 다 넣기 힘들기 때문에 **상위의 레이아웃을 만들고** 그 아래에 cat, dog을 넣을 수 있도록 한다. 

- **AnimalLayout.jsx** 를 만든다. </code></pre><p>import Header from &quot;./Header&quot;;</p>
<p>const AnimalLayout = () =&gt;{
    return (
        <div>
            <Header></Header>
            애니멀 헤더입니다. 
        </div></p>
<pre><code>)</code></pre><p>}</p>
<p>export default AnimalLayout;</p>
<pre><code>
</code></pre><p>// 📁 src/router.js
const router = createBrowserRouter ([
    {
        path: '/',
        element: <Home></Home>,
    },
    {
        path: '/',
        element: <AnimalLayout></AnimalLayout>,
        children: [
            {
                path: '/cat/:name?',
                element: <Cat></Cat>,
            },
            {
                path: '/dog',
                element: <Dog></Dog>,
            }
        ]
    },</p>
<p>])</p>
<pre><code>
- ```&lt;outlet/&gt; ```으로 자식 라우터들이 들어가는 자리이다. 
- AnimalLayout이 상위 컴포넌트로서 고정 틀 역할
자식 컴포넌트 위치를 표시해준다. </code></pre><p>import Header from &quot;./Header&quot;;
import { Outlet } from &quot;react-router-dom&quot;;</p>
<p>const AnimalLayout = () =&gt;{
    return (
        <div>
            <Header></Header>
            <Outlet></Outlet>
            애니멀 헤더입니다. 
        </div></p>
<pre><code>)</code></pre><p>}</p>
<p>export default AnimalLayout;</p>
<pre><code>

#### header와 animalLayout 
header는 페이지 상단에 고정된 메뉴와 컴포넌트이다. 

AnimalLayout은 header를 포함하고 자식 페이지를 감싸는 레이아웃 컴포넌트이다. 


| 항목         | `Header`                  | `AnimalLayout`                                         |
| ---------- | ------------------------- | ------------------------------------------------------ |
| **정의**     | 페이지 상단에 고정된 메뉴바 컴포넌트      | `Header`를 포함하고 자식 페이지(`cat`, `dog`)를 감싸는 **레이아웃** 컴포넌트 |
| **역할**     | UI 구성 요소 중 하나 (내비게이션 바 등) | 페이지 구조와 라우팅 중첩을 담당                                     |
| **사용 위치**  | 보통 여러 곳에서 재사용             | 라우터 설정에서 상위 `element`로 지정됨                             |
| **렌더링 위치** | `&lt;AnimalLayout /&gt;` 내부     | `router.js`에서 중첩 라우팅의 상위 경로에 지정됨                       |

🔹 AnimalLayout이 Header를 포함하고,
🔹 AnimalLayout이 Cat과 Dog를 감싸고 있는 상위 컴포넌트입니다.


## Network

yarn create-react-app network-ex

my_mock_api mkdir 

cd my_mock_api

yarn init -y

yarn add json-server

my_mock_api 폴더 안에 db.json을 만든다. 

json의 키값을 무조건 &quot;&quot; 따옴표를 붙여야 한다.
벨류값은 get/myList 에서의 myList를 넣어준다. 
어떤 배열에서 데이터를 넣어주는데 id와 time를 
</code></pre><p>{
    &quot;sleep_times&quot; : [
        {
            &quot;id&quot;: 0,
            &quot;day&quot;: &quot;화&quot;,
            &quot;sleep_times&quot;: &quot;10:00&quot;
        },
        {
            &quot;id&quot;: 1,
            &quot;day&quot;: &quot;화&quot;,
            &quot;sleep_times&quot;: &quot;10:00&quot;
        },
        {
            &quot;id&quot;: 2,
            &quot;day&quot;: &quot;화&quot;,
            &quot;sleep_times&quot;: &quot;10:00&quot;
        },
        {
            &quot;id&quot;: 3,
            &quot;day&quot;: &quot;화&quot;,
            &quot;sleep_times&quot;: &quot;10:00&quot;
        }
    ]
}</p>
<pre><code>

my_moc_api 경로 안에서 json 서버를 만들어서 파일명을 지켜보겠다. 포트를 설정해주어야 한다. 안하면 3000으로 열린다. 
yarn json-server --watch db.json --port 5001
![](https://velog.velcdn.com/images/ehekaanldk/post/9abb87f4-a77a-4701-bf76-a5cf0bff29b8/image.png)

연결되는 데이터를 api로 ㄴ넘겨준다. 

---
## 자바스크립트와 동시성

새 터미널에 cd network-ex 로 이동해서 yarn start로 실행한다. 

XMLHTTPRequest는 통신을 위한 객체이다. 

js는 쓰레드가 1개이다. 


### 동기와 비동기

동시에 일어나는 것을 동기, 동시에 일어나지 않는 것을 비동기라고 한다. 

요청에 대한 결과를 바로바로 처리하는 것이 동기방식이다. 
요청에 대한 결과를 순차적ㅇ로 처리한다. 

비동기는 동시에 일어나지 않고 a,b,c 라는 일에서 a 요청으로 시작해두고, b도 시작해두고, c도 시작해주면서 끝날 때까지 기다리지 않아도 된다. 

최소한 일꾼이 3명은 있어야 비동기로 할 수 있다. 하지만 **자바스크립트**는 싱글 쓰레드로 동작하는 언어로 **비동기가 불가능할 것 같지만.......**

#### 할 수 있다. 

runtocomplete </code></pre><p>// src/App.js
function App() {</p>
<p>  debugger;</p>
<p>  console.log('aaa')
  alert('hi???')
  console.log('bbbbb')</p>
<pre><code>alert만 했을 때는 aaa 만 출력되고
![](https://velog.velcdn.com/images/ehekaanldk/post/7d65945d-493d-4d98-81ac-93b6bf57718b/image.png)

alert를 닫으면 이후의 단계인 bbbbb가 출력된다. 
![](https://velog.velcdn.com/images/ehekaanldk/post/9ffa0797-0617-4219-835b-e0f24126790c/image.png)


스레드가 기다리는 것을 확인한다.  비동기적으로 실행이 된다. </code></pre><p>  useEffect(()=&gt; {
    window.setTimeout(( // 1초 기다리고 실행되는 callback함수임
      console.log('6000')
    ), 1000) // 1초를 기다려....</p>
<pre><code>console.log('aaaa')</code></pre><p>  }, [])</p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/57414a47-a8ed-492f-9fb7-e6f3f3eb1328/image.png)

js는 비동기 된다. 브라우저가 도와줘서!! 가능하다. 

js는 내부적으로는 heap과 stack으로 나뉜ㄴ다. 
- heap은 메모리에 위치한다. 변수/함수를 만들면 저장되는 곳이다. 
- call stack은 할일을 쌓아두는 곳이다. a()라는 실행자()를 붙이면 일이 쌓이는 것이다. 일감 목록이다. 

js가 돌아가는 것은 할일을 모아두는 것이다. 
window.setTimeout 와 같은 할일을 call stack에 쌓는다. webapi에게 도와달라고 부탁한다. 1초 기다려줄께 등의 일을 하고 일이 끝났다고 알려주고 나머지 작업을 처리한다. 

web api는 끝난 일을 event queue 에 쌓아둔다. 
event queue와  call stack의 사이에 event loop가 감시한다. 
event loop는 감시하면서 call stack이 비어 있으면 event queue에서 하나 꺼내서 call stack에 넣는다. 

js가 webApp에게 도와달라고 요청하고, webapp 처리결과를 

일을 끝난 다음에 실행되는 것이 callback이다.

컴포넌트가 생성이 완료되고? 생성 도중에? 사라질 때?
생성된 다음에 알려줘야 하고 이를 위해서 useEffect를 사용한다. 

??

fetch는 어떤 엔드포인트로 요청을 보낼 것인지..
fetch로 요청을 보내고 기본값은 GET이다. </code></pre><p>  useEffect(() =&gt; {
    // const myPromise = new Promise()
    const data = fetch('<a href="http://localhost:5001/sleep_times'">http://localhost:5001/sleep_times'</a>)
    console.log(data)
  }, [])</p>
<pre><code>요청을 보냈다는 결과를 network에서 확인한다. 
![](https://velog.velcdn.com/images/ehekaanldk/post/79b43d9e-0cb9-4668-a825-5a60aa7da2c7/image.png)

일단 web api에게 시켜두고, 약속된 일을 하고 있을껄..? promise로 
비동기 작업이 끝나면 알려주겠다 해서 promise이다. 

promise를 기다리는 2가지 방법
1. .than
2. async / await

.then을 하면 respone 형태를 받는다. </code></pre><pre><code>useEffect(() =&gt; {
// const myPromise = new Promise()
fetch('http://localhost:5001/sleep_times').then((result)=&gt; {
  console.log(result)</code></pre><p>  }, [])      </p>
<pre><code>![](https://velog.velcdn.com/images/ehekaanldk/post/a3905449-06f9-4a95-8613-3d5fc50efe34/image.png)
</code></pre><pre><code>useEffect(() =&gt; {
// const myPromise = new Promise()
fetch('http://localhost:5001/sleep_times').then((result)=&gt; {
  console.log(result)

  // json 데이터만 뺴오는 json() 함수도 비동기 형식임으로 또 then을 해줘야한다. 
  const myData = result.json()
  console.log(myData)
  return result.json()
}).then((result) =&gt; {
  console.log(result)
})</code></pre><p>  }, [])</p>
<pre><code>놓챴따!!


synac, await
![](https://velog.velcdn.com/images/ehekaanldk/post/ae59599e-a474-454a-a7ca-f5ecd5e6a20a/image.png)
.then은 return을 안하면 오류가 발생한다. 
작성하기 까다로울 수 있어서 async와 await를 사용하는 것이 더 편하다. 


</code></pre>
