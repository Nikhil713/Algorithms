class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {

        vector<int> daysToWarm(temperatures.size(), 0);
        stack<int> st;
        int prev;
        for(int i =0; i < temperatures.size(); i++){
            while(!st.empty() && temperatures[i] > temperatures[st.top()]){
                prev = st.top();
                st.pop();
                daysToWarm[prev] = i - prev;
            }
            st.push(i);
        }
        return daysToWarm;

    }
};