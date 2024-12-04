import os

# File paths
main_data_file = "main_data.txt"  # Main data file
file2_file = "file2.txt"          # File to compare with main_data.txt

# Output folder and files
output_folder = "output"
similar_main_data_file = os.path.join(output_folder, "similar_main_data.txt")
not_main_match_file = os.path.join(output_folder, "not_main_match.txt")
similar_file2_data_file = os.path.join(output_folder, "similar_file2_data.txt")
not_file2_match_file = os.path.join(output_folder, "not_file2_match.txt")

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read files
with open(main_data_file, 'r') as f1, open(file2_file, 'r') as f2:
    main_data_lines = set(f1.readlines())
    file2_lines = set(f2.readlines())

# Calculate similar and non-matching lines
similar_data = main_data_lines.intersection(file2_lines)
not_main_match = main_data_lines - file2_lines
not_file2_match = file2_lines - main_data_lines

# Write outputs
with open(similar_main_data_file, 'w') as f_similar_main, \
     open(not_main_match_file, 'w') as f_not_main, \
     open(similar_file2_data_file, 'w') as f_similar_file2, \
     open(not_file2_match_file, 'w') as f_not_file2:
    
    # Writing similar data
    f_similar_main.writelines(similar_data)
    f_similar_file2.writelines(similar_data)
    
    # Writing non-matching data
    f_not_main.writelines(not_main_match)
    f_not_file2.writelines(not_file2_match)

print(f"Comparison complete!")
print(f"Outputs saved in the '{output_folder}' folder.")