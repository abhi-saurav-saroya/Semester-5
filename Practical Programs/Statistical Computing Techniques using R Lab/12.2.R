data(iris)

n <- nrow(iris)
x <- sum(iris$Species == "setosa")
p0 <- 0.30

# Sample proportion
p_hat <- x / n

# Calculate Z-statistic
z <- (p_hat - p0) / sqrt(p0 * (1 - p0) / n)

# Calculate two-tailed p-value
p_value <- 2 * pnorm(-abs(z))

cat("Number of Setosa flowers =", x, "\n")
cat("Sample Proportion =", p_hat, "\n")
cat("Z-statistic =", z, "\n")
cat("P-value =", p_value, "\n")

if (p_value < 0.05) {
  cat("Reject the null hypothesis")
} else {
  cat("Do not reject the null hypothesis")
}
