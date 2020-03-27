## Logistic Regression Modeling For Covid
This is a simple way of predicting the total number of deaths or cases by assuming that the growth in these numbers will follow a logistic growth curve.

Virtually every major epidemic has resulted in growth curves that look like this (even in some cases where there is under-testing), and every country has been roughly following this pattern so far.

One simple way to fit this model is to plot the number on the x axis and the percent growth from the previous point on the y axis. For a perfect logistic curve this relationship will be linear. So then I fit a line to the resulting points and project out to where the growth rate eventually falls to 0, indicating the total number has plateaued. I take that number as the prediction. 

This model is not likely to work well when the total number is still small, so  am focusing on countries that have reported more than 100 deaths.

I will be updating this data daily using [this colab](https://colab.research.google.com/drive/12g8pgy-KfQmAzToFC33JWS2zgincoire)
![Image](deaths.png)
![Image](cases.png)
