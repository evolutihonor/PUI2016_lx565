
Author: Le Xu

**Best time to drive a cab?**
**When are the longer trips and higher average fares likely to happen? **

<Le Xu, github: lx565, NYU ID: lx565>


## Problem Description:
It is generally known that: Fridays’ and Saturdays’ nights are the busiest time period during the week, or bad weather could also help to drive up taxi demands. After the CUSP hack-day working on NYC Taxi dataset, I would love to further study the taxi fares by analyzing with the taxi trip occurring time and the daily weather.  In my data analysis, I will answer questions like: What time of the day has better chance of longer trips or higher average trip fare? How bad weather (rain/snow) could affect taxi ridership, etc. 



## Data: (ready for analysis) [Data](https://github.com/lx565/PUI-Extra-Credit/tree/master/Data)

### Taxi trip data
_Source: NYC Taxi & Limousine Commission - NYC.gov_

Since there will be time series analysis, the taxi data from NYC.gov has included the time of the trip occurring, both the pick-up time and drop-off time, and the total fare as well as the total tip amount. 
The anticipated data processing will mainly include: binning the timestamps, to discover the trend/periodicity of the taxi income during the day/week/month. 




### Daily Central Park weather data
_Source: National Climatic Data Center_ 
https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00094728/detail

This dataset could give me the weather data that I need. 

*Since the size of the taxi data is rather huge, so I might consider take a subset of the dataset, however I am not sure currently.


## Analysis Plan:

Idea 1: Night has more people go out/dine out and trains are getting slower or less, so night has more long trips than the day.

**NULL HYPOTHESIS: The ratio of numbers of Taxi longer trips over total numbers of trips occurred during the daytime is same or higher than the ratio of numbers of Taxi longer trip over total numbers of trips occurred during the nighttime.**


Range of hours for this analysis. 
Day time (from 6:00 to 18:00)
Night time (from 18:00 to 6:00)

$$H0 : \frac{Day Long Trips}{Total Day Trip}\geq \frac{Night Long Trips}{Total Night Trips} $$
$$H1 : \frac{Day Long Trips}{Total Day Trip}\< \frac{Night Long Trips}{Total Night Trips} $$


I will use a significance level  $$\alpha=0.05$$

I will probably use one month data in the winter and one month in the summer time.  


Idea 2: How the weather would affect the taxi demand? Rainy day could either drive up demands because people might not have umbrellas, or idle the demand because less people want to go out because of the rain. 
For the taxi rides with weather condition analysis, extreme events will be identified through outlier detection via thresholds. Clustering/Correlation Analysis could be performed in order to examine the relationship between taxi demands and weather.


## Analysis Tools:  Pandas, matplotlib




## References: 
Analyzing 1.1 Billion NYC Taxi and Uber Trips, with a Vengeance - Todd W. Schneider
http://toddwschneider.com/posts/analyzing-1-1-billion-nyc-taxi-and-uber-trips-with-a-vengeance/

Visual Exploration of Big Spatio-Temporal Urban Data: A Study of New York City Taxi Trips - Nivan Ferreira, Jorge Poco, Huy T. Vo, Juliana Freire, and Claudio T. Silva

NYC Taxi Trip and Fare Data Analytics using BigData - Umang Patel #




## Deliverable:  
Idea 1: The result of the statistical analysis, with at least two figures to support.  
Idea 2: The result of the Clustering/Correlation Analysis. 
