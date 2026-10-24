class Solution:
    def calPoints(self, input_array: List[str]) -> int:
        
        stack = []

        for i in range(0, len(input_array), 1):
            
            if input_array[i] == '+':
                if stack[-1] and stack[-2]:
                    value = int(stack[-1] + stack[-2])
                    stack.append(value)

            elif input_array[i] == 'C':
                if stack:
                    stack.pop()

            elif input_array[i] == 'D':
                if stack:
                    value = int(stack[-1] * 2)
                    stack.append(value)   

            elif input_array[i].lstrip('-+').isdigit():
                value = int(input_array[i])
                stack.append(value) 

        return sum(stack)              