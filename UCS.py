# Name = Muhammad Ali Ahson
# Roll = 21i-2535
# Assignment 2



import heapq

class UCS:
    def __init__(self, grid, start, goal, no_of_steps):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.path = []
        self.step_used = 0
        self.no_of_steps = no_of_steps
        self.cost = 0

    def performance_measure(self):
        performance = 100 - ((self.step_used / self.no_of_steps) * 100)
        print("The Performance of the Model Agent is", performance, "%")

    def check_termination(self):
        return self.step_used >= self.no_of_steps

    def ucs(self):
        # Directions: (row_offset, col_offset) for up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Initialize priority queue for UCS
        pq = []
        heapq.heappush(pq, (0, self.start))  # (cost, current_position)
        visited = set()
        costs = {self.start: 0}
        predecessors = {self.start: None}
        
        while pq:
            current_cost, current_position = heapq.heappop(pq)
            current_row, current_col = current_position
            
            # Check if the goal is reached
            if current_position == self.goal:
                # Reconstruct the path from goal to start
                while current_position:
                    self.path.append(current_position)
                    current_position = predecessors[current_position]
                self.path.reverse()  # Reverse the path to be from start to goal
                print("Path found:", self.path)
                print("Total Cost:", current_cost)
                return self.path
            
            if current_position not in visited:
                visited.add(current_position)
                self.step_used += 1
                
                # Check for termination
                if self.check_termination():
                    break
                
                # Explore neighbors
                for row_offset, col_offset in directions:
                    neighbor_row = current_row + row_offset
                    neighbor_col = current_col + col_offset
                    neighbor_position = (neighbor_row, neighbor_col)
                    
                    # Calculate the new cost to move to the neighbor
                    if 0 <= neighbor_row < len(self.grid) and 0 <= neighbor_col < len(self.grid[0]):
                        new_cost = current_cost + self.grid[neighbor_row][neighbor_col]
                        
                        # Check if the neighbor has a lower cost
                        if neighbor_position not in costs or new_cost < costs[neighbor_position]:
                            costs[neighbor_position] = new_cost
                            predecessors[neighbor_position] = current_position
                            heapq.heappush(pq, (new_cost, neighbor_position))
        
        print("No Solution Found")
        return None  # Return None if no path is found