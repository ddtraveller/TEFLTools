# ## Learning Unit 2

## Learning Unit 2: Advanced HTML and Document Structure
- Objectives:
  * Use semantic HTML elements effectively
  * Create well-structured and accessible web pages
- Topics:
  * Semantic HTML5 elements
  * Forms and input types
  * Accessibility considerations
- Activities:
  * Develop a multi-page website for a local Timorese business or organization
  * Conduct an accessibility audit of a popular Timorese website

## Unit Resources

# Lecture Notes

## Semantic HTML5 Elements

### Introduction to Semantic HTML
- Definition: HTML that uses tags to convey the meaning of content, not just its appearance
- Importance: Improves accessibility, SEO, and code readability
- Contrast with non-semantic elements like `<div>` and `<span>`

### Key Semantic Elements
1. `<header>`: Introductory content or navigational aids
2. `<nav>`: Section with navigation links
3. `<main>`: Main content of the document
4. `<article>`: Self-contained composition (e.g., blog post, news article)
5. `<section>`: Standalone section of a document
6. `<aside>`: Content tangentially related to the content around it
7. `<footer>`: Footer for its nearest sectioning content or sectioning root element

### Example of Semantic Structure
```html
<body>
  <header>
    <h1>My Website</h1>
    <nav>
      <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article>
      <h2>Article Title</h2>
      <p>Article content...</p>
    </article>
    <aside>
      <h3>Related Links</h3>
      <ul>
        <li><a href="#">Link 1</a></li>
        <li><a href="#">Link 2</a></li>
      </ul>
    </aside>
  </main>
  <footer>
    <p>&copy; 2023 My Website</p>
  </footer>
</body>
```

## Forms and Input Types

### Basic Form Structure
- `<form>`: Container for the entire form
- `<input>`: Creates interactive controls
- `<label>`: Provides a text label for form controls

### HTML5 Input Types
1. `text`: Single-line text input
2. `email`: Email address input
3. `password`: Password input field
4. `number`: Numeric input
5. `date`: Date picker
6. `tel`: Telephone number input
7. `url`: URL input
8. `checkbox`: Checkboxes for multiple selections
9. `radio`: Radio buttons for single selection
10. `file`: File upload control

### Form Validation Attributes
- `required`: Specifies a required field
- `pattern`: Defines a regular expression for input validation
- `min` and `max`: Set minimum and maximum values for number inputs
- `minlength` and `maxlength`: Set minimum and maximum length for text inputs

### Example of a Form with Validation
```html
<form action="/submit" method="post">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>

  <label for="phone">Phone:</label>
  <input type="tel" id="phone" name="phone" pattern="[0-9]{9}" required>

  <label for="birthdate">Birthdate:</label>
  <input type="date" id="birthdate" name="birthdate" required>

  <button type="submit">Submit</button>
</form>
```

## Accessibility Considerations

### Introduction to Web Accessibility
- Definition: Making websites usable by as many people as possible, including those with disabilities
- WCAG: Web Content Accessibility Guidelines
- Four principles: Perceivable, Operable, Understandable, Robust (POUR)

### Key Accessibility Practices
1. Proper heading structure (`<h1>` to `<h6>`)
2. Alternative text for images (`alt` attribute)
3. Descriptive link text
4. Color contrast for readability
5. Keyboard navigation support
6. ARIA attributes for complex interactions

### Example of Accessible Markup
```html
<img src="logo.png" alt="Company Logo">

<a href="contact.html" aria-label="Contact Us">
  <img src="envelope.png" alt="">
</a>

<button type="button" aria-pressed="false">
  Toggle Feature
</button>

<div role="alert" aria-live="assertive">
  Form submitted successfully!
</div>
```

# Discussion Questions

1. How does semantic HTML improve the overall quality of a website?
2. What are some challenges in implementing accessible web design in Timor Leste?
3. How can proper form design and validation enhance user experience?
4. Discuss the balance between aesthetics and accessibility in web design.
5. How might semantic HTML and accessibility features benefit Timorese businesses online?

# Writing Exercise Instructions

1. Write a brief proposal (250-300 words) for a Timorese business website, outlining:
   - The type of business
   - Key features the website should include
   - How you would implement semantic HTML and accessibility features
   - Potential challenges and solutions for creating an accessible site in Timor Leste

2. Create a wireframe sketch of the homepage for your proposed website, labeling semantic HTML elements.

# Assignment Details

## Multi-page Website Project

### Objective
Create a multi-page website for a local Timorese business or organization, implementing semantic HTML structure and accessible design principles.

### Requirements
1. Minimum of 4 pages (e.g., Home, About, Services/Products, Contact)
2. Use semantic HTML5 elements throughout
3. Include a navigation menu using `<nav>`
4. Implement at least one form with proper validation
5. Ensure all images have appropriate alt text
6. Use heading tags (`<h1>` to `<h6>`) in a logical hierarchy
7. Include ARIA attributes where appropriate
8. Ensure the site is keyboard navigable

### Deliverables
- HTML files for all pages
- A brief document explaining your semantic HTML choices and accessibility features

## Accessibility Audit

### Objective
Conduct an accessibility audit of a popular Timorese website to identify areas for improvement.

### Steps
1. Choose a well-known Timorese website
2. Use the WAVE Web Accessibility Evaluation Tool (https://wave.webaim.org/)
3. Manually check for keyboard navigation and logical reading order
4. Review color contrast using a tool like WebAIM's Contrast Checker

### Deliverables
A report (500-750 words) including:
- Name and URL of the website audited
- Summary of accessibility issues found
- Specific examples of problems (with screenshots if possible)
- Recommendations for improvements
- Reflection on the importance of accessibility for Timorese websites

# Additional Materials

## HTML5 Semantic Elements Cheat Sheet

| Element   | Purpose                                          |
|-----------|--------------------------------------------------|
| `<header>`| Introductory content or navigational aids        |
| `<nav>`   | Section with navigation links                    |
| `<main>`  | Main content of the document                     |
| `<article>`| Self-contained composition                      |
| `<section>`| Standalone section of a document                |
| `<aside>` | Content tangentially related to surrounding content |
| `<footer>`| Footer for nearest sectioning content or root    |

## WCAG 2.1 Quick Reference

1. Perceivable
   - Provide text alternatives for non-text content
   - Provide captions and alternatives for audio/video content
   - Present content in different ways without losing information
   - Make it easier for users to see and hear content

2. Operable
   - Make all functionality available from a keyboard
   - Give users enough time to read and use content
   - Do not use content that causes seizures or physical reactions
   - Provide ways to help users navigate and find content

3. Understandable
   - Make text readable and understandable
   - Make content appear and operate in predictable ways
   - Help users avoid and correct mistakes

4. Robust
   - Maximize compatibility with current and future user tools

## Example of Non-Semantic vs. Semantic HTML

### Non-Semantic
```html
<div class="header">
  <h1>My Website</h1>
  <div class="nav">
    <ul>
      <li><a href="#home">Home</a></li>
      <li><a href="#about">About</a></li>
    </ul>
  </div>
</div>
<div class="main-content">
  <div class="article">
    <h2>Article Title</h2>
    <p>Article content...</p>
  </div>
  <div class="sidebar">
    <h3>Related Links</h3>
    <ul>
      <li><a href="#">Link 1</a></li>
      <li><a href="#">Link 2</a></li>
    </ul>
  </div>
</div>
<div class="footer">
  <p>&copy; 2023 My Website</p>
</div>
```

### Semantic
```html
<header>
  <h1>My Website</h1>
  <nav>
    <ul>
      <li><a href="#home">Home</a></li>
      <li><a href="#about">About</a></li>
    </ul>
  </nav>
</header>
<main>
  <article>
    <h2>Article Title</h2>
    <p>Article content...</p>
  </article>
  <aside>
    <h3>Related Links</h3>
    <ul>
      <li><a href="#">Link 1</a></li>
      <li><a href="#">Link 2</a></li>
    </ul>
  </aside>
</main>
<footer>
  <p>&copy; 2023 My Website</p>
</footer>
```