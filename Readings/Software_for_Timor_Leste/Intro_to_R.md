# Understanding R: A Guide to Usage and Script Analysis

## Introduction to R

R is a powerful programming language and environment for statistical computing and graphics. It provides a wide variety of statistical and graphical techniques, including linear and nonlinear modeling, time-series analysis, classification, clustering, and more.

## Getting Started with R

1. **Installation**: Download and install R from the official CRAN website (https://cran.r-project.org/). It's also recommended to install RStudio, an integrated development environment (IDE) for R.

2. **Basic Operations**: R can be used as a calculator. For example:
   ```r
   5 + 3
   10 * 2
   ```

3. **Variable Assignment**: Use `<-` or `=` to assign values to variables:
   ```r
   x <- 10
   y = 20
   ```

4. **Data Types**: R has various data types including numeric, character, logical, and factor.

5. **Data Structures**: Common structures include vectors, lists, matrices, and data frames.

6. **Functions**: R has many built-in functions. You can also create your own:
   ```r
   mean(c(1, 2, 3, 4, 5))
   ```

## Understanding the Script

Now, let's break down the script and explain its components:

### 1. Loading Libraries

```r
library(tidyverse)
library(lubridate)
```
These lines load the tidyverse collection of packages (which includes ggplot2, dplyr, and tidyr) and lubridate for date manipulation. The `library()` function is used to load packages in R.

### 2. Creating Sample Data

```r
data <- tibble(
  Date = seq(as.Date("2023-01-01"), as.Date("2023-01-07"), by = "days"),
  Municipality = c("Dili", "Baucau", "Aileu", "Dili", "Ermera", "Baucau", "Dili"),
  Product = c("Rice", "Corn", "Coffee", "Rice", "Coffee", "Corn", "Coffee"),
  Sales = c(100, 150, 80, 120, 90, 130, 70),
  Price = c(1.5, 1.2, 3.0, 1.5, 3.2, 1.3, 3.1)
)
```
This creates a tibble (a modern take on data frames) with sample data. The `seq()` function generates a sequence of dates, and `c()` combines values into a vector.

### 3. Data Cleaning and Manipulation

```r
cleaned_data <- data %>%
  mutate(
    CleanProduct = str_to_lower(str_replace_all(Product, "[^[:alpha:]]", "")),
    TotalValue = Sales * Price
  )
```
This uses dplyr's `mutate()` function to add new columns. `str_to_lower()` and `str_replace_all()` are stringr functions for string manipulation. The `%>%` is the pipe operator, which passes the result of one function to the next.

### 4. Creating a Pivot Table

```r
pivot_table <- cleaned_data %>%
  group_by(Municipality, CleanProduct) %>%
  summarise(TotalSales = sum(Sales)) %>%
  pivot_wider(names_from = CleanProduct, values_from = TotalSales, values_fill = 0)
```
This creates a pivot table using dplyr and tidyr functions. `group_by()` groups the data, `summarise()` calculates the sum of sales, and `pivot_wider()` reshapes the data.

### 5. Data Aggregation

```r
aggregated_data <- cleaned_data %>%
  group_by(Municipality) %>%
  summarise(
    TotalSales = sum(Sales),
    AverageSales = mean(Sales),
    MinPrice = min(Price),
    MaxPrice = max(Price)
  )
```
This aggregates the data by municipality, calculating various summary statistics.

### 6. Data Visualization

```r
ggplot(cleaned_data, aes(x = Municipality, y = Sales, fill = Product)) +
  geom_col() +
  labs(title = "Total Sales by Municipality and Product",
       x = "Municipality",
       y = "Total Sales") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```
This creates a bar plot using ggplot2. `ggplot()` initializes the plot, `aes()` sets the aesthetics, `geom_col()` adds the bars, and additional functions customize the appearance.

### 7. Time Series Analysis

```r
time_series <- cleaned_data %>%
  group_by(Date) %>%
  summarise(TotalSales = sum(Sales))

ggplot(time_series, aes(x = Date, y = TotalSales)) +
  geom_line() +
  geom_point() +
  labs(title = "Daily Total Sales",
       x = "Date",
       y = "Total Sales") +
  theme_minimal()
```
This creates a time series plot. The data is first aggregated by date, then plotted using `geom_line()` and `geom_point()`.

### 8. Advanced Data Manipulation

```r
high_value_sales <- cleaned_data %>%
  filter(TotalValue > 200) %>%
  arrange(desc(TotalValue))
```
This filters the data for high-value sales and arranges it in descending order of total value.

### 9. Statistical Analysis

```r
model <- lm(Sales ~ Price, data = cleaned_data)
summary(model)
```
This performs a linear regression of Sales on Price using the `lm()` function, and `summary()` provides a detailed summary of the model.

### 10. Scatter Plot with Regression Line

```r
ggplot(cleaned_data, aes(x = Price, y = Sales)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Sales vs Price with Regression Line",
       x = "Price",
       y = "Sales") +
  theme_minimal()
```
This creates a scatter plot with a regression line. `geom_smooth()` adds the regression line.

## Conclusion

This script demonstrates the power and elegance of R for data manipulation, visualization, and analysis. It showcases the seamless integration of various operations, from data cleaning to statistical modeling, all within a coherent and readable framework. The tidyverse packages, particularly dplyr and ggplot2, provide an intuitive grammar for data manipulation and visualization, making complex operations accessible and expressive.

By understanding and experimenting with this script, users can gain proficiency in R and leverage its capabilities for their own data analysis projects.