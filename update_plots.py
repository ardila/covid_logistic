import pandas as pd
import io

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

import requests
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import datetime
url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
s=requests.get(url).content
d =pd.read_csv(io.StringIO(s.decode('utf-8')))
model = LinearRegression()
today = datetime.datetime.today().strftime("%B %d, %Y")
plt.rcParams.update({'font.size': 30})
for data_type in ('cases', 'deaths'):
  legends = []
  plt.figure(figsize=(20,15))
  for country, color in (('Italy', 'r'), ('US', 'b'), ('China', 'g'), ('Iran', 'y'), ('Spain', 'purple'), ('Korea, South', 'black')):
    def filter(x):
      return country == x['Country/Region']
    selected_data = d[d.apply(filter, axis=1)]
    selected_data_deaths = selected_data.iloc[:, 4:].sum(axis=0)
    selected_data = c[c.apply(filter, axis=1)]
    selected_data_confirmed_cases = selected_data.iloc[:, 4:].sum(axis=0)
    if data_type == 'deaths':
      last_zero_day = np.argwhere(selected_data_deaths.values<50).max()
      start = last_zero_day+1
      xdata = selected_data_deaths.values[start:]
      ydata = selected_data_deaths.diff().values[start:]/selected_data_deaths.values[start-1:-1]
    elif data_type == 'cases':
      last_zero_day = np.argwhere(selected_data_deaths.values<50).max()
      start = last_zero_day +1
      xdata = selected_data_confirmed_cases.values[start:]
      ydata = selected_data_confirmed_cases.diff().values[start:]/selected_data_confirmed_cases.values[start-1:-1]
    plt.scatter(xdata, ydata, color=color)

    model.fit(xdata.reshape((-1, 1)), ydata, sample_weight=xdata)
    x_intercept = -model.intercept_/model.coef_
    if x_intercept < 0:
      x_intercept = 'TOO NOISY'
    info = "Predicted total %s in %s: %s" % (data_type, country, int(np.round(x_intercept[0])))
    print(info)
    legends.append(info)
    #if x_intercept > 0:
    new_x = np.arange(max(xdata)).reshape(-1,1)
    plt.plot(new_x, model.predict(new_x), color=color)
    plt.xlabel('Number of %s' % data_type)
    plt.ylabel('Percent growth (diff/ number confirmed)')
    plt.grid()
    plt.ylim([0, .5])
  plt.legend(legends)
  plt.title('Logistic Model Predictions of %s for %s' % (data_type, today))
  plt.savefig('%s.png' % data_type)
