numbers <- c(10, 20, 30, 40, 50)

# Basic mathematical functions
cat("Sum:", sum(numbers), "\n")
cat("Mean:", mean(numbers), "\n")
cat("Minimum:", min(numbers), "\n")
cat("Maximum:", max(numbers), "\n")
cat("Range:", range(numbers), "\n")
cat("Length:", length(numbers), "\n")

# Mathematical functions
cat("Absolute value:", abs(-25), "\n")
cat("Square root:", sqrt(25), "\n")
cat("Round:", round(12.5678, 2), "\n")
cat("Ceiling:", ceiling(12.3), "\n")
cat("Floor:", floor(12.8), "\n")

# Statistical functions
cat("Median:", median(numbers), "\n")
cat("Standard deviation:", sd(numbers), "\n")
cat("Variance:", var(numbers), "\n")

# Sorting functions
cat("Sorted values:", sort(numbers), "\n")
cat("Reverse sorted values:", sort(numbers, decreasing = TRUE), "\n")

# Sequence function
cat("Sequence:", seq(1, 10, by = 2), "\n")

# Repetition function
cat("Repeat:", rep(5, 4), "\n")

# Type checking functions
x <- 10
cat("Is numeric:", is.numeric(x), "\n")
cat("Is character:", is.character(x), "\n")
cat("Is integer:", is.integer(x), "\n")

# Conversion functions
y <- "100"
cat("Character to numeric:", as.numeric(y), "\n")

# Other useful functions
cat("Class:", class(numbers), "\n")
cat("Number of elements:", length(numbers), "\n")