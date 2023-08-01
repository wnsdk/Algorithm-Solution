import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        System.out.println(LIS(arr));
    }

    private static int LIS(int[] arr) {

        int[] dp = new int[arr.length];
        int size = 0;

        for (int i = 0; i < arr.length; i++) {
            int pos = Arrays.binarySearch(dp, 0, size, arr[i]);
            if (pos >= 0) continue;
            
            int insertPos = Math.abs(pos) - 1;  // 맨 뒤 또는 기존원소 대체 자리
            dp[insertPos] = arr[i];
            
            // 맨 뒤에 추가한거라면
            if (insertPos == size) size++;
        }
        
        return size;
    }
}