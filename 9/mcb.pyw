"""
USAGE: 
must have a mcb.bat file in a place your PATH points to. with the contents:
->>@py.exe "C:\path\to\this\very\file\in\this\case\called\mcb.pyw" %*
->>timeout /t 1 /nobreak >nul
->>exit

TO RUN do Win+R:
mcb save <keyword>:     Save clipboard content
mcb delete <keyword>:   Delete an entry
mcb list:               List all keywords
mcb <keyword>:          Retrieve content by keyword
mcb delete_all:         Delete all entries
"""
#! python 3
# mcb.pyw - saves and loads pieces of text to the clipboard

import shelve
import pyperclip
import sys
from pathlib import Path

# the directory of the script
here = Path(__file__).resolve().parent
# create a folder where all the shelved data will be if it doesn't exist
shelve_folder = here / "mcb_shelve_folder"
shelve_folder.mkdir(exist_ok=True)

# open a shelve in the previous folder
mcbShelf = shelve.open(str(shelve_folder / "mcb"))

if len(sys.argv) == 3:
    command = sys.argv[1].lower()
    key = sys.argv[2]

    if command == "save":
        mcbShelf[key] = pyperclip.paste()
        print(f"Saved\n{key}: {mcbShelf[key]}")

    elif command == "delete":
        if key in mcbShelf:
            del mcbShelf[key]
            print(f"Deleted: {key}")
        else:
            print(f"Error: {key} not found")

elif len(sys.argv) == 2:
    command = sys.argv[1].lower()

    if command == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
        print("Copied all keywords to your clipboard")

    elif command in mcbShelf.keys():
        pyperclip.copy(mcbShelf[command])
        print(f"Loaded\n {mcbShelf[command]} to clipboard")

    elif command == "delete_all":
        mcbShelf.clear()
        print("All entries deleted")

    else:
        print("Error: keyword does not exist. Clipboard unaltered")

else:
    print("Invalid number of arguments")

mcbShelf.close()

# list could also list the items in the cmd window but its not implemented
