# with open("./weather_data.csv", "r") as data_files:
#     data = data_files.readlines()
#     print(data)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)  # Skip the header row
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas


# data = pandas.read_csv("./weather_data.csv")
# # print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)

# init_temp = 0
# for temp in temp_list:
#     init_temp += temp
#
# average_temp = init_temp / len(temp_list)
# print(average_temp)
#
# print(sum(temp_list)/len(temp_list))

# avg_pandas = data["temp"].mean()
# print(avg_pandas)
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "monday"]
# print(monday.condition)

#create a dataframe from scratch

# csv_filename = input("please enter your ticket number")
#
# data_dict ={
#     "students": ["amy", "james", "Angela"],
#     "scores": [76, 98, 88]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv(f"{csv_filename}.csv")

squirrel_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

gray_squirrel_count = gray_squirrels.shape[0]
cinnamon_squirrels_count = cinnamon_squirrels.shape[0]
black_squirrels_count = black_squirrels.shape[0]

squirrels_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrels_count, black_squirrels_count]
}

df_squirrel_dict = pandas.DataFrame(squirrels_dict)
df_squirrel_dict.to_csv("squirrel_count.csv")
print(df_squirrel_dict)
