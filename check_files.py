import os
from pathlib import Path

def check_sequence(folder_path):
    missing_files = []
    users_with_issues = set()
    
    # Get all user folders
    data_path = Path(folder_path)
    letter_folders = [f for f in data_path.iterdir() if f.is_dir()]
    
    print("\nChecking for missing files...")
    
    for letter_folder in letter_folders:
        letter = letter_folder.name
        print(f"\nChecking letter {letter}:")
        
        # Get all files in the letter folder
        files = [f.name for f in letter_folder.iterdir() if f.is_file() and f.suffix.lower() == '.jpg']
        
        # Get unique users from the files
        users = set()
        for file in files:
            # Split filename like "Andrew_P_99.jpg" into parts
            parts = file.split('_')
            if len(parts) >= 2:
                user = '_'.join(parts[:-2])  # Handle usernames with underscores
                users.add(user)
        
        # Check each user's sequence
        for user in users:
            missing = []
            for i in range(100):  # Check files 0-99
                expected_file = f"{user}_{letter}_{i}.jpg"
                if expected_file not in files:
                    missing.append(i)
            
            if missing:
                users_with_issues.add(user)
                missing_files.append({
                    'user': user,
                    'letter': letter,
                    'missing': missing
                })
                print(f"  User {user} is missing files: {missing}")
    
    # Print summary
    print("\nSummary:")
    print(f"Total users with missing files: {len(users_with_issues)}")
    if users_with_issues:
        print("Users with issues:", ', '.join(users_with_issues))
    
    return missing_files

if __name__ == "__main__":
    data_folder = "./data"  # Change this to your data folder path
    missing_files = check_sequence(data_folder)
    
    if not missing_files:
        print("\nAll sequences are complete!") 