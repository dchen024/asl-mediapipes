import os
from collections import defaultdict
from tabulate import tabulate  # pip install tabulate

DATA_DIR = './data'

def count_images():
    # Dictionary to store counts: {user: {letter: count}}
    counts = defaultdict(lambda: defaultdict(int))
    
    # Dictionary to store total counts per letter across all users
    total_per_letter = defaultdict(int)
    
    # Scan through the directory structure
    for user_dir in os.listdir(DATA_DIR):
        user_path = os.path.join(DATA_DIR, user_dir)
        if os.path.isdir(user_path):
            for letter_dir in os.listdir(user_path):
                letter_path = os.path.join(user_path, letter_dir)
                if os.path.isdir(letter_path):
                    # Count image files in the letter directory
                    image_count = len([f for f in os.listdir(letter_path) 
                                    if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
                    counts[user_dir][letter_dir] = image_count
                    total_per_letter[letter_dir] += image_count

    # Print results in a table format
    print("\n=== Images per Letter per User ===")
    
    # Prepare data for tabulate
    headers = ['User'] + sorted(total_per_letter.keys()) + ['Total']
    rows = []
    
    for user in sorted(counts.keys()):
        row = [user]
        user_total = 0
        for letter in sorted(total_per_letter.keys()):
            count = counts[user][letter]
            row.append(count)
            user_total += count
        row.append(user_total)
        rows.append(row)
    
    # Add totals row
    total_row = ['TOTAL']
    grand_total = 0
    for letter in sorted(total_per_letter.keys()):
        total = total_per_letter[letter]
        total_row.append(total)
        grand_total += total
    total_row.append(grand_total)
    rows.append(total_row)
    
    # Print the table
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid")) 