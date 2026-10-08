class Solution {
public:
    bool isValid(string s) {
            stack<char> st;
            char checker;
            for(int i = 0; i < s.size(); i++){
                if(s[i] == '(' or s[i] =='{' or s[i] =='['){
                    st.push(s[i]);
                }
                if(st.empty()){
                    return false;
                }
                if(s[i] == ')'){
                    checker = st.top();
                    st.pop();
                    if (checker != '('){
                        return false;
                    }
                }
                if(s[i] == '}'){
                    checker = st.top();
                    st.pop();
                    if (checker != '{'){
                        return false;
                    }
                }
                if(s[i] == ']'){
                    checker = st.top();
                    st.pop();
                    if (checker != '['){
                        return false;
                    }
                }
            }
        return st.empty();
    }
};