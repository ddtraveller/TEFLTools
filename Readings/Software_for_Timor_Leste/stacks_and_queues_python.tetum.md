'# Stacks no Queues: Estrutura Dadus Esensiál ba Prosesamentu Sekuensial

## Introdusaun

Stacks no queues mak estrutura dadus fundamentál iha siénsia komputadór nian ne'ebé trata koleksaun husi elementu sira iha orden espesífiku. Maibé, maski sira hotu uza ba armazena no hetan dadus, sira la hanesan iha orden ne'ebé elementu sira hetan. Komprensaun estrutura sira ne'e importante tebes ba resolve problema komputasionál sira no implementa algoritmu ne'ebé efisiente.

## Stacks

Stack mak estrutura dadus ida ne'ebé uza prinsípiu Last-In-First-Out (LIFO). Signifika katak elementu ikus ne'ebé taka ba stack sei sai primeiru liu.

### Estrutura no Operasaun

1. **Push**: Aumenta elementu ida ba leten stack.
2. **Pop**: Hasai elementu iha leten stack.
3. **Peek** (ka Top): Haree elementu iha leten stack la'ós atu hasai.
4. **isEmpty**: Verifika se stack mamuk ka lae.

### Kompleksidade Tempu

Operasaun báziku hotu (push, pop, peek, isEmpty) iha kompleksidade tempu O(1) - tempu konstante.

### Aplikasaun

1. **Function Call Stack**: Uza husi lingua programasaun atu kontrola funsaun sira ne'ebé bolu no variável lokál.
2. **Expression Evaluation**: Uza iha kalkuladora ba avalia espresaun aritmétika.
3. **Undo Mechanism**: Implementa funsaun undo iha aplikasaun sira.
4. **Backtracking Algorithms**: Uza iha algoritmu resolve labirintu no inteligénsia artifisiál iha jogu.
5. **Balanced Parentheses Checking**: Verifika se parénteses iha espresaun balansu ka lae.

## Queues

Queue mak estrutura dadus ida ne'ebé uza prinsípiu First-In-First-Out (FIFO). Signifika katak elementu primeiru ne'ebé taka ba queue sei sai primeiru liu.

### Estrutura no Operasaun

1. **Enqueue**: Aumenta elementu ida ba ikus queue.
2. **Dequeue**: Hasai elementu iha oin queue.
3. **Front**: Haree elementu iha oin queue la'ós atu hasai.
4. **isEmpty**: Verifika se queue mamuk ka lae.

### Kompleksidade Tempu

Operasaun báziku hotu (enqueue, dequeue, front, isEmpty) iha kompleksidade tempu O(1) - tempu konstante.

### Aplikasaun

1. **Task Scheduling**: Jere prosesu iha sistemas operasaun.
2. **Breadth-First Search**: Uza iha algoritmu grafo ba traversa ka buka estrutura dadus hanesan ai-hun ka grafo.
3. **Print Queue Management**: Jere servisu imprime iha printer spooler.
4. **Keyboard Buffer**: Jere tekladu iha buffer tekladu.
5. **Web Server Request Management**: Jere pedidu sira ne'ebé mai husi web server.

## Komparasaun: Stacks vs Queues

Wainhira kompara stacks ho queues, ne'e hotu estrutura dadus lineár maibé la hanesan iha padraun aksesu:

- **Stacks** útil bainhira ita presiza halo servisu ho dadus iha orden reversu ka bainhira ita presiza kontrola estadu durante operasaun rekursivu.
- **Queues** di'ak liu ba jere dadus ne'ebé presiza prosesa tuir orden ne'ebé simu, hanesan iha situsaun ne'ebé iha fila ka prosesamentu sekuensial.

## Konsiderasaun Implementasaun

Stacks no queues bele implementa uza arrays ka linked lists:

- **Array Implementation**: Oferece aksesu ne'ebé lais maibé iha tamañu fixu.
- **Linked List Implementation**: Permite tamañu dinám