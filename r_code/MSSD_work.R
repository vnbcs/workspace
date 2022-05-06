#authored by: Kelly Barry 
# Code to pull MSSD and descriptive stats from participant video ratings

#set working directory to the participant subfolder
fold_name <- "~/OneDrive - University of Pittsburgh/participants/5_ps_06082021/combined_responses_by_participant"

library("psych", "tidyverse")

# to check the subfolders within "participants" 
list.files(fold_name)

filenames <- list.files(fold_name)
filenames
ldf <- lapply(filenames, read.csv)

pivot_df <- function(df){
  tidyr::pivot_wider(df, names_from = "source", 
                     values_from = "rating") -> new_df
  return(new_df)
}

ldf_names <- c()
#extracting individual df's 
# creates df1.mssd to df5.mssd
for (i in 1:length(ldf)){
  ldf_names[i] <- paste(paste("df", i, sep=""), "mssd", sep=".")
  }

# creates df1.mssd.flattened to df5.mssd.flattened
for (i in 1:length(ldf)){
  temp <- ldf[[i]] 
  new_name <- paste(ldf_names[[i]],".flattened",sep="")
  assign(new_name, pivot_df(temp))
}

#here I was doing work extracting MSSD, M, SD from df's but ideally I want to be able to 
  # do this in a loop/function, so I can do it for multiple participants/ folders of participants (and not each one individually)
  # storing the MSSD, M, SD for each video, for each participant as a new data frame

#extracting mssd, mean, sd from each video
mssd_each_vid <-lapply(df1_separated_videos[,3:11], function(x) mssd(x))
m_each_vid <-lapply(df1_separated_videos[,3:11], function(x) mean(x, na.rm=T))
sd_each_vid <-lapply(df1_separated_videos[,3:11], function(x) sd(x, na.rm=T))


#Extracting and renaming mssd, mean, and sd variables for each video 
mssd_each_vid<- as.data.frame(mssd_each_vid)
names(mssd_each_vid) <- gsub(".csv", "_mssd", names(mssd_each_vid))

m_each_vid<- as.data.frame(m_each_vid)
names(m_each_vid) <- gsub(".csv", "_mean", names(m_each_vid))

sd_each_vid<- as.data.frame(sd_each_vid)
names(sd_each_vid) <- gsub(".csv", "_sd", names(sd_each_vid))


#Binding into a single data.frame
  #each row = 1 participant
saved_stats <- rbind(c(mssd_each_vid, m_each_vid, sd_each_vid))
saved_stats <- as.data.frame(saved_stats)


#adding participant ID column 
saved_stats$participant_id <- rbind(df1_separated_videos$participant_id)


#moving participant ID to the front 
saved_stats<-saved_stats[, c(28, 1:27)]


#saved_stats <- dplyr::bind_rows(c(mssd_each_vid, m_each_vid, sd_each_vid))


#descriptives
summary(df1$rating)
sd(df1$rating)
>>>>>>> afa4b8e80bd8b6879e832819e7e00f2ea11c4047

#STILL NEED TO GET: get 1 total MSSD, across all videos

<<<<<<< HEAD

=======
?psych::mssd

psych::mssd(df1$rating, lag=1, group=NULL)
>>>>>>> afa4b8e80bd8b6879e832819e7e00f2ea11c4047


#end product should be CSV with MSSD listed for each participant 
#write.csv(XX, 'mssd03102022.csv')

! manually push to GitHub repo









