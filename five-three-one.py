import os 
from dotenv import load_dotenv, find_dotenv 
load_dotenv(find_dotenv()) 

import math
import json 
import requests


#KEYS
API_NINJAS_KEY = os.getenv('API_NINJAS_KEY')    
print(API_NINJAS_KEY)
#CONSTANTS
DAYS = ["Leg", "Push", "Pull"] * 2 
MAIN_WORKOUT = ["Squat", "Bench", "Light Deadlift", "Squat", "OHP", "Light Deadlift"]
PERCENT = [75,85,95]
LIGHT_PERCENT = 65
NINJAS_GET_URL = "https://api.api-ninjas.com/v1/exercises?" 

def get_call(api_url):
	response = requests.get(api_url, headers={'X-Api-Key': API_NINJAS_KEY})
	return response

def get_execises_by_muscle(muscle):
	by_muscle_url = f"{NINJAS_GET_URL}muscle={muscle}"
	return get_call(by_muscle_url)

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
	#calcualte_weight()
	print(get_execises_by_muscle("glutes").json())
	return 0 



if __name__ == "__main__":
	main()
