import flask
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

mock_stock_prices = {
    "BBCA": {"price": 9500, "change": "+50", "volume": 1500000},
    "TLKM": {"price": 3800, "change": "-20", "volume": 2200000},
    "ASII": {"price": 5200, "change": "+100", "volume": 1800000},
    "GOTO": {"price": 60, "change": "+1", "volume": 5000000},
    "BRIS": {"price": 2500, "change": "-30", "volume": 900000},
}
valid_symbols = list(mock_stock_prices.keys())

@app.route('/get_stock_price', methods=['GET'])
def get_stock_price():
    symbol_param = request.args.get('symbol')
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    if symbol_param:
        symbol = symbol_param.upper()
        if symbol in mock_stock_prices:
            data = mock_stock_prices[symbol]
            data["symbol"] = symbol
            print(f"[SERVER] Sending price for {symbol}: {data} (after {delay:.2f}s delay)")
            return jsonify(data)
        else:
            error_msg = {"error": "symbol_not_found", "message": f"Stock symbol '{symbol}' not found."}
            print(f"[SERVER] Symbol {symbol} not found (after {delay:.2f}s delay)")
            return jsonify(error_msg), 404
    else:
        random_symbol = random.choice(valid_symbols)
        data = mock_stock_prices[random_symbol]
        data["symbol"] = random_symbol
        print(f"[SERVER] Sending random stock price for {random_symbol}: {data} (after {delay:.2f}s delay)")
        return jsonify(data)

if __name__ == '__main__':
    print("Simple Stock Price API Server running on http://127.0.0.1:5000")
    print("Endpoint: GET /get_stock_price (opsional: ?symbol=BBCA)")
    app.run(debug=False, threaded=True, use_reloader=False)