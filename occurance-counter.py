#!/usr/bin/python
#csv occurance counter
#Author: Jason Keyes
#Description: Input a csv file with one column, output csv with number of times each item occurs in the first csv
#Requires output file be created before running the Description
#Change names of in an outfile as to what you require

import csv
from collections import Counter

inFile = "file1.csv" #name of your file
outFile = "file2.csv" #name of your output file
reader = csv.reader(open(inFile))
writer = csv.writer(open(outFile, 'wb'))
item_list = []

for row in reader:
    rawItem = str(row)
    item = (rawItem.strip("['']"))
    item_list.append(item)

#count how many times names appear in the list
item_dict = Counter(item_list)
#output to new csv
writer.writerows(item_dict.items())
