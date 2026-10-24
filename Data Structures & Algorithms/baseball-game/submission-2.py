class Solution:
    def calPoints(self, input_array: List[str]) -> int:
        
        stack = []
        value = 0

        for i in range(0, len(input_array), 1):
            
            if input_array[i] == '+':
                if stack[-1] and stack[-2]:
                    value = value + int(stack[-1] + stack[-2])
                    stack.append(int(stack[-1] + stack[-2]))

            elif input_array[i] == 'C':
                if stack:
                    value = value - stack[-1]
                    stack.pop()

            elif input_array[i] == 'D':
                if stack:
                    value = value + int(stack[-1] * 2)
                    stack.append(int(stack[-1] * 2))   

            elif input_array[i].lstrip('-+').isdigit():
                value = value + int(input_array[i])
                stack.append(int(input_array[i])) 

        return value             