import pandas as pd

# load the dataset (same folder as this Python file)
crime_df = pd.read_csv("crime.csv")

# create an empty list for risk categories
risk_list = []

# assign risk based on ViolentCrimesPerPop
for value in crime_df["ViolentCrimesPerPop"]:
    if value >= 0.50:
        risk_list.append("HighCrime")
    else:
        risk_list.append("LowCrime")

# add the new column to the DataFrame
crime_df["risk"] = risk_list

# group by risk and calculate average unemployment
avg_unemployment = crime_df.groupby("risk")["PctUnemployed"].mean()

# print results clearly
print("Average Unemployment Rate by Crime Risk:")
print("HighCrime:", avg_unemployment["HighCrime"])
print("LowCrime:", avg_unemployment["LowCrime"])
