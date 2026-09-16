library(moments)

data(iris)

cat("6 TOPMOST ROWS OF DATASET:\n")
print(head(iris))

skewness_values <- apply(iris[, 1:4], 2, skewness)
kurtosis_values <- apply(iris[, 1:4], 2, kurtosis)

cat("\nSKEWNESS VALUES OF ALL NUMERIC COLUMNS:\n")
print(skewness_values)
cat("\nKURTOSIS VALUES OF ALL NUMERIC COLUMNS:\n")
print(kurtosis_values)

# Plotting the numerical columns as histograms to check their distributions visually
hist(
  iris$Sepal.Length,
  main = "Distribution of Sepal Length with KDE",
  xlab = "Sepal Length",
  ylab = "Density",
  breaks = 20,
  border = "darkgreen",
  col = "lightgreen",
  ylim = c(0, 0.6),
  xlim = c(4, 8),
  freq = FALSE
)

kde_Sepal.Length <- density(iris$Sepal.Length)

lines(
  kde_Sepal.Length,
  col = "red",
  lwd = 2
)

hist(
  iris$Sepal.Width,
  main = "Distribution of Sepal Width with KDE",
  xlab = "Sepal Width",
  ylab = "Density",
  breaks = 20,
  border = "darkgreen",
  col = "lightgreen",
  ylim = c(0, 1.9),
  xlim = c(2, 4.5),
  freq = FALSE
)

kde_Sepal.Width <- density(iris$Sepal.Width)

lines(
  kde_Sepal.Width,
  col = "red",
  lwd = 2
)

hist(
  iris$Petal.Length,
  main = "Distribution of Petal Length with KDE",
  xlab = "Petal length",
  ylab = "Density",
  breaks = 20,
  border = "darkgreen",
  col = "lightgreen",
  ylim = c(0, 0.6),
  xlim = c(1, 6.9),
  freq = FALSE
)

kde_Petal.Length <- density(iris$Petal.Length)

lines(
  kde_Petal.Length,
  col = "red",
  lwd = 2
)

hist(
  iris$Petal.Width,
  main = "Distribution of Petal Width with KDE",
  xlab = "Petal Width",
  ylab = "Density",
  breaks = 20,
  border = "darkgreen",
  col = "lightgreen",
  ylim = c(0, 2.4),
  xlim = c(0.1, 2.6),
  freq = FALSE
)

kde_Petal_Width <- density(iris$Petal.Width)

lines(
  kde_Petal_Width,
  col = "red",
  lwd = 2
)
