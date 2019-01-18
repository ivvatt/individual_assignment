#install.packages("tidyverse")
#install.packages("maps")

library(tidyverse)
library('maps')

afghanistan <- read.csv('R/afghanistan.csv', stringsAsFactors = FALSE)

format(as.Date(Year, format="%Y-%M-%D"),"%Y")
factor('Year', levels= c("1998", "2004"))
factor('Side B', levels = c('Taleban', 'UIFSA'))

'Side B' <- afghanistan %>%
  filter(afghanistan$'Side B'== 'Taleban' & afghanistan$'Side B' == 'UIFSA')

ggplot() +
  geom_polygon(data=map_data('world', region='Afghanistan'), aes(x=long, y=lat, group=group), fill=NA, colour="black") +
  geom_point(data=afghanistan, aes(x=Long, y=Lat, fill=Type.of.Violence, size=Deaths.B, color=Side.B)) +
  facet_wrap(Year ~ .) +
  coord_fixed(1) 




