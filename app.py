import os
from flask import Flask, request
from binance.cm_futures import CMFutures
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Binance API setup using the Futures Connector SDK
# api_key = os.getenv('BINANCE_API_KEY')
# api_secret = os.getenv('BINANCE_API_SECRET')
# cm_futures_client = CMFutures()

# # get server time
# print(cm_futures_client.time())

# cm_futures_client = CMFutures(key='<api_key>', secret='<api_secret>')

# # Get account information
# print(cm_futures_client.account())
# Trading variables
percentage_per_trade = 0.10  # 10% of available capital

# Flask setup
app = Flask(__name__)

# def get_balance():
#     try:
#         balance_info = cm_futures_client.get_balance()
#         for asset in balance_info:
#             if asset.asset == 'USDT':
#                 return float(asset.balance)
#     except Exception as e:
#         print(f"An exception occurred while fetching balance: {e}")
#         return 0.0

# def get_max_leverage(symbol):
#     try:
#         leverage_brackets = cm_futures_client.get_leverage_bracket()
#         for bracket in leverage_brackets:
#             if bracket.symbol == symbol:
#                 return max([lever.initialLeverage for lever in bracket.brackets])
#     except Exception as e:
#         print(f"An exception occurred while fetching leverage info: {e}")
#         return 0

# def calculate_optimal_leverage(capital, max_leverage):
#     # Example strategy: Leverage increases as capital decreases
#     if capital < 50:
#         return min(20, max_leverage)
#     elif capital < 100:
#         return min(15, max_leverage)
#     elif capital < 500:
#         return min(10, max_leverage)
#     else:
#         return min(5, max_leverage)

# def calculate_position_size(capital, percentage, leverage):
#     return (capital * percentage) * leverage

# def calculate_quantity(position_size, current_price):
#     return position_size / current_price

# def place_order(symbol, side, quantity, leverage):
#     try:
#         # Adjust leverage for the symbol
#         cm_futures_client.change_initial_leverage(symbol=symbol, leverage=leverage)
#         order = cm_futures_client.post_order(
#             symbol=symbol,
#             side=side,
#             ordertype="MARKET",
#             quantity=quantity)
#     except Exception as e:
#         print(f"An exception occurred: {e}")
#         return False
#     return order

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f'data {data}')
    current_price = float(data['price'])  # Assume the price is sent in the alert
    symbol = data['symbol']  # Assume the symbol is sent in the alert
    # capital = get_balance()  # Fetch available balance
    # max_leverage = get_max_leverage(symbol)  # Fetch max leverage for the symbol
    # leverage = calculate_optimal_leverage(capital, max_leverage)  # Calculate optimal leverage
    # position_size = calculate_position_size(capital, percentage_per_trade, leverage)
    # quantity = calculate_quantity(position_size, current_price)
    
    # if data['type'] == 'buy':
    #     place_order(symbol, 'BUY', quantity, leverage)
    # elif data['type'] == 'sell':
    #     place_order(symbol, 'SELL', quantity, leverage)
    
    return 'success', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
