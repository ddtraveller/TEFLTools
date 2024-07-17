# ## Learning Unit 4

## Learning Unit 4: Advanced CSS and Layout Techniques
- Objectives:
  * Implement responsive design principles
  * Use advanced CSS layout techniques
- Topics:
  * Flexbox and Grid layout
  * Media queries and responsive design
  * CSS frameworks (e.g., Bootstrap) with a focus on customization for Timorese aesthetics
- Activities:
  * Create a responsive portfolio website
  * Adapt an existing CSS framework to reflect Timorese design preferences

## Unit Resources

# Lecture Notes

## Flexbox

### Introduction to Flexbox
- Flexbox is a one-dimensional layout method for arranging items in rows or columns
- It allows for flexible element sizes to accommodate different screen sizes and devices
- Main components: flex container (parent) and flex items (children)

### Key Flexbox Properties
1. For the flex container:
   - `display: flex;` - Defines a flex container
   - `flex-direction` - Sets the main axis (row, column, row-reverse, column-reverse)
   - `justify-content` - Aligns items along the main axis
   - `align-items` - Aligns items along the cross axis
   - `flex-wrap` - Controls whether items wrap to new lines

2. For flex items:
   - `flex-grow` - Determines how much an item can grow
   - `flex-shrink` - Determines how much an item can shrink
   - `flex-basis` - Sets the initial main size of an item
   - `align-self` - Overrides the container's align-items for specific items

### Common Use Cases
- Navigation menus
- Card layouts
- Centering content vertically and horizontally
- Creating equal-height columns

## Grid

### Introduction to Grid
- CSS Grid is a two-dimensional layout system
- Allows for complex layouts with rows and columns
- Provides more control over both dimensions simultaneously

### Key Grid Properties
1. For the grid container:
   - `display: grid;` - Defines a grid container
   - `grid-template-columns` - Defines column sizes
   - `grid-template-rows` - Defines row sizes
   - `grid-gap` - Sets spacing between grid items
   - `justify-items` - Aligns items horizontally within their cell
   - `align-items` - Aligns items vertically within their cell

2. For grid items:
   - `grid-column` - Specifies which column(s) the item should span
   - `grid-row` - Specifies which row(s) the item should span
   - `justify-self` - Overrides container's justify-items for specific items
   - `align-self` - Overrides container's align-items for specific items

### Common Use Cases
- Page layouts with header, sidebar, main content, and footer
- Image galleries
- Dashboard layouts
- Magazine-style layouts

## Media Queries and Responsive Design

### Introduction to Media Queries
- Media queries allow CSS to be applied based on device characteristics
- They are a fundamental part of responsive web design

### Writing Media Queries
```css
@media screen and (max-width: 600px) {
  /* CSS rules for screens up to 600px wide */
}
```

### Common Breakpoints
- Mobile: up to 600px
- Tablet: 601px to 900px
- Desktop: 901px and above

### Mobile-First Approach
- Start with styles for mobile devices
- Use media queries to add complexity for larger screens
- Benefits: faster load times on mobile, forces prioritization of content

### Responsive Design Principles
1. Fluid grids
2. Flexible images
3. Media queries
4. Content prioritization

## CSS Frameworks (Bootstrap)

### Introduction to Bootstrap
- Popular CSS framework for building responsive, mobile-first websites
- Provides pre-built components and utilities

### Key Bootstrap Features
- Grid system
- Responsive breakpoints
- Pre-styled components (buttons, forms, navbars, etc.)
- Utility classes for quick styling

### Customizing Bootstrap
- Using Sass variables to override default styles
- Creating custom themes
- Extending Bootstrap classes

### Incorporating Timorese Design Elements
- Customizing color schemes to reflect traditional Timorese colors
- Adapting typography to include local fonts or styles
- Modifying component designs to incorporate traditional patterns or motifs

# Discussion Questions

1. How does flexbox differ from traditional CSS layout methods like floats? What advantages does it offer?
2. In what scenarios would you choose to use CSS Grid over Flexbox, and vice versa?
3. Why is responsive design important, especially in the context of Timor Leste's internet usage?
4. How can we balance the use of a CSS framework like Bootstrap with creating a unique, culturally relevant design for Timorese websites?
5. What challenges might arise when implementing responsive design for websites targeting Timorese users, and how can we address them?
6. How can we incorporate traditional Timorese design elements into modern web layouts using advanced CSS techniques?
7. What are the potential accessibility concerns when using flexbox or grid layouts, and how can we address them?
8. How might the mobile-first approach to responsive design benefit users in Timor Leste?

# Writing Exercise Instructions

## Exercise: Responsive Design Case Study

1. Choose a popular Timorese website or app that could benefit from improved responsive design.
2. Analyze its current layout and identify areas for improvement across different device sizes.
3. Write a 500-word proposal outlining:
   - The current issues with the site's responsiveness
   - Specific recommendations for improvement using flexbox, grid, and media queries
   - How you would incorporate Timorese design elements into the responsive layout
   - Potential challenges and how to overcome them
4. Include rough sketches or wireframes to illustrate your proposed changes for at least three different screen sizes (mobile, tablet, desktop).

# Assignment Details

## Responsive Portfolio Website

### Objective
Create a responsive portfolio website that showcases your web development skills and incorporates Timorese design elements.

### Requirements
1. Use HTML5 semantic elements for structure
2. Implement a responsive layout using both flexbox and grid
3. Include at least three different pages (e.g., Home, Projects, Contact)
4. Use media queries to ensure the site is fully responsive across mobile, tablet, and desktop sizes
5. Incorporate at least three unique Timorese design elements (colors, patterns, imagery)
6. Include a responsive navigation menu
7. Optimize all images for web use
8. Ensure the site passes basic accessibility checks
9. Use Git for version control and deploy the site using GitHub Pages

### Deliverables
1. Link to the live website
2. Link to the GitHub repository containing your code
3. A brief (300-500 word) reflection on your design choices, challenges faced, and how you incorporated Timorese elements

### Grading Criteria
- Responsiveness and layout (30%)
- Code quality and organization (20%)
- Incorporation of Timorese design elements (20%)
- Accessibility and best practices (15%)
- Creativity and overall design (15%)

# Additional Resources

## Flexbox and Grid Tutorials
- [Flexbox Froggy](https://flexboxfroggy.com/) - Interactive game for learning flexbox
- [Grid Garden](https://cssgridgarden.com/) - Interactive game for learning CSS grid
- [CSS-Tricks Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [CSS-Tricks Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

## Responsive Design Resources
- [Responsive Web Design Fundamentals](https://www.udacity.com/course/responsive-web-design-fundamentals--ud893) - Free Udacity course
- [Responsive Images](https://developers.google.com/web/fundamentals/design-and-ux/responsive/images) - Google Developers guide

## Bootstrap Customization
- [Official Bootstrap Customization Guide](https://getbootstrap.com/docs/5.0/customize/overview/)
- [Bootstrap Themes](https://themes.getbootstrap.com/) - For inspiration on customization

## Timorese Design Inspiration
- [Traditional Timorese Textiles](https://www.google.com/search?q=traditional+timorese+textiles&tbm=isch)
- [Timor-Leste Tourism Website](https://www.timorleste.tl/) - For examples of how Timorese culture is currently represented online

## Tools
- [Responsively App](https://responsively.app/) - For testing responsive designs across multiple screen sizes simultaneously
- [Adobe Color](https://color.adobe.com/create/color-wheel) - For creating color schemes inspired by Timorese designs