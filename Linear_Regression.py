import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

data = pandas.read_csv('cost_revenue_clean.csv')

data.describe()

x = DataFrame(data,columns=['production_budget_usd'])
y = DataFrame(data, colums=['worldwide_gross_usd'])

plt.figure(figsize-(10,6))
plt.scatter(x, y, alpha=0.3)
plt.title('Film Cost vs Global Revenue')
plt.xlabel('production Budget $')
plt.ylabel('Worldwide Gross $')
plt.ylim(0,3000000000)
plt.xlim(0,450000000)
plt.show()

regression = LinearRegression()
regression.fit(x,y)

regression.coef_

regression.intercept_

plt.figure(figsize-(10,6))
plt.scatter(x, y, alpha=0.3)
plt.plot(x, regression.predict(x), color='red', linewidth=4)

plt.title('Film Cost vs Global Revenue')
plt.xlabel('production Budget $')
plt.ylabel('Worldwide Gross $')
plt.ylim(0,3000000000)
plt.xlim(0,450000000)
plt.show()
