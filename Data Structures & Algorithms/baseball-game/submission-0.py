class Solution:
    def calPoints(self, input_array: List[str]) -> int:
        
        stack = []

        for i in range(0, len(input_array), 1):
            
            if input_array[i] == '+':
                if stack[-1] and stack[-2]:
                    stack.append(int(stack[-1] + stack[-2]))

            elif input_array[i] == 'C':
                if stack:
                    stack.pop()

            elif input_array[i] == 'D':
                if stack:
                    stack.append(int(stack[-1] * 2))   

            elif input_array[i].lstrip('-+').isdigit():
                stack.append(int(input_array[i])) 

        return sum(stack)              