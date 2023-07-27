# Install libraries
!pip install yfinance==0.2.4
!pip install pandas==1.3.3
!pip install requests==2.28.01
!pip install nbformat==5.1.0
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y
!pip install lxml==4.9.1
!pip install plotly=5.3.1

#  Import libraries
from bs4 import BeautifulSoup as bs
import requests
import html5lib
import lxml
import yfinance as yf
import pandas as pd
import plotly as pt

# Tesla Data 
#  Get the stock source data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

#Question 1 - Extracting Tesla Stock Data Using yfinance - 2 Points
#  Extract Tesla Stock information using yfinance
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period = "max")
tesla_data.reset_index (inplace = True)
print ('Tesla Stock Data', tesla_data.head())
#print (tesla_data.head())

#Question 2 - Extracting Tesla Revenue Data Using Webscraping - 1 Points
# Get the revenue source data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

html_data = requests.get(url).text
soup = bs(html_data, 'html5lib')
table = soup.find('table')
tesla_revenue = pd.read_html(str(table))[0]
tesla_revenue.columns = ['Date', 'Revenue']
print(tesla_revenue)
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace(',|\$', "")
print ('Tesla Revenue\n', tesla_revenue.tail())

#Question 5 - Tesla Stock and Revenue Dashboard - 2 Points
def make_graph(stock_data, revenue_data, stock_name):
    fig = make_subplots(rows=1, cols=1, subplot_titles = [f"{stock_name} Stock Data"])
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode = 'lines', name = f"{stock_name} Stock Price"))
    fig.update_layout(title=f"{stock_name} Stock Price", xaxis_title = 'Date', yaxis_title = 'Closing Price')
    fig.show()

make_graph(tesla_data, tesla_revenue, 'Tesla')


#GameStop Data
#Question 3 - Extracting GameStop Stock Data Using yfinance - 2 Points
#  Extract GameStop Stock information using yfinance
gamestop = yf.Ticker("GME")
gme_data = gamestop.history(period = "max")
gme_data.reset_index (inplace = True)
print ('GameStop Stock Data', gme_data.head())
#print (gme_data.head())

#Question 4 - Extracting GameStop Revenue Data Using Webscraping - 1 Points
# Get the revenue source data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

html_data = requests.get(url).text
soup = bs(html_data, 'html5lib')
table = soup.find('table')
gme_revenue = pd.read_html(str(table))[0]
gme_revenue.columns = ['Date', 'Revenue']
print(gme_revenue)
gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace(',|\$', "")
print ('GameStop Revenue\n', gme_revenue.tail())

#Question 6 - GameStop Stock and Revenue Dashboard- 2 Points
def make_graph(stock_data, revenue_data, stock_name):
    fig = make_subplots(rows=1, cols=1, subplot_titles = [f"{stock_name} Stock Data"])
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode = 'lines', name = f"{stock_name} Stock Price"))
    fig.update_layout(title=f"{stock_name} Stock Price", xaxis_title = 'Date', yaxis_title = 'Closing Price')
    fig.show()

make_graph(gme_data, gme_revenue, 'GameStop')

quit()
