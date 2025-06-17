---
title: "[JAVA] DFS"
date: "2025-06-05"
link: "https://velog.io/@ehekaanldk/JAVA-DFS"
series: "Uncategorized"
---

<h2 id="dfs">DFS</h2>
<p>DFS는 Depth-First Search 로 그래프 탐색 알고리즘 중 하나로,</p>
<blockquote>
<p>한 노드를 정점으로 하여 가능한 한 깊게 탐색한 후, 더 이상 갈 수 없게 되면 되돌아와서 다른 경로를 탐색하는 방식</p>
</blockquote>
<h3 id="dfs의-특징">DFS의 특징:</h3>
<ul>
<li>재귀 또는 스택을 이용해 구현</li>
<li>백트래킹(Backtracking) 구조와 잘 어울림</li>
<li>트리, 그래프, 미로 탐색 등에 자주 사용</li>
<li>방문한 노드를 기억해야 무한 루프 방지 가능</li>
</ul>
<h2 id="dfs의-동작-방식">DFS의 동작 방식</h2>
<ul>
<li><p>노드 정보 저장 공간
<code>List&lt;List&lt;Integer&gt;&gt; graph = new ArrayList&lt;&gt;();</code></p>
</li>
<li><p>방문 여부 체크 공간</p>
</li>
</ul>
<ol>
<li>시작 노드를 스택에 넣고 <strong>방문</strong> 표시</li>
<li>현재 노드에서 갈 수 있는 노드 중 <strong>방문하지 않은 노드</strong>를 찾아 이동</li>
<li><strong>더 이상 방문할 곳이 없으면 이전 노드</strong>로 되돌아간다. (Backtrack)</li>
</ol>
<pre><code>1번 노드 방문
→ 연결된 2번 확인 → 방문 안 했으니 dfs(2)

2번 노드 방문
→ 연결된 1, 4 확인 → 1은 이미 방문 → 4로 dfs(4)

4번 노드 방문
→ 연결된 2는 이미 방문 → 종료, 되돌아감

→ 다시 2로 돌아와서 더 갈 곳 없음 → 다시 1로 돌아감

→ 이제 1의 또 다른 연결된 3번으로 dfs(3)

→ 3 방문 → 5로 dfs(5)

→ 5 방문 → 끝 → 역순으로 되돌아감
</code></pre><h2 id="dfs-그래프">DFS 그래프</h2>
<h3 id="인접-리스트--재귀">인접 리스트 : 재귀</h3>
<p>각 노드에 대해서, 연결된 노드 목록을 저장한다.
<code>ArrayList&lt;Integer&gt;[]</code> 배열을 사용해서 구현한다.</p>
<p>graph[] : 인접 리스트, 각 노드의 연결 정보를 저장
visited[] : 이미 방문한 노드인지 확인용
addEdge() : 두 노드를 연결하는 함수(양방향)
<strong>dfs()</strong> : <strong>현재 노드 방문</strong> -&gt; 연결된 노드 재귀 탐색</p>
<pre><code>
public class DFS {

    static ArrayList&lt;Integer&gt;[] graph;
    static boolean[] visited;

    public static void main(String[] args) {
        int n = 5;
        graph = new ArrayList[n+1]; // 0번 인덱스는 사용하지 않느다.
        visited = new boolean[n+1];

        // arraylist 객체를 요소로 가지는 배열을 초기화 한다.
        for(int i=1; i&lt;=n; i++){
            graph[i] = new ArrayList&lt;&gt;();
        }



    }
    static void addEdge(int u, int v){
        // 양방향이여서
        graph[u].add(v);
        graph[v].add(u);
    }

    static void dfs(int node){
        visited[node] = true;
        for(int next : graph[node]){
            if(!visited[next]){ // 방문 안했으면 dfs 재귀 호출
                dfs(next);
            }
        }
    }
}</code></pre><ul>
<li><p>graph[node] 는 현재 노드가 아니라, 현재 노드와 연결된 이웃 노드들의 리스트</p>
</li>
<li><p>for(int next : graph[node])는 현재 노드 node에 연결된 모든 이웃 노드들을 하나씩 꺼내서 next로 탐색한다.</p>
</li>
<li><p>DFS는 깊이를 우선으로 탐색하기에 </p>
</li>
<li><p>어떤 노드의 이웃으로 존재한 것을 발견해도</p>
</li>
<li><p>직접 그 노드로 들어가서 밟지 않으면 방문하지 않은 것이다.</p>
</li>
<li><p>visited 배열에 요소들이 true가 되는 순서가 실제 방문한 순서이다.</p>
</li>
<li><p>방문 순서 저장하려고 하면,</p>
</li>
<li><p>해당 저장용 리스트를 만들어서 visited[node]=true 할 때마다 따로 저장한다. </p>
</li>
</ul>
<h2 id="dfs-그리드">DFS 그리드</h2>
<blockquote>
<p>2차원 배열 grid[row][col]은 상하좌우 4방향으로 이동하면서 방문한다. 
방문했던 곳은 다시 가지 않도록 visited 값을 변경하여 체크한다.</p>
</blockquote>
<ul>
<li><p>방문 여부를 저장하는 visited[] 배열</p>
</li>
<li><p>grid를 그리는 배열</p>
</li>
<li><p>BFS에서와 동일하게 현재위치의 x, y 좌표를 뽑아내서</p>
</li>
<li><p>x와 y에 상하좌우로 이동하도록 dx와 dy를 더해서 nx와 ny를 만든다.</p>
</li>
<li><p>범위 내에 존재 &amp;&amp; 조건 만족 &amp;&amp; !visited</p>
</li>
<li><p>모두 만족할 때 DFS를 재귀 호출하도록 한다.</p>
</li>
</ul>
<pre><code>import java.util.*;

public class GridDFS {
    static int[][] grid = {
        {1, 1, 0, 0, 0},
        {0, 1, 0, 1, 1},
        {0, 0, 0, 1, 1},
        {0, 0, 0, 0, 0},
        {1, 1, 1, 0, 0}
    };
    static boolean[][] visited = new boolean[5][5];
    static int n = 5, m = 5;

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) {
        int count = 0;

        for (int i = 0; i &lt; n; i++) {
            for (int j = 0; j &lt; m; j++) {
                if (grid[i][j] == 1 &amp;&amp; !visited[i][j]) {
                    dfs(i, j);
                    count++;
                }
            }
        }

        System.out.println(&quot;영역 개수: &quot; + count);
    }

    static void dfs(int x, int y) {
        visited[x][y] = true;

        for (int i = 0; i &lt; 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx &gt;= 0 &amp;&amp; nx &lt; n &amp;&amp; ny &gt;= 0 &amp;&amp; ny &lt; m) {
                if (grid[nx][ny] == 1 &amp;&amp; !visited[nx][ny]) {
                    dfs(nx, ny);
                }
            }
        }
    }
}
</code></pre>
