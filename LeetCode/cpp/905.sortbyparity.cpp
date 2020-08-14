// Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

// You may return any answer array that satisfies this condition.

 

// Example 1:

// Input: [3,1,2,4]
// Output: [2,4,3,1]
// The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

 

// Note:

//     1 <= A.length <= 5000
//     0 <= A[i] <= 5000

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector<int> odd,even;
        for(auto i:A){
            if(i%2 == 1){
                odd.push_back(i);
            }   
            else{
                even.push_back(i);
            }
        }
        even.insert(even.end(),odd.begin(),odd.end());
        return(even);
    }
};