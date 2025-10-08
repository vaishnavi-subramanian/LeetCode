class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq=0
        max_length = 0
        l=0
        char_count={}
        for r in range(len(s)):
            char_count[s[r]]=char_count.get(s[r],0)+1
            max_freq = max(max_freq,char_count[s[r]])
            while (r-l+1)-max_freq >k:
                char_count[s[l]]-=1
                l+=1
            max_length = max(max_length,r-l+1)
        return max_length