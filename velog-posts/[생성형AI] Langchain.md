---
title: "[생성형AI] Langchain"
date: "2025-04-21"
link: "https://velog.io/@ehekaanldk/%EC%83%9D%EC%84%B1%ED%98%95AI-Langchain"
series: "Uncategorized"
---

<p><strong>LLM 체인의 구성요소</strong>
LLM 체인은 prompt와 LLM의 결합으로 LLM기반 애플리케이션 개발에 핵심적인 개념 중 하나이다.
사용자의 입력인 프롬프트를 받아서 LLM을 통해 적절한 응답이나 결과를 생성하는 구조이다. </p>
<ul>
<li>프롬프트 : LLM에게 특정 작업을 수행하도록 요청하는 지시문</li>
<li>LLM : 대규모 언어 모델로 LLM은 프롬프트를 바탕으로 적절한 응답을 생성하거나, 주어진 작업을 수행한다.</li>
</ul>
<h2 id="1-langchain">1. Langchain</h2>
<p>LangChain은 대규모 언어 모델인 LLM을 활용하여 체인을 구성해 복작한 작업을 자동화하고 쉽게 수행할 수 있는 프레임워크이다. </p>
<p><strong>LLM 체인의 구성요소</strong>
LLM 체인은 prompt와 LLM의 결합으로 LLM기반 애플리케이션 개발에 핵심적인 개념 중 하나이다.
사용자의 입력인 프롬프트를 받아서 LLM을 통해 적절한 응답이나 결과를 생성하는 구조이다. </p>
<ul>
<li>프롬프트 : LLM에게 특정 작업을 수행하도록 요청하는 지시문</li>
<li>LLM : 대규모 언어 모델로 LLM은 프롬프트를 바탕으로 적절한 응답을 생성하거나, 주어진 작업을 수행한다.</li>
</ul>
<p><strong>구성요소</strong></p>
<ul>
<li><p><strong>모델</strong> : 답변을 생성하는 두뇌</p>
<ul>
<li><code>OpenAI()</code>, <code>ChatOpenAI()</code>, <code>HuggingFaceHub()</code>로 모델을 불러온다.</li>
</ul>
</li>
<li><p><strong>프롬프트</strong> : 모델이 무엇을 해야 할지 알려주는 지시문</p>
<ul>
<li><code>PromptTemplate</code> : 단일 문장 기반</li>
<li><code>ChatPromptTemplate</code> : 역할(role)이 포함된 대화 기반</li>
<li><code>{변수}</code>를 포함해서 사용자 입력을 동적으로 받을 수 있다. </li>
</ul>
</li>
<li><p><strong>체인</strong> : 프롬프트 -&gt; 모델 -&gt; 결과 까지의 흐름을 묶은 것</p>
<ul>
<li><code>LLMChain()</code></li>
</ul>
</li>
<li><p><strong>메모리</strong> : 대화를 기억하고 이전 질문/답변을 저장</p>
<ul>
<li><code>ConversationBufferMemory</code></li>
<li><code>ConversationSummartMemory</code></li>
<li><code>ConversationWindowMemory</code></li>
<li>이전 대화 내용을 저장해서 저장된 내용을 참조해서 답변을 준다.</li>
</ul>
</li>
<li><p><strong>인덱스</strong> : 검색을 위한 문서 저장소 구조</p>
<ul>
<li>문자을 임베딩하고 Vector DB에 저장</li>
<li><code>Chroma</code>, <code>FAIss</code>,  <code>Weaviate</code></li>
<li>RAG에서 핵심</li>
</ul>
</li>
<li><p><strong>에이전트와 도구</strong> : 모델이 스스로 어떤 도구를 쓸지 판단하고 실행하는 구조</p>
<ul>
<li>Agent : 결정하는 AI</li>
<li>Tools : 계산기, 검색기 등 외부 기능</li>
</ul>
</li>
<li><p><strong>LangGraph</strong> : 체인보다 더 복잡한 흐름을 설계할 수 있는 그래프 구조</p>
</li>
</ul>
<hr />
<h2 id="2-model">2. Model</h2>
<p>Langchain에서 사용할 수 있는 모델들에 대해서 알아본다. 대표적으로 OpenAI 플랫폼과 Huggingface 플랫폼에서의 모델을 가져온다.</p>
<ul>
<li>OpenAI : ChatOpenAI, OpenAI</li>
<li>HuggingFace : HuggingFaceHub</li>
</ul>
<h3 id="21-open-ai의-langchain의-함수-chatopenai를-사용해서-모델을-불러온다">2.1. <strong>open AI의 langchain의 함수</strong> <code>ChatOpenAI</code>를 사용해서 모델을 불러온다.</h3>
<p><code>ChatOpenAI</code>는 대화형 모델을 불러오는 용도이다.</p>
<p><strong>모델을 사용하는 방법</strong>
(1) <code>llm.invoke(prompt)</code> 또는 <code>llm(messages)</code>로 호출한다.</p>
<pre><code>from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model_name = '모델이름')
response = chat.invoke(&quot;세계에서 가장 큰산은?&quot;)
print(response.content)</code></pre><p>사람의 질문을 <strong>HumanMessage</strong>, llm의 답변을 <strong>AIMessage</strong>이다.
여러개의 값을 받는 리스트로 역할을 부여한다. </p>
<pre><code>sys_role = 'AI답변 역할'
question = &quot;Human 질문&quot;

result = chat.invoke([
    HumanMessage(content = question), 
    SystemMessage(content = sys_role)])
result</code></pre><p>(2) 프롬프트와 함께 chain으로 묶는다. =&gt; <code>chain.run()</code></p>
<pre><code>from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

# 1. 프롬프트 템플릿
prompt = PromptTemplate.from_template(&quot;오늘 {city}의 날씨는 어때?&quot;)

# 2. 모델 선언
llm = ChatOpenAI(model_name=&quot;gpt-3.5-turbo&quot;)

# 3. 체인 연결 (프롬프트 + 모델)
chain = LLMChain(prompt=prompt, llm=llm)

# 4. 실행
response = chain.run(city=&quot;서울&quot;)

# 5. 출력
print(response)</code></pre><h3 id="22-huggingfacehub로-모델을-사용한다">2.2. <strong>huggingfaceHub로</strong> 모델을 사용한다.</h3>
<p>huggingface의 모델을 다운받은 것이 아니라 <strong>API로 접근하는 방식</strong>이다. </p>
<pre><code>llm = HuggingFaceHub(
    repo_id = &quot;모델명&quot;,
    model_kwargs={&quot;temperature&quot;: 0.5, &quot;max_new_tokens&quot;: 100},
    task = &quot;테스크명 선언&quot;
)
response = llm(&quot;질문&quot;)</code></pre><p><strong>huggingface에서 모델을 로컬에서 다운로드 받아서</strong> 사용하는 방식이다. </p>
<pre><code>generator = pipeline(
    &quot;text-generation&quot;,
    model=&quot;gpt2&quot;,  # 또는 &quot;tiiuae/falcon-7b-instruct&quot; 등
    max_new_tokens=100,
    temperature=0.7
)

llm = HuggingFacePipeline(pipeline=generator)</code></pre><h3 id="23-chain의-역할">2.3. Chain의 역할</h3>
<p>chain으로 조합을 해서 <code>사용자 질문 -&gt; 프롬프트 템플릿 -&gt; LM호출 -&gt; 파싱 -&gt; DB저장 -&gt; 다음 질문과 연결 과정</code>을 묶어주는 자동화 도구이다.</p>
<pre><code>prompt = PromptTemplate.from_template(&quot;사용자 질문: {question}&quot;)
chain = LLMChain(llm=llm, prompt=prompt)
output = chain.run(question=&quot;기후 변화에 대해 알려줘&quot;)</code></pre><p><strong>파싱(Output Parser)</strong>
LLM이 자유롭게 답변한 텍스트를 원하는구조로 정리한다. </p>
<p>문자열 =&gt; 리스트
문자열 =&gt; 딕셔너리
문자열 =&gt; JSON 구조 등으로 변환</p>
<p><strong>DB 저장</strong>
파싱된 데이터를 기록하는 단계이다. 
질문/답변을 기록하고 분석한다.</p>
<p><strong>다음 질문과 연결</strong>
memory / context : 이전의 대화를 기억해서 대화의 흐름을 이어간다.</p>
<hr />
<h2 id="2-prompt">2. Prompt</h2>
<blockquote>
<p>프롬프트는 인간이 인공지능(LLM)에게 전달하는 지시문이다. </p>
</blockquote>
<p>HumanMessage : 사용자의 메시지
AIMessage : LLM의 응답 및 답변</p>
<p><strong>모델에게 전달되는 프롬프트는 결국 &quot;현재 질문 + 과거 대화의 기록&quot;이고, 그 전체가 모델 입장에서 “지금 내가 뭘 대답해야 하는지”를 결정하는 재료가 된다.</strong></p>
<p>이전 기억은 메모리에 담고, 현재 질문은 프롬프트에 넣는다. </p>
<p>방식 | 클래스 | 용도
|--|--|--|
일반 템플릿 | PromptTemplate | 문장 1개 기반 템플릿
대화 템플릿 | ChatPromptTemplate | ChatGPT 스타일 역할 기반 메시지 템플릿</p>
<p>langchain의 프롬프트</p>
<ul>
<li>PromptTemplate : 변수 기반 동적 프롬프트 생성</li>
<li>ChatPromptTemplate: 여러 메시지를 구조화하여 대화 설계</li>
</ul>
<h3 id="21-prompttemplate-기본-프롬프트-템플릿">2.1. PromptTemplate (기본 프롬프트 템플릿)</h3>
<p>사용자 입력을 동적으로 받을 수 있는 변수를 선언해 <strong>프롬프트에 변수를 담아서 사용</strong>한다. 
문장 안에 {변수}를 넣어서, 나중에 동적으로 문장을 완성할 수 있다.</p>
<ul>
<li>Input_variables : 템플릿 입력 변수 지정</li>
<li>template : 입력 변수를 {}로 표현하여 템플릿을 구성</li>
</ul>
<p>리스트 안에 문자열 형식으로 입력 변수를 선언해준다. 템플릿을 지정해서 변수만 바꾸어주면 바로 적용이 가능하다.</p>
<p>PromptTemplate와 llm을 선언하고, LLMChain으로 llm과 prompt를 연결해준다.
<strong>chain.run()</strong>은 프롬프트에 변수를 채워 넣고, LLM에게 질문하고 결과를 받는 과정을 한번에 실행하는 메서드이다.</p>
<pre><code>prompt = PromptTemplate(
    Input_variables=['변수명1', '변수명2'],
    template = &quot;{변수명1} 언어로 번역한다 : {변수명2}&quot;
)
llm = ChatOpenAI(model_name='모델명', temperature=0)
chain = LLMChain(prompt=prompt, llm=llm)

print(chain.run({&quot;변수명2&quot;: &quot;I love Gen AI&quot;, &quot;변수명1&quot;: &quot;한국어&quot;}))</code></pre><p>temperature는 확률분포로 내부적인 단어의 후보를 로짓으로 계산한 뒤에 softmax로 학률을 변환한 값에 기준을 세운다. </p>
<ul>
<li>0에 가까우면 높은 확률의 단어를 골라서 일관되게 예측을 한다. </li>
<li>1에 가까우면 낮은 확률의 단어를 골라서 창의성을 부여한다. </li>
</ul>
<h3 id="22-chatprompttemplate-대화형-템플릿">2.2. ChatPromptTemplate (대화형 템플릿)</h3>
<p>역할별로 메시지를 구분해서 여러개를 기반으로 프롬프트를 구성한다.
다중 메시지를 기반으로 프롬프트의 흐름을 구성할 수 있도록 도와준다.</p>
<ul>
<li>SystemMessage : AI에게 역할/성격을 지정 (모델에게 역할을 부여)</li>
<li>HumanMessage : 사용자 질문 또는 요청</li>
<li>AIMessage : AI 응답</li>
</ul>
<p>직접 메시지들의 리스트를 받기 때문에 <code>from_messages()</code>를 거의 항상 사용한다. </p>
<pre><code>s_msg = &quot;system message로 역할을 부여한다.&quot;
h_msg = &quot;human message로 사용자의 질문을 넣어준다.&quot;
chat_prompt = ChatPromptTemplate.from_messages([
    (&quot;system&quot;, s_msg),
    (&quot;human&quot;, h_msg),
])
llm = ChatOpenAI(model_name = '모델명', temperature=1.1, model_kwargs={&quot;top_p&quot;: 0.95})

messages = chat_prompt.format_messages()
response = llm(messages)</code></pre><ul>
<li><code>ChatPromptTemplate.from_messages()</code>는 역할과 메시지를 정의하는 템플릿이다.</li>
<li><code>format_messages()</code>을 템플릿에서 호출해주면 역할(role)이 붙은 메시지 객체 리스트가 반환된다..</li>
<li><code>messages</code>의 형태는 아래와 같다.<pre><code>[
  SystemMessage(content=&quot;system message로 역할을 부여한다.&quot;),
  HumanMessage(content=&quot;human message로 사용자의 질문을 넣어준다.&quot;)
]</code></pre></li>
<li>모델에게 메시지 리스트를 전달하면 모델이 각 역할을 이해하고 문맥에 맞게 응답한다.</li>
</ul>
<h3 id="추가-format_message">[추가] format_message()</h3>
<p>Python에서의 print() 문에 format() 메서드와 같은 의미이다.
LangChain에서도 프롬프트 템플릿 안에 {변수}가 있을 경우, format_messages()를 통해 그 값을 실제로 넣어주는 과정이 필요하다.</p>
<p>LangChain에서 ChatPromptTemplate.from_messages()는 메시지의 틀(템플릿)을 정의하는 단계이고,
format_messages()는 그 틀에 데이터를 채워 실제로 LLM이 이해할 수 있는 메시지를 만드는 단계이다.</p>
<hr />
<h2 id="3-파싱output-parser">3. 파싱(Output Parser)</h2>
<blockquote>
<p>파싱은 문자열을 잘라서, 내가 원하는 구조화된 데이터로 바꿔주는 작업이다. </p>
</blockquote>
<p><code>text = &quot;apple, banana, orange&quot;</code>를 <code>[&quot;apple&quot;, &quot;banana&quot;, &quot;orange&quot;]</code>으로 바꾸어주는 것이 파싱이고, 이 일을 해주는 것이 파서이다.</p>
<p><strong>llm은 항상 텍스트로만 주기 때문에</strong> 그 텍스트를 내가 <strong>쓰기 좋게 바꿔주는 도구</strong>가 바로 lanchain의 output parser이다. </p>
<p>리스트 형태나 딕셔너리 형태의 데이터를 받아야 할 때, 틀을 고정해서 제공하면 틀에 맞게 답변을 해준다.</p>
<p><strong>Output Parser의 종류</strong></p>
<ul>
<li>CommaSeparatedListOutputParser : 쉼표 구분 문자열 → 리스트로 변환</li>
<li>PydanticOutputParser : 텍스트 → Pydantic 모델로 파싱</li>
<li>StructuredOutputParser : JSON 기반 구조화 파싱</li>
</ul>
<p>Pydantic에 맞는 자료형을 사용하고 자료형이 맞는지 확인해준다...?</p>
<h3 id="commaseparatedlistoutputparser">CommaSeparatedListOutputParser</h3>
<ul>
<li>콤마로 구분된 결과이여야 리스트로 변환이 된다. =&gt; LLM이 쉼표로 나눈 텍스트를 생성한다는 전제하에 작용된다.</li>
<li>프롬프트에 꼭 &quot;쉼표로 구분해줘&quot;라고 작성해야 한다. </li>
</ul>
<blockquote>
<p><strong>쉼표로 구분된 텍스트</strong> -&gt; <strong>리스트</strong>로 변환</p>
</blockquote>
<ul>
<li><p>출력 파서 선언
사용할 <code>CommaSeparatedListOutputParser()</code>를 선언해준다. </p>
</li>
<li><p>프롬프트 템플릿 구성
ChatPromptTemplate으로 프롬프트 템플릿을 구성하고 system에게 <code>format_insturctions</code> 자리에 &quot;쉼표로 말해줘!&quot;와 같은 출력 형식 힌트를 넣는다.</p>
</li>
<li><p>포멧팅 힌트 넣기
<code>parser.get_format_instructions()</code>가 포맷팅 힌트를 준다.
선언한 <code>CommaSeparatedListOutputParser()</code>안에 <code>get_format_insrunctions()</code>함수를 통해서 LLM에게 쉼표 구분 응답을 하라고 힌트를 준다.</p>
</li>
<li><p>모델 호출
<code>response = llm.invoke(formatted_messages)</code> 는 메세지 리스트를 모델에 넣고 응답을 받아온다. 
구성한 프롬프트를 llm.invoke()안에 넣어주고 응답을 받으면 아직 그냥 텍스트 형태이다. (예: &quot;치킨, 피자, 떡볶이, 라면, 김밥&quot;)</p>
</li>
<li><p>파싱으로 리스트 만들기
<code>parser.parse()</code>에서 응답 텍스트를 <code>CommaSeparatedListOutputParser</code>가 split() 해서 리스트로 변환</p>
</li>
</ul>
<p><strong>Parser = CommaSeparatedListOutputParser()</strong> 에는 아래와 같은 역할을 한다.</p>
<ul>
<li><code>.get_format_instrunctions()</code>으로 모델에게 줄 포맷 힌트 문장을 생성한다.</li>
<li><code>.parse(output_text)</code>는 쉼표로 된 텍스트로 split(',')해서 리스트로 변환한다.</li>
</ul>
<p>그럼으로 {format_instructions} 자리에 parser.get_format_insturctions() 로 모델에게 줄 포맷 힌트 문장이 생성되어 담긴다.
힌트 문장은 <code>Your response should be a comma-separated list of values, like: `item1, item2, item3`</code>과 같다.</p>
<h3 id="structuredoutputparser">StructuredOutputParser</h3>
<blockquote>
<p>LLM의 응답을 JSON처럼 정해진 구조로 받고 결과를 Python dict(schema)으로 파싱한다.</p>
</blockquote>
<p>복잡한 데이터 구조인 딕셔너리나 리스트가 포함되었을 때 사용된다. </p>
<ul>
<li><p>스카마를 정의한다. 
출력하고자 하는 구조의 형식을 정의한다. </p>
<pre><code>schemas = [
  ResponseSchema(name=&quot;headline&quot;, description=&quot;뉴스 제목&quot;),
  ResponseSchema(name=&quot;summary&quot;, description=&quot;뉴스 내용을 한 문장으로 요약&quot;)
]</code></pre></li>
<li><p>파서를 생성한다.
스키마를 기반으로 변환하기 때문에 <code>.from_respnnse_schemas(schemas)</code> 를 추가로 작성해주어야 한다. 
<code>parser = StructuredOutputParser.from_response_schemas(schemas)</code>는 schemas를 기반으로 모델에게 <strong>출력 형식의 힌트</strong>를 알려주고, 결과를 <strong>딕셔너리 형태로 바꾸어주는 기능</strong>을 담당한다.</p>
</li>
<li><p>프롬프트를 구성한다.</p>
<ul>
<li>&quot;system&quot;: 역할 설정</li>
<li>&quot;human&quot;: 사용자 질문</li>
<li>&quot;system&quot;: {format_instructions} ← 여기 출력 힌트가 들어갈 자리</li>
</ul>
</li>
<li><p>형식 힌트 삽입
LLM이 스키마 구조에 맞게 힌트 {&quot;key1&quot; : &quot;value1&quot;, &quot;key2&quot; : &quot;value2&quot;}를 얻게 된다. </p>
<pre><code>messages = prompt.format_messages(
  format_instructions=parser.get_format_instructions()
)</code></pre></li>
</ul>
<ul>
<li>모델 호출
<code>response = llm.invoke(messages)</code> 로 LLM이 ChatPrompt를 읽고 JSON 형태로 응답을 생성한다. (예: &quot;{&quot;headline&quot;: &quot;손흥민 해트트릭&quot;, &quot;summary&quot;: &quot;손흥민이 놀라운 활약으로 승리를 이끌었다.&quot;}&quot;)</li>
</ul>
<ul>
<li>파싱
텍스트 응답을 딕셔너리로 변환한다. <code>result = parser.parse(response.content)</code></li>
</ul>
<pre><code>{
    &quot;headline&quot;: &quot;손흥민 해트트릭&quot;,
    &quot;summary&quot;: &quot;손흥민이 놀라운 활약으로 승리를 이끌었다.&quot;
}</code></pre><h3 id="pydanticoutputparser">PydanticOutputParser</h3>
<blockquote>
<p>LLM의 응답을 <strong>딕셔너리처럼 정리</strong>할 뿐만 아니라, 그 안에 <strong>각 필드가 어떤 타입이여야 하는지</strong>까지 <strong>검증</strong>하는 엄격한 파서이다. </p>
</blockquote>
<p>JSON은 단순히 구조만 갖췄을 뿐,</p>
<ul>
<li>&quot;name&quot;은 꼭 문자열이어야 해!</li>
<li>&quot;likes&quot;는 리스트 아니면 에러야!</li>
</ul>
<p>같은 타입 검증은 못 한다.</p>
<p>다른 시스템들 간의 데이터를 주고 받을 때는 json을 사용한다. 
json과 동일한데 스키마 이름만 지정한다. 
스키마의 값의 타입을 지정해야 할 때는 PydanticOutputParser를 사용해야 한다.</p>
<ul>
<li>Pydantic모델을 정의한다.
정보를 받아오는 틀인 Pydantic 모델을 선언한다. 
값의 타입을 고정해준다.<pre><code>from pydantic import BaseModel
</code></pre></li>
</ul>
<p>class Person(BaseModel):
    name: str
    age: int
    likes: list[str]</p>
<pre><code>
- 파서를 생성한다. 
```PydanticOutputParser([pydantic_object=Person)``` 파서는 정보의 틀을 받아 올 수 있도록 변수로 넣어준다.
```parser = PydanticOutputParser(pydantic_object=Person)```는 llm에게 어떻게 출력해야할지 가이드와 모델의 응답을 자동으로 Person객체로 바꾸어 주는 기능을 가진다.

- 프롬프트 템플릿 구성
    - system: LLM에게 역할 부여 (너는 어떤 도우미야!)
    - human: 사용자의 요청 (사람 정보 생성 요청)
    - system: 파서가 제공할 출력 형식 지침이 들어갈 자리 {format_instrunctions}

- 형식 가이드/힌트 입력
``` messages = prompt.format_messages(format_instructions=parser.get_format_instructions())``` 으로 힌트를 {format_instrunctions}에 넣어준다. 
```{format_instrunctions}```에는 아래와 같은 내용이 들어간다. </code></pre><p>The output should be a JSON object with the following fields:</p>
<ul>
<li><p>name: string</p>
</li>
<li><p>age: integer</p>
</li>
<li><p>likes: array of strings</p>
<pre><code></code></pre></li>
<li><p>모델 호출
<code>response = llm.invoke(messages)</code> 으로 llm에게 메시지를 주고 아직은 문자열 형태의 답변을 받아온다. </p>
</li>
<li><p>응답 변환
<code>person = parser.parse(response.content)</code> 문자열 형태의 답변을 person 객체로 변환한다. </p>
</li>
</ul>
<p><strong>system 메시지</strong>에는 <strong>PydanticOutputParser.get_format_instructions()</strong> 로 생성한 출력 형식 설명을 넣어, LLM이 정확한 구조(JSON)로 응답하도록 유도한다.</p>
<h2 id="4-출력방식">4. 출력방식</h2>
<p>LangChain에서 LLM의 출력 방식은 invoke(프롬프트)와 stream() 이 있다. </p>
<h3 id="41-invoke--일반적인-호출-방식-한-번에-결과받기">4.1. invoke : 일반적인 호출 방식 (한 번에 결과받기)</h3>
<p><code>invoke()</code>는 메시지를 LLM에게 넘기고 <strong>LLM이 다 생성한 후</strong>에 <strong>전체 응답을 한번에</strong> 받는다. </p>
<pre><code>response = llm.invoke(messages)
print(response.content)</code></pre><h3 id="42-stream--스트리밍-방식-한-글자씩-받아오기">4.2. stream : 스트리밍 방식 (한 글자씩 받아오기)</h3>
<p><code>stream()</code>은 LLM이 <strong>텍스트를 생성</strong>하면서 <strong>조금씩 실시간으로 결과를 반환</strong>한다. </p>
<ul>
<li><p>streaming = True
<code>llm = ChatOpenAI(..., streaming=True)</code> 으로 LLM이 실시간으로 토큰을 생성하면서 응답을 보낼 수 있도록 허용한다. </p>
</li>
<li><p>ll.stream(messages)
생성 중인 토큰들을 작은 단위인 청크로 계속 보내준다. </p>
<pre><code>for chunk in llm.stream(messages):
  print(chunk.content, end=&quot;&quot;)</code></pre></li>
</ul>
<h2 id="5-memory">5. Memory</h2>
<p>대화의 맥락을 이어가려면 <strong>이전 대화를 기억</strong>하면서 이전 질문 답변을 <strong>memory에 저장</strong>하고 이를 <strong>prompt에 포함</strong>시킨다.</p>
<blockquote>
<ul>
<li>메모리는 이전의 대화를 기억하는 것이다.</li>
</ul>
</blockquote>
<ul>
<li>chain과 엮어야만 memory를 사용할 수 있다. </li>
</ul>
<p>메모리 = 버퍼</p>
<p><strong>메모리의 역할</strong></p>
<ol>
<li>사용자의 질문 HumanMessage와 </li>
<li>모델의 답볍 AIMessage를 </li>
<li>내부에 자동 저장한다. </li>
<li>다음 프롬프트에 자동으로 붙여준다. </li>
</ol>
<p><strong>Memory의 종류</strong>
대화 메모리 : 모든 대화를 순차적으로 그대로 저장한다. 
요약 메모리 : 핵심의 대화만 저장한다.
윈도우 메모리 : 동일한 간격으로 최근 N턴만 기억한다. 이외는 삭제한다.</p>
<h3 id="conversationbuffermemory">ConversationBufferMemory</h3>
<p>모든 대화 내용을 토씨하나 안틀리고 그대로 저장한다. </p>
<p>어떤 memory를 사용할지 선언한다. 사용할 llm을 선언해 준다. 
mermory와 llm을 ConverstionChain으로 묶어준다.
chain은 run()으로 실행해준다.</p>
<pre><code>from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
llm = ChatOpenAI(model_name = '모델명' ,temperature = 0.5)
chain = ConversationChain(llm=llm, memory=memory)

print(chain.run(&quot;안녕? 나는 00이야.&quot;))
print(chain.run(&quot;내 이름이 뭐라고?&quot;))</code></pre><ul>
<li><p>메모리 객체를 선언한다. 
<code>memory = ConversationBufferMemory()</code>
메모리를 만들면 아직은 아무것도 저장되어 있지 않다. </p>
</li>
<li><p>모델을 선언한다. 
ChatOpenAI() 함수를 사용해서 모델을 불러온다. </p>
</li>
<li><p>체인을 선언한다. (메모리와 모델 결합)
<code>ConversationChain(llm=llm, memory=memory)</code>으로 모델과 메모리를 연결해서 <strong>대화형 체인</strong>을 완성한다 </p>
</li>
<li><p>질문한다.
<code>print(chain.run(&quot;안녕? 나는 00이야.&quot;))</code> </p>
<blockquote>
<p>chain을 실행할 때는 run()
llm을 실행할 때는 invoke()</p>
</blockquote>
</li>
<li><p>주고 받은 모든 메시지를 확인한다.
memory에 대화 내용이 차곡차곡 저장되어 HumanMessage와 AIMessage가 쌍으로 저장된다. 
<code>memory.chat_memory.messages</code>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/d7603ed4-90cb-4976-8191-e178864ecfc5/image.png" /></p>
</li>
</ul>
<h3 id="conversationsummarymemory">ConversationSummaryMemory</h3>
<p>이전의 대화 내용을 모두 기억하지 않고, 중요한 대화 내용을 요약해서 메모리에 저장한다. </p>
<p>요약은 llm이 하기 떄문에 요약용 llm을 호출해주어야 한다. 
요약의 범위는 이전 요약 + 새 메시지들만 요약해서 업데이트 해준다. </p>
<pre><code>from langchain.memory import ConversationSummaryMemory

# 요약 메모리 생성 (요약용 LLM 필요)
memory = ConversationSummaryMemory(llm = llm)

# 체인 구성
chain = ConversationChain(llm = llm, memory = memory)

# 대화
print(chain.run(&quot;오늘은 운동하고, 친구랑 밥도 먹고, 강의도 들었어.&quot;))</code></pre><ul>
<li><p>메모리 객체 선언
<code>ConversationSummaryMemory(llm = llm)</code>으로 memory를 선언하면서 memory에 담을 내용인 요약을 담기 위해서 <strong>요약용 llm을 지정</strong>해주어야 한다. 현재는 같은 llm을 요약과 응답에 모두 사용하고 있다.</p>
</li>
<li><p>체인 연결
mermory와 llm을 ConverstionChain으로 묶어준다.</p>
</li>
<li><p>질문한다.
chain은 run()으로 실행해준다.</p>
</li>
<li><p>담긴 메모리 확인한다. 
<code>memory.chat_memory.messages</code> 로 지금까지 주고받은 모든 메시지를 확인한다. 프롬프트에 전달되는 내용은 아니고 메시지 객체 리스트의 형태이다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/f4fb6c4d-90f3-430d-9a77-5b895747e158/image.png" /></p>
</li>
<li><p>요약 내용을 확인한다.
<code>memory.buffer</code>로 확인한다. 프롬프트에 넣을 떄 요약본만 넣는다. 프롬프트의 길이가 유지된다.</p>
</li>
<li><p>프롬프트 앞에 붙이는 문맥 요약 history
프롬프트에 포함되는 내용을 확인하기 위해서는 <code>memory.load_momory_variables({})</code> 로 확인한다.</p>
</li>
</ul>
<h3 id="conversationbufferwindowmemory">ConversationBufferWindowMemory</h3>
<blockquote>
<p>과거의 내용을 자동으로 삭제되고 최신 K턴의 대화내용만 기억한다.</p>
</blockquote>
<p>Memory의 용량을 조절한다. </p>
<pre><code>from langchain.memory import ConversationBufferWindowMemory

# 최근 2턴만 기억하는 메모리
memory = ConversationBufferWindowMemory(k=2)
chain = ConversationChain(llm=llm, memory=memory)

# 대화
print(chain.run(&quot;나는 기영이야.&quot;))
memory.load_memory_variables({})</code></pre><ul>
<li>메모리 객체를 선언
memory를 선언하면서 memory에 담을 내용의 턴수를 지정해주어야 한다. 
mermory와 llm을 ConverstionChain으로 묶어준다.
chain은 run()으로 실행해준다</li>
</ul>
<h2 id="추가-lcellangchain-expression-language">[추가] LCEL(Langchain Expression Language)</h2>
<p>체인, 모델, 파서, 프롬프트 등의 여러 구성요소를 파이프라인처럼 | 연산자로 연결하는 표현식 기반의 체인 구성 방식이다. </p>
<p><code>chain = prompt | llm | parser</code> 과 같이 선언한다. </p>
