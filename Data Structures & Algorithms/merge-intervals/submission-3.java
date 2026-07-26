class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals,(x,y) -> Integer.compare(x[0],y[0]));
        List<int[]> ans = new ArrayList<>();
        ans.add(intervals[0]);
        for (int i = 1; i < intervals.length;i++){
            int[] interval = intervals[i];
            int[] last = ans.get(ans.size()-1);
            int s1 = last[0];
            int f1 = last[1];
            int s2 = interval[0];
            int f2 = interval[1];
            
            if (f1 >=s2){
                last[0] = Math.min(s1,s2);
                last[1] = Math.max(f1,f2);
            }
            else{
                ans.add(interval);
            }
        }
        return ans.toArray(new int[ans.size()][]);
    }
}
