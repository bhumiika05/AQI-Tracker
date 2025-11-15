import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# SAMPLE AQI + POLLUTANT DATA FOR DELHI (7 DAYS)
# --------------------------------

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "AQI": [280, 315, 300, 340, 360, 375, 355],
    "PM2.5": [185, 205, 195, 225, 240, 250, 235],
    "PM10": [255, 275, 265, 300, 315, 330, 320],
    "NO2": [45, 50, 48, 52, 55, 58, 54],
    "SO2": [12, 14, 13, 15, 16, 17, 16],
    "CO": [1.2, 1.4, 1.3, 1.5, 1.6, 1.7, 1.6],
    "O3": [30, 35, 33, 37, 39, 40, 38]
       }

df = pd.DataFrame(data)
print("=== Delhi AQI & Pollutant Data (Weekly) ===")
print(df)
print()


# --------------------------------
# LINE GRAPH: AQI TREND (WEEKLY)
# --------------------------------

plt.figure(figsize=(8, 5))
plt.plot(df["Day"], df["AQI"], marker="o")
plt.title("AQI Trend in Delhi (Weekly)")
plt.xlabel("Day")
plt.ylabel("AQI Level")
plt.grid(True)
plt.show()

9
# --------------------------------
# PIE CHART: AVERAGE CONTRIBUTION OF ALL POLLUTANTS
# --------------------------------

pollutants = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]
average_values = [
    df["PM2.5"].mean(),
    df["PM10"].mean(),
    df["NO2"].mean(),
    df["SO2"].mean(),
    df["CO"].mean(),
    df["O3"].mean()  
    ]

plt.figure(figsize=(8, 6))
plt.pie(average_values, labels=pollutants, autopct="%1.1f%%", startangle=90)
plt.title("Average Pollutant Contribution in Delhi (Weekly)")
plt.show()

