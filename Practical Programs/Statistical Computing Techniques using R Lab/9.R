# Parameters of the binomial distribution
n <- 20
p <- 0.4

# Possible numbers of successes
x <- 0:n

# Probability Mass Function (PMF)
pmf <- dbinom(x, size = n, prob = p)

# Cumulative Distribution Function (CDF)
cdf <- pbinom(x, size = n, prob = p)

# Display the probability table
result <- data.frame(
  x = x,
  PMF = pmf,
  CDF = cdf
)
print(result)

# Draw both graphs side by side
par(mfrow = c(1, 2))

# Graph 1: PMF
plot(x, pmf,
     type = "h",
     lwd = 3,
     col = "blue",
     main = "Binomial PMF",
     xlab = "Number of successes (x)",
     ylab = "P(X = x)")
points(x, pmf, pch = 16, col = "blue")

# Graph 2: CDF
plot(x, cdf,
     type = "s",
     lwd = 2,
     col = "red",
     main = "Binomial CDF",
     xlab = "Number of successes (x)",
     ylab = "P(X <= x)",
     ylim = c(0, 1))
