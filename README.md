## Goal

Conduct EDA and build a model for an on-demand company to predict churn of customers. 

This project was built over 1 day as a collaboration between myself and Eugene Huang (eugeneh101). 

##### The Data
50,000 rows of user log data in csv

##### The Deliverables
* Insights on user retention and churn
* Machine learning model to predict churn

## EDA

We ran an initial model in Random Forest in order to get a feature importance analysis. 

![feature importance](http://s16.postimg.org/ysdxvma8l/features_churn.jpg)

As we dived deeper, we found that users that rode a longer distance seemed to churn more. 

![average distance](http://s15.postimg.org/qaxpfhzuj/distance.jpg)

And that users that rode on all days, rather than just weekends or weekdays tended to retain. 

![weekday vs weekend](http://s9.postimg.org/5mpywepsf/weekday.jpg)

Lots of use within the first 30 days tended to create lasting retention. 

![30 day behavior](http://s27.postimg.org/khaha4v5v/30days.jpg)

Users that are price sensitive tended to churn. Since we didn't have actual price sensitivity data on customers, we used two data points as proxies: percentage of use during pricing and having an Android phone (since iPhone users tend to be less price sensitive).

![price sensitivity](http://s7.postimg.org/v77etnbyj/price_sensitivity.jpg)


## The Model

We tried a few different models and used Grid Search on the parameters. 

What we tried: 
* Logistic Regression
* Support Vector Classifier
* Gradient Boosted Classifier.

Gradient Boosted Classifer with the following parameters produced the best result: 
Parameters: 
* n_estimators = 100
* learning rate = 0.33
* max_depth = 3
* max_features = log2

Here's a ROC plot with our model.

![GBR model](http://s24.postimg.org/7zq7l6m9h/gbr_analysis.jpg)

This model still needs a lot of work. Had we had more time, we would do feature engineering. There was lots of interesting information that require time series analysis. There was also fruitful work to be done in experimentation & A/B Testing, which I cover in the next section.

## Next Steps

The analysis produced a lot of great starting points for future experiments.

* <b>New marketing efforts</b> should target 
  * Price Insensitive Users
  * City dwellers
* <b>Retain users</b> of Android with cost savings
  * Coupons
  * UX comparison of cost savings vs taxi
* <b>Build habitual user behavior</b> by: 
  * Incentivize more use in first 30 days by not having surge pricing
  * Offer discounts on weekdays for weekend users (and vice versa)

## Repo Structure
|- Code <br>
    |- case-study (clean data & run models)<br>
    |- case-study.ipynb (EDA and analysis)<br>
    |- roc.py (code to run roc plot)<br>
