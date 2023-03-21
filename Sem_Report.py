import os
import pandas as pd
from datetime import datetime, timedelta

# Set the start and end dates of the semester
semester_start_date = datetime(2023, 1, 9).date()
semester_end_date = semester_start_date + timedelta(weeks=15) - timedelta(days=1)

# Create an empty attendance dataframe with columns for Name, DateTime, Day, and Date
attendance_columns = ["Name", "DateTime", "Day", "Date"]
attendance = pd.DataFrame(columns=attendance_columns)

# Loop through the attendance files in the Attendance folder
attendance_folder = "Attendance"
for file_name in os.listdir(attendance_folder):
    if file_name.endswith(".csv"):
        # Read the attendance data from the file
        file_path = os.path.join(attendance_folder, file_name)
        df = pd.read_csv(file_path)
        
        # Convert the DateTime column to datetime format
        df["DateTime"] = pd.to_datetime(df["DateTime"])
        
        # Filter the attendance data for the semester
        mask = (df["DateTime"].dt.date >= semester_start_date) & (df["DateTime"].dt.date <= semester_end_date)
        semester_attendance = df.loc[mask]
        
        # Add the attendance data to the main attendance dataframe
        for label, row in semester_attendance.iterrows():
            name = row["Name"]
            date_time = row["DateTime"]
            day = date_time.strftime("%A")
            date = date_time.date()
            attendance.loc[label] = [name, date_time, day, date]

# Calculate the attendance percentage for each employee
employee_attendance = attendance.groupby("Name").agg(
    {"DateTime": "count"}).reset_index()
employee_attendance.rename(columns={"DateTime": "Attendance Count"},
                           inplace=True)
employee_attendance["Attendance Percentage"] = (employee_attendance["Attendance Count"]
                                                 / len(pd.date_range(semester_start_date, semester_end_date, freq="D"))
                                                 * 100)

# Save the attendance report as a CSV file in the "Semester_Reports" folder
report_folder = "Semester_Reports"
if not os.path.exists(report_folder):
    os.makedirs(report_folder)

report_file = os.path.join(report_folder,
                           f"Attendance Report Semester {semester_start_date} to {semester_end_date}.csv")
employee_attendance.to_csv(report_file, index=False)
