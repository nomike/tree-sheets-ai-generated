#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import shutil

libreoffice_image_dir = "/home/nomike/coding/tree-sheets-ai-generated/design/latex/exported-photos/"
target_image_dir = "/home/nomike/coding/tree-sheets-ai-generated/photos/"

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data
    

libreoffice = read_csv("libreoffice_ids.csv")
treelist = read_csv("tree_list.csv")

def find_record(list, column, value):
    for record in list:
        if record[column] == value:
            return record
    return None


for row in libreoffice:
    image_id = row['ID']
    # print(f'Image ID: {image_id}, LibreOffice Botanical Name: "{row["Botanical name"]}" Tree List Botanical Name: "{find_record(treelist, "ID", image_id)["Botanical name"]}"')
    libreoffice_image_path = os.path.join(libreoffice_image_dir, f'{row["Botanical name"]}.jpg')
    target_image_path = os.path.join(target_image_dir, find_record(treelist, "ID", image_id)['Botanical name'])
    # Check if the file exists
    if not os.path.isfile(libreoffice_image_path):
        print(f"({image_id}) File {libreoffice_image_path} does not exist.")
        continue
    # Check if the target directory exists
    if not os.path.isdir(os.path.dirname(target_image_path)):
        print(f"({image_id}) Directory {os.path.dirname(target_image_path)} does not exist.")
        continue
    
    shutil.copy(libreoffice_image_path, target_image_path)

    