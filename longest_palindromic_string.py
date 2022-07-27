# use slicing to reverse a tring s[::-1]
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# check in descenfig order
# a= "yuwwababadfed"
# a= "weqyuwwa"
# a1="-ad"
# a_ = "dabab"

# Method to get longest palindrome via dynamic prgramming
# time complexity: O(n*2)
import pdb
class Solution:
    def longestPalindrome(self, s: str) -> str:
        print("input string:", s)
        longest_palindrome=""
        for i in range(len(s)-1):# range =  0,1,2 ..., 11
            print(f"Iteration: {i} Character: {s[i]}")
            palindrome=""
            k = 1
            if s[i]==s[i+1]:
                print("geting even palindrome")
                palindrome = self.get_even_palindrome(s, i)
                if len(palindrome)> len(longest_palindrome):
                    longest_palindrome = palindrome
            elif s[i-1] == s[i+1]:
                palindrome = self.get_odd_palindrome(s, i)
                if len(palindrome)> len(longest_palindrome):
                    longest_palindrome = palindrome
        return longest_palindrome                
            

    def get_even_palindrome(self, s: str, i: int) -> str:
        k=2
        palindrome = s[i] + s[i+1]
        print(f"k: {k} palindrome: {palindrome}")
        while(k<i+1 and k<len(s)-i):
            if s[i-k]==s[i+1+k]:
                palindrome = s[i-k] + palindrome + s[i+1+k]
                k = k+1
            else:
                return palindrome
        return palindrome

    def get_odd_palindrome(self, s: str, i: int) -> str:
        k=2 # i  = 
        # pdb.set_trace()
        palindrome = s[i-1] + s[i] + s[i+1]
        while(k<i+1 and k<len(s)-i):
            if s[i+k]==s[i-k]:
                palindrome = s[i-k] + palindrome + s[i+k]
                k = k+1
            else:
                return palindrome
        return palindrome

print(Solution().longestPalindrome("yuwwababadfed")) # len = 13

