---
title: "[JAVA] 순열(Permutation)과 조합(Combination)"
date: "2025-05-20"
link: "https://velog.io/@ehekaanldk/JAVA-%EC%88%9C%EC%97%B4Permutation%EA%B3%BC-%EC%A1%B0%ED%95%A9Combination"
series: "Uncategorized"
---

<p>자바에서 순열(Permutation)은 서로 다른 n 개의 원소 중 r 개를 선택하여 순서를 고려하여 나열하는 것을 의미한다. </p>
<p>자바에서 조합()은 서로 다른 n 개의 원소 중 r 개를 순서와 상관없이 선택하는 것을 의미한다. </p>
<p>순열과 조합은 알고리즘 문제 풀이, 완전탐색에서 자주 사용된다. </p>
<h2 id="순열permutation">순열(Permutation)</h2>
<blockquote>
<p>n 개의 원소 중 r 개를 선택하여 순서를 고려하여 나열하는 경우의 수</p>
</blockquote>
<p>자바에서의 구현 
: 재귀 함수를 사용하여 구현한다. 
선택된 원소를 저장하는 배열과 선택 여부를 나나타내는 방문 배열을 사용한다. </p>
<p>공식
: nPr = n! / (n-r)! (n!은 n팩토리얼) </p>
<hr />
<h2 id="조합combination">조합(Combination)</h2>
<blockquote>
<p>n 개의 원소 중 r 개를 선택하여 순서를 고려하지 않고 나열하는 경우의 수</p>
</blockquote>
<p>자바에서의 구현
: 재귀 함수를 사용하여 구현한다. 
순열처럼 선택된 원소들을 저장하는 배열과 선택 여부를 나타내는 방문 배열을 사용한다. </p>
<p>공식
: nCr = n! / (r! * (n-r)!) (n!은 n팩토리얼) </p>
<hr />
<h2 id="중복-순열과-중복-조합">중복 순열과 중복 조합</h2>
<h3 id="중복-순열">중복 순열</h3>
<p>n 개의 원소 중 중복을 허용하여 r 개를 선택하고 순서를 고려하여 나열하는 경우의 수</p>
<h3 id="중복-조합">중복 조합</h3>
<p>n 개의 원소 중 중복을 허용하여 r 개를 선택하고 순서를 고려하지 않고 나열하는 경우의 수 </p>
<hr />
<h2 id="순열-구현">순열 구현</h2>
<pre><code>    static int N;
    static int[] nums;
    static boolean[] visited; // 모든 재귀 호출에서 공유되어야 함
    static int[] result;    // 모든 재귀 호출에서 공유되어야 함

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        // 순열
        // 원소를 저장하는 배열과 선택 여부를 나타내는 방문 배열을 사용한다.

        int[] nums = new int[N];
        for(int i=0; i&lt;N; i++){
            nums[i] = scanner.nextInt();
        }

        // 선택 여부를 나타내는 방문 배열
        boolean[] visited = new boolean[N];
        // 원소를 저장하는 배열
        int[] result = new int[N];

        permutation(0, N);

    }
    // depth는 현재 고정된 원소의 인덱스
    public static void permutation(int depth, int n){
        if(depth == n){
            System.out.println(Arrays.toString(result));
        }

        for(int i=0; i&lt; N; i++){
            if(!visited[i]){ // 아직 선택하지 않은 원소이면
                visited[i] = true;
                result[depth] = nums[i];
                permutation(depth+1, n);
                visited[i] = false; // 백트래킹으로 현재 원소의 선택을 해제한다.
            }
        }
    }</code></pre><h4 id="백트래킹">백트래킹</h4>
<p>모든 가능한 경우의 수를 탐색하는 알고리즘에서 특정 조건을 만족하는 해를 찾거나, 모든 해를 찾는 데 사용되는 기법</p>
<ul>
<li><p>가지치기 : 현재까지의 선택이 해답으로 이어질 가능성이 없다고 판단하면, 더 이상 탐색하지 않고 해당 경로를 포기한다. </p>
</li>
<li><p>되돌아가기 : 한 번의 선택을 한 후에 다음 선택으로 나아간다. 해당 선택이 만족스럽지 않거나 모든 하위 경로를 탐색하였다면, 이전 선택으로 되돌아가 다른 선택을 시도한다. </p>
</li>
</ul>
<p>예를 들어, [1, 2, 3]으로 순열을 만드는 상황을 가정해본다.</p>
<ul>
<li><p>depth = 0에서 1을 선택합니다. (result = [1, _ , _], visited[0] = true)</p>
</li>
<li><p>depth = 1로 들어가 2를 선택합니다. (result = [1, 2, _], visited[1] = true)</p>
</li>
<li><p>depth = 2로 들어가 3을 선택합니다. (result = [1, 2, 3], visited[2] = true)</p>
<ul>
<li>depth == N이므로 [1, 2, 3]을 출력하고 재귀 호출이 끝난다.</li>
</ul>
</li>
</ul>
<p>[1, 2, 3]을 출력한 후, 우리는 [1, 3, 2]와 같은 다른 순열도 찾아야 한다.</p>
<ul>
<li><p>[1, 2, 3]을 만든 후, depth=2의 재귀 호출이 종료되고 depth=1로 돌아온다.</p>
</li>
<li><p>depth=1에서는 이전에 2를 선택했었다. 이제 2의 선택을 '해제'하고 3을 선택해야 [1, 3, 2]와 같은 순열을 만들 수 있다.</p>
</li>
</ul>
<p>선택 해제 과정이 백트레킹이다. visited[i] = false 를 실행하여 해당 원소를 마치 선택하지 않았던 것처럼 되돌려 놓아야 다음 for 루프 반복에서 그 원소를 다시 고려하여 새로운 조합을 만든다. </p>
