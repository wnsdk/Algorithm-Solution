class Solution {
    public int solution(String s) {      
        int answer = Integer.MAX_VALUE;
        for (int unit = 1; unit <= s.length(); unit++) {
            int cnt = 1;
            int l = 0;
            int r = l + unit;
            
            String prev = "";
            StringBuilder result = new StringBuilder();
            
            while (r <= s.length()) {
                if (prev.equals(s.substring(l, r))) {
                    cnt++;
                }
                else {
                    if (cnt > 1)
                        result.append(cnt);
                    result.append(prev);                    
                    cnt = 1;
                }
                
                prev = s.substring(l, r);
                l += unit;
                r = l + unit;
            }
            
            if (cnt > 1)
                result.append(cnt);
            result.append(prev);
            
            // 마지막에 남는 문자열은 그대로 붙여주면 됩니다.
            if (l < s.length())
                result.append(s.substring(l));
            
            answer = Math.min(answer, result.length());
            
        }
        return answer;
    }
}