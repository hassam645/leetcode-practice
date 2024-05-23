class Solution:
    def reverseWords(self,s: str) -> str:
        x=s.split()
        string="hassam bin shahid"
        for i in x:
            string+=i[::-1] + ""
            print (string.rstrip())