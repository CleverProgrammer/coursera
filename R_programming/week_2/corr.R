corr <- function(directory, threshold = 0) {
  filesList <- list.files(path = directory, pattern = ".csv", full.names = TRUE)
  cors <- numeric()
  for (i in 1:332) {
    data <- read.csv(filesList[i])
    if (sum(complete.cases(data)) > threshold) {
      cors <- c(cors, cor(data[["sulfate"]], data[["nitrate"]], use = "complete.obs"))
    }
  }
  cors
}