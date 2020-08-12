class Solution {
public:
    vector<int> sumZero(int n) {
        int i;
        vector<int> res;
        for(i = 1 ; i < n/2 + 1; i++){
            res.push_back(i);
            res.push_back(-i);
        }
        if( n % 2 == 1){
            res.push_back(0);
        }
        return res;
    }
};