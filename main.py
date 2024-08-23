import os
import pandas as pd


def convert_to_xlsx(file_path):
    # Read the file with pandas
    df = pd.read_excel(file_path)
    # Create the new file path with .xlsx extension
    new_file_path = os.path.splitext(file_path)[0] + '.xlsx'
    # Save the dataframe to the new file path
    df.to_excel(new_file_path, index=False)


def traverse_and_convert(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.xls', '.xlsm', '.xlsb', '.odf', '.ods', '.odt')):
                file_path = os.path.join(root, file)
                convert_to_xlsx(file_path)


# Example usage
folder_path = 'path_to_your_folder'
traverse_and_convert(folder_path)
