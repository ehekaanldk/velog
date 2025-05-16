---
title: "[생성형 AI] Quantization"
date: "2025-05-15"
link: "https://velog.io/@ehekaanldk/%EC%83%9D%EC%84%B1%ED%98%95-AI-Quantization"
series: "Uncategorized"
---

<h2 id="양자화quantization">양자화(Quantization)</h2>
<blockquote>
<p>큰 수치(float)를 더 작고 단순한 정수(int)로 근사화하여 메모리와 계산 차원을 줄이는 기술</p>
</blockquote>
<ul>
<li>일반적으로 <code>float32</code> =&gt; <code>int8</code>, <code>int4</code>, <code>int16</code> 등으로 변환</li>
<li>정밀도 손실을 감수하고 모델의 크기를 줄이고 추론 속도를 높이는데 사용한다.</li>
</ul>
<h2 id="양자화를-사용하는-이유">양자화를 사용하는 이유</h2>
<p>💡 문제점 
최신 생성형 AI는 수억-수천억 개의 파라미터를 가진다. (GPT-3)</p>
<ul>
<li>파라미터 수가 매우 많아 계산량이 큼</li>
<li>VRAM 부족, 추론 속도 저하, 배포 제한</li>
</ul>
<p>✅ 양자화의 기대 효과</p>
<table>
<thead>
<tr>
<th>항목</th>
<th>효과</th>
</tr>
</thead>
<tbody><tr>
<td>모델 크기 감소</td>
<td>float32 → int8 시 약 <strong>4배 압축</strong></td>
</tr>
<tr>
<td>연산 속도 향상</td>
<td>정수 연산 기반으로 GPU/CPU 처리 속도 향상</td>
</tr>
<tr>
<td>전력 절감</td>
<td>모바일/엣지 환경에서 <strong>에너지 소모 절감</strong></td>
</tr>
<tr>
<td>배포 용이성</td>
<td>서버 비용 절감 + 로컬에서 실행 가능</td>
</tr>
</tbody></table>
<ul>
<li>복잡한 수는 더 많은 공간을 필요로 한다.  </li>
<li>숫자를 단순하게 바꾸면 공간도 덜 차지하고, 속도도 빨라진다.</li>
</ul>
<h2 id="양자화의-전체-흐름">양자화의 전체 흐름</h2>
<p><img alt="" src="https://velog.velcdn.com/images/ehekaanldk/post/19dc2a7f-cebd-47b5-8492-36c4c1abfbb7/image.jpg" /></p>
<ul>
<li>제일 큰 숫자를 찾아서 바꾸려는 타입에서 가장 크게 표현할 수 있는 값에 맞춘다.</li>
</ul>
<h3 id="원본-벡터float16">원본 벡터(float16)</h3>
<p><code>[1.2, -0.5, -4.3, 1.2, -3.1, 0.8, 2.4, 5.4]</code></p>
<ul>
<li>모든 값의 절대값</li>
<li>가장 큰 값 Max(abs) = 5.4</li>
</ul>
<h3 id="왜-maxabs를-쓰는가">왜 max(abs)를 쓰는가?</h3>
<p>float 값을 정수(int8)로 바꾸기 위해 <strong>비율(스케일)</strong>이 필요함</p>
<p>가장 큰 절댓값을 <strong>127(int8 최댓값)</strong>에 대응시키면,
나머지 값들도 [-127, 127] 범위로 자연스럽게 매핑됨</p>
<p>$$5.4 ⟶ 127$$ (정규화 기준)</p>
<h3 id="양자화-스케일α-계산">양자화 스케일(α) 계산</h3>
<p>$$α= \frac{max(abs)}{127} = \frac{5.4}{127} ≈ 0.0425$$</p>
<h3 id="양자화-수식-float---int">양자화 수식 (float -&gt; int)</h3>
<p>$$q = round (\frac{x}{a})$$</p>
<ul>
<li>int8 범위를 넣으려면 정수를 만들어야 함으로 round를 사용한다. </li>
</ul>
<p>양자화는 float32를 정수(int)로 바꾸어야 하고, 어떤 기준으로 바꿀지 정해야 함으로 최대값을 기준값으로 사용한다. </p>
<p>int8로 바꾸기 위해서 [-127, 127]  범위 안으로 매핑한다. 해당 범위로 매핑하기 때문에 가장큰 값인 5.4는 127로 매핑된다. </p>
<h3 id="요약">요약</h3>
<ul>
<li><p>float32 → int8로 바꾸기 위해, 입력값 중 가장 큰 값을 기준으로 전체 값을 정규화</p>
</li>
<li><p>값들을 [-127, 127] 사이의 정수로 바꾸고 저장</p>
</li>
<li><p>2byte로 표현하던거를 1byte로 표현하면서 메모리 이득을 본다. </p>
</li>
<li><p>but 정밀도가 떨어져서 완벽하게 원래 숫자를 복원할 수 없다. =&gt; 정확도에 약간의 변화</p>
</li>
</ul>
<h2 id="bitsandbytes">bitsandbytes</h2>
<p>✅ Bitsandbytes (by HuggingFace)
4bit, 8bit 양자화 지원</p>
<p>LoRA + 양자화 조합으로 fine-tuning 가능</p>
<p><strong>LLaMA-2 모델을 4bit 양자화(Quantization)</strong></p>
<pre><code>from transformers import AutoModelForCausalLM, BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(load_in_4bit=True)
model = AutoModelForCausalLM.from_pretrained(&quot;meta-llama/Llama-2-7b&quot;, quantization_config=bnb_config)
</code></pre><h2 id="양자화의-종류">양자화의 종류</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>설명</th>
<th>사용 예</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Weight-only Quantization</strong></td>
<td>가중치만 정수화, 활성값은 float 유지</td>
<td>HuggingFace <code>bitsandbytes</code></td>
</tr>
<tr>
<td><strong>Activation-aware Quantization</strong></td>
<td>가중치 + 활성값 모두 양자화</td>
<td>ONNX QAT 등</td>
</tr>
<tr>
<td><strong>QAT (Quantization Aware Training)</strong></td>
<td>학습 시점에 정수화 반영</td>
<td>정확도 보존에 적합</td>
</tr>
<tr>
<td><strong>GPTQ (Post-Training Quantization)</strong></td>
<td>GPT 모델 전용 PTQ 기법</td>
<td>LLaMA, GPT-Neo 등에서 사용</td>
</tr>
<tr>
<td><strong>AWQ (Activation-aware Weight Quantization)</strong></td>
<td>활성 분포를 고려한 PTQ</td>
<td>LLM 성능 저하 최소화</td>
</tr>
</tbody></table>
