def printTable(table_list):
    # get a list of the widths of each column
    widths = [max([len(item) for item in col]) for col in table_list]

    # transform the list of columns into a list of rows
    rows = zip(*table_list)

    # iterate through the rows, creating the table string
    table_string = ''
    for row in rows:
        table_string += '{}\n'.format(row_to_string(row, widths))
    return table_string

def row_to_string(row, widths):
    row_string = ''
    for i, item in enumerate(row):
        row_string += item.rjust(widths[i] + 1)
    return row_string


test_table = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
print(printTable(test_table))