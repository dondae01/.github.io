Crypto Market Trends Dashboard

Project Summary  
The Crypto Market Trends Dashboard visualizes cryptocurrency market performance using Tableau Public. It focuses on three key visualizations:
1. Market Cap Distribution: Ranks cryptocurrencies based on market capitalization.
2. Price vs. 24h Volume: A scatterplot showing trading volumes relative to prices.
3. 24h Price Change Heatmap: Highlights the top gainers and losers in the past 24 hours.

This dashboard helps users quickly identify major trends and insights in the cryptocurrency market.

 Data Source  
The data was sourced using the CoinGecko API, which provides real-time cryptocurrency market data.

Python Code for Data Extraction:
```python
import requests
import pandas as pd

# API Endpoint and Parameters
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 100,
    'page': 1,
    'sparkline': False
}

# API Request
response = requests.get(url, params=params)
data = response.json()

# Convert to DataFrame
crypto_data = pd.DataFrame(data)

# Select Relevant Columns
columns_to_keep = ['id', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']
crypto_data = crypto_data[columns_to_keep]

# Save as CSV for Tableau
crypto_data.rename(columns={
    'id': 'Name',
    'symbol': 'Symbol',
    'current_price': 'Price',
    'market_cap': 'Market Cap',
    'total_volume': '24h Volume',
    'price_change_percentage_24h': '24h Price Change (%)'
}, inplace=True)
crypto_data.to_csv('crypto_data.csv', index=False)

print("Data saved successfully!")
```

 Key Features  
- Interactive Visualizations:  
   Users can explore market cap rankings, price-volume relationships, and heatmaps for quick insights.  
- Live Data:  
   Real-time data fetched via CoinGecko API.  

[Link to the Dashboard Screenshot](/images/dashboard_screenshot.png)

 Tools Used  
- Python: Data extraction using CoinGecko API.  
- Tableau Public: Data visualization and dashboard creation.
