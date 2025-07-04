---
title: "[생성형AI] Agent"
date: "2025-04-23"
link: "https://velog.io/@ehekaanldk/%EC%83%9D%EC%84%B1%ED%98%95AI-Agent"
series: "Uncategorized"
---

<p>고도화된 RAG를 agent로 만든다. </p>
<p>langGraph를 이용해서 agent를 구축한다. </p>
<h2 id="1-ai-agent">1. AI Agent</h2>
<p>스스로 의사 결정하며, 도구를 사용하여, 목표를 달성하는 시스템 =&gt; 문제를 스스로 해결하는 시스템
RAG에서의 외부지식 문서 이외에도 도구를 사용하여 검색을 통한 확장이 가능하다.</p>
<h2 id="2-langgraph">2. LangGraph</h2>
<p><code>AI Agent</code> 간의 형업을 <strong>그래프 기반</strong>으로 설계하는 프레임워크이다. 
그래프는 워크플로우로 작업의 순서를 의미한다. 노드와 엣지로 이루어져 있다. </p>
<h3 id="21-그래프의-구성요소">2.1. 그래프의 구성요소</h3>
<ul>
<li><strong>node</strong> : Node는 작업이나 판단을 하는 수행단위이다. 
  사용자의 질문을 이해하는 작업
  필요한 정보를 검색하는 작업</li>
<li><strong>edge</strong> : node간의 연결을 나타내며 작업의 흐름이다. 
  node의 작업 이후에 다른 노드로 이동할지 결정하는 작업</li>
<li><strong>conditional edge</strong> : 특정 조건에 따라 노드 간의 분기처리하는 작업이다</li>
<li><strong>state</strong> : 그래프의 현재 상태값을 나타낸다.</li>
</ul>
<p>Node는 함수로 state를 입력으로 받아서 함수를 처리하고 state로 출력한다. Edge는 어디로 갈지의 연결이다. State는 그래프에서 주고받는 데이터들의 틀을 말한다. conditional edge는 조건에 의한 분기로 결과에 따라서 다른 node로 이동하도록 한다.</p>
<p>node는 들어온 것을 처리하고 결과만 내뱉고 어디로 이동해야하는지 알 수 없다. 어디로 이동하는지 정하기 위해서 조건에 해당하는 함수를 정의하고 그에 따른 이동을 conditional edge로 구현한다. node를 정의한 함수에 넣고 결과에 따라서 다른 node로 분기되어 이동한다. </p>
<h3 id="22-그래프의-예시">2.2. 그래프의 예시</h3>
<p><strong>1. LLM 프록시 방식</strong> 
가장 간단한 방법으로 사용자가 입력한 요청을 그대로 LLM에게 전달하여 응답을 그대로 사용자에게 반환한다. </p>
<p><strong>2. 프롬프트 엔지니어링을 통한 개선</strong>
사용자의 입력과 사전에 정의된 가이드를 포함해 구조화된 문서의 형태로 LLM에게 구체적인 요청을 전달한다. </p>
<p><strong>3. 프롬프트 체이닝</strong></p>
<ul>
<li>단일 LLM + 여러 단계의 프롬프트 체이닝
여러 개의 프롬프트를 순차적으로 LLM에게 요청하고 각 단계의 출력을 다음 단계의 입력으로 사용한다. 모호한 질문을 답변에 따라서 명확하게 잡을 수 있음</li>
<li>다중 LLM + 역할 분리 체이닝
여러 LLM을 단계별로 활용하여 각 단계에서 특화된 역할을 수행하고 연결을 통해서 최종 응답을 생성한다. </li>
</ul>
<p><strong>4. RAG</strong>
프롬프트를 만들기 전에 외부DB에서의 관련 정보를 검색하여, 검색 문서와 사용자의 질문으로 구성한 프롬프트를 LLM에게 요청한다. </p>
<blockquote>
<p><strong>AI GENT</strong>는 목표 달성을 위해서 LLM의 답변을 잘 받아내야 한다. 
<strong>내부적인 판단은 모두 LLM이 한다.</strong></p>
</blockquote>
<ul>
<li>분기1) tool이 필요한가?</li>
<li>분기2) tool의 결과가 질문과 관련이 있는가?</li>
</ul>
<h3 id="23-그래프-구조-만들기-절차">2.3. 그래프 구조 만들기 절차</h3>
<p><strong>step1. 시스템 목표 설정</strong>
<strong>step2. LLM모델 선정</strong>
<strong>step3. Toolset 준비</strong>
<strong>step4. State 정의</strong>
<strong>step5. Node 정의</strong>
<strong>step6. 그래프 구조</strong>
<strong>step7. 그래프 실행</strong></p>
<hr />
<h2 id="3-state">3. State</h2>
<blockquote>
<p><strong>state</strong>는 그래프 전체에서 주고 받는 <strong>데이터 구조(틀)</strong> 을 정의한다.</p>
</blockquote>
<p>그래프의 노드의 입력과 출력를 관리하는 딕셔너리 형태의 자료형이다.
<strong>각 노드들은 입력과 출력을 state에 담아서 처리한다.</strong> </p>
<p><code>TypedDict 클래스</code> 를 사용해서 class의 형태로 state를 정의한다.
State라는 이름의 클래스로 state의 틀을 만들어준다.
클래스의 key이름과 type을 정해서 선언한다.</p>
<pre><code>from typing import TypedDict

class State(TypedDict):
    text: str
    step: int</code></pre><hr />
<h2 id="4-node">4. Node</h2>
<blockquote>
<p><strong>Node</strong>는 하나의 <strong>함수</strong>처럼 작동한다.</p>
</blockquote>
<p>노드의 입력과 출력은 모두 state 의 구조를 따른다. 노드는 state를 받아서 처리하고, 다시 state를 반환함으로써 그래프 흐름 내에서 <strong>일관된 데이터 구조를 유지</strong>한다. </p>
<p><strong>state는 매개변수</strong>이고, <strong>State</strong>는 해당 매개면수의 <strong>타입</strong>을 의미한다. </p>
<p>현재 입력 type은 State(선언한 클래스)이고 , <code>-&gt;</code> 는 <strong>출력 type의 hit</strong>로 State(선언한 클래스)인 것을 알려준다. </p>
<pre><code>def node_example(state: State) -&gt; State:
    state[&quot;text&quot;] += &quot; 처리됨&quot;
    return state</code></pre><hr />
<h2 id="5-graph">5. Graph</h2>
<h3 id="51-그래프-초기화">5.1. 그래프 초기화</h3>
<p><code>langgraph.graph</code>의 <code>StateGraph</code>를 통해서 그래프를 초기화 한다. 
<code>builder = StateGraph(State)</code>으로 state의 타입은 위에서 선언한 State클래스를 따르면서 builder라는 이름으로 그래프를 초기화한다.</p>
<h3 id="52-node-추가">5.2. Node 추가</h3>
<p>생성한 함수를 node로 추가한다. <code>add_node('별칭명', 함수명)</code>으로 노드를 추가한다. 
사용자가 적어주는 별칭명이** class에서의 key들의 이름과 겹치지 않아야 한다.**</p>
<h3 id="53-node-연결">5.3. Node 연결</h3>
<p>node간의 edge를 통해 연결한다. <code>add_edge(노드1, 노드2)</code>으로 2에서 선언한 노드의 이름을 넣어준다. </p>
<p>START와 END는 langgraph에서 고정으로 지정해준다. 
<code>add_edge(START, 노드2)</code> 는 <code>set_entry_point(노드2)</code>로 작성할 수 있다. 
<code>add_edge(노드1, END)</code> 는 <code>set_finish_point(노드1)</code>로 작성할 수 있다. </p>
<h3 id="54-그래프-compile">5.4. 그래프 compile</h3>
<p><code>graph = builder.compile()</code>으로 그래프를 컴파일한다. 
<code>graph.invoke({})</code>을 통해서 값을 넣고 그래프를 실행할 수 있다. </p>
<hr />
<h2 id="추가-state를-class로-정의하는-이유">[추가] state를 class로 정의하는 이유</h2>
<blockquote>
<p><strong>State</strong>를 <strong>class (TypedDict) 형태</strong>로 정의하는 이유는 <strong>&quot;일관성 있고, 오류 없는 흐름 관리&quot;</strong> 때문이다.</p>
</blockquote>
<p>딕셔너리만 사용할 때 | State 클래스 사용하는 경우
|--|--|
키 이름 실수해도 바로 에러가 안 나고, 오류 찾기 어려움 | 키와 타입이 정해져 있어 자동완성, 타입 검사 가능
흐름 중에 잘못된 필드 추가 가능 (일관성 깨짐) | 선언된 키 외에는 못 쓰게 막음
협업하거나 코드를 재사용할 때 구조를 알기 어려움 | 구조 명확, 문서화 없이도 어떤 데이터 쓰는지 알 수 있음</p>
<ul>
<li><p><strong>1. 일관성 유지</strong>
상태를 딕셔너리로만 관리하면 키 실수나 타입 오류가 생기기 쉬움
TypedDict로 클래스화하면 사용 가능한 <strong>key와 타입이 명확</strong>해져서 에러 방지 가능</p>
</li>
<li><p><strong>2. 흐름 전체의 통일된 데이터 구조 제공</strong>
그래프(또는 에이전트)가 공유하는 공식적인 상태 구조(state) 로 사용
어떤 노드든 동일한 State 구조를 기준으로 데이터를 주고받음</p>
</li>
</ul>
<hr />
<h2 id="6-conditional-edge조건부엣지">6. Conditional Edge(조건부엣지)</h2>
<blockquote>
<p><strong>conditional_edge</strong>는 조건에 따라서 분기하여 다른 노드로 이동한다.
<strong>조건 분기 함수(사용자 정의 함수)</strong>는 노드가 아니다.</p>
</blockquote>
<p>node는 처리만 하고 내보내기 때문에 조건에 따라서 어디로 보낼지는 정의하지 않는다. 그럼으로 <strong>조건을 판단하는 함수를 정의</strong>해주어야 한다. 이 함수는 <strong>노드가 아님을 유의한다</strong>. </p>
<p>사용자 정의함수로 조건 분기 함수를 <code>def path_function(state : State):</code> 와 같이 함수를 선언하고 <code>if문</code>을 통해서 <code>case1</code>과 <code>case2</code>의 조건을 작성해준다. </p>
<pre><code>def path_function(state : State):
    return 'case1' if 조건식 else 'case2'</code></pre><p>conditional_edge는 그래프를 구성할 때 <code>add_conditional_edges()</code>으로 함수로 그래프에서 edge로 조건에 맞게 연결해준다. 
<strong>조건 노드</strong>는 <strong>분기 이전의 노드</strong>를 의미한다. case와 node 순서로 딕셔너리 형태로 작성해주어야 한다. node의 이름과 case의 이름이 같으면 생략이 가능하다.</p>
<pre><code>builder.add_conditional_edges(
    &quot;조건노드&quot;,          # 조건 판단할 노드 이름
    path_function,       # 조건 판단 로직 (함수)
    {
        &quot;case1&quot;: &quot;노드1&quot;,  # 결과가 case1이면 → 노드1으로
        &quot;case2&quot;: &quot;노드2&quot;,  # 결과가 case2면 → 노드2로
    }
)</code></pre><hr />
<h2 id="7-기본-graph의-종류">7. 기본 Graph의 종류</h2>
<h3 id="71-간단한-그래프">7.1. 간단한 그래프</h3>
<p>입력, 처리, 출력 순으로 이어지는 단순한 흐름의 그래프이다. </p>
<h3 id="72-routing">7.2. Routing</h3>
<p><strong>Routing(라우팅)</strong> 은 특정 입력에 따라 서로 다른 경로를 선택하여 실행 흐름을 제어하는 기능이다. 사용자의 입력이나 특정 조건에 따라서 서로 다른 노드를 실행하도록 하다. 라우팅은  <strong>conditional edge</strong> 를 통해서 구현한다.</p>
<h3 id="73-reflection">7.3. Reflection</h3>
<p><strong>Reflection(리플렉션)</strong> 은 특정 입력에 따라서 분기를 하고 분<strong>기에 따른 노드 중 하나</strong>에서 분기 이전 노드로 다시 되돌아와서 <strong>분기 노드를 재실행</strong>하게 되는 플로우이다. 재고하는 과정과 같으며 박복적인 수행으로 <strong>점진적으로 성능을 향상</strong>시킨다. </p>
<p>보통은 state 정의에서 <strong>bool타입의 변수</strong>나 <strong>int타입의 변수</strong>를 선언해서 조건의 만족하는지의 여부의 척도를 추가하여 <strong>판단의 기준</strong>으로 이용한다. </p>
<pre><code>class State(TypedDict):
    text: str
    is_valid: bool       # 조건 만족 여부
    score: int           # 점수 또는 단계 수준
</code></pre><blockquote>
<p><strong>분기가 일어나는 노드</strong> <strong>안</strong>에서 <strong>만족 여부를 확인하는 코드</strong>를 추가한다. 
분기노드 내 코드에서의 <strong>판단 척도</strong>를 <strong>기준</strong>으로 <strong>조건 분기 함수에서</strong> case1과 case2를 세운다.</p>
</blockquote>
<hr />
<h2 id="8-tools">8. Tools</h2>
<p>LLM은 사용자의 입력을 받아 응답을 생성한다. LLM은 계산이나 검색, APi호출, 파일 처리와 같은 실질적인 행위는 못한다. GPT나 LangGraph 에이전트가 모든 것을 직접 알지는 못하기 때문에 tool을 선택해 호출한다. </p>
<p>이러한 기능을 함수로 정의하여 tool를 만들거나, llm의 내장된 tool을 불러서 llm이 필요할 때 불러 쓸 수 있게 해주는 도구가 tool이다.</p>
<h3 id="81-비교-일반-vs-tool-기반-agent">8.1. 비교: 일반 vs tool 기반 Agent</h3>
<p><strong>일반적인 state 선언</strong></p>
<pre><code>class State(TypedDict):
    num: int
    is_correct: bool</code></pre><p><strong>tool기반 ai agent</strong></p>
<pre><code>class State(TypedDict):
    messages: Annotated[list, add_messages]</code></pre><ul>
<li>messages: LLM이 주고받은 대화 메시지를 추적하는 필드</li>
<li>Annotated: Python 타입 주석 확장 도구</li>
<li>add_messages: LangGraph에서 메시지를 추가·관리하기 위한 메타데이터 역할 함수</li>
</ul>
<blockquote>
<p><strong>llm과 사용자가 주고 받는 메시지</strong>를 계속 <strong>누적해서 자동 저장</strong>한다.
이전의 대화를 참고해서 새로운 응답과 함께 messages를 생성하기 위함이다.</p>
</blockquote>
<h3 id="82-custom-tool">8.2. Custom tool</h3>
<p>사용자 함수 선언을 통해서 tool을 정의하고 llm에게 도구로 제공해줄 수 있다. </p>
<p><strong>사용자 정의 tool를 작성할 때는 아래의 2가지를 주의해서 작성해야 한다.</strong></p>
<ul>
<li><strong>데코레이터</strong>를 통해서 함수를 도구라고 등록해준다. =&gt; 함수를 도구로 등록</li>
<li><strong>doc_string</strong>이라고 tool이 하는 과정을 설명해주는 부분을 함수 선언 바로 아래에 작성한다. =&gt; 도구에 대한 설명<pre><code>from langchain.tools import tool</code></pre></li>
</ul>
<ol>
<li>tool 함수 선언
@tool
def 함수이름(입력값: 타입) -&gt; 반환타입:
 &quot;&quot;&quot;도구 설명 (LLM이 읽을 수 있음)&quot;&quot;&quot;<h1 id="기능-구현">기능 구현</h1>
 return 결과<pre><code></code></pre></li>
</ol>
<h4 id="case1-수식을-계산해주는-tool">case1) 수식을 계산해주는 tool</h4>
<pre><code>@tool
def calculator_tool(expression: str) -&gt; str:  # type hint : 함수의 출력 type은 str
    '''수식을 입력 받아 계산하는 도구''' 
    try:
        result = eval(expression)  # Python 내장 함수 eval()을 사용해서 문자열로 된 식을 계산
        return f&quot;계산 결과: {result}&quot;
    except Exception as e:
        return f&quot;오류 발생: {str(e)}&quot;</code></pre><h4 id="case2-llm에게-메시지를-전달해주는-tool">case2) llm에게 메시지를 전달해주는 tool</h4>
<pre><code>def call_model(state: State):
    messages = state[&quot;messages&quot;]
    response = llm_with_tools.invoke(messages)
    return {&quot;messages&quot;: [response]}</code></pre><h4 id="tool-등록-및-toolnode-인스턴스-생성">tool 등록 및 ToolNode 인스턴스 생성</h4>
<ul>
<li><p>@tool 데코레이터
python 함수에 <code>@tool</code>를 붙이면 langchain에서 tool 도구로 등록한다.
<code>tools</code> 리스트에 담아서 tool 목록을 보관한다.</p>
</li>
<li><p><code>llm.bind_tools(tools)</code>
llm.bind_tools(tools)는 LLM이 사용할 수 있는 도구 목록을 등록하는 작업이다.
tool 목록인 <code>tools</code>를 bind할 때 붙인다. </p>
</li>
<li><p><em>llm*</em>은 <strong>필요하면 이 도구를 써도 된다는 권한</strong>을 가지게 된다.</p>
</li>
<li><p>ToolNode 생성
그래프에서 노드로 사용할 수 있도록 감싸주는 클래스이다.
tools 리스트를 넣어서 tool node 객체를 만들어준다.</p>
</li>
<li><p><code>tool_calls</code></p>
</li>
<li><p><em>tool_calls*</em>는 <strong>속성</strong>으로, llm이 도구 사용을 결정하면, 해당 도구를 호출라하는 의도를 담은 정보가 담긴다. 
tool_calls는 llm이 반환하는 응답 메시지의 일부이고, 리스트 형태의 변수로 <strong>어떤도구</strong> 와 <strong>어떤 인자</strong> 가 <strong>딕셔너리 구조로 리스트</strong>에 담겨있다.
<code>{&quot;tool_name&quot;: ..., &quot;arguments&quot;: {...}}</code> 형태의 딕셔너리
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/56c6d0c1-0ad2-493a-94f4-9afff3f72ad2/image.png" />
last_message = message[-1]안에 too_calls가 있으면 tools를 사용하도록 이동한다. *<em>tool_calls 속성은 도구를 호출하려고 할 때만 포함된다. *</em></p>
</li>
</ul>
<h3 id="83-내장-tool">8.3. 내장 tool</h3>
<blockquote>
<p>tool도 그래프에서 노드가 된다.</p>
</blockquote>
<ul>
<li><p>load_tools
<code>tools = load_tools([&quot;llm-math&quot;, &quot;wikipedia&quot;], llm=llm)</code></p>
</li>
<li><p><em>일부 내장 tool들*</em>은 사용을 위해서 llm이 필요함으로 <strong>tool 사용을 위한 llm을 로드</strong>한다. </p>
</li>
<li><p>ToolNode 객체
ToolNode 클래스로 tools 리스트를 넣어서 그래프에서 사용할 tool node를 만든다.</p>
</li>
<li><p>llm.bind_tools(tools)
llm을 정의할 때 <strong>tools리스트를 바인딩</strong> 하여 <strong>llm 호출할 수 있는 tool 목록을 연결</strong>한다.</p>
</li>
<li><p>선언하는 조건 분기 함수
분기 함수에서 llm과의 대화에서 가장 마지막 문장을 last_messages객체에 담아서 tool가 필요한지 확인한다. </p>
</li>
<li><p><code>last_message.tool_calls</code>
last_message는 llm의 마지막 응답 메시지를 담은 객체이고, 객체의 속성 중의 하나로 tool_calls가 정의되어 <code>last_message.tool_calls</code>로 접근한다.
<code>.tool_calls</code> 으로 <strong>llm이 어떤 도구를 쓰려고 했는지 확인</strong>이 가능하다.</p>
</li>
</ul>
<hr />
<h2 id="9-memory">9. Memory</h2>
