class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<vector<int>> mat2 = mat;
        sort(mat2.begin(),mat2.end());
        vector<int> res;
        vector<int> temp(mat2[0].size(),-1);
        int ind,j=0;
        for (int i = 0; i<k;i++ ){
            j=0;
            while(j<mat.size()){
                if (mat2[i] == mat[j]){
                    mat[j] = temp;
                    ind = j;
                    j++;
                    break;
                }
                j++;
            }
            res.push_back(ind);
        }
        return res;
    }
};