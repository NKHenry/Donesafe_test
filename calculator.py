#Calculator for Donesafe coding test
#written by Nathaniel Henry

#to run this program provide the filename of people.json and rules.json as
#first and second arguments on the command line
#a csv payment report in the format 'name,weeks injured,payment' will both
#be printed to the screen and output to payment.csv

import json
import sys
from datetime import *
import re

#calculates the number of weeks since injury
#takes a string representing date in yyyy/mm/dd format and a datetime object
#that representing the current day
#returns integer number of weeks
def getWeeks(injury, now):
	#now = datetime.now()
	fields = injury.split("/")
	injuryDate = datetime(int(fields[0]), int(fields[1]), int(fields[2]))
	days = (now - injuryDate).days
	
	#so we don't divide by 0 or pay for negative time
	if days <= 0:
		weeks = 0	
	else:
		weeks = days / 7
	
	return weeks


#calculates this weeks pay based on rules
#arguments: float, float, int, list
#returns float
def getPay(normal, overtime, weeks, rules):
	if weeks == 0:
		return 0

	pay = -1
	
	for r in rules:
		range = r['applicableWeeks'].split("-")
		
		#we've reached final bracket and can calculate
		if len(range) == 1:
			range[0] = re.sub("[^0-9]", "", range[0])
			break
		
		elif weeks >= int(range[0]) and weeks <= int(range[1]):
			break
	
	if r['overtimeIncluded']:
		pay = (normal + overtime) * (float(r['percentagePayable']) / 100)
	else:
		pay = normal * (float(r['percentagePayable']) / 100)

	return pay	


################################## START OF MAIN PROGRAM ######################

def main():
	file_people = sys.argv[1]
	file_rules = sys.argv[2]
	outfile = "payments.csv"

	file = open(file_people, "r")
	data = file.read()
	people = json.loads(data)['people']
	file.close()

	file = open(file_rules, "r")
	data = file.read()
	rules = json.loads(data)['rules']
	file.close()

	data = ""

	for p in people:
		
		normalPay = p['hourlyRate'] * p['normalHours']
		overtimePay = p['overtimeRate'] * p['overtimeHours']
		
		weeks = getWeeks(p['injuryDate'], datetime.now())

		pay = getPay(normalPay, overtimePay, weeks, rules)

		data += p['name'] + "," + str(weeks) + "," + "{0:.2f}".format(pay) + "\n"

	data = data.strip("\n")

	#payment report
	print data

	file = open(outfile, 'w')
	file.write(data)
	file.close()

if __name__ == '__main__':
	main()