data(mtcars)

# Define events:
# A = automatic transmission (am = 0)
# B = 8 cylinders (cyl = 8)

# Calculate prior probability P(A)
P_A <- mean(mtcars$am == 0)

# Calculate likelihood P(B | A)
P_B_given_A <- mean(mtcars$cyl[mtcars$am == 0] == 8)

# Calculate evidence P(B)
P_B <- mean(mtcars$cyl == 8)

# Apply Bayes' theorem
P_A_given_B <- (P_B_given_A * P_A) / P_B

# Display results
cat("Prior P(A):", P_A, "\n")
cat("Likelihood P(B|A):", P_B_given_A, "\n")
cat("Evidence P(B):", P_B, "\n")
cat("Posterior P(A|B):", P_A_given_B, "\n")
cat("Posterior percentage:", P_A_given_B * 100, "%\n")

