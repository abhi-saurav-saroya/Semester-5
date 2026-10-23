data(mtcars)

# Take two variables
x <- mtcars$wt
y <- mtcars$mpg

# Calculate means
xbar <- mean(x)
ybar <- mean(y)

# Regression coefficients
b_yx <- cov(x, y) / var(x)
b_xy <- cov(x, y) / var(y)

# Intercepts
a_yx <- ybar - b_yx * xbar
a_xy <- xbar - b_xy * ybar

# Display coefficients
cat("Regression coefficient of Y on X =", b_yx, "\n")
cat("Regression coefficient of X on Y =", b_xy, "\n")

# Display regression equations
cat("Y on X: Y =", a_yx, "+", b_yx, "* X\n")
cat("X on Y: X =", a_xy, "+", b_xy, "* Y\n")

# Plot both regression lines
par(mfrow = c(1, 2))

# Regression of Y on X
plot(x, y,
     main = "Regression of MPG on Weight",
     xlab = "Weight (1000 lbs)",
     ylab = "Mileage (MPG)",
     pch = 19,
     col = "blue")

abline(a = a_yx, b = b_yx, col = "red", lwd = 2)

# Regression of X on Y
plot(y, x,
     main = "Regression of Weight on MPG",
     xlab = "Mileage (MPG)",
     ylab = "Weight (1000 lbs)",
     pch = 19,
     col = "blue")

abline(a = a_xy, b = b_xy, col = "red", lwd = 2)