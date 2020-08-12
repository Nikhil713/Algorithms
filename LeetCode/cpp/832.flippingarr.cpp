class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        for( auto &i : A){
            reverse(i.begin(),i.end());
        }
        for( auto &i :A){
            for( auto &j : i){
                j = j^1;
            }
        }
        return A;
    }
};