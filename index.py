import pandas as pd
dfAQI = pd.DataFrame({
"color": ["Green", "Yellow", "Orange", "Red", "Purple", "Maroon"],
"concern": ["Good", "Moderate", "Unhealthy for Sensitive Groups",
"Unhealthy", "Very Unhealthy", "Hazardous"],
"low": [0, 51, 101, 151, 201, 301],
"high": [50, 100, 150, 200, 300, 999]
}).set_index("color")
print(dfAQI)
print("First two rows:", dfAQI.head(2))
print("Last two rows:", dfAQI.tail(2))
print("Rows and columns:", dfAQI.shape)
print("Number of rows:", len(dfAQI))
dfAQI.info()
