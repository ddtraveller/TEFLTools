import matplotlib.pyplot as plt

# Figure 4-1: Regional distribution of water resources
labels = ['Asia', 'South America', 'North America', 'Africa', 'Europe', 'Australia and Oceania']
sizes = [32, 28, 18, 9, 7, 6]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ff99cc','#99ccff']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90)
plt.axis('equal')
plt.title("Regional Distribution of Water Resources")
plt.show()

# Figure 4-2: Renewable water resources by country
countries = ['Indonesia', 'India', 'China', 'Bangladesh', 'Myanmar', 'Viet Nam', 'Malaysia', 'Philippines', 'Thailand', 'Japan', 'Nepal', 'Cambodia', 'Lao PDR', 'Sri Lanka', 'Korea Rep.', 'Bhutan', 'Mongolia', 'Singapore']
resources = [2838, 1260.5, 2812.4, 1210.6, 880.6, 366.5, 580, 479, 210, 430, 198.2, 120.6, 190.4, 50, 64.9, 95, 34.8, 0.6]

plt.figure(figsize=(12,6))
plt.barh(countries, resources)
plt.xlabel('Renewable Water Resources (km3)')
plt.title('Renewable Water Resources by Country')
plt.tight_layout()
plt.show()

# Figure 4-4: Increase of water consumption by region
years = [1900, 1925, 1950, 1975, 2000, 2025]
asia = [200, 300, 500, 900, 1400, 1900]
north_america = [50, 150, 300, 500, 600, 700]
europe = [100, 150, 250, 400, 450, 500]

plt.figure(figsize=(10,6))
plt.plot(years, asia, label='Asia')
plt.plot(years, north_america, label='North America')  
plt.plot(years, europe, label='Europe')
plt.xlabel('Year')
plt.ylabel('Water Consumption (km3)')
plt.title('Increase of Water Consumption by Region')
plt.legend()
plt.show()

# Figure 4-5: Population without improved sanitation by region in 2002
regions = ['South Asia', 'Eastern Asia', 'Sub-Saharan Africa', 'South-Eastern Asia', 'Latin America & Caribbean', 'Eurasia', 'Western Asia', 'Northern Africa', 'Developed Regions', 'Oceania']
population = [938, 749, 437, 208, 137, 50, 38, 40, 20, 3]

plt.figure(figsize=(12,6))
plt.barh(regions, population)
plt.xlabel('Population (millions)')
plt.title('Population Without Improved Sanitation by Region in 2002')
plt.tight_layout()
plt.show()