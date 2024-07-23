'# Gia HTML5

HTML5 mak versaun foun liu husi Hypertext Markup Language, lian standard ba halo pájina web. HTML5 introduz elementu semántika foun sira ne'ebé fornese signifikadu ba estrutura pájina web, hodi fasil hela ba motor buka, leitor ekrã, no dezenvolvedor sira atu komprende konteúdu.

## Estrutura Báziku husi Dokumentu HTML5

Dokumentu HTML5 iha estrutura báziku hanesan tuir mai:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Títulu Dokumentu</title>
</head>
<body>
    <!-- Konteúdu pájina ne'e tama iha ne'e -->
</body>
</html>
```

- `<!DOCTYPE html>`: Deklara katak dokumentu ida ne'e dokumentu HTML5.
- `<html>`: Elementu as liu husi pájina HTML. Atributu `lang` hatudu lian husi dokumentu.
- `<head>`: Kontein metadata kona ba dokumentu, inklui kodifikasaun karakter, definisaun viewport, no títulu pájina.
- `<body>`: Kontein konteúdu visível husi pájina web.

## Elementu Semántika HTML5

HTML5 introduz elementu semántika balu ne'ebé fornese signifikadu ba estrutura pájina web:

- `<header>`: Reprezenta konteúdu introdutóriu, normalmente inklui navigasaun no logo.
- `<nav>`: Defini grupu husi ligasaun navigasaun.
- `<main>`: Hatudu konteúdu prinsipál husi dokumentu.
- `<article>`: Reprezenta kompozisaun ne'ebé iha nia rasik, hanesan post blog ka notísia.
- `<section>`: Defini seksaun jenerál ida husi dokumentu ka aplikasaun.
- `<aside>`: Reprezenta konteúdu ne'ebé relasiona ho konteúdu prinsipál, hanesan sidebar.
- `<footer>`: Normalmente kontein informasaun autor, informasaun direitu autór, no ligasaun relasionadu.
- `<figure>`: Hatudu konteúdu ne'ebé iha nia rasik, hanesan ilustrasaun, diagrama, foto, ka lista kódigu.
- `<figcaption>`: Defini legenda ba elementu `<figure>`.

Iha ne'ebé ezemplu ida kona ba oinsá elementu semántika sira ne'e bele uza iha dokumentu HTML5:

```html
<body>
    <header>
        <h1>Títulu Website</h1>
        <nav>
            <ul>
                <li><a href="#">Uma</a></li>
                <li><a href="#">Kona Ba</a></li>
                <li><a href="#">Kontaktu</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <article>
            <h2>Títulu Artigu</h2>
            <p>Konteúdu artigu...</p>
        </article>

        <section>
            <h2>Títulu Seksãun</h2>
            <p>Konteúdu seksaun...</p>
        </section>

        <aside>
            <h3>Ligasaun Relasionadu</h3>
            <ul>
                <li><a href="#">Ligasaun 1</a></li>
                <li><a href="#">Ligasaun 2</a></li>
            </ul>
        </aside>
    </main>

    <footer>
        <p>&copy; 2023 Naran Website. Direitu hotu-hotu rezervadu.</p>
    </footer>
</body>
```

Husi uza elementu semántika sira ne'e, ita bele kria dokumentu HTML5 ida ne'ebé iha estrutura di'ak no signifikadu, ne'ebé fasil liu atu komprende no mantein.