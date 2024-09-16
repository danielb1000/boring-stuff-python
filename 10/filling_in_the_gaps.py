"""
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder
and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
Have the program rename all the later files to close this gap.

the program explicitely looks for a range of files that start with the prefix and have numbers in front followed by the extension
it asks for a sample file to gather the extension type. and looks for parent folder of such file for the sequence
"""

import os
import re
import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from tkinter import simpledialog

# we want to pick an example file and retrieve its directory aswell as its extension
def choose_file_to_search():
    root = tk.Tk() # 
    root.withdraw # hide window
    sample_file = filedialog.askopenfilename(title="Select sample file") # abs path of selected file
    sample_file = Path(sample_file) # 
    prefix = simpledialog.askstring("Input", "Enter the prefix:") # the prefix of spam000001.txt
    return (sample_file, prefix)


# print(choose_file_to_search())


def find_missing(abs_file: Path, prefix: str):
    parent_folder = Path(abs_file).parent # abs_file is already a path object but converting it to a path object here
    file_ext = Path(abs_file).suffix # makes it more easy to understand how it can call .parent and .suffix 

    
    # group(1) will be the number part --->    (\d+)    <---
    pattern = re.compile(rf'{re.escape(prefix)}(\d+){re.escape(file_ext)}')
    
    numbers = []
    # for each file check if it matches the regex pattern and if it does
    # we add the number part to the list of seen numbers
    for file in os.listdir(parent_folder):
        match = pattern.search(file)
        if match:
            try:
                # convert the numeric part
                number = int(match.group(1))
                numbers.append(number)
            except ValueError:
                # ignore error 
                pass

    if numbers:
        # list of every number that should be in the sequence
        expected_nums = [_ for _ in range(min(numbers), max(numbers) + 1)]
        
        # to find missing numbers
        # subtract the ones that exist from the expected
        # turning the list into a set() makes subracting them possible
        missing_numbers = list(set(expected_nums) - set(numbers))
        
        if missing_numbers:
            # print(f"Missing files: {', '.join(f'{prefix}{num:03d}.txt' for num in sorted(missing_numbers))}")
            print (f"Missing numbers: {", ".join(str(num) for num in missing_numbers)}")
        else:
            print("No files are missing in the sequence.")
    else:
        print("No files with the given prefix found.")

    return "Done"

# run the choose the files to search function then pass the arguments to the find_missing function
find_missing(*choose_file_to_search())


#
#
#
# todo: As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.
#
#
#