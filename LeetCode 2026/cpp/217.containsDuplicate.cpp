class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seenNumbers;
        for(int i: nums){
            if (seenNumbers.count(i)){
                return true;
            }
            seenNumbers.insert(i);
        }
        return false;
    }
};