#create a hash table on the fly

def lengthOfLongestSubstring(s):
    max_len = 0
    longest_substr = ""
    for i in range(len(s)):
        leading_char = s[i]
        print('leading_char i ', leading_char, i)
        char_set = set()
        substr = ""
        for j, char in enumerate(s[i:]):
            print("char j ",char, j)
            if char not in char_set:
                substr = substr + char
                char_set.add(char)
            else:
                if len(substr)> max_len:
                    max_len = len(substr)
                    longest_substr = substr
                print("temp sub str", longest_substr)
                break                          
            if j == len(s)-i-1 and len(substr)>= max_len:
                print("Last char")
                max_len = len(substr)
                longest_substr = substr
                print(longest_substr)
                return max_len
    print(longest_substr)
    return max_len


s = "aab"                
print(lengthOfLongestSubstring(s))

