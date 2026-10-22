# Generate x values from 0 to 20
x <- seq(0, 20, by = 1)

# Calculate PDF and CDF
pdf <- dnorm(x, mean = 10, sd = 3)
cdf <- pnorm(x, mean = 10, sd = 3)

# Display the values
result <- data.frame(x, PDF = pdf, CDF = cdf)
print(result)

par(mfrow = c(1, 2))

# Plot PDF
plot(x, pdf, type = "l",
     main = "PDF of Normal Distribution",
     xlab = "x", ylab = "Density",
     col = "blue", lwd = 2)

# Plot CDF
plot(x, cdf, type = "l",
     main = "CDF of Normal Distribution",
     xlab = "x", ylab = "Cumulative Probability",
     col = "red", lwd = 2)
