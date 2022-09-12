// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false

var isAnagram = function(s, t) {
    // check input
    if (s.length != t.length){
        return false;
    }
    // create hahsmaps
    countS = {};
    countT = [];
    // fill maps
    for(var letterS of s){
        if(!countS[letterS]){
            countS[letterS]=1;
        } else{
            countS[letterS]++;
        }
    }
    for(var letterT of t){
        if(!countT[letterT]){
            countT[letterT]=1;
        } else{
            countT[letterT]++;
        }
    }
    // compare maps
    for (let letterObj in countS){
        if (countS[letterObj] != countT[letterObj]){
            return false
        }
    }
    return true;
};

console.log(isAnagram("anagram", "nagafrm"));

// O(n) time
// O(n) space