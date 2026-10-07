class Solution {
public:
    int maxArea(vector<int>& height) {
        int left =0;
        int right = height.size() - 1;
        int maxVolume = 0;
        int currentVolume = 0;
        while(left < right){
            currentVolume = min(height[left],height[right]) * (right - left);
            if (maxVolume < currentVolume) {
                maxVolume = currentVolume;
            }
            if (height[left] < height[right]){
                left++;
            }
            else{
                right--;
            }
            
        } 
        return(maxVolume);
    }
};