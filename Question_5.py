import pandas as pd

# file path (same folder as this Python file)
file_path = "student.csv"

# load the dataset
students_df = pd.read_csv(file_path)

# create grade_band column
def assign_band(grade):
    if grade <= 9:
        return "Low"
    elif grade <= 14:
        return "Medium"
    else:
        return "High"

students_df["grade_band"] = students_df["grade"].apply(assign_band)

# create grouped summary table
summary_df = students_df.groupby("grade_band").agg(
    num_students=("grade", "count"),
    avg_absences=("absences", "mean"),
    internet_percentage=("internet", "mean")
)

# convert internet proportion to percentage
summary_df["internet_percentage"] = summary_df["internet_percentage"] * 100

# save the summary table (same folder)
output_path = "student_bands.csv"
summary_df.to_csv(output_path)

# print summary table
print(summary_df)
