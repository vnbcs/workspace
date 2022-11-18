library("tidyverse")

fold <- "Documents/PittLifeLab/esther dissertation"
list.files(fold)

stress <- read_csv(paste(fold,"/StressShell (1).csv",sep=""))

stress