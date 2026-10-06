class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> seenNums;
        for (int i = 0; i < nums.size(); i++){
            int complement = target - nums[i];
            if(seenNums.count(complement)){
                return{seenNums[complement],i};
            }
            seenNums[nums[i]] = i;
        }
        return{};
    }
};