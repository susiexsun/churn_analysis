## Goal

Conduct EDA and build a model for an on-demand company to predict churn of customers. 

This project was built over 1 day as a collaboration between myself and Eugene Lee. 

##### The Data
50,000 rows of user log data in csv

##### The Deliverables
* Insights on user retention and churn
* Machine learning model to predict churn

## EDA

![feature importance](http://s16.postimg.org/ysdxvma8l/features_churn.jpg)

![average distance](http://s15.postimg.org/qaxpfhzuj/distance.jpg)

![weekday vs weekend](http://s9.postimg.org/5mpywepsf/weekday.jpg)

![30 day behavior](http://s27.postimg.org/khaha4v5v/30days.jpg)

![price sensitivity](http://s7.postimg.org/v77etnbyj/price_sensitivity.jpg)


## The Model
![GBR model](http://s24.postimg.org/7zq7l6m9h/gbr_analysis.jpg)

## Next Steps

The EDA produced a lot of great starting points for future experiments.

* <b>New marketing efforts</b> should target 
  * Price Insensitive Users
  * City dwellers
* <b>Retain users</b> of Android with cost savings
  * Coupons
  * UX comparison of cost savings vs taxi
* <b>Build habitual user behavior</b> by: 
  * Incentivize more use in first 30 days by not having surge pricing
  * Offer discounts on weekdays for weekend users (and vice versa)
