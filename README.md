Binance Futures Testnet Trading Bot
Overview

This project is a Python-based command line trading bot designed to interact with the Binance Futures Testnet (USDT-M).
The application allows users to place Market and Limit orders using simple CLI inputs while maintaining a clean architecture, structured logging, and proper error handling.

The goal of the project is to demonstrate a modular approach to building trading tools with input validation, reusable components, and transparent logging of API interactions.

Features
Core Functionality

Place Market Orders

Place Limit Orders

Supports both BUY and SELL

Works with Binance Futures Testnet

CLI Interface

Users can provide order parameters via command line arguments:

symbol (Example: BTCUSDT)

side (BUY / SELL)

order_type (MARKET / LIMIT)

quantity

price (required only for LIMIT orders)

Output

The bot prints:

Order request summary

Order response details:

orderId

status

executedQty

avgPrice (if available)

Success or failure message

Logging

All interactions are logged to a file including:

API request details

API responses

Errors and exceptions

Example log file:

logs/trading_bot.log
Project Structure
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging configuration
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
└── logs/
Requirements

Python 3.8+

Binance Futures Testnet account

API key and secret

Setup Instructions
1. Clone the Repository
git clone https://github.com/yourusername/binance-trading-bot.git
cd binance-trading-bot
2. Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate

Windows:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

Example dependencies:

python-binance
requests
python-dotenv
4. Configure API Credentials

Create a .env file in the root directory:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key
BASE_URL=https://testnet.binancefuture.com

You can obtain testnet credentials from:

https://testnet.binancefuture.com

Running the Bot

The bot is executed through the CLI.

Example: Market Order
python cli.py \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.001

Output Example:

Order Request Summary
---------------------
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Order Response
--------------
Order ID: 12345678
Status: FILLED
Executed Quantity: 0.001
Average Price: 64350.21

Order placed successfully.
Example: Limit Order
python cli.py \
--symbol BTCUSDT \
--side SELL \
--type LIMIT \
--quantity 0.001 \
--price 65000

Output Example:

Order Request Summary
---------------------
Symbol: BTCUSDT
Side: SELL
Type: LIMIT
Quantity: 0.001
Price: 65000

Order Response
--------------
Order ID: 12345690
Status: NEW
Executed Quantity: 0.0
Average Price: N/A

Limit order placed successfully.
Logging

All API interactions are stored in:

logs/trading_bot.log

Example log entry:

2026-03-14 12:10:02 INFO Sending order request to Binance
2026-03-14 12:10:03 INFO Order response received: orderId=12345678 status=FILLED

Logs help track:

API calls

Request parameters

Responses

Errors

Error Handling

The bot includes handling for:

Invalid CLI inputs

Missing parameters

API errors from Binance

Network failures

User-friendly messages are printed to the console while full details are logged.

Assumptions

The user has an active Binance Futures Testnet account.

API credentials are valid and stored securely.

The symbol used exists on Binance Futures (e.g., BTCUSDT).

Quantity and price values follow Binance contract requirements.

Example Logs Submitted

The repository includes logs from:

One Market Order

One Limit Order

These can be found in the logs/ directory.
