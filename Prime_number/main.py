import zipfile
import os

# Your Sumdoku solving logic
def is_valid(grid, row, col, num):
    # Check if 'num' is not already present in the current row and column.
    for i in range(N):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

def solve_sumdoku(grid, rules, rule_idx):
    if rule_idx == len(rules):
        return True  # All rules have been successfully applied.

    rule = rules[rule_idx]
    result, operation, region = rule

    for row in range(N):
        for col in range(N):
            if grid[row][col] == region:
                if operation == '+':
                    for num in range(1, N + 1):
                        if is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if solve_sumdoku(grid, rules, rule_idx + 1):
                                return True
                            grid[row][col] = region
                elif operation == '*':
                    for num in range(1, N + 1):
                        if result % num == 0 and is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if solve_sumdoku(grid, rules, rule_idx + 1):
                                return True
                            grid[row][col] = region
                elif operation == '-':
                    for num1 in range(1, N + 1):
                        num2 = num1 + result
                        if num2 <= N and is_valid(grid, row, col, num1) and is_valid(grid, row, col, num2):
                            grid[row][col] = num1
                            if solve_sumdoku(grid, rules, rule_idx + 1):
                                return True
                            grid[row][col] = region
                elif operation == '/':
                    for num1 in range(1, N + 1):
                        num2 = num1 * result
                        if num2 <= N and is_valid(grid, row, col, num1) and is_valid(grid, row, col, num2):
                            grid[row][col] = num1
                            if solve_sumdoku(grid, rules, rule_idx + 1):
                                return True
                            grid[row][col] = region
    return False

def solve_grid(grid, rules):
    global N
    N = len(grid)
    if solve_sumdoku(grid, rules, 0):
        return grid
    return None

# Define the function to unscramble the password using the Sumdoku algorithm
def unscramble_password(password, grid, rules):
    # Your Sumdoku solving logic here to unscramble the password
    return unscrambled_password

# Path to the challenge.zip file on your desktop
desktop_path = os.path.expanduser("~/Desktop")
challenge_zip_path = os.path.join(desktop_path, "challenge.zip")

# Initialize the initial password as None
initial_password = None

# Initialize a counter for the level
level = 1

while os.path.exists(challenge_zip_path):
    # Open the challenge.zip file with the current password
    with zipfile.ZipFile(challenge_zip_path, 'r', compression=zipfile.ZIP_STORED) as zip_archive:
        # If this is the first level, extract the password from the first entry in the zip file
        if level == 1 and initial_password is None:
            first_entry_name = zip_archive.namelist()[0]
            initial_password = first_entry_name.encode('utf-8')

        # Extract and read the text file for the current level
        text_file_name = f'lvl_{level}.txt'
        with zip_archive.open(text_file_name, 'r', pwd=initial_password) as text_file:
            text_content = text_file.read().decode('utf-8')

    # Unscramble the password from the text content
    unscrambled_password = unscramble_password(initial_password.decode('utf-8'), grid, rules)

    # Use the unscrambled password to open the next level's zip file
    next_level_zip = f'lvl_{level + 1}.zip'
    next_level_txt = f'lvl_{level + 1}.txt'

    with zipfile.ZipFile(challenge_zip_path, 'r', compression=zipfile.ZIP_STORED) as next_zip_archive:
        with next_zip_archive.open(next_level_txt, 'r', pwd=unscrambled_password.encode('utf-8')) as text_file:
            text_content = text_file.read().decode('utf-8')

    # Update the password and level for the next iteration
    initial_password = unscrambled_password.encode('utf-8')
    level += 1

    # Update the path to the challenge.zip file
    challenge_zip_path = os.path.join(desktop_path, next_level_zip)

# Display the contents of the last zip file
if os.path.exists(challenge_zip_path):
    with zipfile.ZipFile(challenge_zip_path, 'r', compression=zipfile.ZIP_STORED) as last_zip_archive:
        last_zip_contents = last_zip_archive.namelist()
        print(f"Contents of the last zip file: {last_zip_contents}")
else:
    print("No more zip files left.")

print("All files have been processed.")