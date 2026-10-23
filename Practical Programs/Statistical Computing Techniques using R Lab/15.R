data(PlantGrowth)

# Select two groups
group1 <- PlantGrowth$weight[PlantGrowth$group == "ctrl"]
group2 <- PlantGrowth$weight[PlantGrowth$group == "trt1"]

# Perform F-test
result <- var.test(group1, group2)

# Display the F-statistic
cat("F-statistic =", result$statistic, "\n")
cat("Degrees of Freedom =", result$parameter[1], "and", result$parameter[2], "\n")
cat("P-value =", result$p.value, "\n")

# Decision at 5% significance level
if (result$p.value < 0.05) {
  cat("Reject the null hypothesis")
} else {
  cat("Do not reject the null hypothesis")
}