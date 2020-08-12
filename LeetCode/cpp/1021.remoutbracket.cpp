// A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

// A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

// Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

// Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

// Example 1:

// Input: "(()())(())"
// Output: "()()()"
// Explanation: 
// The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
// After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

// Example 2:

// Input: "(()())(())(()(()))"
// Output: "()()()()(())"
// Explanation: 
// The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
// After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

// Example 3:

// Input: "()()"
// Output: ""
// Explanation: 
// The input string is "()()", with primitive decomposition "()" + "()".
// After removing outer parentheses of each part, this is "" + "" = "".

 

// Note:

//     S.length <= 10000
//     S[i] is "(" or ")"
//     S is a valid parentheses string

class Solution {
public:
    string removeOuterParentheses(string S) {
        int i,count,j;
        i = 0;
        j = 0;
        count = 0;
        string res;
        while(j < S.size() && i < S.size()){
            if (S[j] == '('){
                count++;
            } 
            if (S[j] == ')'){
                count--;
            }
            if (count == 0 && i!=j){
                res += S.substr(i+1,j-i-1);
                i = j+1;
            }
            j++;
        }
        return res;
    }
};