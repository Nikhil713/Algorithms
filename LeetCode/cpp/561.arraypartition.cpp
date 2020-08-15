class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int sum = 0;
        for(int i = 0; i<nums.size();i++){
            int temp = min(nums[i],nums[i+1]);
            sum+= temp;
            i++;
        }
        return sum;
    }
};