# Data for the grid
grid = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T"],
    ["U", "V", "W", "X", "Y"],
    ["Z", "AA", "AB", "AC", "AD"]
]

# position finding function within grid
def find_cell(cell):
    for row_index, row in enumerate(grid):
        if cell in row:
            return (row_index, row.index(cell))
    return None

# Function to visit the adjacent cells
def get_neighbors(cell):
    neighbors = []
    row, col = find_cell(cell)
    
    # Check Up
    if row > 0:
        neighbors.append(grid[row - 1][col])
    # Check Down
    if row < len(grid) - 1:
        neighbors.append(grid[row + 1][col])
    # Check Left
    if col > 0:
        neighbors.append(grid[row][col - 1])
    # Check Right
    if col < len(grid[0]) - 1:
        neighbors.append(grid[row][col + 1])
    
    return neighbors

# user input for initial and goal state
start_state = input("Enter the starting state: ")
goal_state = input("Enter the goal state: ")

# //initialization
found_goal = False
open_list = [(start_state, None)]  
visited_cells = []  
examined_states = []  

# loop for performing operation like removing state from open queue and adding into closed list
while open_list:
    current_cell = open_list.pop(0)
    visited_cells.append(current_cell)
    examined_states.append(current_cell[0])  # Append the current cell to examined states
    
    # Check if the goal is found
    if current_cell[0] == goal_state:
        found_goal = True
        break
    
    neighbors = get_neighbors(current_cell[0])
    
    # Add unvisited neighbors to the open list
    for neighbor in neighbors:
        if neighbor not in [cell[0] for cell in open_list] and neighbor not in [cell[0] for cell in visited_cells]:
            open_list.append((neighbor, current_cell[0]))

# display of examined states
print(f"\nExamined states: {examined_states}")

# solution path output if goal found
if found_goal:
    print("\nGoal Found!")
    path = [current_cell[0]]
    while current_cell[1] is not None:
        for cell in visited_cells:
            if cell[0] == current_cell[1]:
                current_cell = cell
        path.append(current_cell[0])
    path.reverse()
    print("\nShortest Path:")
    print(" -> ".join(path))
else:
    print("\nGoal Not Found!")

# display the total number of examined cells
print(f"\nTotal number of cells examined: {len(examined_states)}")
