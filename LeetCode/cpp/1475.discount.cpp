class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        vector<int> res;
        int i,j,temp;
        for( i = 0 ; i<prices.size();i++){
            temp = 0;
            for( j = i + 1 ; j < prices.size(); j++){
                if ( prices[j] <= prices[i]){
                    temp = prices[j];
                    break;
                }
            }
            res.push_back(prices[i] - temp);
        }
        return res;
    }
};