# Load the built-in dataset
data(mtcars)

# Display the dataset
print(head(mtcars))

# 1. Bar Chart - Number of Cars by Cylinders
cylinder_count <- table(mtcars$cyl)

barplot(
  cylinder_count,
  names.arg = names(cylinder_count),
  main = "Cars by Number of Cylinders",
  xlab = "Number of Cylinders",
  ylab = "Number of Cars"
)

# 2. Histogram - Miles per Gallon
hist(
  mtcars$mpg,
  main = "Distribution of MPG",
  xlab = "Miles per Gallon",
  ylab = "Frequency"
)

# 3. Boxplot - MPG
boxplot(
  mtcars$mpg,
  main = "Boxplot of MPG",
  ylab = "Miles per Gallon"
)

# 4. Scatter Plot - MPG vs Weight
plot(
  mtcars$wt,
  mtcars$mpg,
  main = "MPG vs Weight",
  xlab = "Weight",
  ylab = "Miles per Gallon",
  pch = 19
)

# 5. Pie Chart - Transmission Type
pie(
  table(mtcars$am),
  labels = c("Automatic", "Manual"),
  main = "Transmission Types"
)

# 6. Line Chart - MPG of Cars
plot(
  mtcars$mpg,
  type = "o",
  main = "MPG of Cars",
  xlab = "Car Number",
  ylab = "Miles per Gallon"
)

# 7. Bar Chart - Horsepower of Cars
barplot(
  mtcars$hp,
  names.arg = rownames(mtcars),
  las = 2,
  main = "Horsepower of Cars",
  xlab = "Cars",
  ylab = "Horsepower"
)
