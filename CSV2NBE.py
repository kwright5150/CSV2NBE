## CSV to NBE ##
import time
import sys
import csv


# Print two lines
sys.stdout.write('timestamps|||scan_start|')
now = time.strftime("%c")
sys.stdout.write("%s" % now)
sys.stdout.write('|')
sys.stdout.write('\n')
sys.stdout.write('timestamps||')
sys.stdout.write('|')
sys.stdout.write('host_start|')
sys.stdout.write("%s" % now)
sys.stdout.write('|')

with open('C:/Users/kwright/Desktop/vulns.csv', 'r') as f:      
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)
