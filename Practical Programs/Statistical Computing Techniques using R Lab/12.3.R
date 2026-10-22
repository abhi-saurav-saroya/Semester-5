data(iris)

x1 <- iris$Sepal.Length[iris$Species == "setosa"]
x2 <- iris$Sepal.Length[iris$Species == "versicolor"]

n1 <- length(x1)
n2 <- length(x2)

mu1 <- mean(x1)
mu2 <- mean(x2)

sigma1 <- 0.8
sigma2 <- 0.8

# Calculate Z-statistic
z <- (mu1 - mu2) /
  sqrt(sigma1^2/n1 + sigma2^2/n2)

# Two-tailed p-value
p_value <- 2 * pnorm(-abs(z))

cat("Mean of Setosa =", mu1, "\n")
cat("Mean of Versicolor =", mu2, "\n")
cat("Z-statistic =", z, "\n")
cat("P-value =", p_value, "\n")

if (p_value < 0.05) {
  cat("Reject the null hypothesis")
} else {
  cat("Do not reject the null hypothesis")
}
