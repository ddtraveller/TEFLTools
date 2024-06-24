import pandas as pd
import numpy as np

print("Welcome to the Mars Exploration Data Analysis Solution!")

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
offline_systems = ship_systems[ship_systems['Status'] == 'Offline']
print("Offline systems:")
print(offline_systems)

print("\nStep 2: Checking Spare Parts")
needed_parts = spare_parts.loc[spare_parts['Compatibility'].isin(offline_systems['System'])]
print("Needed spare parts:")
print(needed_parts)

print("\nStep 3: Updating System Efficiency")
def increase_efficiency(x):
    return x * 1.1 if x > 0 else x

ship_systems['New_Efficiency'] = ship_systems['Efficiency'].apply(increase_efficiency)
print("Updated ship systems with new efficiency:")
print(ship_systems)

print("\nStep 4: Analyzing Mission Logs")
activity_summary = mission_logs.groupby('Activity')['Duration'].agg(['mean', 'sum'])
print("Activity summary:")
print(activity_summary)

print("\nStep 5: System Maintenance Analysis")
ship_systems['Last_Maintenance'] = pd.to_datetime(ship_systems['Last_Maintenance'])
ship_systems['Days_Since_Maintenance'] = (pd.Timestamp.now() - ship_systems['Last_Maintenance']).dt.days

urgent_maintenance = ship_systems.sort_values('Days_Since_Maintenance', ascending=False).iloc[:2]
print("Systems needing urgent maintenance:")
print(urgent_maintenance[['System', 'Days_Since_Maintenance']])

print("\nStep 6: Final System Check")
system_summary = ship_systems.agg({
    'Efficiency': ['min', 'max', 'mean'],
    'New_Efficiency': ['min', 'max', 'mean'],
    'Days_Since_Maintenance': ['min', 'max', 'mean']
})
print("System summary:")
print(system_summary)

print("\nStep 7: Repair Plan")
repair_plan = pd.merge(offline_systems, needed_parts, left_on='System', right_on='Compatibility')
print("Repair plan:")
print(repair_plan[['System', 'Part', 'Quantity']])

print("\nStep 8: Mission Log Analysis")
mission_logs['Date'] = pd.to_datetime(mission_logs['Date'])
daily_activity = mission_logs.set_index('Date').resample('D')['Duration'].sum()
print("Daily activity duration:")
print(daily_activity)

print("\nStep 9: System Efficiency Correlation")
efficiency_correlation = ship_systems['Efficiency'].corr(ship_systems['Days_Since_Maintenance'])
print(f"Correlation between Efficiency and Days Since Maintenance: {efficiency_correlation:.2f}")

print("\nStep 10: Final Repair Checklist")
final_checklist = ship_systems.copy()
final_checklist['Needs_Repair'] = final_checklist['Status'] == 'Offline'
final_checklist['Needs_Maintenance'] = final_checklist['Days_Since_Maintenance'] > 100
final_checklist['Action_Required'] = np.where(final_checklist['Needs_Repair'], 'Repair', 
                                              np.where(final_checklist['Needs_Maintenance'], 'Maintenance', 'None'))
print("Final repair checklist:")
print(final_checklist[['System', 'Status', 'Efficiency', 'Days_Since_Maintenance', 'Action_Required']])

print("\nCongratulations! You've successfully analyzed all ship systems using advanced Pandas operations.")
print("With this comprehensive analysis, you can now repair your ship and safely return to Earth.")