# HTML5 Guide

HTML5 is the latest version of the Hypertext Markup Language, the standard language for creating web pages. HTML5 introduced several new semantic elements that provide meaning to the structure of a web page, making it easier for search engines, screen readers, and developers to understand the content.

## Basic Structure of an HTML5 Document

An HTML5 document has the following basic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Title</title>
</head>
<body>
    <!-- Page content goes here -->
</body>
</html>
```

- `<!DOCTYPE html>`: Declares that this is an HTML5 document.
- `<html>`: The root element of the HTML page. The `lang` attribute specifies the language of the document.
- `<head>`: Contains metadata about the document, such as the character encoding, viewport settings, and the page title.
- `<body>`: Contains the visible content of the web page.

## HTML5 Semantic Elements

HTML5 introduced several semantic elements that provide meaning to the structure of a web page:

- `<header>`: Represents introductory content, typically including navigation and logo.
- `<nav>`: Defines a set of navigation links.
- `<main>`: Specifies the main content of a document.
- `<article>`: Represents a self-contained composition, such as a blog post or news story.
- `<section>`: Defines a generic section of a document or application.
- `<aside>`: Represents content that is tangentially related to the main content, such as sidebars.
- `<footer>`: Typically contains authorship information, copyright information, and related links.
- `<figure>`: Specifies self-contained content, such as illustrations, diagrams, photos, or code listings.
- `<figcaption>`: Defines a caption for a `<figure>` element.

Here's an example of how these semantic elements might be used in an HTML5 document:

```html
<body>
    <header>
        <h1>Website Title</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <article>
            <h2>Article Title</h2>
            <p>Article content...</p>
        </article>

        <section>
            <h2>Section Title</h2>
            <p>Section content...</p>
        </section>

        <aside>
            <h3>Related Links</h3>
            <ul>
                <li><a href="#">Link 1</a></li>
                <li><a href="#">Link 2</a></li>
            </ul>
        </aside>
    </main>

    <footer>
        <p>&copy; 2023 Website Name. All rights reserved.</p>
    </footer>
</body>
```

By using these semantic elements, you can create a well-structured and meaningful HTML5 document that is easier to understand and maintain.