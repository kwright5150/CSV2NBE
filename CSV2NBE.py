import xlrd
import time
import datetime
import sys

today = datetime.datetime.now()

# Open the workbook
book = xlrd.open_workbook("report.xlsx")

# get the list of sheets
sheets = book.sheets()

text_file = open("Output.nbe", "w")

for row in range(1, sheets[0].nrows):

    # Print two lines
    text_file.write('timestamps|||scan_start|')
    text_file.write(today.ctime())
    text_file.write('|')
    text_file.write('\n')
    text_file.write('timestamps||')
    text_file.write (sheets[0].cell_value(row, 4))
    text_file.write('|')
    text_file.write('host_start|')
    text_file.write(today.ctime())
    text_file.write('|')

# Print results
    text_file.write('\n')
    text_file.write('results|ip_address|')
    text_file.write (sheets[0].cell_value(row, 4))
    text_file.write('|')
    text_file.write (str(sheets[0].cell_value(row, 6)))
    text_file.write('/')
    text_file.write (sheets[0].cell_value(row, 5))
    text_file.write('|')
    text_file.write (str(sheets[0].cell_value(row, 0)))
    text_file.write('|Security Warning|')
    text_file.write(r'\nSummary:')
    text_file.write (sheets[0].cell_value(row, 8))
    text_file.write(r'\nVulnerability Detection Result:')
    text_file.write (sheets[0].cell_value(row, 12))
    text_file.write(r'\nSolution:')
    text_file.write (sheets[0].cell_value(row, 10))
    text_file.write(r'\nVulnerability Detection Method:')
    text_file.write(r'\nDetails:')
    text_file.write(r'\n')
    text_file.write (sheets[0].cell_value(row, 7))
    text_file.write('$')
    text_file.write(r'\nCVSS Base Score:')
    text_file.write (sheets[0].cell_value(row, 7))
    text_file.write('\n')
    text_file.write('timestamps||')
    text_file.write(sheets[0].cell_value(row, 4))
    text_file.write('|host_end|')
    text_file.write(today.ctime())
    text_file.write('|')
    text_file.write('\n')
text_file.write('timestamps|||')
text_file.write('scan_end|')
text_file.write(today.ctime())
text_file.write('|')

text_file.close()
