# import packages
import os

import pandas as pd


# set directory
my_path = 'D://Robson/home_office'

# list files and directories
list_files = os.scandir(my_path)

# initialize empty lists to directories and files
dir_size = []
dir_name = []
file_size = []
file_names = []

# loop over files
for i in list_files:

        # check out if there is a file and append to a file list
        if os.path.isfile(i):
                file_size.append(os.path.getsize(i))
                file_names.append(i)
        else:
                dir_size.append(os.path.getsize(i))
                dir_name.append(i)

# put the results into dataframes
files_df = pd.DataFrame({'name': file_names,
                        'size': file_size})

files_df.sort_values('size', ascending=False)

dir_df = pd.DataFrame({'name': dir_name,
                      'size': dir_size})

dir_df.sort_values('size', ascending=False)

# save dataframes as csv files
files_df.to_csv('files_df.csv', index=False)
dir_df.to_csv('dir_df.csv', index=False)

# open csv files
files = pd.read_csv('files_df.csv')
dir = pd.read_csv('dir_df.csv')

# data cleaning
#files['name'] = files['name'].astype(str)

files['name'] = files['name'].replace(to_replace="<DirEntry \'|\'>", value="", regex=True)
dir['name'] = dir['name'].replace(to_replace="<DirEntry \'|\'>", value="", regex=True)

# print out
print(files.head(), end='\n\n')
print(dir.head())

# save the neaty dataframes as csv files
files.to_csv('files_df_clean.csv', index=False)
dir.to_csv('dir_df_clean.csv', index=False)

