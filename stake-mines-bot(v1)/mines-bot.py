import pyautogui
import random
import time

# Function to generate a random position around a base position within a specified randomness range
def randomize_position(base_x, base_y, randomness):
    return (base_x + random.randint(-randomness, randomness),
            base_y + random.randint(-randomness, randomness))

# Function to generate unique random positions within a specified range
def generate_unique_positions(x_min, x_max, y_min, y_max, min_distance, num_positions):
    def is_valid_position(x, y, positions):
        return all(abs(x - pos[0]) >= min_distance and abs(y - pos[1]) >= min_distance for pos in positions)
    
    positions = []
    attempts = 0
    while len(positions) < num_positions and attempts < 1000:
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        if is_valid_position(x, y, positions):
            positions.append((x, y))
        attempts += 1
    
    if len(positions) < num_positions:
        raise Exception("Could not generate enough unique positions")
    
    return positions

# Function to execute the sequence of actions
def perform_actions(precomputed_positions):
    # Part 1: Move to and click a slightly randomized position around (620, 448)
    base_x, base_y = 620, 448
    randomness = 20
    target_x, target_y = randomize_position(base_x, base_y, randomness)
    pyautogui.moveTo(target_x, target_y, duration=random.uniform(0.1, 0.4))
    pyautogui.click()
    print(f"Mouse moved to and clicked at position: ({target_x}, {target_y})")

    # Add a short random delay before the next set of actions
    time.sleep(random.uniform(0.1, 0.4))

    # Part 2: Click at precomputed unique random locations
    for pos in precomputed_positions:
        x, y = pos
        pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.4))
        pyautogui.click()
        print(f"Mouse moved to and clicked at position: ({x}, {y})")
        time.sleep(random.uniform(0.1, 0.4))

    # Part 3: Move to and click a slightly randomized position around (638, 575)
    base_x, base_y = 638, 575
    randomness = 20
    target_x, target_y = randomize_position(base_x, base_y, randomness)
    pyautogui.moveTo(target_x, target_y, duration=random.uniform(0.1, 0.4))
    pyautogui.click()
    print(f"Mouse moved to and clicked at position: ({target_x}, {target_y})")

# Main loop to perform actions repeatedly
def main():
    num_iterations = int(input("Enter the number of iterations: "))
    num_positions_sets = 4  # Number of unique sets of positions to precompute
    positions_per_set = 4 # Number of positions per set

    x_min, x_max = 937, 1504 #Adjust this based on your screensize
    y_min, y_max = 240, 824
    min_distance = 100

    # Precompute sets of unique positions
    precomputed_positions_sets = []
    for _ in range(num_positions_sets):
        positions = generate_unique_positions(x_min, x_max, y_min, y_max, min_distance, positions_per_set)
        precomputed_positions_sets.append(positions)
    
    for i in range(num_iterations):
        # Use a different set of positions every few iterations to maintain variability
        precomputed_positions = precomputed_positions_sets[i % num_positions_sets]
        perform_actions(precomputed_positions)
        time.sleep(random.uniform(0.1, 0.4))  # Random delay between iterations

if __name__ == "__main__":
    main()
