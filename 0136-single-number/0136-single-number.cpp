class Solution {
public:
    int singleNumber(vector<int>& nums) {
        // O(n) and O(n) -> fails because uses extra space
        /*
            unordered_map<int,int> um;
            for(int i=0;i<nums.size();i++){
                um[nums[i]]++;
            }
            for(auto x:um) {
                if(x.second==1)
                    return x.first;
            }
            return -1;
        */
        // O(n) and O(1)
        int a = 0;
        for(int i=0;i<nums.size();i++){
            a ^= nums[i];
        }
        return a;
    }
};