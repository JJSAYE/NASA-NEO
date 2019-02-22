from datetime import date, datetime, timedelta
import json
import psycopg2
import requests
from time_function import daterange
import time

conn = psycopg2.connect(
                        database="asteroids", 
                        user="jsaye", 
                        password="pythonic", 
                        host="localhost", 
                        port="5432"
                        )
cur = conn.cursor()

# cur.execute(""" DELETE FROM asteroids; """)
# COMMIT CHANGES
# conn.commit()
#CLOSE THE CONNECTION
# conn.close()

# api_key = 'MkD1FdT063uYPQmw2NqBjEFTFvyzHpnWnyfN5P0h'
api_key = 'pXKcehWP1T131kX3JCWPx3Npbd4IfQrpchOVodWW'

start_dt = date(2017, 10, 21)
end_dt = date(2019, 2, 7)

count = 0
for dt in list(daterange(start_dt, end_dt)):
    count +=1
    print('FIRST STOP ' + str(count))
    bow = dt.strftime("%Y-%m-%d")
    eow = dt + timedelta(days=6)

    resp = requests.get(
                        'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + 
                        str(bow) + 
                        '&end_date=' + 
                        str(eow) + 
                        '&api_key=' + 
                        api_key
                        )
    asteroids = resp.json()
    dates = list(asteroids['near_earth_objects'].keys())    

    for date in dates:
        print('SECOND STOP ' + str(date))
        for ids in range(0,len(asteroids['near_earth_objects'][date])):
            print('ID ', ids)
            count +=1
            orbiting_body = asteroids['near_earth_objects'][date][ids]['close_approach_data'][0]['orbiting_body']
            velocity = asteroids['near_earth_objects'][date][ids]['close_approach_data'][0]['relative_velocity']['miles_per_hour']
            name = asteroids['near_earth_objects'][date][ids]['name']
            magnitude = asteroids['near_earth_objects'][date][ids]['absolute_magnitude_h']
            miles = asteroids['near_earth_objects'][date][ids]['close_approach_data'][0]['miss_distance']['miles']
            approach_date = asteroids['near_earth_objects'][date][ids]['close_approach_data'][0]['close_approach_date']
            hazardous = asteroids['near_earth_objects'][date][ids]['is_potentially_hazardous_asteroid']
            asteroid_id = asteroids['near_earth_objects'][date][ids]['id']
            estimated_diameter_min = asteroids['near_earth_objects'][date][ids]['estimated_diameter']['miles']['estimated_diameter_min']
            estimated_diameter_max = asteroids['near_earth_objects'][date][ids]['estimated_diameter']['miles']['estimated_diameter_max']    

            print(count, ",", date, ",", name, ",", velocity, ",", bow, eow)

            cur.executemany("""
                             INSERT INTO asteroids (
                                                    approach_date, 
                                                    estimated_diameter_max,
                                                    estimated_diameter_min,
                                                    hazardous,
                                                    magnitude,
                                                    miles,
                                                    orbiting_body,
                                                    velocity
                                                      ) 
                              VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
                              """, 
                              [( 
                                 approach_date, 
                                 estimated_diameter_max, 
                                 estimated_diameter_min, 
                                 hazardous, 
                                 magnitude, 
                                 miles, 
                                 orbiting_body, 
                                 velocity
                                 )]);
# COMMIT CHANGES
            conn.commit()
            # time.sleep()
# # #CLOSE THE CONNECTION
conn.close()