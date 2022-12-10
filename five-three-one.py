

import math
import json 

#CONSTANTS
DAYS = ["Leg", "Push", "Pull"] * 2 
MAIN_WORKOUT = ["Squat", "Bench", "Light Deadlift", "Squat", "OHP", "Light Deadlift"]
PERCENT = [75,85,95]
LIGHT_PERCENT = 65


def calcualte_weight():
	pr = open('pr.json')
	pr = json.load(pr)
	m = {}
	for i,p in enumerate(PERCENT):
		week = f"WEEK {i}"
		m[week] = {}
		for day,main in zip(DAYS,MAIN_WORKOUT):
			max_w = 0
			if main in pr:
				max_w = p*pr[main]/100.00
			else:
				max_w = LIGHT_PERCENT*pr[main.split(" ")[1]]/100.00
			m[week][main] = math.ceil(max_w)
	


def main():
	calcualte_weight()
	return 0 



if __name__ == "__main__":
	main()
