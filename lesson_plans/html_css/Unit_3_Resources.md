# ## Learning Unit 3

## Learning Unit 3: Introduction to CSS
- Objectives:
  * Understand CSS syntax and selectors
  * Apply basic styling to HTML documents
- Topics:
  * CSS syntax and selectors
  * Color theory and typography for web design
  * Box model and layout basics
- Activities:
  * Style the previously created HTML pages
  * Create a color scheme inspired by traditional Timorese textiles

## Unit Resources

# Lecture Notes

## CSS Syntax and Selectors

### Introduction to CSS
- CSS stands for Cascading Style Sheets
- Used to control the visual presentation of HTML documents
- Separates content (HTML) from presentation (CSS)

### Basic CSS Syntax
- Rule structure: selector { property: value; }
- Example: `p { color: blue; }`
- Multiple declarations: `h1 { color: red; font-size: 24px; }`

### Types of Selectors
1. Element Selector
   - Selects all instances of a specific HTML element
   - Example: `p { color: black; }`

2. Class Selector
   - Selects elements with a specific class attribute
   - Denoted by a period (.) before the class name
   - Example: `.highlight { background-color: yellow; }`

3. ID Selector
   - Selects a single element with a specific id attribute
   - Denoted by a hash (#) before the id name
   - Example: `#header { font-size: 36px; }`

4. Attribute Selector
   - Selects elements based on their attributes or attribute values
   - Example: `input[type="text"] { border: 1px solid gray; }`

### Combining Selectors
- Descendant selector: `div p { ... }`
- Child selector: `ul > li { ... }`
- Adjacent sibling selector: `h1 + p { ... }`

### Specificity and Cascading
- Explain how CSS resolves conflicts when multiple rules apply to the same element
- Order of specificity: Inline styles > IDs > Classes > Elements

### Linking CSS to HTML
1. External Stylesheet
   ```html
   <link rel="stylesheet" href="styles.css">
   ```
2. Internal Styles
   ```html
   <style>
     body { font-family: Arial, sans-serif; }
   </style>
   ```
3. Inline Styles
   ```html
   <p style="color: red;">This is red text.</p>
   ```

## Color Theory and Typography for Web Design

### Color Theory Basics
- Primary colors: Red, Blue, Yellow
- Secondary colors: Green, Orange, Purple
- Tertiary colors: Combinations of primary and secondary colors
- Color wheel: Tool for understanding color relationships

### Color Schemes
- Monochromatic: Various shades and tints of a single color
- Complementary: Colors opposite each other on the color wheel
- Analogous: Colors adjacent to each other on the color wheel
- Triadic: Three colors evenly spaced on the color wheel

### Color in CSS
- Named colors: `color: red;`
- Hexadecimal: `color: #FF0000;`
- RGB: `color: rgb(255, 0, 0);`
- RGBA (with alpha for transparency): `color: rgba(255, 0, 0, 0.5);`
- HSL (Hue, Saturation, Lightness): `color: hsl(0, 100%, 50%);`

### Typography Basics
- Serif vs. Sans-serif fonts
- Web-safe fonts: Fonts commonly available across different operating systems
- Font stacks: List of fonts in order of preference

### CSS Font Properties
- `font-family`: Specifies the font for an element
  ```css
  body { font-family: Arial, Helvetica, sans-serif; }
  ```
- `font-size`: Sets the size of the font
  ```css
  p { font-size: 16px; }
  ```
- `font-weight`: Sets the thickness of characters
  ```css
  h1 { font-weight: bold; }
  ```
- `font-style`: Sets the style of the font (normal, italic, oblique)
  ```css
  em { font-style: italic; }
  ```
- `text-align`: Aligns the text within an element
  ```css
  .center { text-align: center; }
  ```
- `line-height`: Sets the height of a line of text
  ```css
  p { line-height: 1.5; }
  ```

### Web Fonts
- Introduction to services like Google Fonts
- How to include web fonts in your CSS

## Box Model and Layout Basics

### The CSS Box Model
- Every HTML element is treated as a box
- Components of the box model:
  1. Content: The actual content of the element
  2. Padding: Space between the content and the border
  3. Border: A line around the padding and content
  4. Margin: Space outside the border

### CSS Properties for Box Model
- `width` and `height`: Set the dimensions of the content area
- `padding`: Sets the padding area
- `border`: Sets the border properties
- `margin`: Sets the margin area

### Example of Box Model CSS
```css
div {
  width: 300px;
  padding: 20px;
  border: 1px solid black;
  margin: 10px;
}
```

### Box-sizing Property
- Explain the difference between `content-box` and `border-box`
- How `border-box` can simplify layout calculations

### Basic Layout Concepts
- Block vs. Inline elements
- Floating elements
- Positioning (static, relative, absolute, fixed)

### Introduction to Flexbox
- Brief overview of Flexbox for modern layout techniques
- Basic Flexbox properties: `display: flex;`, `flex-direction`, `justify-content`, `align-items`

# Discussion Questions

1. How does CSS enhance the user experience of a website? Can you think of examples where poor CSS implementation might negatively impact a site?

2. Discuss the advantages and disadvantages of using external stylesheets versus inline styles. In what situations might you prefer one over the other?

3. How might color theory principles be applied to create a website that reflects Timorese culture? What colors are significant in Timorese art and textiles?

4. Why is typography important in web design? How can font choices affect the readability and mood of a website?

5. Explain the CSS box model in your own words. How does understanding the box model help in creating precise layouts?

6. How might responsive design principles be applied to ensure websites are accessible on the various devices commonly used in Timor-Leste?

7. Discuss the potential challenges of implementing modern web design techniques in Timor-Leste, considering factors like internet connectivity and device availability.

8. How can we balance the use of global web design trends with the need to create websites that resonate with local Timorese users?

# Writing Exercise Instructions

## Exercise 1: CSS Selector Challenge

Write CSS selectors for the following scenarios:

1. Select all paragraph elements within a div with the class "content".
2. Select the third list item in an unordered list.
3. Select all links that have been visited.
4. Select all input elements of type "text".
5. Select the first letter of every paragraph.

## Exercise 2: Color Scheme Creation

Create a color scheme for a website about Timorese culture:

1. Choose a primary color that you feel represents an aspect of Timorese culture.
2. Using color theory principles, select 2-3 additional colors that complement your primary color.
3. Write CSS code to apply your color scheme to a simple webpage structure (provide HTML structure).
4. Explain your color choices and how they relate to Timorese culture.

## Exercise 3: Typography Exploration

1. Research and list 5 font combinations (1 heading font and 1 body text font each) that you think would work well for a Timorese government website.
2. For each combination, write a brief explanation of why you chose it and how it might enhance the website's readability and professionalism.
3. Implement your favorite combination using CSS and apply it to a sample HTML structure.

# Assignment Details

## Assignment 1: Styling Your Personal Webpage

Take the personal webpage you created in the HTML unit and style it using CSS:

1. Create an external CSS file and link it to your HTML document.
2. Apply appropriate colors, fonts, and layout to enhance the visual appeal of your page.
3. Use at least three different types of selectors (element, class, and ID).
4. Implement the box model to create spacing and borders around elements.
5. Make sure your design is cohesive and reflects your personal style or a theme related to Timor-Leste.

Submission: HTML file, CSS file, and a brief explanation of your styling choices.

## Assignment 2: Timorese Textile-Inspired Color Scheme

1. Research traditional Timorese textiles (tais) and their color patterns.
2. Create a color scheme inspired by these textiles, consisting of at least 4 colors.
3. Design a simple one-page website about a Timorese cultural topic (e.g., traditional dance, cuisine, or festival) using your color scheme.
4. Implement your design using HTML and CSS.
5. Write a short report (200-300 words) explaining your color choices and how they relate to Timorese textiles.

Submission: HTML file, CSS file, images used (if any), and your written report.

# Additional Materials

## CSS Color Resources
- [Adobe Color](https://color.adobe.com/create/color-wheel): Interactive color wheel and scheme generator
- [Coolors](https://coolors.co/): Color scheme generator with export options

## Typography Resources
- [Google Fonts](https://fonts.google.com/): Free web fonts
- [Font Pair](https://fontpair.co/): Suggestions for font pairings

## CSS Layout Tutorials
- [CSS-Tricks: A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [MDN: CSS Layout](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout)

## Timorese Design Inspiration
- [Timor-Leste Government Portal](http://timor-leste.gov.tl/): Official government website
- [Tais Market](https://www.taismarket.com/): Website showcasing traditional Timorese textiles

## Example: Basic CSS for a Timorese-Inspired Website

```css
/* Timorese-inspired color scheme */
:root {
  --primary-color: #d62828;    /* Deep red, inspired by tais */
  --secondary-color: #fcbf49;  /* Golden yellow, common in Timorese art */
  --text-color: #003049;       /* Dark blue for readability */
  --background-color: #eae2b7; /* Light beige, reminiscent of natural fibers */
}

body {
  font-family: 'Lato', sans-serif;
  color: var(--text-color);
  background-color: var(--background-color);
  line-height: 1.6;
  margin: 0;
  padding: 0;
}

header {
  background-color: var(--primary-color);
  color: white;
  text-align: center;
  padding: 1rem;
}

h1, h2, h3 {
  font-family: 'Montserrat', sans-serif;
}

.container {
  width: 80%;
  margin: 0 auto;
  padding: 2rem;
}

.highlight {
  background-color: var(--secondary-color);
  padding: 0.5rem;
  border-radius: 5px;
}

a {
  color: var(--primary-color);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

.btn {
  display: inline-block;
  background-color: var(--primary-color);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  text-transform: uppercase;
  font-weight: bold;
}

.btn:hover {
  background-color: var(--text-color);
  text-decoration: none;
}
```

This CSS example provides a basic structure and color scheme inspired by Timorese textiles and culture. It can be used as a starting point for students to create their own Timorese-themed websites.