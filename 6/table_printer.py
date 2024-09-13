"""
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(strings:list):
    num_rows = len(strings)
    num_cols = len(strings[0])

    # make a rotated empty table
    rotated_table = [['' for _ in range(num_rows)] for _ in range(num_cols)]

    # populate it
    for x in range(num_cols):
        for y in range(num_rows):
            rotated_table[x][y] = strings[y][x]

    # turn every list inside the list into a string
    # stringified will be a list of strings
    stringified = []
    for lista in rotated_table:
        stringified.append(" ".join(lista))

    # helper function to find the max length of the strings in the list
    def find_longest_string(strings:list):
        max_length = 0

        for string in strings:
            current_length = len(string)
            if current_length > max_length:
                max_length = current_length

        return max_length

    # right-adjust every string with spaces making them all the same length as the longest string in the list of strings
    for i in range(len(stringified)):
        stringified[i] = stringified[i].rjust(find_longest_string(stringified)," ")

    # return the list of strings now that they're right-adjusted
    return stringified

# this is the code that will actually print stuff
# passes the tableData to the previous function and
# prints the content of each element
for a in printTable(tableData):
    print(a, end="\n")


