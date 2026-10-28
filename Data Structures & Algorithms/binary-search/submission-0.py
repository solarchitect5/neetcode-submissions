class Solution:
    def search(self, input_array: List[int], target: int) -> int:
        left_index = 0 
        right_index = len(input_array) - 1
        while left_index <= right_index: 
            mid_index = (left_index + right_index) // 2
            if target > input_array[mid_index]:
                left_index = mid_index + 1
            elif target < input_array[mid_index]:
                right_index = mid_index - 1
            else:
                return mid_index
        return -1