data(airquality)

# Remove missing values
ozone <- na.omit(airquality$Ozone)

# Sample size
n <- length(ozone)

# Sample mean
xbar <- mean(ozone)

# Assume known population standard deviation
sigma <- 30

# Confidence level
confidence_level <- 0.95

# Z value for 95% confidence interval
z <- qnorm(1 - (1 - confidence_level) / 2)

# Margin of error
margin_error <- z * sigma / sqrt(n)

# Confidence interval
lower <- xbar - margin_error
upper <- xbar + margin_error

# Display results
cat("Sample Mean =", xbar, "\n")
cat("Sample Size =", n, "\n")
cat("Confidence Interval = (", lower, ",", upper, ")\n")