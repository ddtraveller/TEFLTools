Here's the support material for the lesson on Introduction to Libraries and APIs, formatted in Markdown:

# Support Material for Introduction to Libraries and APIs

## 1. Key Vocabulary List with Definitions

- **Library**: A collection of pre-written code that can be used to extend Python's capabilities.
- **API (Application Programming Interface)**: A set of protocols and tools for building software applications, allowing different systems to communicate with each other.
- **JSON (JavaScript Object Notation)**: A lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.
- **HTTP request**: A message sent by a client to a server to request specific information or action.
- **Data visualization**: The graphical representation of information and data using visual elements like charts, graphs, and maps.
- **pip**: The package installer for Python, used to install external libraries.
- **GET request**: An HTTP method used to retrieve data from a specified resource.
- **POST request**: An HTTP method used to send data to a server to create or update a resource.
- **Parsing**: The process of analyzing a string of symbols in natural language or computer languages according to the rules of a formal grammar.

## 2. Visual Aids or Diagrams

1. **API Request-Response Cycle Diagram**
   Description: A flowchart showing:
   - User/Client (Python program)
   - Arrow labeled "HTTP Request" pointing to API
   - API box
   - Arrow labeled "JSON Response" pointing back to User/Client

2. **Library Import Visualization**
   Description: A diagram showing:
   - Main Python script as a central circle
   - Smaller circles representing different libraries (requests, matplotlib, etc.)
   - Arrows pointing from libraries to the main script, labeled "import"

3. **JSON Structure Example**
   Description: A simple JSON object with key-value pairs, showing nested structures:
   ```json
   {
     "city": "Dili",
     "weather": {
       "temperature": 30,
       "description": "Sunny"
     },
     "forecast": [
       {"day": "Monday", "temp": 31},
       {"day": "Tuesday", "temp": 29}
     ]
   }
   ```

## 3. Handouts or Worksheets

1. **API Documentation Handout**
   Content: Simplified documentation for a weather API, including:
   - Base URL
   - Required parameters (e.g., city, API key)
   - Example request URL
   - Sample JSON response
   - Brief explanation of key data points in the response

2. **Python API Request Worksheet**
   Content:
   - Step-by-step guide to making an API request using the requests library
   - Fill-in-the-blank code snippet for students to complete
   - Questions prompting students to extract specific data from the JSON response

3. **Matplotlib Quick Reference**
   Content:
   - Basic syntax for creating different types of plots (line, bar, scatter)
   - Common customization options (titles, labels, colors)
   - Example code snippets for each plot type

## 4. Additional Resources for Further Reading or Practice

1. **Python Libraries and APIs**
   - "Python for Data Analysis" by Wes McKinney (Chapter on Working with APIs)
   - Requests library documentation: https://docs.python-requests.org/
   - "Python API Tutorial" on Real Python: https://realpython.com/python-api/

2. **Data Visualization with Matplotlib**
   - Matplotlib official tutorials: https://matplotlib.org/stable/tutorials/index.html
   - "Python Plotting With Matplotlib" on Real Python: https://realpython.com/python-matplotlib-guide/

3. **Timor-Leste Specific Resources**
   - Timor-Leste Government Data Portal (if available)
   - World Bank Timor-Leste Data: https://data.worldbank.org/country/timor-leste

## 5. Tips for Teachers on Potential Challenges and How to Address Them

1. **Challenge**: Students struggling with API concepts
   **Tip**: Use real-world analogies, like ordering food at a restaurant, to explain APIs. The menu is like API documentation, your order is the request, and the food you receive is the response.

2. **Challenge**: Difficulty in parsing JSON data
   **Tip**: Start with simple, flat JSON structures before introducing nested objects. Use visual representations of JSON to help students understand the structure.

3. **Challenge**: Issues with library installation
   **Tip**: Prepare a troubleshooting guide for common installation errors. Consider setting up a virtual environment to ensure all students have the same setup.

4. **Challenge**: Students overwhelmed by matplotlib options
   **Tip**: Begin with the simplest possible plots and gradually introduce customization. Provide a cheat sheet with the most common plotting commands.

5. **Challenge**: Connecting APIs to local context
   **Tip**: Research and prepare examples of APIs that provide data relevant to Timor-Leste (e.g., weather, economic indicators). If such APIs are limited, consider creating mock APIs with local data for practice.

6. **Challenge**: Varying internet connectivity
   **Tip**: Have offline alternatives prepared, such as saved API responses in JSON files that students can work with locally.