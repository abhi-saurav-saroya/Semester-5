data(HairEyeColor)

# Convert the table into a data frame
d <- as.data.frame(HairEyeColor)

# Create a contingency table of hair color and eye color
hair_eye <- xtabs(Freq ~ Hair + Eye, data = d)

# Perform Chi-Square Test of Independence
result <- chisq.test(hair_eye)
print(hair_eye)

# Display the Chi-Square statistic
cat("Chi-Square Statistic =", result$statistic, "\n")

# Display degrees of freedom
cat("Degrees of Freedom =", result$parameter, "\n")

# Display p-value
cat("P-value =", result$p.value, "\n")

# Decision at 5% significance level
if (result$p.value < 0.05) {
  cat("Reject the null hypothesis")
} else {
  cat("Do not reject the null hypothesis")
}