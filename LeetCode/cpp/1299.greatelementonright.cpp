class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        vector<int> res = arr;
        int g = -1;
        for(int i = arr.size()-1;i >= 0;i--){
            res[i] = g;
            g = max(g,arr[i]);   
        }
        return res;
    }
};