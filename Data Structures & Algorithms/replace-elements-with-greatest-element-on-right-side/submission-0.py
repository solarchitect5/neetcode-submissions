class Solution:
    def replaceElements(self, input_array: List[int]) -> List[int]:
        
        rightMax: int = -1
        output_array = [0] * len(input_array)

        for i in range(len(input_array)-1, -1, -1):
            output_array[i] = rightMax
            rightMax = max(rightMax, input_array[i])

        return output_array    