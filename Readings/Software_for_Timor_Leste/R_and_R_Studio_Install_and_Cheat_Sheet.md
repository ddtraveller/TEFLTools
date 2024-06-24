# R and RStudio: Installation Guide and Comprehensive Cheat Sheet

## Part I: Installation Guide

### Installing R and RStudio on Windows

1. **Install R:**
   - Go to https://cran.r-project.org/
   - Click on "Download R for Windows"
   - Click on "base"
   - Click on the download link for the latest version of R
   - Run the downloaded .exe file and follow the installation wizard

2. **Install RStudio:**
   - Go to https://www.rstudio.com/products/rstudio/download/
   - Scroll down to "RStudio Desktop"
   - Click on "Download RStudio Desktop"
   - Run the downloaded .exe file and follow the installation wizard

### Installing R and RStudio on Mac

1. **Install R:**
   - Go to https://cran.r-project.org/
   - Click on "Download R for macOS"
   - Click on the .pkg file appropriate for your macOS version
   - Open the downloaded .pkg file and follow the installation wizard

2. **Install RStudio:**
   - Go to https://www.rstudio.com/products/rstudio/download/
   - Scroll down to "RStudio Desktop"
   - Click on "Download RStudio Desktop"
   - Open the downloaded .dmg file
   - Drag the RStudio icon to your Applications folder

## Part II: R Cheat Sheet

### Basic Operations

```r
# Assignment
x <- 5
y = 10  # Also works, but '<-' is preferred

# Basic arithmetic
a <- 10 + 5  # Addition
b <- 10 - 5  # Subtraction
c <- 10 * 5  # Multiplication
d <- 10 / 5  # Division
e <- 10 ^ 2  # Exponentiation
f <- 10 %% 3 # Modulus (remainder)

# Logical operators
g <- TRUE & FALSE  # AND
h <- TRUE | FALSE  # OR
i <- !TRUE         # NOT
```

### Data Types

```r
# Numeric
num <- 42.5

# Integer
int <- 42L

# Character
char <- "Hello, World!"

# Logical
log <- TRUE

# Factor
fac <- factor(c("yes", "no", "yes", "maybe"))

# Date
date <- as.Date("2023-06-24")
```

### Data Structures

```r
# Vector
vec <- c(1, 2, 3, 4, 5)

# List
lst <- list(a = 1, b = "hello", c = TRUE)

# Matrix
mat <- matrix(1:9, nrow = 3, ncol = 3)

# Data frame
df <- data.frame(
  id = 1:3,
  name = c("Alice", "Bob", "Charlie"),
  score = c(85, 92, 78)
)

# Array
arr <- array(1:24, dim = c(2, 3, 4))
```

### Control Structures

```r
# If-else
if (x > 0) {
  print("Positive")
} else if (x < 0) {
  print("Negative")
} else {
  print("Zero")
}

# For loop
for (i in 1:5) {
  print(i)
}

# While loop
while (x < 10) {
  x <- x + 1
}

# Function definition
my_function <- function(arg1, arg2) {
  result <- arg1 + arg2
  return(result)
}
```

### Data Manipulation

```r
# Subsetting
vec[2]  # Second element of vector
df$name  # 'name' column of data frame
mat[1, 2]  # Element in first row, second column of matrix

# Filtering
df[df$score > 80, ]  # Rows where score is greater than 80

# Sorting
sort(vec)  # Sort vector
df[order(df$score), ]  # Sort data frame by score

# Applying functions
apply(mat, 1, sum)  # Sum each row of matrix
lapply(lst, length)  # Apply length() to each element of list
```

### Data Import/Export

```r
# Reading data
df_csv <- read.csv("file.csv")
df_txt <- read.table("file.txt", header = TRUE)
df_excel <- readxl::read_excel("file.xlsx")

# Writing data
write.csv(df, "output.csv")
write.table(df, "output.txt", sep = "\t")
writexl::write_xlsx(df, "output.xlsx")
```

### Basic Statistics

```r
mean(vec)  # Mean
median(vec)  # Median
sd(vec)  # Standard deviation
var(vec)  # Variance
cor(x, y)  # Correlation
summary(df)  # Summary statistics for data frame
```

### Plotting

```r
# Base R plotting
plot(x, y)
hist(vec)
boxplot(df$score ~ df$name)

# ggplot2
library(ggplot2)
ggplot(df, aes(x = name, y = score)) +
  geom_bar(stat = "identity")
```

### Working with Packages

```r
# Installing packages
install.packages("dplyr")

# Loading packages
library(dplyr)

# Using specific functions from packages without loading
dplyr::filter(df, score > 80)
```

### Useful Functions

```r
# Getting help
?mean  # Help for mean function
help(package = "dplyr")  # Help for dplyr package

# Workspace management
ls()  # List objects in workspace
rm(x)  # Remove object 'x'
rm(list = ls())  # Clear workspace

# Working directory
getwd()  # Get working directory
setwd("path/to/directory")  # Set working directory

# Viewing data
head(df)  # First 6 rows
tail(df)  # Last 6 rows
View(df)  # Open data viewer
str(df)  # Structure of object
```

This cheat sheet covers the basics of R programming and should serve as a quick reference for common operations. Remember that R has many more functions and capabilities, especially when you start using additional packages. As you become more familiar with R, you'll discover more advanced techniques and functions suited to your specific needs.