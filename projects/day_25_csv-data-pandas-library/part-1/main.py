# with open("./weather_data.csv", "r") as data_files:
#     data = data_files.readlines()
#     print(data)
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    next(data)  # Skip the header row
    temperatures = []
    for row in data:
        temperatures.append(int(row[1]))
    print(temperatures)