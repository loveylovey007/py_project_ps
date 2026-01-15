import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

# --- Stock list (yfinance format) ---
stock_list = [
    "NMDC.NS", "GTLINFRA.NS", "ITC.NS", "NBCC.NS", "RPOWER.NS",
    "UCOBANK.NS", "PNB.NS", "RTNPOWER.NS", "IFCI.NS",
    "MMTC.NS", "GOLDBEES.NS", "SUZLON.NS"
]

period = "60d"
interval = "1d"
future_days = 7

# --- Container for wide-format data ---
wide_predictions = {}

# --- Loop through each stock ---
for stock_symbol in stock_list:
    print(f"Processing: {stock_symbol}")
    try:
        df = yf.download(tickers=stock_symbol, period=period, interval=interval, auto_adjust=True)
        df.reset_index(inplace=True)
        df = df[['Date', 'Close']].dropna()
        df['DateOrdinal'] = df['Date'].map(datetime.toordinal)

        # Train Linear Regression
        model = LinearRegression()
        model.fit(df[['DateOrdinal']], df['Close'])

        # Predict future days
        last_date = df['Date'].max()
        future_dates = [last_date + timedelta(days=i) for i in range(1, future_days + 1)]
        future_ordinals = [d.toordinal() for d in future_dates]
        predicted_prices = model.predict(np.array(future_ordinals).reshape(-1, 1)).flatten()

        # Add to dictionary
        stock_name = stock_symbol.replace(".NS", "")
        wide_predictions[stock_name] = predicted_prices

        # Save dates only once
        if 'Date' not in wide_predictions:
            wide_predictions['Date'] = [d.strftime("%Y-%m-%d") for d in future_dates]

    except Exception as e:
        print(f"Error processing {stock_symbol}: {e}")

# --- Create final DataFrame ---
date_headers = wide_predictions.pop('Date')  # Extract dates to use as column headers
df_wide = pd.DataFrame.from_dict(wide_predictions, orient='index', columns=date_headers)
df_wide.reset_index(inplace=True)
df_wide.rename(columns={'index': 'Stock Name'}, inplace=True)

# --- Save to CSV ---
df_wide.to_csv("wide_stock_predictions.csv", index=False)
print("\n✅ Predictions saved to wide_stock_predictions.csv")
