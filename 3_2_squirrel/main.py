import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_counts = data[data["Primary Fur Color"] == 'Gray']
red_squirrels_counts = data[data["Primary Fur Color"] == 'Cinnamon']
black_squirrels_counts = data[data["Primary Fur Color"] == 'Black']

data_dict = {
    "Fur Color": ["grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_counts, red_squirrels_counts, black_squirrels_counts]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count")