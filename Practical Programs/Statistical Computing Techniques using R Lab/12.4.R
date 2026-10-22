data(Titanic)

# Convert the table into a data frame
d <- as.data.frame(Titanic)

# Total passengers by sex
totals <- aggregate(Freq ~ Sex, data = d, sum)

# Number of survivors by sex
survivors <- aggregate(
  Freq ~ Sex,
  data = subset(d, Survived == "Yes"),
  sum
)

n1 <- totals$Freq[totals$Sex == "Female"]
n2 <- totals$Freq[totals$Sex == "Male"]

x1 <- survivors$Freq[survivors$Sex == "Female"]
x2 <- survivors$Freq[survivors$Sex == "Male"]

p1 <- x1 / n1
p2 <- x2 / n2

# Pooled proportion
p_pool <- (x1 + x2) / (n1 + n2)

# Calculate Z-statistic
se <- sqrt(p_pool * (1 - p_pool) *
             (1/n1 + 1/n2))

z <- (p1 - p2) / se

# Two-tailed p-value
p_value <- 2 * pnorm(-abs(z))

cat("Female Survival Proportion =", p1, "\n")
cat("Male Survival Proportion =", p2, "\n")
cat("Z-statistic =", z, "\n")
cat("P-value =", p_value, "\n")

if (p_value < 0.05) {
  cat("Reject the null hypothesis")
} else {
  cat("Do not reject the null hypothesis")
}