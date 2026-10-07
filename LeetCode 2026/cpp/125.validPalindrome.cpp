class Solution {
public:
    bool isPalindrome(string palindrome) {
        int left =0;
        int right=palindrome.size()-1;
        while(left < right){
            if (!isalnum(palindrome[left])){
                left++;
                continue;
            }
            if (!isalnum(palindrome[right])){
                right--;
                continue;
            }
            if(tolower(palindrome[left]) != tolower(palindrome[right])){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};