# Name = Muhammad Ali Ahson
# Roll = 21i-2535
# Assignment 2


import random
import numpy as np

class DFS:
    def __init__(self, grid, start, goal,no_of_steps):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.path = []
        self.step_used = 0
        self.no_of_steps = no_of_steps

    def check_termination(self):
        if self.no_of_steps == self.step_used:
            return True
        else:
            return False

    def performance_measure(self):
        performance = 100 - ((self.step_used / self.no_of_steps) * 100)
        print("The Performance of the Model Agent is", performance, "%")


    def dfs(self):
        # Directions: (row_offset, col_offset) for up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Initialize stack for DFS
        stack = [(self.start, [])]  # (current_position, path)
        visited = set()
        
        while stack:
            (current_row, current_col), path = stack.pop()
            
            # Check if the goal is reached
            if (current_row, current_col) == self.goal:
                self.path = path + [(current_row, current_col)]
                print("Path found:", self.path)
                return self.path
            
            if (current_row, current_col) not in visited:
                visited.add((current_row, current_col))
                self.step_used += 1  # Increment step count after each step
                
                # Explore neighbors
                for row_offset, col_offset in directions:
                    neighbor_row = current_row + row_offset
                    neighbor_col = current_col + col_offset
                    
                    # Check bounds and if the neighbor is not visited
                    if 0 <= neighbor_row < len(self.grid) and 0 <= neighbor_col < len(self.grid[0]) and (neighbor_row, neighbor_col) not in visited:
                        stack.append(((neighbor_row, neighbor_col), path + [(current_row, current_col)]))
        
        print("No Solution Found")
        return None  # Return None if no path is found
