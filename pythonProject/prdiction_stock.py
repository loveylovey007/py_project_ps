import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
#from ayx import Alteryx  # For Alteryx-specific output

# --- Parameters ---
stock_symbol = "RELIANCE.NS"  # NSE symbol, change as needed
period = "60d"                # Last 60 days of data
interval = "1d"               # Daily frequency

# --- Step 1: Fetch data ---
df = yf.download(tickers=stock_symbol, period=period, interval=interval)
df.reset_index(inplace=True)

# Keep only necessary columns
df = df[['Date', 'Close']]
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(inplace=True)

# --- Step 2: Convert dates for model ---
df['DateOrdinal'] = df['Date'].map(datetime.toordinal)

# --- Step 3: Train Linear Regression Model ---
model = LinearRegression()
model.fit(df[['DateOrdinal']], df['Close'])

# --- Step 4: Predict future prices ---
future_days = 7
last_date = df['Date'].max()
future_dates = [last_date + timedelta(days=i) for i in range(1, future_days + 1)]
future_ordinals = [d.toordinal() for d in future_dates]
predicted_prices = model.predict(np.array(future_ordinals).reshape(-1, 1))

# --- Step 5: Create prediction DataFrame ---
# --- Step 5: Create prediction DataFrame ---
prediction_df = pd.DataFrame({
    'Date': future_dates,
    'Predicted_Close': predicted_prices.flatten()  # Flatten to 1D
})


# Optional: Combine with historical for comparison
combined_df = pd.concat([
    df[['Date', 'Close']].rename(columns={'Close': 'Actual_Close'}),
    prediction_df.rename(columns={'Predicted_Close': 'Actual_Close'})
], ignore_index=True)

# --- Step 6: Output for Alteryx ---
#Alteryx.write(prediction_df, 1)  # Output prediction
# Alteryx.write(combined_df, 2)  # Optional: Output historical + prediction
print(prediction_df)  # Just display the output in PyCharm
prediction_df.to_csv("predicted_prices.csv", index=False)  # Optional: save to file
