import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int[] dy = new int[]{0, 0, 1, -1};
    static int[] dx = new int[]{1, -1, 0, 0};
    static int N;
    static int M;
    static class Point {
        int y;
        int x;

        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    static public boolean isCoord (int y, int x) {
        return 0 <= y && y < N && 0 <= x && x < M;
    }

    public static void main(String[] args) throws IOException {



        //입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int[][] matrix = new int[N][M];
        int cnt = 0;

        for (int y = 0; y < N; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < M; x++) {
                int v = Integer.parseInt(st.nextToken());
                if (v == 1) {
                    cnt++;
                }
                matrix[y][x] = v;
            }
        }

        int time = 0;

        //치즈 녹이기
        while (cnt > 0) {
            time++;
            Queue<Point> q = new LinkedList<>();
            int[][] visited = new int[N][M];    // 방문한 적 없음(0), 방문한 적 있는 빈공간(1), 방문한 적 있는 치즈(2)

            q.offer(new Point(0, 0));
            visited[0][0] = 1;

            while (!q.isEmpty()) {
                Point point = q.poll();
                int y = point.y;
                int x = point.x;

                for (int k = 0; k < 4; k++) {
                    int ny = y + dy[k];
                    int nx = x + dx[k];

                    if (isCoord(ny, nx) && visited[ny][nx] != 1) {
                        // 빈 공간
                        if (matrix[ny][nx] == 0) {
                            q.offer(new Point(ny, nx));
                            visited[ny][nx] = 1;
                        }
                        // 치즈의 한 면이 노출되어 있다.
                        else if (matrix[ny][nx] == 1 && visited[ny][nx] == 0) {
                            visited[ny][nx] = 2;
                        }
                        // 치즈의 두 면이 노출되어 있다. (녹는다)
                        else if (visited[ny][nx] == 2) {
                            matrix[ny][nx] = 0;
                            visited[ny][nx] = 1;
                            cnt--;
                        }
                    }
                }
            }
        }

        System.out.println(time);
    }
}