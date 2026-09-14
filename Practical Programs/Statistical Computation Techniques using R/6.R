x <- c(10, 80, 93, 56, 36, 6, 93, 72, 62, 43)

mean_value <- mean(x)
median_value <- median(x)
sd_value <- sd(x)
quartiles <- quantile(x)

cat("Given set of observations:", x, "\n\n")

cat("Number of Observations: ", length(x), "\n")
cat("Mean: ", mean(x), "\n")
cat("Median: ", median(x), "\n")
cat("Standard Deviation: ", sd(x), "\n")
cat("Quartiles:\n")
print(quartiles)