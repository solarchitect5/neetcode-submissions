class Solution:
    def searchMatrix(self, input_matrix: List[List[int]], target: int) -> bool:

        for current_row in range(0, len(input_matrix), 1):

            left_index = 0 
            right_index = len(input_matrix[current_row]) - 1

            while left_index <= right_index: 
                mid_index = (left_index + right_index) // 2

                if target > input_matrix[current_row][mid_index]:
                    left_index = mid_index + 1

                elif target < input_matrix[current_row][mid_index]:
                    right_index = mid_index - 1

                else:
                    return True
        
        return False