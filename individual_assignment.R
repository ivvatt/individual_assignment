library(tidyverse)
library('maps')

afghanistan <- read.csv('afghanistan.csv', stringsAsFactors = FALSE)

factor('Year', levels= c(1998, 2004))

ggplot() +
  geom_polygon(data=map_data('world', region='Afghanistan'), aes(x=long, y=lat, group=group), fill=NA, colour="black") +
  geom_point(data=afghanistan, aes(x=Long, y=Lat, size=Deaths.Civilians, color=Side.B)) +
  facet_wrap(Year ~ .) +
  ggtitle('State-based conflicts in Afghanistan for the years 1998 and 2004') +
  xlab("Longitude") + 
  ylab("Latitude") +
  scale_color_discrete(name="Conflict\nwith") +
  scale_size_continuous(name = "Number\nof\ncivilian\ndeaths") +
  coord_fixed(1) 

ggplot(data=afghanistan) +
  geom_bar(stat = "identity", aes(x=Year, y=Deaths.Civilians)) +
  ggtitle("Number of civilian deaths in 1998 and 2004") +
  xlab("Year") +
  ylab("Number of civilian deaths")



