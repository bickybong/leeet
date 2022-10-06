from sqlalchemy import false


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # bracket counter for each type
        # loop through string and count open and closed brackets
        # if all 0 at end return true
        # counterRound, counterCurl, counterRect = 0,0,0
        # for brac in s:
        #     print(brac)

        # hashmap to map closing bracket to opening bracket
        # go through stack, if open bracket add to stack
        # if close bracket check with latest stack
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        for brac in s:
            if brac in closeToOpen:
                if stack and stack[-1] == closeToOpen[brac]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brac)
        if not stack:
            return True
        else:
            return False



            
sol = Solution()
print(sol.isValid( "()[]{}"))