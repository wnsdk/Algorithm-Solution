import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static final int SIZE = 100001;
    static final int INF = Integer.MAX_VALUE;
    static class Point {
        int pos;
        int time;

        Point(int pos, int time) {
            this.pos = pos;
            this.time = time;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();   // 수빈이의 위치
        int k = sc.nextInt();   // 동생의 위치
        int ans1 = INF; // 최단 시간
        int ans2 = 0;   // 그 때의 경우의 수

        Queue<Point> q = new LinkedList();
        int[] visited = new int[SIZE];
        Arrays.fill(visited, INF);

        q.offer(new Point(n, 0));
        visited[n] = 0;

        while (!q.isEmpty()) {
            Point p = q.poll();
            int x = p.pos;
            int d = p.time;

            if (d > visited[k]) {
                continue;
            }

            if (x == k) {
                if (d < visited[k]) 
                    visited[k] = d;
                
                else if (d == visited[k]) 
                    ans2++;
                
                continue;
            }

            int[] move = {x - 1, x + 1, x * 2};
            for (int nx : move) {
                int nd = d + 1;
                if (0 <= nx && nx < SIZE && nd <= visited[nx]) {
                    q.offer(new Point(nx, nd));
                    visited[nx] = nd;
                }
            }
        }

        System.out.println(visited[k]);
        System.out.println(ans2);
    }
}