library(dplyr)
library(stringr)
original_names <- read.csv("../names-magdeburg.csv", fileEncoding = "UTF-8")

get_gender_names <- read.csv("../names-magdeburg_test.csv", fileEncoding = "UTF-8")


# "transalte" gender description

get_gender_names <- get_gender_names %>% mutate(Gender = str_replace(Gender,"weiblich", "f")) %>%
  mutate(Gender = str_replace(Gender,"männlich","m")) %>%
  mutate(Gender= ifelse(is.na(Gender),"n",Gender))

# remove "?" gender from original dataframe and treat it as "n" to better compare the two dataframes

original_names <- original_names %>% mutate(Gender = str_replace(Gender,"\\?","n"))


result <- table(get_gender_names$Gender == original_names$Gender)
result

