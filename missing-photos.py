#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd


def list_missing_photos():
    """
    This function reads the file "tree_list.csv" and loops over the values of the column labled "Botanical name".
    For each entry, it checks whether a file exists with the name f'design/latex/photos/{botanical_name}/{botanical_name}.jpeg'.
    If not, it prints the botanical name to the console.
    """

    # Read the CSV file into a DataFrame
    df = pd.read_csv('tree_list.csv')

    # Loop over the values in the 'Botanical name' column
    for botanical_name in df['Botanical name']:
        # Construct the file path
        file_path = f'design/latex/photos/{botanical_name}/{botanical_name}.jpg'
        # Check if the file exists
        if not os.path.exists(file_path):
            # print(file_path)
            print(botanical_name)

if __name__ == "__main__":
    list_missing_photos()
