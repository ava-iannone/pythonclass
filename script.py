# Project 1

#create variables
rainList = []
windList = []
end_loop = True

#create functions
def avg_rain (rainList):
    sum = 0
    for x in rainList:
        sum = x + sum
    avg = sum / len(rainList)
    return avg

def avg_wind (windList):
    sum = 0
    for x in windList:
        sum = x + sum
    avg = sum / len(windList)
    return avg

def weatherSeverity(rain_avg, wind_avg):
    severity = (rain_avg * 10) + wind_avg
    return severity

while end_loop:
    # input from user
    input_string = input("Enter rain and wind separated by a space: \n")

    # Parse the string for the two numbers
    rain_num, wind_num = input_string.split()

    #check if value of rain is -1.0
    if float(rain_num) == -1.0:
        end_loop = False
    else:
        # convert strings to floats
        rainList.append(float(rain_num))
        windList.append(float(wind_num))

# output to console
average_rain = (avg_rain(rainList))
average_wind = (avg_wind(windList))
days = len(rainList)
severity = weatherSeverity(average_rain, average_wind)

print("The average rain is ", average_rain, " inches")
print("The average wind is ", average_wind, " mph")
print("The weather severity for these ", days, " readings is ", severity)
