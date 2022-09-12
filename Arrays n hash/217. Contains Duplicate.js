// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

/**
 * @param {number[]} nums
 * @return {boolean}
 */


 var containsDuplicate = function(nums) {
    // check inputs
    if (!nums || nums.length === 0){
        return false
    }
    //create hashmap
    let hash = {};
    //loop through the nums and add to map if not in map
    //if  in map return true
    for(const num of nums){
        if (!hash[num]){
            hash[num] = 1;
        } else{
            return true
        }
    }
    return false
};
console.log(containsDuplicate([1,2,3]));
// O(n) time 
// O(n) space