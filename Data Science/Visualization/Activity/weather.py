import pandas as pd
import seaborn as sns

print("Hello")

weather = pd.read_csv(r'C:\Users\hp\Desktop\Codingal\Data Science\Visualization\Activity\Weather Dataset.csv')
print(weather.head())
print(weather.info())
sns.barplot(weather['wind_speed'])
sns.barplot(weather['temperature'])
sns.distplot(weather['temperature'])
sns.distplot(weather['humidity'], rug=True);
sns.jointplot(weather['humidity'])
sns.jointplot(weather['temperature'])
sns.jointplot(weather['humidity'], kind="hex")
sns.jointplot(weather['temperature'], kind="hex")
sns.jointplot(weather['temperature'], kind="kde")
sns.jointplot(weather['temperature'], kind="kde")
sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])
sns.stripplot(weather['weather_type'], weather['temperature'])
sns.stripplot(weather['weather_type'], weather['temperature'], jitter = True)
sns.swarmplot(weather['humidity'], weather['temperature'])
sns.boxplot(weather['humidity'], weather['temperature'], hue=weather['weather_type'])
sns.barplot(weather['humidity'], weather['temperature'], hue=weather['weather_type'])
sns.countplot(weather['weather_type'])
sns.pointplot(weather['humidity'], weather['temperature'], hue=weather['weather_type'])
sns.lmplot(x="humidity", y="temperature", data=weather)
sns.lmplot(x="humidity", y="temperature", hue="weather_type", data=weather)
