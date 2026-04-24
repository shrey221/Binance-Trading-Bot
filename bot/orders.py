import time
import hmac
import hashlib
import requests
from bot.client import API_KEY, API_SECRET, BASE_URL


def _sign(params: dict) -> str:
    query_string = "&".join([f"{k}={v}" for k, v in params.items()])
    return hmac.new(
        API_SECRET.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()


def place_order(symbol, side, order_type, quantity, price=None):
    endpoint = "/fapi/v1/order"

    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity,
        "timestamp": int(time.time() * 1000)
    }

    if order_type.upper() == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    params["signature"] = _sign(params)

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    try:
        response = requests.post(
            BASE_URL + endpoint,
            headers=headers,
            params=params,
            timeout=10
        )

        data = response.json()

        # Handle Binance API error format
        if "code" in data and data["code"] < 0:
            return {"error": data.get("msg")}

        return data

    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}