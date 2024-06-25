# HTML/HTML5 Cheat Sheet

## Basic Structure
The basic structure of an HTML document includes the `<!DOCTYPE html>` declaration, the `<html>` root element with the `lang` attribute, the `<head>` section for metadata and document information, and the `<body>` section for the main content of the page.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page Title</title>
</head>
<body>
    <!-- Page content goes here -->
</body>
</html>
```

## Common Elements
- `<p>`: Paragraph element, used to represent a paragraph of text.
- `<h1>` to `<h6>`: Heading elements, used to represent section headings with different levels of importance. `<h1>` is the highest level and `<h6>` is the lowest.
- `<a href="">`: Anchor element, used to create hyperlinks to other web pages or to sections within the same page. The `href` attribute specifies the link target.
- `<img src="" alt="">`: Image element, used to embed images into the HTML document. The `src` attribute specifies the image source, and the `alt` attribute provides alternative text for accessibility.
- `<ul>`, `<ol>`, `<li>`: List elements, used to create unordered (bullet) lists with `<ul>` and ordered (numbered) lists with `<ol>`. List items are represented by `<li>` elements.
- `<div>`: Division element, a generic container used to group and style content.
- `<span>`: Inline generic container, used to group and style inline elements without breaking the flow of the document.

## HTML5 Semantic Elements
HTML5 introduced semantic elements that provide meaning and structure to the content of a web page. These elements help search engines, screen readers, and developers understand the purpose of different parts of the document.

- `<header>`: Represents introductory content, such as a logo, navigation, or a banner.
- `<nav>`: Represents a section of navigation links, typically used for the main menu of a website.
- `<main>`: Represents the main content of the document, unique to that page.
- `<article>`: Represents a self-contained composition, such as a blog post, news article, or forum post.
- `<section>`: Represents a generic section of the document, typically used to group related content.
- `<aside>`: Represents content that is tangentially related to the main content, such as sidebars or call-out boxes.
- `<footer>`: Represents the footer of the document or a section, typically containing authorship information, copyright notices, or related links.

## Form Elements
HTML provides various form elements for collecting user input and submitting data to a server.

- `<form action="" method="">`: Represents a form, with the `action` attribute specifying the URL to which the form data is submitted and the `method` attribute specifying the HTTP method (e.g., "get" or "post").
- `<input type="">`: Represents an input field, with the `type` attribute specifying the type of input (e.g., "text", "radio", "checkbox", "password", "email", "number", etc.).
- `<textarea>`: Represents a multi-line text input field.
- `<select>` and `<option>`: Represent a drop-down list, with `<option>` elements representing the available options.
- `<button type="submit">`: Represents a submit button for the form.

## Media Elements
HTML5 introduced native support for multimedia content, such as audio and video, without the need for plugins.

- `<audio>`: Represents an audio player, with the `src` attribute specifying the audio file source or `<source>` elements nested inside for multiple sources.
- `<video>`: Represents a video player, with the `src` attribute specifying the video file source or `<source>` elements nested inside for multiple sources.
- `<source>`: Represents a media source for `<audio>` and `<video>` elements, allowing for multiple formats to ensure browser compatibility.

## Global Attributes
Global attributes are attributes that can be used on any HTML element to provide additional functionality or metadata.

- `class`: Specifies one or more CSS class names for an element, used for styling and selecting elements with JavaScript.
- `id`: Specifies a unique identifier for an element, used for styling, linking, and selecting elements with JavaScript.
- `style`: Specifies inline CSS styles for an element, overriding external stylesheets.
- `data-*`: Allows custom data attributes to be added to elements, which can be accessed and manipulated with JavaScript. The asterisk (`*`) is replaced with a specific name for the data attribute.

This cheat sheet covers the essential elements and concepts of HTML and HTML5. For more detailed information and advanced topics, refer to the official HTML specification and web development resources.