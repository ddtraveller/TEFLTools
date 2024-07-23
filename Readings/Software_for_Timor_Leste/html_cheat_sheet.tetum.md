'HTML/HTML5 Karta Trigu 

## Estrutura Baziku 
Estrutura bázika dokumentu HTML nian inklui deklarasaun `<!DOCTYPE html>`, elementu huun `<html>` ho atribuisaun `lang`, seksaun `<head>` ba informasaun metadadu no dokumentu, no seksaun `<body>` ba konteúdu prinsipál pájina nian. 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Titulu Pájina</title>
</head>
<body>
    <!-- Konteúdu pájina ba iha ne'e -->
</body>
</html>
```

## Elementu Komún 
- `<p>`: Elementu parágrafu, uza atu reprezenta parágrafu ida husi testu. 
- `<h1>` to'o `<h6>`: Elementu sira ne'ebé uza atu reprezenta títulu seksaun ho nivel importánsia diferente. `<h1>` mak nivel aas liu no `<h6>` mak ki'ik liu. 
- `<a href="">`: Elementu Anchor, ne'ebé uza atu kria hiperlinks ba pájina web seluk ka ba seksaun sira iha pájina ida-deit. Atribuisaun `href` espesífika ligasaun alvu. 
- `<img src="" alt="">`: Elementu imajen, ne'ebé uza atu inklui imajen sira iha dokumentu HTML. Atribuisaun `src` espesífika fonte imajen, no atribuisaun `alt` fornese testu alternativu ba asesibilidade. 
- `<ul>`, `<ol>`, `<li>`: Lista elementu sira, ne'ebé uza atu kria lista ne'ebé la iha orden (bullet) ho `<ul>` no númeru (ordenadu) ho `<ol>`. Lista item sira reprezenta husi `<li>` elementu sira.
- `<div>`: Elementu Divizaun, kontentór jerál ne'ebé uza ba grupu konteúdu no estilu. 
- `<span>`: Konteiner jerál ne'ebé iha ligasaun, uza ba grupu elementu no estilu iha ligasaun sein halo rahun dokumentu nia suli. 

## HTML5 Elementu Semantiku 
HTML5 introdús elementu semantiku sira ne'ebé fó signifikasaun no estrutura ba konteúdu pájina web. Elementu hirak-ne'e ajuda buka mákina, lee-nain sira ne'ebé haree, no dezenvolve-nain sira atu komprende objetivu husi parte oioin husi dokumentu ne'e. 
- `<header>`: Reprezentante konteúdu introdutóriu, hanesan logo, navigasaun, ka banner. 
- `<nav>`: Reprezentante seksaun ida kona-ba ligasaun navigasaun, baibain uza ba menu prinsipál iha website. 
- `<main>`: Reprezentante konteúdu prinsipál husi dokumentu nee, úniku ba pájina nee. 
- `<article>`: Reprezentante kompozisaun ne'ebé iha konteúdu rasik, hanesan postu blog, artigu notísia, ka postu forum. 
- `<section>`: Reprezentante seksaun jerál ida husi dokumentu nee, baibain uza ba grupu konteúdu ne'ebé relasiona. 
- `<aside>`: Reprezentante konteúdu ne'ebé tangente relasiona ho konteúdu prinsipál sira, hanesan kaixa boot ka kaixa kedas. 
- `<footer>`: Reprezentante footer husi dokumentu ka seksaun ida, baibain kontein informasaun kona-ba autór, notísia direitu direitu, ka ligasaun sira ne'ebé iha relasaun. 

## Formasaun Elementu 
HTML fornese elementu formuláriu oioin atu halibur input utilizadór no submete dadus ba serveiru ida. 
- `<form action="" method="">`: Reprezentante