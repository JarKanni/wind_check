from noaa_sdk import NOAA
import pandas as pd
from statistics import mode

#greets user
print("\n"*2 + "...breath deep..." + "\n"*2 + "...relax..." + "\n"*2 + "...let's check the weather..." + "\n"*3)

#ask user for zip
zip = str(input("Which zip would you like to check? "))

#request forecasts and store it into variable 'forecast'
forecast = NOAA().get_forecasts(zip, 'US')

#store 'windSpeed' values into a list, ex: '5mph'
windspeed = [d['windSpeed'] for d in forecast]
direction = [d['windDirection'] for d in forecast]
start_time = [d['startTime'] for d in forecast]
end_time = [d['endTime'] for d in forecast]

#combine into one dictionary
data = { 'Wind Speed': windspeed, 'Direction': direction, 'Start Time': start_time, 'End Time': end_time }
#create DataFrame
df = pd.DataFrame(data)


#checks start and end time of df
print(f"Start time is: {min(start_time)}")
print(f"End time is: {max(end_time)}\n")


#checks for windspeeds over 5 mph within 'windspeed', prints warning and wind speed if detected
index = 0
counter = 0
for wind in windspeed:
    index += 1
    if wind != '0 mph' and wind != '5 mph':
        counter += 1
        if counter == 1:
            print(f"Look out!  {windspeed[index]} wind is coming at {start_time[index]}")

print(f"There are {counter} hours in the next 5 days that look to be windy!\n")


#finds max windspeed
max_windspeed = []
max_windspeed = windspeed.copy()

index = 0
for i in max_windspeed:
    if len(i) == 5:
        max_windspeed[index] = int(max_windspeed[index][:1])
        index += 1
    if len(i) == 6:
        max_windspeed[index] = int(max_windspeed[index][:2])
        index += 1
        
max = max(max_windspeed)


#prints other info about forecast
print(f"Highest Wind Speed: {max}")
print(f"Most common direction: {mode(direction)}")


#====DEBUGGING==== divider line ====DEBUGGING====
print("\n\n" + "*"*40 + "\n\n")


