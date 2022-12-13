import os 
from dotenv import load_dotenv, find_dotenv 
load_dotenv(find_dotenv()) 

import math
import json 
import requests




#KEYS
API_NINJAS_KEY = os.getenv('API_NINJAS_KEY')    

#CONSTANTS
DAYS = ["Leg", "Push", "Pull"] * 2 
MAIN_WORKOUT = ["Squat", "Bench", "Light Deadlift", "Squat", "OHP", "Deadlift"]
PERCENT = [75,85,95]
LIGHT_PERCENT = 65
NINJAS_GET_URL = "https://api.api-ninjas.com/v1/exercises?" 
STABLES = {
	"Leg" : ["Glute Bridge", "Lunge", "Leg Press"],
	"Push": ["Bench","Incline Bench", "Dumbbell Shoulder Press", "Lateral Raise"],
	"Pull": ["Single Hand Row", "Pull Up"]
}
pr = open('pr.json')
pr = json.load(pr)

def get_call(api_url):
	response = requests.get(api_url, headers={'X-Api-Key': API_NINJAS_KEY})
	return response

def get_execises_by_muscle(muscle):
	by_muscle_url = f"{NINJAS_GET_URL}muscle={muscle}"
	return get_call(by_muscle_url)


def stable_workout(day,main):
	if main == "Bench": 
		return STABLES[day][1:]
	return STABLES[day]

def calcualte_weight(main,p):
	max_w = 0
	if main in pr:
		max_w = p*pr[main]/100.00
	else:
		max_w = LIGHT_PERCENT*pr[main.split(" ")[1]]/100.00
	return math.ceil(max_w)

def create_workout():
	m = {}
	for i,p in enumerate(PERCENT):
		week = f"WEEK {i+1}"
		m[week] = {}
		j = 0
		for day,main in zip(DAYS,MAIN_WORKOUT):
			print(day,main)
			j += 1 
			weight = calcualte_weight(main,p)
			d = f"{day} {str(j//4+1)}"
			m[week][d] = [f"{main}: {weight}"]
			m[week][d] += stable_workout(day,main)
	return m 	
	
	

def main():
	workout = create_workout()
	print(workout)
	return 0 



if __name__ == "__main__":
	main()
	
