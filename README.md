# Binance Futures Testnet Trading Bot 🚀

## 📌 Overview

This project is a Python-based CLI trading bot that interacts with the **Binance Futures Testnet (USDT-M)** using direct REST API integration.

It allows users to place **MARKET** and **LIMIT** orders with proper validation, logging, and error handling.

---

## ✨ Features

* Place **MARKET** and **LIMIT** orders
* Supports both **BUY** and **SELL**
* CLI-based input using `argparse`
* Input validation and error handling
* Logging of API requests and responses
* Uses `.env` for secure API key management
* Modular and clean code structure

---

## 🏗️ Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Loads API keys and config
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── .env                   # API credentials (not committed)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/binance-trading-bot.git
cd binance-trading-bot
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
BASE_URL=https://testnet.binancefuture.com
```

👉 Get API keys from Binance Futures Testnet:
https://testnet.binancefuture.com

---

## ▶️ Usage

### 🔹 Place a MARKET order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### 🔹 Place a LIMIT order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## 📊 Sample Output

```
📌 Order Request Summary
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

📊 Order Response
Order ID: 12345678
Status: FILLED
Executed Qty: 0.001
Avg Price: 65000
✅ Order placed successfully
```

---

## 🪵 Logging

All API requests, responses, and errors are logged in:

```
bot.log
```

Example log entry:

```
2026-04-24 | INFO | Order Request: {...}
2026-04-24 | INFO | Order Response: {...}
```

---

## ⚠️ Error Handling

The application handles:

* Invalid CLI inputs
* Missing required parameters
* Binance API errors (e.g., insufficient balance)
* Network issues and timeouts

---

## 🔐 Security Notes

* API keys are stored in `.env`
* `.env` is excluded via `.gitignore`
* Never commit sensitive credentials

---

## 🧠 Assumptions

* Using Binance Futures Testnet (not live trading)
* Internet connection is stable
* Valid API credentials are provided

---

## 🚀 Future Improvements (Optional)

* Stop-Loss / Take-Profit orders
* Retry mechanism for failed requests
* Enhanced CLI (Typer / interactive menu)
* Basic UI dashboard

---

## 👨‍💻 Author

Shrey Gupta
