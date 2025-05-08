---
title: "[생성형 AI] 미니프로젝트 2차"
date: "2025-05-08"
link: "https://velog.io/@ehekaanldk/%EC%83%9D%EC%84%B1%ED%98%95-AI-%EB%AF%B8%EB%8B%88%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-2%EC%B0%A8"
series: "Uncategorized"
---

<p>AI agent </p>
<pre><code>from typing import TypedDict, List, Dict

class InterviewState(TypedDict):
    # 고정 정보
    resume_text: str
    resume_summary: str
    resume_keywords: List[str]
    question_strategy: Dict[str, Dict] # 키는 str, 값은 dict

    # 인터뷰 로그
    current_question: str
    current_answer: str
    current_strategy: str
    conversation: List[Dict[str, str]] # 키와 값 모두 str
    evaluation : List[Dict[str, str]]
    next_step : str</code></pre><p>🔒 고정 정보</p>
<ul>
<li><p>resume_text: str
이력서 전체 원문 (자기소개서, 경력기술서 등 포함 가능)</p>
</li>
<li><p>resume_summary: str
이력서 요약 (핵심 경력이나 강점 위주로 요약된 정보)</p>
</li>
<li><p>resume_keywords: List[str]
이력서에서 추출한 핵심 키워드들 (예: 기술 스택, 역할, 도메인 등)</p>
</li>
<li><p>question_strategy: Dict[str, Dict]
질문 유형에 따른 전략 설정
예: &quot;기술역량&quot;: {&quot;목표&quot;: &quot;프로젝트 경험 강조&quot;, &quot;예시&quot;: &quot;TensorFlow 활용 사례&quot;}
key는 질문 분류(기술, 협업, 성장과정 등), value는 해당 전략의 세부 내용</p>
</li>
</ul>
<p>💬 인터뷰 로그</p>
<ul>
<li><p>current_question: str
현재 진행 중인 인터뷰 질문</p>
</li>
<li><p>current_answer: str
해당 질문에 대한 현재 사용자의 답변</p>
</li>
<li><p>current_strategy: str
해당 질문에 적용된 답변 전략 (예: STAR 방식, 구체적 사례 강조 등)</p>
</li>
<li><p>conversation: List[Dict[str, str]]
이전 질문-답변 대화 기록</p>
</li>
</ul>
<p>각 항목은 {&quot;question&quot;: &quot;...&quot;, &quot;answer&quot;: &quot;...&quot;} 형식의 dict</p>
<ul>
<li><p>evaluation: List[Dict[str, str]]
각 질문-답변에 대한 피드백 또는 평가
각 항목은 {&quot;question&quot;: &quot;...&quot;, &quot;evaluation&quot;: &quot;...&quot;} 형식</p>
</li>
<li><p>next_step: str
인터뷰 시스템이 제안하는 다음 행동
예: &quot;다음 질문 출제&quot;, &quot;현재 답변 수정&quot;, &quot;종합 피드백 제공&quot;</p>
</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/b770e127-e3bb-47f1-9af5-eaff4d490baa/image.png" />
PromptTemplate을 생성할 때 input_variables 인수는 <strong>문자열의 리스트 형태로 제공</strong>되어야 합니다. 
input_variables에 <strong>state['resume_text']</strong> 와 같이 문자열을 직접 입력하면 오류가 발생한다. </p>
<hr />
<p>PromptTemplate을 생성할 때 <strong>template 인수</strong>는 <strong>프롬프트 템플릿 문자열</strong> 을 나타낸다. template=&quot;&quot;&quot;{resume_text}는... 으로 template과 선언하는 template의 명이 겹치지 않도록 한다. </p>
<hr />
<p>전략 수립과정에서 프롬프트가 길어질 경우에는 \n 을 문장마다 붙여주어서 늘려주면 된다. </p>
<pre><code>    strategy_prompt = ChatPromptTemplate.from_messages([
        (&quot;system&quot;, &quot;당신은 이력서 분석을 통해 개인화된 질문을 뽑기 위한 질문 전략 수립 어시스턴트입니다.&quot;),
        (&quot;human&quot;, 
         &quot;다음 resume_summary와 resume_keywords를 기반으로 이력서 분석을 수행하세요. \n&quot;
         &quot;3가지 분야: '경력 및 경험', '동기 및 커뮤니케이션', '논리적 사고' \n&quot;
         &quot;각 분야마다 다음 항목을 포함한 전략을 작성하세요. \n&quot;
         &quot;1. 질문 방향 \n&quot;
         &quot;2. 예시 질문 2개 \n&quot;
         &quot;resume_summary: {resume_summary}\n&quot;
         &quot;resume_keywords: {resume_keywords}\n&quot;
         &quot;위 정보를 바탕으로 3개의 전략을 수립하세요.&quot;         
         )
    ])</code></pre><hr />
<p>현재 return값인 question_strategy는 Dict[str, Dict]의 형태임으로 LLM이 <strong>&quot;JSON 형식으로 출력하라&quot;</strong> 는 명시적 프롬프트를 보고
아래 구조를 정확히 따르기 때문에 결과가 Dict[str, Dict] 형태가 되도록 한다. </p>
<pre><code>&quot;- 3가지 분야: '경력 및 경험', '동기 및 커뮤니케이션', '논리적 사고'\n&quot;
&quot;- 각 분야마다 다음 항목을 포함한 전략을 작성하세요. \n&quot;
&quot;  - 1. 질문 방향 \n&quot;
&quot;  - 2. 예시 질문 2개 \n&quot;</code></pre><p>같이 작성해주면서 llm에게</p>
<pre><code>{
  &quot;경력 및 경험&quot;: {
    &quot;질문 방향&quot;: &quot;...&quot;,
    &quot;예시 질문&quot;: [&quot;...&quot;, &quot;...&quot;]
  },
  ...
}</code></pre><p>형태를 유도한다. </p>
<hr />
<p>'question_strategy_state' 변수는 값이 사전이어야 하지만 <strong>JSON 내용을 포함하는 문자열</strong>로 저장된다. JSON 문자열은 아직 파이썬 사전으로 변환되지 않았기 때문에 문자열 인덱싱을 사용하면 오류가 발생한다. 
<code>json.loads()</code>으로 json 문자열을 파이썬 dict으로 변환한다. 
<code>strategy_dict = json.loads(strategy_json)</code>
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/bd54b2af-df9a-451f-83ed-5197374965bb/image.png" /></p>
<p><code>json.loads()</code>를 추가했지만 LLM이 dict형태로 생성하지 않는 문제가 발생함.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/0a1a352a-f993-4d7c-9cad-ff2c9212607a/image.png" />
<code>json.loads(question_strategy_state['question_strategy'])</code> 코드에서 파싱을 할 수 없는 요소인 ```json이 앞뒤에 붙어버려서 이를 제거해주어야 한다. </p>
<p>LLM 출력 결과는 &quot;<code>json\n{ ... }\n</code>&quot; 같은 코드블럭이 포함된 JSON 문자열이고,
그래서 결과 타입은 str이고 json.loads()를 바로 쓸 수 없습니다.</p>
<pre><code>import json
import re

raw_output = strategy_chain.invoke({
    &quot;resume_summary&quot;: resume_summary,
    &quot;resume_keywords&quot;: resume_keywords
})

# 코드블럭(```json ... ```) 제거
cleaned_output = re.sub(r&quot;```(?:json|python)?\n?&quot;, &quot;&quot;, raw_output).strip().rstrip(&quot;```&quot;)

# JSON 파싱
strategy_dict = json.loads(cleaned_output)</code></pre><p>프롬프트에는 설명없이 json형식으로 출력하도록 하였지만 프롬프트에서 <code>\</code>`\와 같은 코드 블럭 없이 json만 출력하도록 하는 문구를 포함시켜준다. </p>
<hr />
<p>from_template과 from_messages의 차이점
<strong>from_template</strong></p>
<ul>
<li>from_template은 하나의 템플릿 문자열로 구성된 프롬프트를 생성한다. 
&quot;너는 {role} 역할을 맡은 {job} 이다.&quot;<pre><code>prompt = ChatPromptTemplate.from_template(&quot;안녕하세요, {name}님. 무엇을 도와드릴까요?&quot;)
formatted = prompt.format(name=&quot;홍길동&quot;)</code></pre></li>
</ul>
<p><strong>from_messages</strong></p>
<ul>
<li>from_messages는 여러 역할의 메시지들을 구성한 대화형 프롬프트를 생성한다.
[(&quot;system&quot;, &quot;...&quot;), (&quot;human&quot;, &quot;...&quot;)]<pre><code>prompt = ChatPromptTemplate.from_messages([
  (&quot;system&quot;, &quot;너는 친절한 영어 튜터야.&quot;),
  (&quot;human&quot;, &quot;고양이를 영어로 뭐라고 해?&quot;),
])
formatted = prompt.format()</code></pre></li>
</ul>
<hr />
<p><strong>evaluation = state['evalution'] 과 evaluation = state.get(&quot;evaluation&quot;, []) 의 차이점</strong></p>
<ul>
<li>evaluation = state['evalution'] 
state에 evalution이라는 키가 반드시 존재해야 한다. </li>
<li>evaluation = state.get(&quot;evaluaion&quot;, [])
state에 evalution이라는 키가 있으면 해당 값을 가져오고, 없으면 기본값 빈 리스트를 반환한다. </li>
</ul>
<hr />
