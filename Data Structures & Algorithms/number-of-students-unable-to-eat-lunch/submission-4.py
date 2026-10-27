from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students_queue = deque(students)
        sandwiches_stack = sandwiches[::-1]
        exit_counter = 0

        while sandwiches_stack:
            if exit_counter == len(students_queue):
                break
            else: 
                if sandwiches_stack[-1] == students_queue[0]:
                    sandwiches_stack.pop()
                    students_queue.popleft()
                    exit_counter = 0
                else:
                    front_student = students_queue.popleft()
                    students_queue.append(front_student)
                    exit_counter += 1
        return exit_counter