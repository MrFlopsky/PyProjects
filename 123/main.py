import zipfile
import itertools

# Define the path to the ZIP file
zip_file = "important_dental_information.zip"

# Define the target file to extract (in this case, "flag.txt")
target_file = "flag.txt"

# Define the charset (digits, lowercase, and uppercase letters)
charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Define the password length
password_length = 6  # Change this to the desired password length

# Generate all possible combinations of characters for the given length
combinations = itertools.product(charset, repeat=password_length)

# Create a file to save tried passwords
with open("tried_passwords.txt", "w") as tried_passwords_file:
    for combination in combinations:
        password = "".join(combination)
        try:
            with zipfile.ZipFile(zip_file, "r") as zipf:
                # Check if the target file exists in the ZIP archive
                if target_file in zipf.namelist():
                    # Extract only the target file
                    zipf.extract(target_file, pwd=password.encode("utf-8"))
                    print(f"Password found: {password}")
                    print(f"Extracted {target_file}")
                    break  # Stop when a valid password is found
            # Save tried passwords to the file
            tried_passwords_file.write(password + "\n")
        except Exception as e:
            # Save failed passwords to the file
            tried_passwords_file.write(password + " (Failed)\n")

print("Extraction completed.")
