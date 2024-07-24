'## Unidade Aprendizajen 6

## Unidade Aprendizajen 6: Introdusaun ba Programasaun Orientadu ba Objetu
- Objetivus:
  * Komprende fundamentus fundamentais Programasaun Orientadu ba Objetu
  * Kria no uza klase simples no objetus
- Topikus:
  * Klase no objetus
  * Atributus no metodus
- Atividades:
  * Dezenvolve klase ida atu reprezenta uma tradisional Timor-Leste (Uma Lulik)
  * Kria sistema simples jestaun inventáriu ba koperativa kafé lokal

## Rekursus Presiza
- Python 3.x instaladu iha komputadores
- IDLE ka editór textu seluk
- Aksesu ba internet atu download Python no rekursus adisionais

## Sugestaun Itens atu Kobre
- Papel Python iha analiza dadus no aplikasaun potensial iha dezenvolvimentu Timor-Leste
- Konsiderasaun étika iha programasaun no jestaun dadus
- Oportunidade karreira iha programasaun iha Timor-Leste no internasionál

## Esperiensia Prátika no Envolvimentu Komunidade
- Dezenvolve website simples ba negósiu lokal ka organizasaun komunidade
- Kria programa ida atu asiste iha esforsu edukasaun (exemplu, aplikasaun aprendizajen lian Tetun)
- Partisipa iha workshop kodifikasaun ba estudantes ensino sekundáriu lokal

## Rekursus Adisionais
- Dokumentasaun Python online (https://docs.python.org/)
- Kursus online grátis iha plataforma hanesan Coursera ka edX
- Komunidade programasaun lokal ka enkontru iha Dili
- Livrus kona-ba programasaun Python traduzidu ba Tetun ka Portuges, se iha

## Rekursus Unidade

Iha ne'e rekursus detalladu ba Unidade Aprendizajen 6: Introdusaun ba Programasaun Orientadu ba Objetu, formatadu iha Markdown:

# Rekursus ba Unidade Aprendizajen 6: Introdusaun ba Programasaun Orientadu ba Objetu

## 1. Nota Leitura

### Introdusaun ba Programasaun Orientadu ba Objetu (OOP)

Programasaun Orientadu ba Objetu mak paradigma programasaun ne'ebé organiza kódigu tuir objetus, ne'ebé mak instansia husi klase. Metodu ida ne'e ajuda hodi kria kódigu modular, reutilizavel, no fasil atu manutensaun.

Konseitus xave:
- Klase: Molde ba kria objetus
- Objetus: Instansia husi klase
- Atributus: Dadus armazenadu iha objetu
- Metodus: Funsaun sira ne'ebé pertense ba klase no define komportamentu objetu

#### Benefísius OOP:
1. Modularidade: Kódigu organizadu iha unidade diskretu (objetus)
2. Reutilizabilidade: Objetus bele uza fali iha parte diferente husi programa ida ka programa sira seluk
3. Enkapsulasaun: Dadus no metodus sira kombinadu hamutuk, esconde detallu internu
4. Abstrasaun: Sistema kompleksu bele modela hanesan reprezentasaun abstratu simples

### Kria Klase no Objetus iha Python

Iha Python, ami define klase uza 'class' palavra-xave:

```python
class UmaLulik:
    def __init__(self, size, location, materials):
        self.size = size
        self.location = location
        self.materials = materials

    def describe(self):
        return f"This Uma Lulik is {self.size} square meters, located in {self.location}, and made of {self.materials}."

    def renovate(self, new_materials):
        self.materials = new_materials
        return f"The Uma Lulik has been renovated with {new_materials}."

# Kria objetu (instansia) husi klase UmaLulik
my_uma