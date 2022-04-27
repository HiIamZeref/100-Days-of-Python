# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temp = int(row[1])
# #             temperature.append(temp)
# #
# #     print(temperature)
# #
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# temp_list = data["temp"].to_list()
#
# averageTemp = sum(temp_list) / len(temp_list)
# print(averageTemp)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# print(data[data.temp == data.temp.max()])
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

graySquirrels = len(data[data["Primary Fur Color"] == "Gray"])
redSquirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
blackSquirrels = len(data[data["Primary Fur Color"] == "Black"])

dataFrame = {
    "Fur color": ["Grey", "Cinnamon", "Black"],
    "Count": [graySquirrels, redSquirrels, blackSquirrels]

}

d = pandas.DataFrame(dataFrame)

d.to_csv("new_list")
