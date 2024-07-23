'# R no RStudio: Guia Instalasaun no Cheat Sheet Komprehensivu

## Parte I: Guia Instalasaun

### Instala R no RStudio iha Windows

1. **Instala R:**
   - Bá ba https://cran.r-project.org/
   - Klik iha "Download R ba Windows"
   - Klik iha "baze"
   - Klik iha link download ba versaun foun liu husi R
   - Halao ficheiro .exe ne'ebé download ona no tuir wizard instalasaun nian

2. **Instala RStudio:**
   - Bá ba https://www.rstudio.com/products/rstudio/download/
   - Rolu kraik ba "RStudio Desktop"
   - Klik iha "Download RStudio Desktop"
   - Halao ficheiro .exe ne'ebé download ona no tuir wizard instalasaun nian

### Instala R no RStudio iha Mac

1. **Instala R:**
   - Bá ba https://cran.r-project.org/
   - Klik iha "Download R ba macOS"
   - Klik iha ficheiro .pkg ne'ebé apropriadu ba ita-nia versaun macOS
   - Abre ficheiro .pkg ne'ebé download ona no tuir wizard instalasaun nian

2. **Instala RStudio:**
   - Bá ba https://www.rstudio.com/products/rstudio/download/
   - Rolu kraik ba "RStudio Desktop"
   - Klik iha "Download RStudio Desktop"
   - Abre ficheiro .dmg ne'ebé download ona
   - Arrasta ikon RStudio ba pasta Aplicasaun ita-nia

## Parte II: R Cheat Sheet

### Operasaun Báziku

```r
# Atribuisaun
x <- 5
y = 10  # Mós servisu, maibé '<-' maka preferidu

# Aritmétika báziku
a <- 10 + 5  # Adisaun
b <- 10 - 5  # Subtrasaun
c <- 10 * 5  # Multiplikasaun
d <- 10 / 5  # Divizaun
e <- 10 ^ 2  # Eksponensiasaun
f <- 10 %% 3 # Modulus (restu)

# Operador lójiku
g <- LOLON & SALA  # NO
h <- LOLON | SALA  # KA
i <- !LOLON        # LA
```

### Tipu Dadus

```r
# Numériku
num <- 42.5

# Intejeru
int <- 42L

# Karater
char <- "Olá, Mundo!"

# Lójiku
log <- LOLON

# Fator
fac <- factor(c("sin", "lae", "sin", "karik"))

# Data
date <- as.Date("2023-06-24")
```

### Estrutura Dadus

```r
# Vetor
vec <- c(1, 2, 3, 4, 5)

# Lista
lst <- list(a = 1, b = "olá", c = LOLON)

# Matriz
mat <- matrix(1:9, nrow = 3, ncol = 3)

# Frame dadus
df <- data.frame(
  id = 1:3,
  naran = c("Alice", "Bob", "Charlie"),
  pontuasaun = c(85, 92, 78)
)

# Array
arr <- array(1:24, dim = c(2, 3, 4))
```

### Estrutura Kontrolu

```r
# Se-seluk
if (x > 0) {
  print("Pozitivu")
} else if (x < 0) {
  print("Negativu")
} else {
  print("Zero")
}

# Loop ba
for (i in 1:5) {
  print(i)
}

# Loop enkuantu
while (x < 10) {
  x <- x + 1
}

# Definisaun funsaun
my_function <- function(arg1, arg2) {
  result <- arg1 + arg2
  return(result)
}
```

### Manipulasaun Dadus

```r
# Subkonjuntu
vec[2]  # Elementu segundu husi vetor
df$naran  # 'naran' koluna husi frame dadus
mat[1, 2]  # Elementu iha liña