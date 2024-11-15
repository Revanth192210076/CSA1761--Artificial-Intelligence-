# Define the map (graph) and constraints
# Each region has a list of neighboring regions

regions = {
    "A": ["B", "C", "D"],
    "B": ["A", "D", "E"],
    "C": ["A", "D"],
    "D": ["A", "B", "C", "E"],
    "E": ["B", "D"]
}

# Define available colors
colors = ["Red", "Green", "Blue"]

# Dictionary to store color assignment
color_assignment = {}

# Function to check if the current color assignment is valid
def is_valid(region, color):
    for neighbor in regions[region]:
        # Check if the neighbor is already colored with the same color
        if color_assignment.get(neighbor) == color:
            return False
    return True

# Backtracking function to color the map
def color_map(region_index=0):
    if region_index == len(regions):
        return True  # All regions are colored successfully
    
    region = list(regions.keys())[region_index]
    
    for color in colors:
        if is_valid(region, color):
            # Assign color and proceed with the next region
            color_assignment[region] = color
            if color_map(region_index + 1):
                return True
            # Backtrack if not successful
            color_assignment[region] = None
    
    return False  # Return false if no color can be assigned

# Run the map coloring CSP
if color_map():
    print("Color Assignment for each region:")
    for region, color in color_assignment.items():
        print(f"{region}: {color}")
else:
    print("No solution found.")
