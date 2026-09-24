

class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> map = new HashSet<>();
        for(int c:nums){
            if(map.contains(c)) return true;
            map.add(c);
        }
        return false;
    }
}