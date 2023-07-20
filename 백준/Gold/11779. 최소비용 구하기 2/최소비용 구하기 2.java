import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static class Edge implements Comparable<Edge> {
        int node;   //도착지 노드
        int cost;   //이동 비용

        Edge(int node, int cost) {
            this.node = node;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge e) {
            return Integer.compare(this.cost, e.cost);
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());    //도시 개수
        int m = Integer.parseInt(br.readLine());    //버스 개수

        List<Edge>[] adj = new ArrayList[n + 1];
        for (int i = 1; i < n + 1; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            adj[s].add(new Edge(e, cost));
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        //다익스트라
        int INF = Integer.MAX_VALUE / 10;
        boolean[] visited = new boolean[n + 1];
        int[] route = new int[n + 1];
        int[] dp = new int[n + 1];
        Arrays.fill(dp, INF);

        PriorityQueue<Edge> pq = new PriorityQueue<>();
        pq.add(new Edge(s, 0));
        route[s] = 0;
        dp[s] = 0;


        while (pq.size() > 0) {
            Edge now = pq.poll();
            if (visited[now.node]) {
                continue;
            }
            visited[now.node] = true;
            
            for (Edge next : adj[now.node]) {
                int cost = now.cost + next.cost;
                if (dp[next.node] > cost) {
                    route[next.node] = now.node;
                    dp[next.node] = cost;
                    next.cost = cost;
                    pq.add(next);
                }
            }
        }

        List<Integer> routes = new ArrayList<>();
        int cur = e;
        while (cur != 0) {
            routes.add(cur);
            cur = route[cur];
        }

        sb.append(dp[e] + "\n");    //출발 도시에서 도착 도시까지 가는데 드는 최소비용
        sb.append(routes.size() + "\n"); //해당 경로에 포함된 도시의 개수
        //해당 경로를 방문하는 도시 순서대로 출력
        for (int i = routes.size() - 1; i >= 0; i--) {
            sb.append(routes.get(i) + " ");
        }

        System.out.println(sb);

    }
}