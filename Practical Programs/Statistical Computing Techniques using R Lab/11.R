# Load the built-in dataset
data(iris)

# Create a scatter plot
plot(iris$Sepal.Length, iris$Sepal.Width,
     main = "ScatterPlot (Sepal Length v/s Width)",
     xlab = "Sepal Length (cm)",
     ylab = "Sepal Width (cm)",
     col = c("red", "blue", "green")[iris$Species],
     pch = 19)

# Add a legend
legend("topright",
       legend = levels(iris$Species),
       col = c("red", "blue", "green"),
       pch = 19)
