import pandas as pd
import os

# Define the path to the folder containing the Excel files
folder_path = 'D:/KFolder/workspace/Bank_Data/downthemall'

# Create an empty DataFrame to hold the merged data
merged_df = pd.DataFrame()

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        file_path = os.path.join(folder_path, filename)
        # Read each Excel file into a DataFrame
        df = pd.read_excel(file_path)
        # Append the DataFrame to the merged DataFrame
        merged_df = pd.concat([merged_df, df], ignore_index=True)

# Define the path to save the merged file
merged_file_path = os.path.join(folder_path, 'D:/KFolder/workspace/Bank_Data/merged_file.xlsx')

# Save the merged DataFrame to a new Excel file
merged_df.to_excel(merged_file_path, index=False)

print(f'Merged file saved to {merged_file_path}')
