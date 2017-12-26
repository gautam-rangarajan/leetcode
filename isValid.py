class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracks = {"]":"[", ")":"(", "}":"{"}
        for brack in s:
            if brack in bracks.values():
                stack.append(brack)
            elif brack in bracks.keys():
                if(stack == [] or bracks[brack] != stack.pop()):
                    return False
            else:
                return False
        if(stack != []):
            return False
        
        return True