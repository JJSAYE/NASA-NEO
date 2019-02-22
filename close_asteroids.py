import json
import requests
import pprint
import pandas as pd
from collections import defaultdict
from time_function import daterange
from datetime import timedelta, date
import time

# api_key = 'pXKcehWP1T131kX3JCWPx3Npbd4IfQrpchOVodWW'
api_key = 'MkD1FdT063uYPQmw2NqBjEFTFvyzHpnWnyfN5P0h'

asteroid_dict = defaultdict(dict)

start_dt = date(2015, 12, 20)
end_dt = date(2019, 2, 9)

# https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=DEMO_KEY

resp = requests.get(
						'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + 
						str(date(2019, 12, 20)) + 
						'&end_date=' + 
						str(date(2019, 12, 27)) + 
						'&api_key=' + 
						api_key
						)

asteroids = resp.json() 
pprint.pprint(asteroids.keys(), indent=4)
pprint.pprint(asteroids['near_earth_objects'].keys(), indent=4)

# for dt in list(daterange(start_dt, end_dt))[0::7]:
# 	eow = dt + timedelta(days=6)
# 	bow = dt.strftime("%Y-%m-%d")

# 	resp = requests.get(
# 						'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + 
# 						str(bow) + 
# 						'&end_date=' + 
# 						str(eow) + 
# 						'&api_key=' + 
# 						api_key
# 						)

	# asteroids = resp.json()
	# dates = list(asteroids['near_earth_objects'].keys())

	# for date in dates:
	# 	print(date)
	# 	for ids in range(0,len(asteroids['near_earth_objects'][date])):
	# 		orbiting_body = asteroids['near_earth_objects'][date][ids]['close_approach_data'][0]['orbiting_body']
	# 		velocity = asteroids['near_earth_objects'][date][ids]['close_approach_data'][0]['relative_velocity']['miles_per_hour']
	# 		name = asteroids['near_earth_objects'][date][ids]['name']
	# 		magnitude = asteroids['near_earth_objects'][date][ids]['absolute_magnitude_h']
	# 		miles = asteroids['near_earth_objects'][date][ids]['close_approach_data'][0]['miss_distance']['miles']
	# 		approach_date = asteroids['near_earth_objects'][date][ids]['close_approach_data'][0]['close_approach_date']
	# 		hazardous = asteroids['near_earth_objects'][date][ids]['is_potentially_hazardous_asteroid']
	# 		asteroid_id = asteroids['near_earth_objects'][date][ids]['id']
	# 		estimated_diameter_min = asteroids['near_earth_objects'][date][ids]['estimated_diameter']['miles']['estimated_diameter_min']
	# 		estimated_diameter_max = asteroids['near_earth_objects'][date][ids]['estimated_diameter']['miles']['estimated_diameter_max']
	# 		asteroid_dict[name]['id'] = asteroid_id 
	# 		asteroid_dict[name]['magnitude'] = magnitude
	# 		asteroid_dict[name]['approach_date'] = approach_date
	# 		asteroid_dict[name]['miles'] = miles
	# 		asteroid_dict[name]['velocity'] = velocity
	# 		asteroid_dict[name]['orbiting_body'] = orbiting_body
	# 		asteroid_dict[name]['hazardous'] = hazardous
	# 		asteroid_dict[name]['estimated_diameter_min'] = estimated_diameter_min
	# 		asteroid_dict[name]['estimated_diameter_max'] = estimated_diameter_max

		# df = pd.DataFrame(asteroid_dict).T
		# df.to_csv('asteroids.csv')

# with open('asteroids.json', 'r') as fp:
# 	asteroids = json.load(fp)

# pprint.pprint(asteroid_dict, indent=4)

# df = pd.DataFrame(asteroid_dict).T
# df.to_csv('asteroids.csv')