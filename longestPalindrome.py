class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestPal = ""
        for i in range(len(s)):
            #Case1
            palLen = 1
            if(palLen > len(longestPal)):
                longestPal = s[i]
            l = i-1
            r = i+1
            while (l >= 0 and r < len(s)):
                if(s[l] == s[r]):
                    palLen = palLen + 2
                    if(palLen > len(longestPal)):
                        longestPal = s[l:r+1]
                    l = l-1
                    r = r+1
                else:
                    break
                    
        for i in range(1,len(s)):      
            #Case2
            if s[i] == s[i-1]:
                palLen = 0
                l = i-1
                r = i
                while (l >= 0 and r < len(s)):
                    if(s[l] == s[r]):
                        palLen = palLen + 2
                        if(palLen > len(longestPal)):
                            longestPal = s[l:r+1]
                        l = l-1
                        r = r+1
                    else:
                        break
        return longestPal
                        