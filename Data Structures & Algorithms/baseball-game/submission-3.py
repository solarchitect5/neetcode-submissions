class Solution:
    def calPoints(self, input_array: List[str]) -> int:
        
        stack = []
        total = 0

        for i in range(0, len(input_array), 1):
            
            if input_array[i] == '+':
                if stack[-1] and stack[-2]:
                    total = total + int(stack[-1] + stack[-2])
                    stack.append(int(stack[-1] + stack[-2]))

            elif input_array[i] == 'C':
                if stack:
                    total = total - stack[-1]
                    stack.pop()

            elif input_array[i] == 'D':
                if stack:
                    total = total + int(stack[-1] * 2)
                    stack.append(int(stack[-1] * 2))   

            elif input_array[i].lstrip('-+').isdigit():
                total = total + int(input_array[i])
                stack.append(int(input_array[i])) 

        return total             