class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> numCounter;
        for(int i: nums){
            numCounter[i]++;
        }
        priority_queue<pair<int,int>> pq;

        for(auto& pair:numCounter){
            pq.push({pair.second, pair.first});
        }
        vector<int> answer;
        for(int i=0; i < k; i++){
            answer.push_back(pq.top().second);
            pq.pop();
        }
        return answer;
    }
};