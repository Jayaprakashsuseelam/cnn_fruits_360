# Read the data from the file
data <- read.csv("/path-to-fortune1000.csv-file")

# Check the structure of the data
str(data)

# Summarize the total revenue by industry
industry_revenue <- aggregate(Revenue ~ Industry, data = data, FUN = sum)

# Sort the industries by total revenue
sorted_industries <- industry_revenue[order(-industry_revenue$Revenue), ]

# Extract the top 10 industries
top_10 <- head(sorted_industries, 10)

# Print the top 10 industries
print(top_10)

# Sort the data by employee size
sorted_data <- data[order(data$Employees, decreasing = TRUE), ]

# Take the top 20 companies based on employee size
top_20 <- head(sorted_data, 20)

# Plot the scatter plot
plot(top_20$Revenue, top_20$Profit,
     xlab = "Revenue", ylab = "Profit",
     main = "Scatter plot of Revenue vs Profit for Top 20 Companies based on Employee Size")
