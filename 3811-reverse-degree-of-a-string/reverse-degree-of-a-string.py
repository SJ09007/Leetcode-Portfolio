class Solution:
    def reverseDegree(self, s: str) -> int:
        
        s1=0
        for i,ch in enumerate(s):
            rev_pos=26-(ord(ch)-ord('a'))   #rem this to reverse a position of letter in a string
            s1+=(i+1)*rev_pos
        return s1