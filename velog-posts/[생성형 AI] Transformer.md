---
title: "[생성형 AI] Transformer"
date: "2025-04-18"
link: "https://velog.io/@ehekaanldk/%EC%83%9D%EC%84%B1%ED%98%95-AI-Transformer"
series: "Uncategorized"
---

<p>사전학습된 모델을 어떻게 활용하는지에 대해서 하나의 프레임워크인 langchain을 배워본다. </p>
<h2 id="01-transformer-와-lm">01. Transformer 와 LM</h2>
<p>google의 논문인 transformer를 알아본다. </p>
<p>거의 많은 모델들을 transformer로 만들려는 추세이다.
비전 =&gt; ViT(vision transforemr)
시계열(CNN, RNN) =&gt; transforemr</p>
<p>transformer </p>
<ul>
<li>GPT</li>
<li>BERT</li>
</ul>
<h3 id="rnn-기반-seq2seq">RNN 기반 Seq2Seq</h3>
<p>기존의 RNN LM은 다음 단어를 예측하고 분류 문제를 푼다. 
인코더 : 기존의 정보를 변형한다. 
디코더 : 변형된 것을 원본으로 되돌린다.</p>
<p>Seq2Seq는 시퀀스를 인코딩하고 디코딩한다. 
인코더는 입력의 가장 마지막 hidden state를 <strong>context 벡터</strong>로 변환한다. (맥락을 포함하는 벡터)
디코더는 벡터를 기반으로 새로운 시퀀스를 생성한다. </p>
<p>번역을 위해서 만들었지만 RNN도 Seq2Seq도 금붕어!</p>
<h3 id="attention">Attention</h3>
<p>Attention은 과거의 맥락상 가장 중요한 기억만 집중해서 기억한다. 
모든 장기 기억을 기억하는 것이 아니라 중요한 정보만 기억한다. 
디코더에서 인코더의 각각의 중간과정에 중요한게 누구였는지 찾는다. </p>
<h3 id="self-attention">Self Attention</h3>
<p>Self Attention은 입력 문장의 모든 당어가 서로 어떤 관계를 가지는지 학습한다.
인코더 안에서 인코더를 보거나, 디코더에서 디코더를 바라보면서 중요한게 누구였는지 찾는다. </p>
<h3 id="multi-head-attention">Multi-Head Attention</h3>
<p>Multi-Head Attention은 다양한 과점으로 문장을 이해하도록 여러개의 head를 가지는 Attention을 준다. Attention은 어디에 집중을 할 것 인가이다. </p>
<h3 id="positional-encoding">Positional Encoding</h3>
<p>Positional Encoding는 단어 간의 관계를 학습한 Attention에서 포함되지 않은 순서 정보를 추가한다. 
문장은 시퀀스인데 토큰으로 변환하면 순서의 정보가 사라진다. 
Attention에서는 순서의 상관이 없다. </p>
<h3 id="feed-forward-network">Feed Forward Network</h3>
<p>Feed Forward Network은 Attention으로 만들어진 정보에 추가적인 비선형 변환을 하는 과정이다. 
Dense와 ReLU를 추가하여 더 복잡한 학습을 할 수 있도록 한다. </p>
<h3 id="transformer--gpt">Transformer : GPT</h3>
<p>인코더 : 입력 문장을 인코딩하여 벡터 표현을 생성한다. 
디코너 : 인코더의 출력 벡터를 받아서 최종적으로 문장을 생성한다. </p>
<ul>
<li>GPT는 생성을 목적으로 개발되어 임베딩 벡터를 기반으로 다음 단어를 예측한다. 문장이 들어올 필요없이 시작단어 하나만 있어도 된다. 디코더만 사용</li>
<li>BERT는 문장을 분석해서 context vector를 만들어낸다. 문맥을 파악하고 이해하는 것이 중요하다는 관점이다. 문장을 직접 생성하지 않는다. 인코더만 사용</li>
</ul>
<p>RLHF는 사람이 피드백해서 강화학습을 진행한다. 
멀티모달은 이미지나 텍스트, 음성등의 멀티모델로 들어와서 멀티모델의 출력을 제공한다. </p>
<h3 id="llm-활용">LLM 활용</h3>
<p>API, Huggingface : 똘똘한 모델을 그대로 사용
Fine-tuning : 똘똘한 모델에 내 데이터로 추가학습
RAG : 똘똘한 모델에 자료집을 바탕으로 </p>
<h2 id="02-huggingface">02. Huggingface</h2>
<p>Pipeline 함수
<code>pipeline(task=&quot;사용 task&quot;, model=&quot;모델명&quot;)</code></p>
<ul>
<li>sentiment-analysis : 감성 분석</li>
<li>zero-shot-classification : 본적 없는 데이터에 대해서 분류</li>
<li>summartization : 요약</li>
<li>번역</li>
<li>텍스트 생성</li>
</ul>
<p>distil은 경량화버전이다. 
zero shot의 후보 레이블은 개인이 정해준다. 
언어 능력이 뛰어나기 때문에 모델에게 목적에 맞게 문제를 내서 맞추도록 하는 것이다. </p>
<hr />
<p>LLM은 large language model로 파라미터가 매우 많아서 인간 사이의 모든 텍스트를 학습해놓은 것이다. 질문을 던지면 무엇이든 답을 해내는 모델이 되었다. </p>
<p>LLM은 제작하는데 돈과 시간이 많이 들기 때문에 전세계적인 빅테크 기업만이 만들어낸다. </p>
<p>LLM의 활용법
api 유료버전으로 모델을 그대로 가져온다. 
나의 데이터로 조금 더 학습시켜서 사용한다. fine-tuninng
지식 데이터를 기반으로 학습을 시킨다. RAG</p>
<p>LLM은 로드하면 tokenizer_config, vocab, tokenizer 를 가져온다. </p>
<p>clue?
모델의 파라미터들에서 중요한 파라미터를 남기고 줄이는 것이 경량화 모델이다.</p>
<p>모델 업로드하기 </p>
<p>new model로 이름과 라이센스를 부여한다. 라이센스는 unlisence를 선택하였다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/34676dda-63ef-4e5b-8ce1-875d51b98937/image.png" /></p>
<p>contribute &gt; upload file 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/59175c0f-5bb1-4f91-8fee-6ec620c3cd26/image.png" /></p>
<p>file을 업로드해서 commit해준다.
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/7d416690-5751-4bff-b846-4fe2862f4d51/image.png" /></p>
<p>이름을 copy해서 불러온다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/0606df0b-549d-4a20-b45d-4c2934225309/image.png" /></p>
<p>model부분에 copy한 값을 넣어서 모델을 사용한다. 
<img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/eb04a495-9647-48c0-bbbf-9fc361585dd5/image.png" /></p>
<h3 id="api">API</h3>
<p>os 레벨의 환경변수로 등록해서 api키를 가져온다. 
키를 하드코딩하지 않는 것을 명심한다.</p>
<pre><code>sys_role = 시스템의 역할
question = 질문
messages = [리스트형태로 {딕셔너리 안에 역할을 부여하고} 요청을 한다.]</code></pre><p>한번 고정시키는 메시지를 시스템 메시지라고 한다. 
user 는 휴먼 메시지이다. </p>
<p><strong>순서</strong></p>
<p>데이터준비</p>
<ol>
<li>데이터셋 분할하기</li>
<li>tensor로 변환하기</li>
<li>토크나이저 다운 받아서 .map()으로 적용
파인튜닝</li>
<li>모델 다운 AutoModelForSequenceClassification + outputlayer 붙여서 다운</li>
<li>학습하는 4개의 단계</li>
</ol>
<ul>
<li>trainingargument() 선언</li>
<li>trainer.trainer()</li>
<li>trainer.train()</li>
<li>trainer.evaluate()</li>
</ul>
