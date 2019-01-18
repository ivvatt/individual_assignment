#install.packages("tidyverse")
#install.packages("maps")

library(tidyverse)
library('maps')

afghanistan <- read.csv('afghanistan.csv', stringsAsFactors = FALSE)

format(as.Date(Year, format="%Y-%M-%D"),"%Y")
factor('Year', levels= c("1998", "2004"))''
afghanistan$Type.of.violence = as.factor(afghanistan$Type.of.violence)
#factor('Type.of.violence', levels = c(1, 2, 3), labels = c('state-based', 'non-state-based', 'one-sided'))

ggplot() +
  geom_polygon(data=map_data('world', region='Afghanistan'), aes(x=long, y=lat, group=group), fill=NA, colour="black") +
  geom_point(data=afghanistan, aes(x=Long, y=Lat, fill=factor(Type.of.violence, labels = c('state-based', 'one-sided')), size=Deaths.B, color=Side.B)) +
  facet_wrap(Year ~ .) +
  ggtitle('Conflicts in Afghanistan for the years 1998 and 2004') +
  #legend() +
  coord_fixed(1) 




