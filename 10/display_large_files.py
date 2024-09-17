import os
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext 

size_threshold = 10 * 1024 * 1024  # 10 MB in bytes

# open dialog to pick which file to search
# returns the absolute path of the select folder
def select_folder():
    root = tk.Tk()   
    root.withdraw()  # hide the root window
    folder_selected = filedialog.askdirectory(title="Select Folder")
    return folder_selected

# will check every file in every folder and subfolder provided
# returns list of absolute path of every file over the size limit
def find_large_files(main_folder, size_limit):
    result = []
    # this loop iterates over each directory and its contents. folders represents the current directory being processed
    for folders, subfolders, files in os.walk(main_folder):
        for file in files:
            file_path = os.path.join(folders, file)
            file_size = os.path.getsize(file_path)
            if file_size > size_limit:
                result.append(f"Large file found: {file_path} -> {file_size/1024/1024} ")
    return result

# opens a new window to display results
def show_results(results: list):
    # create a new window 
    result_window = tk.Tk()
    result_window.title("Large Files Finder")
    
    # open a scrollable text area, where strings of results will be displayed
    text_area = scrolledtext.ScrolledText(result_window)
    
    # make sure the text area expands when the window is resized
    # and fills the entire window both horizontally and vertically
    text_area.pack(fill=tk.BOTH, expand=True)
    
    # insert the results into the text area
    text_area.insert(tk.END, "\n".join(results))
    
    # disable editing of the text area to prevent user modification
    text_area.config(state=tk.DISABLED)
    
    # keep window alive
    result_window.mainloop()



# invoke the select folder function
folder_to_check = select_folder()
# if a folder is chosen
if folder_to_check:
    # get all the large files
    all_large_files = find_large_files(folder_to_check, size_threshold)
    # invoke the function to display the results
    show_results(all_large_files)