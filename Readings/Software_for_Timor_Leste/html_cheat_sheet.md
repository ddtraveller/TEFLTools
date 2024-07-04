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

# HTML/HTML5 Karta trigu 
 # # Estrutura Baziku 
 Estrutura bázika dokumentu HTML nian inklui deklarasaun <!DOTYPE html>, elementu huun <html> ho atribuisaun "lang," seksaun "<head>" ba informasaun metadadu no dokumentu, no seksaun "<body>" ba konteúdu prinsipál pájina nian. 
 "Html 
 DOTYPE html> Htmllang="en"> Ulun Meta jawset="UTF-8"> 
 Titulu pájina</titulu> 
 Ulun-toos Body> Konteudu pájina ba iha ne'e --> 
 Body> Html> " 
 # # # Elementu komún 
 - 
: Elementu Paragrafu, uza atu reprezenta parágrafu ida husi testu. 
 -<h1> to'o <h6>: Elementu sira ne'ebé uza atu reprezenta títulu seksaun ho nivel importánsia diferente. <h1> mak nivel aas liu no <h6> mak ki'ik liu. 
 - <a href=">: Elementu Anchor, ne'ebé uza atu kria hiperlinks ba pájina web seluk ka ba seksaun sira iha pájina ida deit. Atribuisaun "href" espesífika ligasaun alvu. 
 -<img src="" alt=">: Elementu imajen, ne'ebé uza atu inklui imajen sira iha dokumentu HTML. Atribuisaun "src" espesífika fonte imajen, no atribuisaun "alt" fornese testu alternativu ba asesibilidade. 
 -<ul>,<ol>,<li>: Lista elementu sira, ne'ebé uza atu kria lista ne'ebé la iha orden (bullet) ho lista ne'ebé la iha orden (<ul>) no númeru (numeru) ho <ol>. Lista item sira reprezenta husi elementu sira. 
 -<div>: Elementu Divizaun, kontentór jerál ne'ebé uza ba konteúdu grupu no estilu. 
 -<span>: Konteiner jerál ne'ebé iha ligasaun, uza ba elementu grupu no estilu iha ligasaun sein halo rahun dokumentu nia suli. 
 # # HTML5 Elementu Semantiku 
 HTML5 introdús elementu semantiku sira ne'ebé fó signifikasaun no estrutura ba konteúdu pájina web. Elementu hirak-ne'e ajuda buka mákina, lee-nain sira ne'ebé haree, no dezenvolve-nain sira atu komprende objetivu husi parte oioin husi dokumentu ne'e. 
 -<head>: Reprezentante konteúdu introdutóriu, hanesan logo, navigasaun, ka banner. 
 -<nav>: Reprezentante seksaun ida kona-ba ligasaun navigasaun, baibain uza ba menu prinsipál iha website. 
 -<main>: Reprezentante konteúdu prinsipál husi dokumentu nee, úniku ba pájina nee. 
 -<artigu>: Reprezentante kompozisaun ne'ebé iha konteúdu rasik, hanesan postu blog, artigu notísia, ka postu forum. 
 -<seksaun> Reprezentante seksaun jerál ida husi dokumentu nee, baibain uza ba konteúdu relasiona ho grupu. 
 -<aside>: Reprezentante konteúdu ne'ebé tangente relasiona ho konteúdu prinsipál sira, hanesan kaixa boot ka kaixa call-out. 
 -<footer>: Reprezentante footer husi dokumentu ka seksaun ida, baibain kontein informasaun kona-ba autór, notísia direitu direitu, ka ligasaun sira ne'ebé iha relasaun. 
## Formasaun Elementu 
 HTML fornese elementu formuláriu oioin atu halibur input utilizadór no submete dadus ba serveiru ida. 
 - <form action="" métodu=">: Reprezentante formuláriu ida, ho asaun ne'ebé espesífika URL ne'ebé submete dadus formuláriu nian no métodu ne'ebé espesífika métodu ne'e métodu (ezemplu, "get" ka "postu"). 
 - <input type=">: Reprezentante kampu input ida, ho tipu atribuisaun espesífika tipu input (ezemplu, "textu," "radia," "checkbox," "password," "email," "number," etc.). 
 -<textu>: Reprezentante kampu input testu multi-line. 
 -<select> no<opsaun>: Reprezentante lista drop-down, ho elementu <opsaun> ne'ebé reprezenta opsaun sira ne'ebé disponivel. 
 -< Button type="submit">: Reprezentante knotak submisaun ba formuláriu. 
 ## Elementu Komunikasaun Sosial 
 HTML5 introdús apoiu nasionál ba konteúdu multimedia, hanesan audio no vídeo, sein nesesidade ba plugins. 
 -<audio>: Reprezentante ba player audio, ho atribuisaun src espesífika fonte fail audio ka elementu <source> ne'ebé la iha iha laran ba fonte oioin. 
 -<video>: Reprezentante ba vídeo-nain ida, ho atribuisaun "src" ne'ebé espesífika fonte fail vídeo ka elementu "<source>" ne'ebé la iha iha laran ba fonte oioin. 
 -<source> Reprezentante fonte média ida ba elementu <audio> no <video>, ne'ebé permite formatu oioin atu asegura kompatibilidade navegador. 
 ## 
 Atributu globál mak atributu ne'ebé bele uza iha kualkér elementu HTML atu fornese funsionalidade adisionál ka metadadu. 
 - Klase: Espesifika naran klase CSS ida ka liu ba elementu ida, uza ba estilu no hili elementu ho JavaScript. 
 - ID: Espesifika identifikador úniku ida ba elementu ida, ne'ebé uza ba estilu, ligasaun, no hili elementu ho JavaScript. 
 - estilu: Espesifika estilu CSS iha liña ba elementu ida, liu husi estilu esternu. 
 - Data-*: Husik atributu dadus kostumeiru sira atu aumenta ba elementu sira, ne'ebé bele hetan asesu no manipulasaun ho JavaScript. Asterisk (*') troka ho naran espesífiku ba atribuisaun dadus. 
 Kaixa bosok ne'e kobre elementu no konseitu esensiál sira husi HTML no HTML5. Atu hetan informasaun detalladu liu no tópiku avansadu sira, refere ba espesifikasaun ofisiál HTML no rekursu dezenvolvimentu web.