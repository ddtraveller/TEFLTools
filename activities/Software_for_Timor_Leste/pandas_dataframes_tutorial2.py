import pandas as pd
import numpy as np

print("Welcome to Mars, Explorer! Your spaceship has malfunctioned, and you need to use your Pandas skills to analyze data and fix it. Let's get started!")

# Create sample data
ship_systems = pd.DataFrame({
    'System': ['Life Support', 'Propulsion', 'Navigation', 'Communication', 'Power'],
    'Status': ['Online', 'Offline', 'Online', 'Offline', 'Online'],
    'Efficiency': [95, 0, 87, 0, 78],
    'Last_Maintenance': ['2023-01-15', '2022-11-30', '2023-02-28', '2022-12-10', '2023-03-05']
})

spare_parts = pd.DataFrame({
    'Part': ['Oxygen Filter', 'Fuel Injector', 'Star Tracker', 'Antenna', 'Solar Panel'],
    'Quantity': [5, 2, 1, 3, 4],
    'Compatibility': ['Life Support', 'Propulsion', 'Navigation', 'Communication', 'Power']
})

mission_logs = pd.DataFrame({
    'Date': ['2023-03-01', '2023-03-02', '2023-03-03', '2023-03-04', '2023-03-05'],
    'Activity': ['Soil Sample', 'Rover Repair', 'Data Transmission', 'Solar Storm', 'Oxygen Leak'],
    'Duration': [120, 240, 60, 180, 90]
})

print("\nStep 1: Analyzing Ship Systems")
print("Use boolean indexing to find offline systems:")
print("offline_systems = ship_systems[ship_systems['Status'] == 'Offline']")
offline_systems = ship_systems[ship_systems['Status'] == 'Offline']
print(offline_systems)

input("\nPress Enter to continue...")

print("\nStep 2: Checking Spare Parts")
print("Use loc[] to select parts compatible with offline systems:")
print("needed_parts = spare_parts.loc[spare_parts['Compatibility'].isin(offline_systems['System'])]")
needed_parts = spare_parts.loc[spare_parts['Compatibility'].isin(offline_systems['System'])]
print(needed_parts)

input("\nPress Enter to continue...")

print("\nStep 3: Updating System Efficiency")
print("Apply a function to increase efficiency of online systems by 10%:")
print("def increase_efficiency(x):")
print("    return x * 1.1 if x > 0 else x")
print("ship_systems['New_Efficiency'] = ship_systems['Efficiency'].apply(increase_efficiency)")

def increase_efficiency(x):
    return x * 1.1 if x > 0 else x

ship_systems['New_Efficiency'] = ship_systems['Efficiency'].apply(increase_efficiency)
print(ship_systems)

input("\nPress Enter to continue...")

print("\nStep 4: Analyzing Mission Logs")
print("Group mission logs by activity and calculate mean duration:")
print("activity_summary = mission_logs.groupby('Activity')['Duration'].mean()")
activity_summary = mission_logs.groupby('Activity')['Duration'].mean()
print(activity_summary)

input("\nPress Enter to continue...")

print("\nStep 5: System Maintenance Analysis")
print("Convert 'Last_Maintenance' to datetime and calculate days since last maintenance:")
ship_systems['Last_Maintenance'] = pd.to_datetime(ship_systems['Last_Maintenance'])
ship_systems['Days_Since_Maintenance'] = (pd.Timestamp.now() - ship_systems['Last_Maintenance']).dt.days

print("Use iloc[] to select systems needing immediate maintenance (top 2 by days since maintenance):")
print("urgent_maintenance = ship_systems.sort_values('Days_Since_Maintenance', ascending=False).iloc[:2]")
urgent_maintenance = ship_systems.sort_values('Days_Since_Maintenance', ascending=False).iloc[:2]
print(urgent_maintenance[['System', 'Days_Since_Maintenance']])

input("\nPress Enter to continue...")

print("\nStep 6: Final System Check")
print("Use aggregation functions to get an overview of ship systems:")
print("system_summary = ship_systems.agg({")
print("    'Efficiency': ['min', 'max', 'mean'],")
print("    'Days_Since_Maintenance': ['min', 'max', 'mean']")
print("})")

system_summary = ship_systems.agg({
    'Efficiency': ['min', 'max', 'mean'],
    'Days_Since_Maintenance': ['min', 'max', 'mean']
})
print(system_summary)

print("\nCongratulations! You've successfully analyzed your ship's data using Pandas.")
print("With these insights, you can now repair your ship and return to Earth.")
print("\nHere's a summary of the Pandas features you've learned:")
print("1. Boolean indexing for filtering data")
print("2. Using loc[] for label-based selection")
print("3. Using iloc[] for integer-based selection")
print("4. Applying functions to Series with apply()")
print("5. Grouping data with groupby()")
print("6. Using aggregation functions like mean()")
print("7. Date handling with to_datetime()")
print("8. Sorting data with sort_values()")
print("9. Advanced aggregation with agg()")

print("\nGood luck on your journey home, Space Explorer!")