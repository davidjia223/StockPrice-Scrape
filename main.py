import requests
import csv

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=OXQZ4ISUNT7H525Z'
r = requests.get(url)
data = r.json()

# Extract the time series data
time_series_data = data.get("Time Series (5min)", {})

# Save to CSV
with open('data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header
    csvwriter.writerow(["Time", "Open", "High", "Low", "Close", "Volume"])
    # Write the data
    for time, values in time_series_data.items():
        csvwriter.writerow([time, values["1. open"], values["2. high"], values["3. low"], values["4. close"], values["5. volume"]])

print("Data saved to data.csv")
