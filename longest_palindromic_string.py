# Method to get longest palindrome via dynamic prgramming
# time complexity: O(n*2)

import pdb
class Solution:
    def longestPalindrome(self, s: str) -> str:
        print("input string:", s)
        longest_palindrome=s[0]
        if len(s)==1:
            return s
        else:
            for i in range(len(s)-1):
                print(f"Iteration: {i} Character: {s[i]}")
                palindrome=""
                if s[i]==s[i+1]:
                    print("getting even palindrome")
                    palindrome = self.get_even_palindrome(s, i)
                    if len(palindrome)> len(longest_palindrome):
                        longest_palindrome = palindrome
                if s[i-1] == s[i+1] and i>=1:
                    palindrome = self.get_odd_palindrome(s, i)
                    if len(palindrome)> len(longest_palindrome):
                        longest_palindrome = palindrome
            return longest_palindrome                
            

    def get_even_palindrome(self, s: str, i: int) -> str:
        k=1# i=1
        palindrome = s[i] + s[i+1]
        while(k<i+1 and k<len(s)-i-1):
            print(f"k: {k} palindrome: {palindrome}")
            if s[i-k]==s[i+1+k]: 
                palindrome = s[i-k] + palindrome + s[i+1+k]
                k = k+1
            else:
                return palindrome
        return palindrome

    def get_odd_palindrome(self, s: str, i: int) -> str:
        k=2
        palindrome = s[i-1] + s[i] + s[i+1]
        while(k<i+1 and k<len(s)-i):
            print(f"k: {k} palindrome: {palindrome}")
            if s[i+k]==s[i-k]:
                palindrome = s[i-k] + palindrome + s[i+k]
                k = k+1
            else:
                return palindrome
        return palindrome

print(Solution().longestPalindrome("ccc")) # len = 13

