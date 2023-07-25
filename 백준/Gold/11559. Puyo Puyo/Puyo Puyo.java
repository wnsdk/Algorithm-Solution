import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[] dy = new int[]{1, -1, 0, 0};
    static int[] dx = new int[]{0, 0, 1, -1};
    static char[][] matrix;
    static final int Y = 12;
    static final int X = 6;

    static class Point {
        int y;
        int x;
        Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    static boolean isCoord(int y, int x) {
        return 0 <= y && y < Y && 0 <= x && x < X;
    }

    // 연쇄 폭발시키기 (터진 뿌요의 개수를 반환)
    static boolean bomb() {

        boolean isBomb = false;
        boolean[][] visited = new boolean[Y][X];

        // 뿌요 위치 찾기
        for (int sy = Y - 1; sy >= 0; sy--) {
            for (int sx = 0; sx < X; sx++) {
                char color = matrix[sy][sx];

                // 뿌요 찾았으면 bfs 시작
                if (color != '.' && !visited[sy][sx]) {
                    int cnt = 0;
                    List<Point> l = new ArrayList<>();
                    Queue<Point> q = new LinkedList<>();
                    q.offer(new Point(sy, sx));
                    visited[sy][sx] = true;

                    while (!q.isEmpty()) {
                        cnt++;
                        Point point = q.poll();
                        int y = point.y;
                        int x = point.x;

                        if (cnt < 4) {
                            l.add(new Point(y, x));
                        }
                        else if (cnt == 4) {
                            isBomb = true;
                            matrix[y][x] = '.';
                            for (Point p : l)
                                matrix[p.y][p.x] = '.';
                        }
                        else {
                            matrix[y][x] = '.';
                        }

                        for (int k = 0; k < 4; k++) {
                            int ny = y + dy[k];
                            int nx = x + dx[k];

                            if (!isCoord(ny, nx) || visited[ny][nx] || matrix[ny][nx] != color)
                                continue;

                            q.offer(new Point(ny, nx));
                            visited[ny][nx] = true;
                        }
                    }
                }
            }
        }


        return isBomb;
    }

    // 떨어지기
    static void fall() {
        for (int x = 0; x < X; x++) {
            int blank = -1;
            List<Character> puyo = new ArrayList<>();

            for (int y = Y - 1; y >= 0; y--) {
                if (matrix[y][x] == '.' && blank < 0)
                    blank = y;

                if (matrix[y][x] != '.' && blank >= 0) {
                    puyo.add(matrix[y][x]);
                    matrix[y][x] = '.';
                }
            }

            for (char color : puyo)
                matrix[blank--][x] = color;

        }
    }

    public static void main(String[] args) throws IOException {

        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        matrix = new char[Y][X];

        for (int y = 0; y < Y; y++) {
            String s = br.readLine();
            for (int x = 0; x < X; x++)
                matrix[y][x] = s.charAt(x);
        }

        // 풀이
        int ans = 0;
        while (bomb()) {
            fall();
            ans++;
        }

        System.out.println(ans);

    }
}