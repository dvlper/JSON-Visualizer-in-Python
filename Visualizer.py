# ENJOY !!
#
# But, do make sure you have following Python modules installed
# - pandas 
# - tabulate
# for installing any module execute: pip install <module-name>

import pandas as pd
from tabulate import tabulate

def extractData(record):
	records = []
	for ind, hpg in enumerate(record['HPG']):
		if ind == 0:
			records.append((record['Name'], record['IP'], record['Memory'], hpg['Num'], hpg['Size']))
			continue
		records.append(('', '', '', hpg['Num'], hpg['Size']))
	return records
		
def main(filename):
	data = pd.read_json(filename)
	records = []
	for r in data.iterrows():
		records += extractData(r[1].to_dict())

	print tabulate(records, headers=('Name', 'IP', 'Memory', 'Num', 'Size'), tablefmt='psql')

if __name__ == "__main__":
	try:
		main("data.json")
	except Exception as e:
		print "You might not be doing as dvlper told.\nException: ", e