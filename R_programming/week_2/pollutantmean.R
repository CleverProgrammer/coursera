pollutantmean <- function(directory, pollutant, id = 1:332) {
  fileList <- list.files("downloads/specdata/", pattern = ".csv", full.names = TRUE)
  values <- numeric()
  
  for (i in id) {
    data <- read.csv(fileList[i])
    values <- c(values, data[[pollutant]])
  }
  mean(values, na.rm = TRUE)
}