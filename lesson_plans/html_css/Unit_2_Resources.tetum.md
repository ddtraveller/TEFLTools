'## Unidade Aprendizajen 2: HTML Avansadu no Estrutura Dokumentu
- Objetivu:
  * Uza efetivamente elementu semantic HTML 
  * Kria pájina web ne'ebé estrutura di'ak no asesivel
- Topiku:
  * Elementu semantic HTML5
  * Formuláriu no tipu input
  * Konsiderasaun asesibilidade
- Atividade:
  * Dezenvolve website pájina oin-oin ba negósiu ka organizasaun Timor oan nian
  * Halo audit asesibilidade ba website popular Timor oan nian

## Rekursu Unidade

# Nota Preleksaun

## Elementu Semantic HTML5

### Introdusaun ba Semantic HTML
- Definisaun: HTML ne'ebé uza tag hodi transmite signifikadu konteúdu, la'ós de'it nia aparensia
- Importánsia: Mella asesibilidade, SEO, no lejibilidade kódigu
- Kontraste ho elementu non-semantic hanesan `<div>` no `<span>`

### Elementu Semantic Xave
1. `<header>`: Konteúdu introdutóriu ka ajuda navegasaun
2. `<nav>`: Seksãun ho ligasaun navegasaun
3. `<main>`: Konteúdu prinsipál dokumentu nian
4. `<article>`: Kompozisaun ne'ebé independente (ezemplu, postu blog, artigu notísia)
5. `<section>`: Seksãun independente dokumentu nian
6. `<aside>`: Konteúdu ne'ebé relasiona la direta ho konteúdu iha nia roda
7. `<footer>`: Footer ba seksaun konteúdu ka elementu seksaun ne'ebé besik liu

### Ezemplu Estrutura Semantic
```html
<body>
  <header>
    <h1>Ha'u nia Website</h1>
    <nav>
      <ul>
        <li><a href="#home">Uma</a></li>
        <li><a href="#about">Kona-ba</a></li>
        <li><a href="#contact">Kontaktu</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article>
      <h2>Títulu Artigu</h2>
      <p>Konteúdu artigu...</p>
    </article>
    <aside>
      <h3>Ligasaun Relasiona</h3>
      <ul>
        <li><a href="#">Ligasaun 1</a></li>
        <li><a href="#">Ligasaun 2</a></li>
      </ul>
    </aside>
  </main>
  <footer>
    <p>&copy; 2023 Ha'u nia Website</p>
  </footer>
</body>
```

## Formuláriu no Tipu Input

### Estrutura Báziku Formuláriu
- `<form>`: Konteiner ba formuláriu tomak
- `<input>`: Kria kontrolu interativu
- `<label>`: Fornese etiketa testu ba kontrolu formuláriu

### Tipu Input HTML5
1. `text`: Input testu liña ida
2. `email`: Input enderesu email
3. `password`: Kampu input password
4. `number`: Input numériku
5. `date`: Selesionador data
6. `tel`: Input númeru telefone
7. `url`: Input URL
8. `checkbox`: Checkbox ba seleksaun múltiplu
9. `radio`: Botãu rádiu ba seleksaun ida de'it
10. `file`: Kontrolu upload arkivu

### Atributu Validasaun Formuláriu
- `required`: Especifica kampu ne'ebé presiza
- `pattern`: Define espresaun regulár ba validasaun input
- `min` no `max`: Estabelese valór mínimu no máximu ba input numériku
- `minlength` no `maxlength`: Estabelese komprimidu mínimu no máximu ba input testu

### Ezemplu Formuláriu ho Validasaun
```html
<form action="/submit" method="post">
  <label for="name">Naran:</label