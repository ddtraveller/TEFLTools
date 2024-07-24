'# Introdução aos Bancos de Dados Relacionais: Conceitos e Estrutura

## 1. O que é um Banco de Dados?

Um banco de dados é uma coleção estruturada de dados persistentes que são organizados para armazenamento eficiente, gestão e recuperação. No contexto da ciência da computação e sistemas de informação, um banco de dados serve como um repositório central para armazenar e gerenciar dados que podem ser acessados ​​e manipulados por várias aplicações e usuários.

Os bancos de dados são cruciais no desenvolvimento de software moderno, alimentando uma ampla gama de aplicações, desde simples aplicativos móveis até sistemas empresariais complexos. Eles fornecem uma maneira confiável e escalável para armazenar e gerenciar grandes quantidades de dados, garantindo a integridade, consistência e disponibilidade dos dados.

Um Sistema de Gestão de Banco de Dados (DBMS) é um sistema de software que facilita a criação, manutenção e consulta de bancos de dados. Ele fornece uma camada de abstração entre o armazenamento físico dos dados e as aplicações que o utilizam, permitindo aos desenvolvedores interagir com o banco de dados usando linguagens de consulta de alto nível e APIs.

Exemplos populares de DBMS incluem:
- **PostgreSQL**: Um poderoso DBMS relacional de código aberto conhecido por sua confiabilidade, robustez de recursos e desempenho.
- **MySQL**: Um DBMS relacional de código aberto amplamente utilizado, popular para aplicações web e sistemas de gestão de conteúdo.
- **Oracle Database**: Um DBMS relacional comercial usado em muitas aplicações empresariais de larga escala.
- **Microsoft SQL Server**: Um DBMS relacional comercial desenvolvido pela Microsoft, comumente usado em ambientes baseados em Windows.

Estes sistemas fornecem ferramentas e interfaces para a criação e gestão de bancos de dados, execução de consultas, e garantia da integridade dos dados. Eles também oferecem funcionalidades como gestão de transações, controle de concorrência, e mecanismos de backup e recuperação para garantir a confiabilidade e consistência dos dados.

### Vocabulário

- **Persistência de Dados**: A propriedade dos dados que garante que eles sobrevivem além do escopo do processo que os criou. No contexto de bancos de dados, persistência significa que os dados são armazenados em um meio de armazenamento estável e podem ser acessados ​​e recuperados mesmo após a aplicação ou sistema que os criou ter sido encerrado.
- **Consulta**: Um pedido de dados ou informações de um banco de dados. As consultas são normalmente escritas em uma linguagem de consulta especializada, como SQL (Structured Query Language), e são usadas para recuperar, inserir, atualizar ou excluir dados do banco de dados.
- **API (Interface de Programação de Aplicações)**: Um conjunto de regras, protocolos e ferramentas que definem como os componentes de software devem interagir. No contexto de bancos de dados, uma API fornece uma maneira para as aplicações se comunicarem com o DBMS e realizarem operações no banco de dados.

## 2. Bancos de Dados Relacionais

Um banco de dados relacional é um tipo de banco de dados que organiza dados em uma ou mais tabelas (também chamadas de relações) com base no modelo relacional proposto por E.F. Codd em 1970. O modelo relacional fornece uma base matemática para representar e manipular dados de maneira estruturada e consistente.

Em um banco de dados relacional, cada tabela consiste em um conjunto de linhas (também conhecidas como tuplas ou registros) e colunas (também chamadas de atributos ou campos). As linhas representam instâncias individuais de uma entidade, enquanto as colunas definem os atributos ou propriedades dessa entidade.

O aspecto "relacional" desses bancos de dados vem da capacidade de estabelecer relações entre tabelas com base em atributos comuns. Isso permite a criação de estruturas de dados complexas e permite capacidades de consulta poderosas.

### Componentes-chave de um Banco de Dados Relacional:

1. **Tabelas**: As tabelas são as principais estruturas para armazenar dados em um banco de dados

Estruturas 'ta.

   Características de uma chave estrangeira:
   - Integridade referencial: Os valores da chave estrangeira devem corresponder aos valores da chave primária existentes na tabela referenciada.
   - Ações em cascata: As chaves estrangeiras podem definir ações em cascata, como atualizações ou exclusões em cascata, para manter a consistência dos dados quando ocorrem alterações na tabela referenciada.

   Por exemplo, numa tabela de Matrículas que conecta Estudantes e Cursos, a coluna student_id seria uma chave estrangeira referenciando a chave primária da tabela Estudantes, e a coluna course_id seria uma chave estrangeira referenciando a chave primária da tabela Cursos.

### Vocabulário

- **Integridade Referencial**: Uma restrição que garante a consistência e validade das relações de dados entre tabelas. Requer que os valores da chave estrangeira em uma tabela correspondam aos valores da chave primária existentes na tabela referenciada.
- **Chave Candidata**: Uma coluna ou conjunto de colunas que poderiam potencialmente servir como a chave primária para uma tabela. As chaves candidatas satisfazem os requisitos de unicidade e não nulidade de uma chave primária.
- **Chave Composta**: Uma chave primária que consiste em várias colunas. As chaves compostas são usadas quando uma única coluna não é suficiente para identificar de forma única os registros numa tabela.
- **Chave Surrogate**: Uma chave artificial gerada pelo sistema do banco de dados para servir como a chave primária para uma tabela. As chaves surrogate são frequentemente usadas quando não existe uma chave candidata natural ou quando o uso de uma chave natural seria impraticável.

## 4. Diagramas de Entidade-Relacionamento (ER)

Os diagramas de Entidade-Relacionamento (ER) são ferramentas visuais usadas para representar a estrutura e as relações de um banco de dados. Eles fornecem uma visão de alto nível do esquema do banco de dados e ajudam a projetar, comunicar e entender o design do banco de dados.

Componentes chave dos diagramas ER:

1. **Entidades**: As entidades são os principais objetos ou conceitos no sistema do banco de dados. Elas são representadas como retângulos no diagrama ER e correspondem às tabelas no banco de dados físico. Exemplos de entidades incluem Estudantes, Cursos e Funcionários.

2. **Atributos**: Os atributos são as propriedades ou características de uma entidade. Eles são representados como óvalos conectados ao retângulo da entidade no diagrama ER. Os atributos correspondem às colunas na tabela do banco de dados físico. Por exemplo, a entidade Estudantes pode ter atributos como student_id, nome e idade.

3. **Relações**: As relações descrevem como as entidades estão relacionadas entre si. Elas são representadas como diamantes no diagrama ER, conectando as entidades participantes. As relações podem ser de um-para-um, de um-para-muitos ou de muitos-para-muitos. Por exemplo, a relação "matricula-se em" entre Estudantes e Cursos indica que um estudante pode se matricular em vários cursos, e um curso pode ter vários estudantes.

4. **Cardinalidade**: A cardinalidade especifica o número de instâncias de uma entidade que podem estar relacionadas ao número de instâncias de outra entidade. É representada por símbolos ou anotações perto do diamante da relação. Os tipos comuns de cardinalidade incluem:
   - Um-para-um (1:1): Cada instância de uma entidade está relacionada a no máximo uma instância da outra entidade.
   - Um-para-muitos (1:N): Cada instância de uma entidade pode estar relacionada a várias instâncias da outra entidade, mas cada instância da outra entidade está relacionada a no máximo uma instância da primeira entidade.
   - Muitos-para-muitos (M:N): Cada instância de uma entidade pode estar relacionada a várias instâncias da outra entidade, e vice-versa.

### Vocabulário

- **Entidade Fraca**: Uma entidade que depende de outra entidade para sua existência. Uma entidade fraca não tem uma chave primária própria e é identificada por uma combina