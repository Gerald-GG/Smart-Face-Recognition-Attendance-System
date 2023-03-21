import os
import pandas as pd
from datetime import datetime, timedelta

# Set the current week's start and end dates
start_date = datetime.now().date() - timedelta(days=datetime.now().weekday())
end_date = start_date + timedelta(days=6)

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
        
        # Filter the attendance data for the current week
        mask = (df["DateTime"].dt.date >= start_date) & (df["DateTime"].dt.date <= end_date)
        week_attendance = df.loc[mask]
        
        # Add the attendance data to the main attendance dataframe
        for label, row in week_attendance.iterrows():
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
                                                 / len(pd.date_range(start_date, end_date, freq="D"))
                                                 * 100)

# Save the attendance report as a CSV file in the "Weekly_Report" folder
report_folder = "Weekly_Report"
if not os.path.exists(report_folder):
    os.makedirs(report_folder)

report_file = os.path.join(report_folder,
                           f"Attendance Report Week {start_date} to {end_date}.csv")
employee_attendance.to_csv(report_file, index=False)
