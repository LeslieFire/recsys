# popularity
popularity <- read.csv("item_popularity.txt", header = FALSE, sep = "\t", colClasses = c("factor", "numeric"))
hist(popularity$popularity, xlab = "product popularity", ylab = "product number of specific popularity", main = "product popularity distribution")

# activity
activity <- read.csv("activity.txt", header = TRUE, sep = "\t", colClasses = c("factor", "numeric"))
names(activity) <- c("IP", "activity")
hist(activity$activity, xlab = "user activity", ylab = "number of specific activity", main = "user activity distribution")
