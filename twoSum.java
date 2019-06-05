class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] answer = new int[2];
        for(int i =0; i < nums.length; i++){
            for(int z= i+1;z<nums.length;z++){
                if(nums[i] + nums[z] == target){
                    answer[0] = i;
                    answer[1] = z;
                    return answer;
                }
            }
        }
        return answer;
        
    }
}