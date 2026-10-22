data(iris)

x <- iris$Sepal.Length
mu0 <- 5.8
sigma <- 0.8
n <- length(x)

# Calculate sample mean and Z-statistic
x_bar <- mean(x)
z <- (x_bar - mu0) / (sigma / sqrt(n))

# Calculate two-tailed p-value
p_value <- 2 * pnorm(-abs(z))

cat("Sample Mean =", x_bar, "\n")
cat("Z-statistic =", z, "\n")
cat("P-value =", p_value, "\n")

if (p_value < 0.05) {
  cat("Reject the null hypothesis")
} else {
  cat("Do not reject the null hypothesis")
}
