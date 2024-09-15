#! python3
# mclip.py - A multi-clipboard program.
"""
USAGE:
must have a mclip.bat file in a place your PATH points to. with the contents:
->> @py.exe "C:\path\to\this\very\file\in\this\case\called\mclip.py" %*
->> @pause
double-clicking the .bat file runs it with no arguments.
but the purpose is to run it with arguments through the Run window (Win+R) as such:
->> mclip busy
or
->> mclip agree
or
->> mclip upsell
note the "mclip" we call in the Run window refers to the batch file
"""

import sys
import pyperclip

TEXT = {
    "agree": """Yes, I agree. That sounds fine to me.""",
    "busy": """Sorry, can we do this later this week or next week?""",
    "upsell": """Would you consider making this a monthly donation?""",
}

# sys,argv are the arguments we put in the run window
if len(sys.argv) < 2:
    print("Usage: mclip [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for " + keyphrase + " copied to clipboard.")
else:
    print("There is no text for " + keyphrase)

