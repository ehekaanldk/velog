---
title: "[MSA] Front"
date: "2025-05-26"
link: "https://velog.io/@ehekaanldk/MSA-Front"
series: "Uncategorized"
---

<p>서버는
클라이언트는</p>
<p>git bash를 설치한 경로와 맞춰준다. <img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7fe6d798-3216-44b5-bd84-d8bb1f15ca19/image.png" /></p>
<p>nvm : node version manager</p>
<ul>
<li>여러 버전의 Node.js를 관리한다.</li>
<li>프로젝트마다 노드의 버전이 다르다.</li>
<li>프론트엔드 폴더마다 nvm use 20.22.1 버전을 사용하겠다고 설정할 수 있다. </li>
</ul>
<p>npm : node package manager</p>
<ul>
<li>node.js에서 패키지를 설치하고 관리한다.</li>
<li>전역적인 사용과 지역적인 사용을 관리할 수 있다. <ul>
<li>전역 설치는 npm install [패키지명] -g</li>
<li>지역 설치는 npm install [패키지명]</li>
</ul>
</li>
</ul>
<p>yarn : npm과 같은 기능을 하는 다른 package manager</p>
<ul>
<li>npm이나 yarn 중 하나만 선택해서 사용하면 된다. 같이 사용하면 충돌의 위험이 있다. </li>
<li>패키지 설치는 <code>yarn add [옵션] [패키지명]</code> </li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7395251b-8325-42fd-a1c8-30b6548ac016/image.png" /></p>
<hr />
<h2 id="react-프로젝트-만들기">React 프로젝트 만들기</h2>
<ol>
<li>yarn을 설치한다.
<code>npm install -g yarn</code>
yarn은 패키지를 설치하고 관리하는 도구이다. npm과 비슷한 역할을 한다. </li>
</ol>
<p>누군가가 만든 코드 뭉치(패키지)를 빌려쓰는 것으로 패키지의 버전으로 확인할 수 있다. </p>
<ol start="2">
<li>create-react-app 설치<blockquote>
<p>create react app은 웹 사이트를 만들 때 필요한 기능을 모두 포함한 패키지이다.</p>
</blockquote>
</li>
</ol>
<p>리엑트 프로젝트를 자동으로 만들어주는 패키지를 yarn을 써서 전역으로 설치한다.
<code>yarn global add create-react-app</code></p>
<ol start="3">
<li>react 프로젝트 생성
create react-app 패키지를 통해서 프로젝트를 만든다.
<code>yarn create react-app [프로젝트 이름]</code></li>
</ol>
<p>노드라는 환경에서 코드를 짜고 코드를 웹에서 동작하게 하려면 복잡한 설정이 필요하다. </p>
<p>create-react-app는 이 설정을 모두 자동으로 처리해주는 도구로 많은 패키지와 설정을 포함한 사전 구성된 개발 환경을 제공한다. </p>
<p>설치 후의 모습을 확인한다. 
react 구동에 필요한 것들을 CRA가 자동으로 설치해준 것을 package.json에서 확인할 수 있다. 
lint는 교정의 뜻으로 코드를 작성하고 잘 작성했는지 확인해준다. 
scrips는 명령어로 프로젝트의 시작,빌드,테스트 등을 입력해서 지정한 약어들이 작성된다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/89712c83-1cb6-459c-a0a4-67c32fa12108/image.png" /></p>
<p>react 프로젝트의 경로로 이동한 후에 
<code>cd week-1</code>
yarn start로 리액트 앱을 실행한다.
<code>yarn start</code>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/ea92cd8d-e937-41f4-8790-f6e127db5659/image.png" /></p>
<hr />
<h2 id="react">React</h2>
<h3 id="component와-element">Component와 Element</h3>
<p>컴포넌트는 UI를 만드는 함수나 클래스</p>
<ul>
<li><strong>설계도</strong>의 역할을 한다.</li>
<li>정의할 때 사용된다.</li>
<li>보통 <strong>함수형으로 정의</strong>하며, <strong>JSX를 return</strong>한다.<pre><code>function Welcome(props) {
return &lt;h1&gt;안녕하세요, {props.name}님!&lt;/h1&gt;;
}</code></pre></li>
</ul>
<p>엘리먼트는 UI를 구성하는 React 요소(객체)</p>
<ul>
<li><p>사용할 때 사용된다.</p>
</li>
<li><p>실제 인스턴스로 실행의 결과물이다</p>
</li>
<li><p>react가 실제로 화면에 그릴 수 있는 객체</p>
</li>
<li><p>html처럼 보이지만, 내부적으로 JS 객체</p>
<pre><code>const element = &lt;h1&gt;Hello!&lt;/h1&gt;;       // 일반 태그
const element2 = &lt;Welcome name=&quot;지현&quot; /&gt;; // 컴포넌트를 사용한 엘리먼트</code></pre></li>
<li><p>react 컴포넌트의 return 값은 엘리먼트이다. </p>
</li>
</ul>
<h3 id="dom">DOM</h3>
<blockquote>
<p>웹 브라우저가 <strong>HTML 문서</strong>를 *<em>구조화해서 *</em> 표현한 트리 형태의 객체 구조</p>
</blockquote>
<ul>
<li>브라우저가 이해할 수 있도록 구조화된 객체로 만든것</li>
<li>웹페이지 전체를 트리 형태로 표현한 JavaScript 객체</li>
</ul>
<h3 id="react의-동작방식">React의 동작방식</h3>
<h4 id="1-브라우저는-기본적으로-html-파일만-읽을-수-있다">1. 브라우저는 기본적으로 .html 파일만 읽을 수 있다.</h4>
<ul>
<li>.html 파일이 시작점이 된다. </li>
<li><code>public</code> 폴더에서 <code>index.html</code>에서 웹이 시작된다.</li>
</ul>
<ul>
<li><code>id=&quot;root&quot;</code>인 <code>&lt;div&gt;</code> 태그는 React가 <strong>동적으로 내용을 삽입할 공간</strong>이다. </li>
</ul>
<blockquote>
<p>React는 root 자리에 컴포넌트를 만들어 넣는 방식으로 화면을 구성한다. </p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/953615ba-0e05-4012-a6ff-f7cf12c7e55b/image.png" /></p>
<h4 id="2-javascript가-html을-제어한다">2. JavaScript가 HTML을 제어한다.</h4>
<ul>
<li><p>html은 <code>src</code>폴더의 <code>index.js(javascript 파일)</code> 을 불러오는 역할을 한다. </p>
</li>
<li><p>JS 파일이 react 컴포넌트를 실행하고 결과를 #root에 렌더링한다.</p>
</li>
<li><p>index.js는 <code>root</code>라는 id를 가진 요소를 찾아서,</p>
</li>
<li><p><code>&lt;App /&gt;</code>이라는 React 컴포넌트를 그 안에 렌더링(render) 합니다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/2a00148a-ab3f-495c-a19f-54a1fc2b16b2/image.png" /></p>
</li>
</ul>
<h4 id="3-컴포넌트가-화면을-구성한다">3. 컴포넌트가 화면을 구성한다.</h4>
<ul>
<li><code>APP.js</code> 은 하나의 react 컴포넌트이다.</li>
<li>컴포넌트는 JSX를 반화하며, 실제로 React 엘리먼트가 된다. </li>
<li>컴포넌트는 HTML처럼 보이지만 javascript 코드이다. </li>
<li>App 처럼 여러 개의 컴포넌트를 조합해서 웹페이지를 구성한다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/8db2ae21-7a4b-4000-b088-568750574a3b/image.png" /></li>
</ul>
<p>웹 사이트를 조각조각(컴포넌트)를 모아서 조각도 개발자가 만들 수 있다. </p>
<h4 id="4-최종실행-개발-서버localhost">4. 최종실행: 개발 서버(localhost)</h4>
<p>Create React App으로 만든 프로젝트는 <code>localhost:3000</code> 포트에서 실행된다.</p>
<blockquote>
<p>웹 = 컴포넌트들의 합
컴포넌트 = 함수(.js 파일)
return = JSX(엘리먼트)
이 엘리먼트들이 root 안에 렌더링됨</p>
</blockquote>
<hr />
<h2 id="jsx">JSX</h2>
<p>JavaScript 안에 HTML을 작성할 수 있게 해주는 문법 확장이다.</p>
<blockquote>
<p>✅ JavaScript 코드 안에 HTML 태그를 그대로 쓰는 것처럼 보이게 만들어줍니다.
✅ 하지만 실제로는 JavaScript 코드로 변환됩니다.</p>
</blockquote>
<h3 id="컴포넌트">컴포넌트</h3>
<p>컴포넌트는 개발자가 직접 정의한 재사용 가능한 UI 코드 조각이다. </p>
<ul>
<li>JSX를 반환하는 함수형 컴포넌트</li>
<li>클래스형 컴포넌트</li>
</ul>
<p>App.js 파일이 APP 컴포넌트를 정의하는 파일이다. 
html처럼 보이는 JSX를 반환한다. 
직접 정의하는 함수나 클래스이다. 
<code>function App() { return &lt;h1&gt;Hello&lt;/h1&gt;; }</code></p>
<h3 id="엘리먼트">엘리먼트</h3>
<p>엘리먼트는 React.createElement(...) 또는 JSX로 만들어지는 컴포넌트의 실행 결과이다. </p>
<p>JSX로 만든 컴포넌트를 실행한 결과이다. 
<code>&lt;App /&gt;</code>, <code>&lt;h1&gt;Hello&lt;/h1&gt;</code></p>
<p><strong>react는 엘리먼트를 읽고</strong>, 가상화 돔에 반영하고, 실제 돔에 렌더링한다.</p>
<blockquote>
<p>App.js는 하나의 컴포넌트 파일이고,  는 컴포넌트를 사용해서 만든 엘리먼트이다. 
react는 엘리먼트를 읽고 브라우저에 실제로 렌더링한다.</p>
</blockquote>
<h3 id="jsx의-규칙">JSX의 규칙</h3>
<p>JSX는 자바스크립트 안에 HTML을 쓰는 것처럼 보이지만, 실제는 자바스크립트 문법이다. </p>
<h4 id="1-return-값은-반드시-하나의-최상위-태그여야-한다">1. return 값은 반드시 하나의 최상위 태그여야 한다.</h4>
<ul>
<li>JSX는 하나의 요소만 반환할 수 있다. </li>
<li>여러 개를 반환하고자 한다면 <code>&lt;div&gt;</code> 나 <code>&lt;&gt;&lt;/&gt;</code> 으로 감싸야 한다. </li>
</ul>
<h4 id="2-모든-태그는-받드시-닫아야-한다">2. 모든 태그는 받드시 닫아야 한다.</h4>
<p><code>&lt;input&gt;</code> 처럼 HTML에서 닫지 않아도 되는 태그도 JSX에서는 반드시 닫아야 한다. 
<code>&lt;input type=&quot;text&quot; /&gt;</code></p>
<h4 id="3-자바스크립트-표현식을-사용할-때는-중괄호를-사용한다">3. 자바스크립트 표현식을 사용할 때는 중괄호<code>{}</code>를 사용한다.</h4>
<ul>
<li>JSX 안에 변수, 연산, 함수 호출 등 자바스크립트 코드를 쓰고 싶다면 <code>{}</code> 으로 감싸야 한다. </li>
</ul>
<h4 id="4-html-속성-이름이-다르다class---classname">4. HTML 속성 이름이 다르다.(class -&gt; className)</h4>
<ul>
<li>JSX는 실제 HTML이 아니라 javascript임으로, 예약어 충돌을 피하기 위해 일부 속성명이 다르다.</li>
<li>실제 브라우저의 F12로 확인하면 class이지만
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/438cbf83-33b4-413b-8bec-1d5c1da9324c/image.png" /></li>
<li>App.js 컴포넌트에서는 className으로 다르다. <img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/097397a5-4f6e-4ba4-b2c6-ea6f9cc096bb/image.png" /></li>
<li>오류가 나지는 않지만 경고가 발생한다.</li>
</ul>
<table>
<thead>
<tr>
<th>HTML 속성</th>
<th>JSX 속성</th>
</tr>
</thead>
<tbody><tr>
<td><code>class</code></td>
<td><code>className</code></td>
</tr>
<tr>
<td><code>for</code></td>
<td><code>htmlFor</code></td>
</tr>
<tr>
<td><code>onclick</code></td>
<td><code>onClick</code></td>
</tr>
<tr>
<td><code>tabindex</code></td>
<td><code>tabIndex</code></td>
</tr>
</tbody></table>
<hr />
<h3 id="실습1">실습1</h3>
<pre><code>function App() {
  let a = 3;
  let title = &quot;안녕하세요!&quot;
  let body = &quot;이름을 입력해주세요.&quot;
  const style={
    color: &quot;orange&quot;
  }

  return (
    // 1. return값이 반드시 1개이여야 한다. 
    // 4. 정확히는 html(동요소?)이 아니라 react의 요소임으로 className으로 해주어야한다.
    &lt;div className=&quot;App&quot;&gt;


      &lt;IamComponet name={&quot;내이름&quot;}/&gt;


      &lt;h1 style={{
        color: &quot;blue&quot;,
        fontSize: &quot;60px&quot;
      }}&gt;{title}&lt;/h1&gt;

      &lt;hr/&gt;
      &lt;p&gt;
      {/* 3. 자바스크립스 값을 보여주고 싶으면 중괄호를 사용한다. */}
      {body}
      &lt;/p&gt;
      {/* 2. 반드시 태그를 닫아줘야한다. */}
      &lt;input type=&quot;text&quot;/&gt; 
    &lt;/div&gt;
  );
}

export default App;</code></pre><p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/4eeaaba8-ff0f-4b0c-aa70-b948cfea482a/image.png" /></p>
<hr />
<h2 id="컨포넌트에서의-데이터-관리-방식">컨포넌트에서의 데이터 관리 방식</h2>
<h3 id="state">State</h3>
<blockquote>
<p>컴포넌트(내가)가 가지고 있는 데이터(내부 상태)</p>
</blockquote>
<p>state는 해당 컴포넌트 내에서 생성과 수정이 가능하다.</p>
<pre><code>const [count, setCount] = useState(0);
</code></pre><h3 id="props">Props</h3>
<blockquote>
<p>컴포넌트가 부모 컴포넌트로 부터 받아온 데이터</p>
</blockquote>
<p>props로 받은 데이터는 읽을 수는 있지만, 수정할 수 없다. </p>
<ul>
<li>자식 컴포넌트는 전달받은 props를 수정할 수 없다.</li>
<li>props는 내부적으로 객체로 전달된다. {{name : &quot;내이름&quot;}}</li>
</ul>
<h4 id="부모-컴포넌트appjs">부모 컴포넌트(App.js)</h4>
<p>아래 코드가 부모 컴포넌트에서의 name 데이터이다. </p>
<pre><code>&lt;IamComponent name=&quot;내이름&quot; /&gt;
</code></pre><h4 id="자식-컴포넌트iamcomponentjs">자식 컴포넌트(IamComponent.js)</h4>
<p>자식 컴포넌트에서 props로 부모 컴포넌트의 name데이터를 받아온다. </p>
<pre><code>function IamComponet(props){ // IamComponent이름으로 함수를 작성하고

  console.log(props)

  return ( // return하면 component가 되고, null이나 빈태그라도 넣어줘야 한다.
    &lt;h1&gt;{props.name} 저는 컴포넌트입니다!&lt;/h1&gt;

  )
}

export default IamComponet;</code></pre><ul>
<li>전달받은 props 객체에서 props.name으로 값을 꺼내 사용할 수 있다. </li>
</ul>
<h3 id="배열과-map을-활용한-반복-렌더링">배열과 map()을 활용한 반복 렌더링</h3>
<p><code>map()</code>은 배열의 내장함수로 요소에 하나씩 접근할 수 있다.</p>
<p>react에서 map() 함수를 활요해서 <strong>여러 JSX 요소를 반복 생성</strong>할 수 있다. </p>
<pre><code>a.map(value, index) =&gt; {
    console.log(value, index)
    return value + 1
}</code></pre><ul>
<li>배열의 요소를 <code>&lt;p&gt;</code> 로 감싸서 표현할 수 있다. <pre><code></code></pre></li>
</ul>
<p>function App() {</p>
<p>  let list = [1,2,3,5]
  return (
    <div>
      <p>{list}</p>
      {list.map((value, index) =&gt; {
        console.log(value, index)
        return (
          <p>{value}</p>
        )
      })}</p>
<pre><code>&lt;/div&gt;</code></pre><p>  );
}</p>
<pre><code>
### [추가] javascript 변수 선언 방식

자바스크립트의 변수는 선언 -&gt; 초기화 -&gt; 할당 순으로 이루어진다. 

| 단계  | 설명                | 예시           |
| --- | ----------------- | ------------ |
| 선언  | 이름만 만들고 메모리 공간 확보 | `let a;`     |
| 초기화 | 선언과 동시에 기본값 지정    | `let a = 0;` |
| 할당  | 값을 넣어 저장함         | `a = 5;`     |

let은 값 변경 가능한 변수
const는 값 변경 불가능한 상수

---

## 스타일링
### 1. 인라인 스타일
태그 내부에 style={{}} 형태로 직접 스타일을 작성한다.
- JavaScript 객체로 작성한다.
- 인라인 스타일을 사용하면 재사용이 불가능하다. 

### 2. 스타일 파일을 따로 만들어서 스타일을 준다.
&gt;외부 CSS 파일을 만들어서 import해서 사용하는 방식이다.

style.css 파일은 ```어디에 스타일을 줄 것인가(선택자)```와 ```어떤 스타일을 줄 것인가(속성과 값)```으로 구성된다. 

- ```p```는 모든 ```&lt;p&gt;``` 태그에 적용된다. 
- ```.App``` 는 클래스의 이름이 app인 요소에 적용된다. 
- ```#root``` 는 id가 root인 요소에 적용된다. </code></pre><p>선택자(selector) {
  속성(property): 값(value);
}</p>
<pre><code>- 기존의 js 파일에 ```&lt;div className=&quot;container&quot;/&gt;```를 작성해주어야 한다. </code></pre><p>import './style.css'
    <div>
    <div></p>
<pre><code>
### 3. 컴포넌트 방식으로 스타일을 준다.
```npm install styled-components``` 또는
```yarn add styled-components```

styled-components 는 해당 웹에서 doc를 보고 작성법을 확인한다. 

내파일에 없는 무언가를 사용하는 것임으로 import로 가져온다.
```import styled from &quot;styled-components&quot;;```

#### 3.1. 기본 styled-component 방식
기존의 코드에서 적용한 인라인 style을 </code></pre><div key={value.id} style={{
              border: "2px solid blue",
              margin: "10px",
              padding: "10px",
              borderRadius: "10px"
            }}>
```
styled-components 방식으로 전환한다. 
```
const Card = styled.div`
  border: 2px solid blue;
  margin: 10px;
  padding: 10px;
  borderRadius: 10px;
`
```
- 컴포넌트 단위로 스타일을 분리한다.
- 속성값에 " 따옴표를 사용하지 않는다.
- CSS 처럼 ; 세미콜론을 붙여야 한다. 

<p>기존의 JSX에는 div대신에 Card를 사용해준다. </p>
<pre><code>&lt;Card key={value.id}&gt;
  {value.name}
&lt;/Card&gt;</code></pre><p>컴포넌트는 데이터를 가질 수 있다. 
가질 수 있는 데이터는 state, props를 가질 수 있다.
스타일 컴포넌트에서는 자기가 데이터를 정의하진 않지만 데이터를 받아갈 수는 있다.</p>
<h4 id="32-백틱---템플릿-리터럴">3.2. 백틱(``) + ${}: 템플릿 리터럴</h4>
<blockquote>
<p>템플릿 리터럴에서는 백틱(``)  안에서는 <code>${}</code> 를 써서 변수/값/함수 결과를 넣을 수 있다. </p>
</blockquote>
<pre><code>const text1 = 'Hello';           // 작은 따옴표
const text2 = &quot;Hello&quot;;           // 큰 따옴표
const name = &quot;a&quot;;
const text3 = `Hello, ${name}`;  // 백틱 + ${} (템플릿 리터럴)
</code></pre><p>#dddddd / rgb(100,100,100), rgba(100,100,100,0.4)</p>
<ul>
<li>카드에 인덱스를 가지고 와서 색상이 투명도가 점점점 달라지도록 한다.</li>
<li>cardIndex를 받아와서 투명도를 다르게 한다.</li>
</ul>
<h4 id="33-styled-components에서-props-사용하는-방법">3.3. styled-components에서 props 사용하는 방법</h4>
<blockquote>
<p>styled-component를 사용해서 부모가 props를 전달해서 자식이 사용하는 것이다. </p>
</blockquote>
<p><code>(props) =&gt; props.cardIndex</code>로 props를 받아와서 사용하는 방식이다. </p>
<p>실제 사용하는 부분이 props에 부모의 역할이다.</p>
<pre><code>&lt;Button buttonColor=&quot;blue&quot;&gt;완료&lt;/Button&gt;</code></pre><ul>
<li>buttonColor=&quot;blue&quot; 는 부모가 자식(button 컴포넌트)에게 값을 주는 것이다. </li>
</ul>
<p>styled-component는 스타일이 입혀진 껍데기로 컴포넌트 정의자이다. </p>
<pre><code>const Button = styled.button`
  width: 100px;
  background-color: ${(props) =&gt; props.buttonIndex};
`</code></pre><ul>
<li>Button 틀이 props 값을 받아서 <code>backgroud-color: blue</code> 로 처리한다. </li>
</ul>
<p>시각적으로 정리하면 다음과 같다. </p>
<pre><code>[App 컴포넌트 (부모)]
     |
     v
&lt;Button color=&quot;blue&quot; /&gt;
     |
     v
[styled.button (자식 역할의 정의)]
 → props.color 사용 → 스타일 완성
</code></pre><p>인라인 스타일이 가장 우선순위가 있다. </p>
<h3 id="정리">정리</h3>
<ul>
<li>패키지를 설치한다. </li>
<li>컴포넌트 단위로 스타일을 분리한다. styled.태그`` 백틱을 사용한다. </li>
<li>만든 스타일 컴포넌트를 return하는 곳에 찾아서 넣어준다. </li>
<li>JSX 에 &lt;컴포넌트 명/&gt; 형태로 넣어준다. </li>
<li>props는 동적으로 스타일을 제어한다.(일방향)</li>
<li>${(props) =&gt; props.속성} 형태로 값을 적용</li>
</ul>
<hr>
<h2 id="브라우저">브라우저</h2>
<blockquote>
<p>브라우저는 여러 구성요소가 협력해서 화면에 페이지를 그리는 시스템이다. </p>
</blockquote>
<h3 id="브라우저의-구성요소">브라우저의 구성요소</h3>
<ul>
<li>사용자 인터페이스 : 브라우저 자체의 UI</li>
<li>브라우저 엔진 : 사용자 인테페이스-렌더링 엔진 사이의 통신</li>
<li>렌더링 엔진 : 실제 화면에 그리는 핵심 엔진</li>
<li>통신 : HTTP 요청/응답 처리, 서버에서 리소스 받아옴</li>
<li>UI 백엔드 : 브라우저 내 UI요소를 그림(OS마다 다름)</li>
<li>자바스크립트 해석기 : JS code 해석하고 실행</li>
<li>자료 저장소 : 클라언트 저장소 제공</li>
</ul>
<h3 id="브라우저-렌더링-엔진-동작">브라우저 렌더링 엔진 동작</h3>
<h4 id="1-html을-로드하고-토큰화한다">1. HTML을 로드하고 토큰화한다.</h4>
<ul>
<li>HTML 문법 요소를 토큰으로 인식한다.</li>
<li>토큰은 태그,속성,내용 등 HTML문서에서 의미있는 최소 단위 조각이다.</li>
</ul>
<h4 id="2-토큰을-파싱하여-dom-tree를-만든다">2. 토큰을 파싱하여 DOM tree를 만든다.</h4>
<ul>
<li>DOM은 HTML문서의 계층구조(부모-자식관계)를 객체 형태로 표현한다<pre><code>&lt;body&gt;
&lt;h1&gt;Hi&lt;/h1&gt;
&lt;/body&gt;</code></pre><pre><code>Document
└── html
   └── body
       └── h1
           └── &quot;Hi&quot;
</code></pre></li>
</ul>
<pre><code>#### 3. CSS로 파싱하여 CSSOM tree를 만든다.
- CSS도 브라우저가 파싱하여 CSSOM라는 트리로 만든다.

#### 4. DOM + CSSOM 으로 Render tree를 만든다.
- render tree는 화면에 보여야하는 것을 명세한다. 

#### 5. Layout단계
- render tree에서 node들의 위치와 크기를 계산해서 좌표로 나타낸다. 
- 컴퓨팅 리소스를 많이 잡아먹는 단계이다.

#### 6. Paint단계
- 계산된대로 화면에 표출하고 배치한다. 
- 픽셀 단위로 시각화한다. 
- 컴퓨팅 리소스를 많이 잡아먹는 단계이다. 

---

## 렌더링 성능 최적화
렌더링 과정에서 자원을 많이 잡아먹는 Layout과 Paint단계에서의 최적화를 위해서 

### 더티 비트 시스템
&gt; UI 요소에 변경이 있을 때, 필요한 부분만 다시 렌더링 하는 방식

- 변경된 부분만 추적해서 업데이트한다.
- 깃발을 꽂아두고 해당 부분을 작업스케줄러에 넣고 모아서 처리한다. 
- 개발자가 직접 더티 부분을 관리해야 해서 복잡하다. 


### 가상돔(Virtual DOM)
&gt; 브라우저의 실제 DOM에 직접 조작하지 않고, 메모리 상의 가짜 DOM tree를 먼저 만들고,
변경 전후를 비교해서 최소한의 변경만 실제 DOM에 반영하는 방식

- state나 props 변경이 발생
- 새로운 가상돔 생성
- 이전의 가상돔과 diff알고리즘으로 비교
- 변경된 부분만 실제 DOM에 반영된다.

#### 가상돔이 새로 그려지는 조건
- 처음 페이지 진입
- 데이터 수점


### [추가] DOM
&gt; 웹 브라우저가 HTML문서를 트리 구조로 표현한 객체이다. 

- HTML을 브라우저가 이해하고 조작할 수 있도록 구조화된 틀 또는 객체 트리
- 각 HTML요소는 **노드**로 표현되고, 부모-자식 간의 관계를 가진다. 
- javascript로 내용 수정/삭제가 가능하다. 
- 수정하면 실시간으로 화면에 바로 반영된다. 

### 컨포넌트의 라이프 사이클

컴포넌트는 3단계의 생애 주기를 가집니다:
- 마운트(Mount): 컴포넌트가 화면에 &quot;처음 나타날 때&quot;

- 업데이트(Update): props나 state가 바뀌어서 다시 렌더링될 때

- 언마운트(Unmount): 컴포넌트가 &quot;사라질 때&quot;

생성 : 컨포넌트를 불러온다.
수정 : 사용자의 입력으로 데이터가 바뀔 때 업데이트
    - props 변경 시 수정
    - state 변경 시 수정
    - 부모 컴포넌트 업데이트 시 수정(리렌더링)
    - 강제 업데이트 시 수정
제거 : 페이지를 이동하거나 컴포넌트가 화면에서 사라짐

---

## 컴포넌트 상태 관리

### 상태관리
&gt; state란 화면 UI에 영향을 주는 데이터 값이다. 
상태 관리는 이 데이터의 변화와 흐름을 제어하는 과정이다. 

사용자의 행동으로 state가 변하면, 화면도 바꿔어야 한다. 

React 함수형 컴포넌트 안에서만 쓸 수 있는 Hook 함수 중 하나인 useState()를 사용한다. 

변경함수를 사용해야 react가 상태 변경을 감지하고 자동으로 다시 렌더링해준다. 


```const [count, setCount] = useState(0);```
- 초기값을 0으로 처음에는 count의 값이 1이란느 뜻이다. 
- 이 함수는 배열 [현재값, 변경함수] 를 반환한다. 
- 현재 상태값인 count를 setCount 상태 값을 바꾸는 함수로 변경한다.


### 프롭스 드릴링
&gt; 상위 컴포넌트의 데이터를 하위 컴포넌트에게 전달하려고, 중간 컴포넌트들을 거쳐 props를 계속 전달하는 현상

필요하지도 않은 컴포넌트들이 props를 운반만 하는 문제이다. 


</code></pre>
