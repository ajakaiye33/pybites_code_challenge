import sys
import csv
from argparse import ArgumentParser

# #this fix_csv.py is suppose to accept the name of an existing pip-delimited File
# and the name of a new comma-delimited file.

# old_filename = sys.argv[1]
# new_filename = sys.argv[2]
#
# old_filename = open(old_filename)
# rows = [
#       line.split('|')
#       for line in old_file.read().splitlines()
# ]
# old_file = open(new_filename, mode='wt', newline = '\r\n')
# print("\n".join(
#      ",".join(row)
#      for row in rows
# ), file=new_file)
# old_file.close()
# new_filename.close()
# ------------------------------------------------------------------------------

# old_filename = sys.argv[1]
# new_filename = sys.argv[2]
#
# with open(old_filename, newline='') as old_file:
#     reader = csv.reader(old_file, delimiter='|')
#     rows = [line for line in reader]
# with open(new_filename, mode='wt', newline='') as new_file:
#     writer = csv.writer(new_file)
#     writer.writerows(rows)
#


# ------------------------------------------------------------------------------


parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    rows = list(csv.reader(old_file, delimiter='|'))
with open(args.new_filename, mode='wt', newline='') as new_file:
    csv.writer(new_file).writerows(rows)
