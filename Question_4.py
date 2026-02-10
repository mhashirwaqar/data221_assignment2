import pandas as pd

# file path (same folder as this Python file)
file_path = "student.csv"

# load the dataset
students_df = pd.read_csv(file_path)

# filter students based on the given conditions
high_engagement_df = students_df[
    (students_df["studytime"] >= 3) &
    (students_df["internet"] == 1) &
    (students_df["absences"] <= 5)
]

# save the filtered data to a new CSV file (same folder)
output_path = "high_engagement.csv"
high_engagement_df.to_csv(output_path, index=False)

# calculate required statistics
num_students = len(high_engagement_df)
average_grade = high_engagement_df["grade"].mean()

# print results
print("Number of students saved:", num_students)
print("Average grade:", average_grade)
