class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or int(s) == 0:
            return 0
        possibs = list()

        for i in range(len(s)):
            if(i == 0):
                if int(s[i]) == 0:
                    return 0
                else:
                    possibs.append(1)
                continue
                    
            if(i == 1):
                num = int("".join(s[i-1:i+1]))
                if(num > 9 and num < 27 and int(s[i]) > 0):
                    possibs.append(2)
                elif(num > 9 and num < 27):
                    possibs.append(1) 
                elif(int(s[i]) == 0):
                    return 0
                else:
                    possibs.append(1)
                continue
                    
               
            num = int("".join(s[i-1:i+1]))
            print num
            if(num > 9 and num < 27 and int(s[i]) > 0):
                possibs.append(possibs[i-1] + possibs[i-2])
            elif(num > 9 and num < 27):
                possibs.append(possibs[i-2])
            elif(int(s[i]) == 0):
                return 0
            else:
                possibs.append(possibs[i-1])
                
        print possibs
        return possibs[len(possibs)-1]