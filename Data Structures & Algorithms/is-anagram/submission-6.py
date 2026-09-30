class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_store = {}
        t_store = {}
        for i in range(len(s)):
            if s[i] not in s_store:
                s_store[s[i]] = 1
            else:
                s_store[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in t_store:
                t_store[t[i]] = 1
            else:
                t_store[t[i]] += 1

        if s_store == t_store:
            return True
        return False
                