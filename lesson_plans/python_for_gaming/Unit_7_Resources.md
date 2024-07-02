# ## Learning Unit 7

## Learning Unit 7: Introduction to Libraries and APIs
- Objectives:
  * Use external libraries to extend Python's capabilities
  * Access web APIs to retrieve data
- Topics:
  * Installing and importing libraries
  * Using the requests library
  * Working with JSON data
- Activities:
  * Use a weather API to get the current weather in Dili
  * Create a simple data visualization of Timor-Leste statistics using matplotlib

## Unit Resources

Here are detailed resources for Learning Unit 7: Introduction to Libraries and APIs, formatted in Markdown:

# Resources for Learning Unit 7: Introduction to Libraries and APIs

## 1. Lecture Notes

### Introduction to Libraries

Libraries in Python are collections of pre-written code that extend Python's functionality. They allow us to reuse code and save time by not having to write everything from scratch.

Key points:
- Libraries are also called modules or packages
- They can be built-in (come with Python) or third-party (need to be installed)
- We use the `import` statement to use libraries in our code

Installing libraries:
- We use `pip`, Python's package manager, to install libraries
- Basic syntax: `pip install library_name`

Example:
```
pip install requests
```

Importing libraries:
```python
import library_name
# or
from library_name import specific_function
```

### Introduction to APIs

API stands for Application Programming Interface. It's a set of rules and protocols that allow different software applications to communicate with each other.

Key points:
- APIs enable us to access data and functionality from other services
- They often return data in JSON format
- We typically interact with APIs using HTTP requests (GET, POST, etc.)

Common use cases:
- Retrieving weather data
- Accessing social media platforms
- Getting financial information

### Using the requests Library

The `requests` library simplifies making HTTP requests in Python.

Basic usage:
```python
import requests

response = requests.get('https://api.example.com/data')
print(response.status_code)  # Should be 200 if successful
print(response.text)  # The content of the response
```

Error handling:
```python
response = requests.get('https://api.example.com/data')
response.raise_for_status()  # Raises an exception for 4xx/5xx status codes
```

### Working with JSON Data

JSON (JavaScript Object Notation) is a lightweight data format that's easy for humans to read and write, and easy for machines to parse and generate.

Parsing JSON in Python:
```python
import json

# Assuming 'response' is from a requests.get() call
data = json.loads(response.text)

# Now 'data' is a Python dictionary or list, depending on the JSON structure
```

### Introduction to matplotlib

matplotlib is a plotting library for Python that allows you to create a wide range of static, animated, and interactive visualizations.

Basic usage:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Graph')
plt.show()
```

## 2. Discussion Questions

1. What are some advantages of using external libraries in Python? Can you think of any potential drawbacks?

2. How do APIs facilitate communication between different software applications? Can you think of some real-world examples of API usage?

3. Why is JSON a popular format for data exchange in APIs? What are its advantages over other data formats?

4. How might we use Python libraries and APIs to address specific challenges or opportunities in Timor-Leste? Brainstorm some ideas.

5. What ethical considerations should we keep in mind when using APIs to collect data?

## 3. Writing Exercise Instructions

Write a short essay (300-500 words) on the following topic:

"The Impact of APIs and Data Visualization on Decision Making in Timor-Leste"

Consider the following points:
- How can easy access to data through APIs benefit decision-makers in Timor-Leste?
- What types of data visualizations might be particularly useful for understanding issues in Timor-Leste?
- What challenges might exist in implementing these technologies in Timor-Leste, and how could they be overcome?

## 4. Assignment Details

### Weather Application

Create a Python program that does the following:

1. Asks the user to input a city in Timor-Leste
2. Uses the OpenWeatherMap API to retrieve current weather data for that city
3. Displays the following information:
   - Current temperature (in both Celsius and Fahrenheit)
   - Weather description (e.g., "clear sky", "light rain")
   - Humidity percentage
4. Handles errors gracefully (e.g., city not found, API request failed)

### Timor-Leste Data Visualization

1. Find a dataset related to Timor-Leste (e.g., population by district, yearly coffee production, literacy rates)
2. Use matplotlib to create at least two different types of visualizations of this data (e.g., bar chart, line graph, pie chart)
3. Write a brief explanation (100-200 words) of what your visualizations reveal about the data

## 5. Additional Materials

### Sample API Documentation

Here's a simplified version of the OpenWeatherMap API documentation:

Endpoint: `https://api.openweathermap.org/data/2.5/weather`

Parameters:
- `q`: City name (e.g., "Dili,TL" for Dili, Timor-Leste)
- `appid`: Your API key
- `units`: Units of measurement (use "metric" for Celsius)

Example request:
```
https://api.openweathermap.org/data/2.5/weather?q=Dili,TL&appid=YOUR_API_KEY&units=metric
```

Sample response:
```json
{
  "weather": [
    {
      "description": "clear sky"
    }
  ],
  "main": {
    "temp": 29.5,
    "humidity": 70
  },
  "name": "Dili"
}
```

### Example: Parsing Weather Data

```python
import requests
import json

API_KEY = "your_api_key_here"
city = "Dili,TL"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = json.loads(response.text)

temp_celsius = data['main']['temp']
temp_fahrenheit = (temp_celsius * 9/5) + 32
description = data['weather'][0]['description']
humidity = data['main']['humidity']

print(f"Current weather in {city}:")
print(f"Temperature: {temp_celsius:.1f}°C / {temp_fahrenheit:.1f}°F")
print(f"Description: {description}")
print(f"Humidity: {humidity}%")
```

### Example: Creating a Bar Chart with matplotlib

```python
import matplotlib.pyplot as plt

districts = ['Dili', 'Baucau', 'Bobonaro', 'Ermera', 'Lautem']
population = [234026, 123203, 92049, 125702, 59787]

plt.bar(districts, population)
plt.title('Population of Timor-Leste Districts')
plt.xlabel('District')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

These resources should provide a comprehensive foundation for teaching the Introduction to Libraries and APIs unit, with a focus on practical applications relevant to Timor-Leste.