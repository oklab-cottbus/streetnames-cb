library(dplyr)
library(stringr)
original_names <- read.csv("../names-magdeburg.csv", fileEncoding = "UTF-8")

get_gender_names <- read.csv("../names-magdeburg_test.csv", fileEncoding = "UTF-8")


# "transalte" gender description

get_gender_names <- get_gender_names %>% mutate(Gender = str_replace(Gender,"weiblich", "f")) %>%
  mutate(Gender = str_replace(Gender,"männlich","m")) %>%
  mutate(Gender= ifelse(is.na(Gender),"n",Gender))

# remove rows with "?" as gender from dataframe since we cant really compare them

uncertain_streetnames <- original_names$Name[original_names$Gender == "?"]

original_names <- original_names[!original_names$Name %in% uncertain_streetnames,]
get_gender_names <- get_gender_names[!get_gender_names$Name %in% uncertain_streetnames,]

result <- table(get_gender_names$Gender == original_names$Gender)
result

# compare shares of f an m

original_woman_share <- table(original_names$Gender)[1]/table(original_names$Gender)[2]

get_gender_woman_share <- table(get_gender_names$Gender)[1]/table(get_gender_names$Gender)[2]

original_woman_share
get_gender_woman_share
