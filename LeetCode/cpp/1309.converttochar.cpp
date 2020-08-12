class Solution {
public:
    string freqAlphabets(string s) {
        int i=0;
        string res;
        while( i < s.size()){
            if (i < s.size() - 2 && s[i+2] == '#'){
                res += 'a' - 1 + (s[i] - '0')*10 + (s[i+1] - '0');
                i+=3;
            }
            else{
                res += 'a'- 1 + (s[i] - '0');
                i++;
            }
        }
        return res;
    }
};