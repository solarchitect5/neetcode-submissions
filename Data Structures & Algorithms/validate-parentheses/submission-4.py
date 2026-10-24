class Solution:
    def isValid(self, input_string: str) -> bool:
        
        if (not input_string) or len(input_string) == 1:
            return False

        stack = []

        for i in range (0, len(input_string), 1):
            if stack: 
                if stack[-1] == '(' and input_string[i] == ')': 
                    stack.pop()
                elif stack[-1] == '{' and input_string[i] == '}': 
                    stack.pop()
                elif stack[-1] == '[' and input_string[i] == ']': 
                    stack.pop()
                else:
                    stack.append(input_string[i])
            else:
                stack.append(input_string[i])

        return (not stack)