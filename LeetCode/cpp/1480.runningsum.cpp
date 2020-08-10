class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int sum = 0;
        vector<int>arr;
        for(int i=0;i< nums.size();i++){
            sum += nums[i];
            arr.push_back(sum);
        }
        return arr;
    }
};