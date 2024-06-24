# Load required libraries
library(tidyverse)
library(lubridate)

# Create sample data
data <- tibble(
  Date = seq(as.Date("2023-01-01"), as.Date("2023-01-07"), by = "days"),
  Municipality = c("Dili", "Baucau", "Aileu", "Dili", "Ermera", "Baucau", "Dili"),
  Product = c("Rice", "Corn", "Coffee", "Rice", "Coffee", "Corn", "Coffee"),
  Sales = c(100, 150, 80, 120, 90, 130, 70),
  Price = c(1.5, 1.2, 3.0, 1.5, 3.2, 1.3, 3.1)
)

# Display the data
print(data)

# Data cleaning and manipulation
cleaned_data <- data %>%
  mutate(
    CleanProduct = str_to_lower(str_replace_all(Product, "[^[:alpha:]]", "")),
    TotalValue = Sales * Price
  )

print(cleaned_data)

# Pivot table
pivot_table <- cleaned_data %>%
  group_by(Municipality, CleanProduct) %>%
  summarise(TotalSales = sum(Sales)) %>%
  pivot_wider(names_from = CleanProduct, values_from = TotalSales, values_fill = 0)

print(pivot_table)

# Data aggregation
aggregated_data <- cleaned_data %>%
  group_by(Municipality) %>%
  summarise(
    TotalSales = sum(Sales),
    AverageSales = mean(Sales),
    MinPrice = min(Price),
    MaxPrice = max(Price)
  )

print(aggregated_data)

# Data visualization
ggplot(cleaned_data, aes(x = Municipality, y = Sales, fill = Product)) +
  geom_col() +
  labs(title = "Total Sales by Municipality and Product",
       x = "Municipality",
       y = "Total Sales") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Time series analysis
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

# Advanced data manipulation
high_value_sales <- cleaned_data %>%
  filter(TotalValue > 200) %>%
  arrange(desc(TotalValue))

print(high_value_sales)

# Statistical analysis
model <- lm(Sales ~ Price, data = cleaned_data)
summary(model)

# Create a scatter plot with regression line
ggplot(cleaned_data, aes(x = Price, y = Sales)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Sales vs Price with Regression Line",
       x = "Price",
       y = "Sales") +
  theme_minimal()