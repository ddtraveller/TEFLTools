# ## Learning Unit 1

## Learning Unit 1: Introduction to HTML and Web Fundamentals
- Objectives:
  * Understand the basic structure of the World Wide Web
  * Create simple HTML documents
- Topics:
  * History of the Web and its importance in Timor Leste
  * Basic HTML structure and syntax
  * Common HTML elements
- Activities:
  * Create a simple personal webpage about yourself
  * Research and present on the current state of internet usage in Timor Leste

## Unit Resources

# Lecture Notes

## History of the Web and its importance in Timor Leste

### The Birth of the World Wide Web
- Invented by Tim Berners-Lee in 1989 at CERN
- Created to share information between scientists
- First website published in 1991

### How the Web Works
- Client-server model
- HTTP protocol
- Role of web browsers and web servers

### The Web in Timor Leste
- Internet introduced in 1999 after independence
- Slow adoption due to infrastructure challenges
- Growing importance for education, business, and government services
- Current challenges: limited access in rural areas, high costs, low digital literacy

## Basic HTML Structure and Syntax

### HTML Document Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Title</title>
</head>
<body>
    <!-- Content goes here -->
</body>
</html>
```

### Explanation of Key Parts
- `<!DOCTYPE html>`: Declares the document type
- `<html>`: Root element of the HTML page
- `<head>`: Contains meta-information about the document
- `<body>`: Contains the visible page content

### HTML Syntax Rules
- Elements are defined by tags
- Most elements have opening and closing tags
- Tags are case-insensitive, but lowercase is recommended
- Elements can be nested inside other elements

## Common HTML Elements

### Text Elements
- `<h1>` to `<h6>`: Headings
- `<p>`: Paragraphs
- `<strong>`: Bold text
- `<em>`: Italicized text

### List Elements
- `<ul>`: Unordered list
- `<ol>`: Ordered list
- `<li>`: List item

### Links and Images
- `<a href="URL">`: Hyperlink
- `<img src="image.jpg" alt="description">`: Image

### Structural Elements
- `<div>`: Generic container
- `<span>`: Inline container

# Discussion Questions

1. How has the World Wide Web changed society since its invention?
2. What are the potential benefits of increased internet access in Timor Leste?
3. How might HTML be used to preserve and share Timorese culture online?
4. What challenges might Timor Leste face in increasing internet adoption?
5. How does the structure of an HTML document reflect the way information is organized on a webpage?
6. Why is it important to use semantic HTML elements?
7. How might learning HTML impact job opportunities in Timor Leste?
8. What types of websites do you think would be most beneficial for Timorese communities?

# Writing Exercises

## Exercise 1: HTML Structure Practice
Write the basic HTML structure for a webpage about your favorite place in Timor Leste. Include:
- A proper document structure with `<!DOCTYPE>`, `<html>`, `<head>`, and `<body>` tags
- A title for your page
- At least one heading and one paragraph of text

## Exercise 2: Creating Lists
Create two lists on your webpage:
1. An unordered list of three traditional Timorese foods
2. An ordered list of the top three tourist attractions in Timor Leste

## Exercise 3: Adding Links and Images
Enhance your webpage by:
- Adding a link to an official Timor Leste tourism website
- Inserting an image of a Timorese landmark (use a placeholder URL if needed)

# Assignments

## Assignment 1: Personal Webpage Creation
Create a simple personal webpage about yourself. The webpage should include:
- Your name as the main heading
- A paragraph introducing yourself
- A list of your hobbies or interests
- An image (it can be a placeholder if you prefer not to use a personal photo)
- A link to your favorite website

Requirements:
- Use proper HTML structure
- Implement at least 5 different HTML elements
- Ensure all tags are correctly opened and closed
- Save the file as "index.html"

## Assignment 2: Timor Leste Internet Usage Research
Conduct research on the current state of internet usage in Timor Leste. Prepare a short presentation (2-3 minutes) and create an HTML document with your findings. Include:
- Statistics on internet penetration
- Main challenges to internet adoption
- Recent developments or initiatives to improve internet access
- Potential impact of increased internet access on Timorese society

Requirements:
- Use at least one heading level
- Include a numbered list of key points
- Cite your sources using HTML links
- Save the file as "timor-leste-internet.html"

# Additional Resources

## Online Tutorials
- [MDN Web Docs: HTML Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [W3Schools HTML Tutorial](https://www.w3schools.com/html/)

## Tools
- [HTML Validator](https://validator.w3.org/)
- [CodePen](https://codepen.io/) - for practicing HTML in the browser

## Timor Leste Specific Resources
- [Government of Timor Leste Official Website](http://timor-leste.gov.tl/)
- [Timor Leste Internet Usage Statistics](https://www.internetworldstats.com/asia/tl.htm)

## Example HTML Code
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Timor Leste</title>
</head>
<body>
    <h1>Discover Timor Leste</h1>
    <p>Timor Leste is a beautiful country in Southeast Asia, known for its rich culture and stunning landscapes.</p>
    <h2>Popular Destinations</h2>
    <ul>
        <li>Dili</li>
        <li>Atauro Island</li>
        <li>Mount Ramelau</li>
    </ul>
    <img src="https://example.com/timor-leste-beach.jpg" alt="Beautiful beach in Timor Leste">
    <p>Learn more about Timor Leste on the <a href="https://www.timorleste.tl/">official tourism website</a>.</p>
</body>
</html>
```