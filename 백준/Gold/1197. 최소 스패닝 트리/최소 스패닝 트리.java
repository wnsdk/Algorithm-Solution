import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	
	static int[] p;
	
	static class Edge implements Comparable<Edge> {
		
		int v1;
		int v2;
		int weight;
		
		public Edge(int v1, int v2, int weight) {
			this.v1 = v1;
			this.v2 = v2;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge edge) {
			return Integer.compare(this.weight, edge.weight);
		}
	}
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		
		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		
		p = new int[V + 1];
		for (int i = 1; i < V + 1; i++) {
			p[i] = i;
		}
		
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			pq.offer(new Edge(A, B, C));
		}
		
		int cnt = 0;
		int ans = 0;
		
		while (cnt < V - 1) {
			
			Edge e = pq.poll();
			if (union(e.v1, e.v2)) {
				ans += e.weight;
				cnt++;
			}
		}
		
		System.out.println(ans);
	}

	private static boolean union(int x, int y) {
		
		int a = find(x);
		int b = find(y);
		if (a == b) return false;
		p[a] = b;
		
		return true;
	}

	private static int find(int x) {
		
		if (x == p[x]) return p[x];
		return p[x] = find(p[x]);
	}

}