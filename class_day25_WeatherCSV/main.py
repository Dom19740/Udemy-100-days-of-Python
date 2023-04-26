# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     skip_first_row = True
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# Read data from a csv
data = pandas.read_csv("weather_data.csv")

# print(data)
# print(data["temp"])
#
# # Create dictionary from data
# data_dict = data.to_dict()
# print(data_dict)
#
# # Create list from the temp column
# temp_list = data["temp"].to_list()
# print(temp_list)

# # Get Data in columns
# print(data.condition)
#
# print("Average temp", data.["temp"].mean())
#
# print("Max temp", data.temp.max())

# # Get Data in rows
# print(data[data.day == "Monday"])
#
# # Get row with the highest temperature
# print(data[data.temp == data.temp.max()])


# # Get monday row´s condition
monday = data[data.day == "Monday"]
print(monday.condition)

# # convert mondays tempt to def F
# monday = data[data.day == "Monday"]
# fahrenheit = (monday.temp * 9 / 5) + 32
# print(fahrenheit)

# # create data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


# Count squirrels in Primary Fur Color column
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("squirrel_count.csv")
