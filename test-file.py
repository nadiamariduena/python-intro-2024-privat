import pandas as pd

# Sample data: employee names and their clock-in times
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'ClockInTime': ['08:30', '09:00', '08:45', '09:15']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the official start time
start_time = '09:00'

# Convert ClockInTime to datetime to make comparisons
df['ClockInTime'] = pd.to_datetime(df['ClockInTime'], format='%H:%M').dt.time

# Convert start_time to datetime.time for comparison
from datetime import datetime
start_time = datetime.strptime(start_time, '%H:%M').time()

# Check if employees are on time
df['OnTime'] = df['ClockInTime'].apply(lambda x: x <= start_time)

# Display the DataFrame
print(df)
