class Solution {
public:
    int maxProduct(vector<int>& nums) {
        vector<int> nums1 = nums;
        sort(nums1.begin(),nums1.end(),greater<int>());
        int last = nums1[0];
        int seclast = nums1[1];
        
        return ((last-1 ) * (seclast - 1)) ;
    }
};