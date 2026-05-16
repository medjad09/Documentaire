import numpy as np
import pandas as pd

def simulate_bitcoin_price(days=60, start_price=60000, mu=0.0006, sigma=0.04):
    """
    Simulates Bitcoin price using Geometric Brownian Motion.
    days: number of days to simulate
    mu: daily drift (expected return)
    sigma: daily volatility
    """
    np.random.seed(42)  # For reproducibility
    # returns are normally distributed
    daily_returns = np.random.normal(mu, sigma, days)
    # price follows GBM: S_t = S_0 * exp(sum(r_i))
    price_ratios = np.exp(daily_returns)
    prices = start_price * np.cumprod(price_ratios)

    # Prepend start price for Day 0
    prices = np.insert(prices, 0, start_price)

    dates = pd.date_range(start="2023-01-01", periods=days+1)
    df = pd.DataFrame({"Date": dates, "Price": prices})
    return df

def apply_trading_strategy(df):
    # Calculate Moving Averages
    df['MA7'] = df['Price'].rolling(window=7).mean()
    df['MA30'] = df['Price'].rolling(window=30).mean()

    # Portfolio initialization
    initial_balance = 10000.0
    balance = initial_balance
    position = 0.0  # BTC amount

    print(f"{'Date':<12} | {'Price':>10} | {'MA7':>10} | {'MA30':>10} | {'Action':<10} | {'Portfolio Value':>15}")
    print("-" * 85)

    for i in range(len(df)):
        date = df.iloc[i]['Date'].strftime('%Y-%m-%d')
        price = df.iloc[i]['Price']
        ma7 = df.iloc[i]['MA7']
        ma30 = df.iloc[i]['MA30']

        action = "Hold"

        # Golden Cross strategy:
        # Buy when MA7 > MA30
        # Sell when MA7 < MA30
        if not np.isnan(ma7) and not np.isnan(ma30):
            if ma7 > ma30 and position == 0:
                action = "BUY"
                position = balance / price
                balance = 0
            elif ma7 < ma30 and position > 0:
                action = "SELL"
                balance = position * price
                position = 0

        current_value = balance + (position * price)

        # Print daily ledger
        ma7_str = f"{ma7:10.2f}" if not np.isnan(ma7) else "       N/A"
        ma30_str = f"{ma30:10.2f}" if not np.isnan(ma30) else "       N/A"
        print(f"{date:<12} | {price:10.2f} | {ma7_str} | {ma30_str} | {action:<10} | {current_value:15.2f}")

    final_value = balance + (position * df.iloc[-1]['Price'])
    print("-" * 85)
    print(f"Initial Balance: ${initial_balance:,.2f}")
    print(f"Final Portfolio Value: ${final_value:,.2f}")
    print(f"Total Return: {((final_value - initial_balance) / initial_balance) * 100:.2f}%")

if __name__ == "__main__":
    # Simulate 60 days of Bitcoin price data
    bitcoin_df = simulate_bitcoin_price(days=60)
    # Apply Golden Cross strategy and print ledger
    apply_trading_strategy(bitcoin_df)
