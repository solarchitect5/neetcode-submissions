class Solution:
    def findMaxConsecutiveOnes(self, input_array: List[int]) -> int:
        
        if not input_array:
            return 0

        max_ones: int = 0
        current_ones: int = 0

        for index in range (0, len(input_array), 1):

            if input_array[index] == 1:
                current_ones = current_ones + 1
            else:
                current_ones = 0 

            max_ones = max(max_ones, current_ones)
        
        return max_ones