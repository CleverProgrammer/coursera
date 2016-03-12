complete <- function(directory, id = 1:332) {
  filelist <- list.files(path = directory, pattern = ".csv", full.names = TRUE)
  print(paste("##", "", "id", "nobs", sep = " "))
  counter <- 0
  for (i in id) {
    counter <- counter + 1
    data = read.csv(filelist[i])
    print(paste("##", counter, i, sum(complete.cases(data)), sep=" "))
  }
}