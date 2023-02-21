# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:54:08 2023

@author: Diogo_Rodrigues
"""

import sys
import re
import pandas
from pandas import *

def tsv_to_csv(given_tsv):
    '''python function to convert .tsv file to .csv file'''
  
    output_csv = given_tsv[:-3] + "csv"
    with open(given_tsv, 'r') as myfile: 
        with open(output_csv, 'w') as csv_file:
            for line in myfile:
                # Replace every tab with comma
                fileContent = re.sub("\t", ",", line)
                # Writing into csv file
                csv_file.write(fileContent)
    return output_csv

def get_plasmids(given_csv):
    '''python function that takes a specific column from a csv file, and writes it into a one line txt document'''

    plasmid_txt = given_csv[:-3] + "txt"
    data = read_csv(given_csv)
    # converting column data to list
    plasmid_list = data['Plasmid'].tolist()
    # writing list to txt line with all plasmids
    with open(plasmid_txt, 'w') as f:
        # go trough all items in the 'Plasmid' column
        for i in range(len(plasmid_list)):
            f.write(plasmid_list[i])
            # for the last item, do not add a separator 
            if i != len(plasmid_list)-1:
                f.write('; ')
    return plasmid_txt

################################################# MAIN ###########################################################

def main():
    array_of_files = list(sys.argv[1:])
    data = []
    for file in array_of_files:
        given_tsv = file
        output_csv = tsv_to_csv(given_tsv)
        print(file)
        print("Successfully made csv file")
        given_csv = output_csv
        output_txt = get_plasmids(given_csv)
        my_file = open(output_txt, "r")
        data.append(my_file.read())
        print("txt file successfully created")
        print()
    df = pandas.DataFrame(data, columns=['Plasmids'])
    df.to_csv('Plasmids.csv', encoding='utf-8')


main()

