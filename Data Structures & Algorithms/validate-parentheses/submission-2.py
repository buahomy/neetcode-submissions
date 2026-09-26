class Solution:
    def isValid(self, s: str) -> bool:
        
        # X two pointers l, r and dict to map >> it does not track the valid order properly 
        # e.g ()[]{} or when [(]) it'd keep finding the match no order
        # stack does it in the right order
        stack = [] # to store (opening brackets), pop later once the match of closing is found
        bracketDict= {")": "(", "]": "[", "}": "{"}

        for bracket in s:
            if bracket in bracketDict: #refer to key (closing bracket)
                # if stack -> not an empty stack (there's opening)
                if stack and stack[-1] == bracketDict[bracket]: 
                    stack.pop()
                else:
                    return False
            # 1) >> it'd append all openings here first  
            else:
                stack.append(bracket)
        return True if not stack else False #true for empty stack (after matching)        




        