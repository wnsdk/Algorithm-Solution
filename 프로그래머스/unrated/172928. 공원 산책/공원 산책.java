class Solution {
    
    static int Y;
    static int X;
    
    static boolean isCoord(int y, int x) {
        return 0 <= y && y < Y && 0 <= x && x < X;
    }
    
    static boolean chk(String[] park, int y, int x, int ny, int nx) {
        
        // 위아래
        if (x == nx) {
            if (y < ny)
                for (int i = y + 1; i <= ny; i++) {
                    if (park[i].charAt(nx) == 'X')
                        return true;
                }
            else
                for (int i = ny; i < y; i++) {
                    if (park[i].charAt(nx) == 'X')
                        return true;
                }
        }
        // 좌우
        else {
            if (x < nx)
                for (int i = x + 1; i <= nx; i++) {
                    if (park[ny].charAt(i) == 'X')
                        return true;
                }
            else
                for (int i = nx; i < x; i++) {
                    if (park[ny].charAt(i) == 'X')
                        return true;
                }
        }
        
        return false;
    }
    
    public int[] solution(String[] park, String[] routes) {
        
        Y = park.length;
        X = park[0].length();
        int y = -1;
        int x = -1;
        
        for (int r = 0; r < Y; r++) {
            for (int c = 0; c < X; c++) {
                if (park[r].charAt(c) == 'S') {
                    y = r;
                    x = c;
                    break;
                }
            }
            if (y > -1)
                break;
        }
        
        for (String comm : routes) {
            char dir = comm.charAt(0);
            int dis = Integer.parseInt(comm.substring(2, 3));
            
            int ny = y;
            int nx = x;
            
            if (dir == 'N') {
                ny -= dis;
            }
            else if (dir == 'S') {
                ny += dis;
            }
            else if (dir == 'W') {
                nx -= dis;
            }
            else if (dir == 'E') {
                nx += dis;
            }
            
            if (!isCoord(ny, nx) || chk(park, y, x, ny, nx))
                continue;
            
            y = ny;
            x = nx;
        }
        
        int[] answer = {y, x};
        return answer;
    }
}