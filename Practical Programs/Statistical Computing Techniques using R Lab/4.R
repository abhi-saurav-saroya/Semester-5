# Create sample data
students <- data.frame(
  Name = c("Abhi", "Saurav", "Mahira", "Shyam", "Shweta", "Akash", "Ibrahim", "Pritam"),
  Marks = c(85, 75, 90, 65, 80, 87, 23, 45),
  Hours = c(5, 3, 6, 2, 4, 3, 1, 2)
)

# Display the data
print(students)


# 1. Histogram
hist(
  students$Marks,
  main = "Histogram of Marks",
  xlab = "Marks"
)


# 2. Boxplot
boxplot(
  students$Marks,
  main = "Boxplot of Marks",
  ylab = "Marks"
)


# 3. Bar Plot
barplot(
  students$Marks,
  names.arg = students$Name,
  main = "Marks of Students",
  xlab = "Students",
  ylab = "Marks"
)


# 4. Pie Chart
pie(students$Marks,
    labels = students$Name,
    main = "Marks Distribution")


# 5. Scatter Plot
plot(
  students$Hours,
  students$Marks,
  main = "Study Hours vs Marks",
  xlab = "Study Hours",
  ylab = "Marks"
)


# 6. Line Plot
plot(
  students$Marks,
  type = "o",
  main = "Marks Trend",
  xlab = "Student",
  ylab = "Marks"
)