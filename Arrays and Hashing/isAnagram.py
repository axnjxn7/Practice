class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        for ch in s:
            s_freq[ch] = s_freq.get(ch, 0) + 1
        
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1
        
        if s_freq == t_freq:
            return True

        return False
        

sol = Solution()
print(sol.isAnagram(s = "racecar", t = "carrace"))
print(sol.isAnagram(s = "jar", t = "jam"))