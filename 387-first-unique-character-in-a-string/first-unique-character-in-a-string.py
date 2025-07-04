class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Accepted but i feel not optimized enough, can use counter and queue but its all the same
        length = len(s)
        if length == 1:
            return 0
        if length == 0:
            return -1
        for i in range(0,length):
            if s[i] not in s[0:i]+s[i+1:]:
                return i
        return -1
        #

