# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0
        n = len(word)
        vwls = ["a","e","i","o","u"]
        for i in range(n):
            if word[i] in vwls:
                ans += (i+1) * (n-i)

        return ans