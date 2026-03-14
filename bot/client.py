from binance.client import Client
from binance.exceptions import BinanceAPIException
from bot.logging_config import logger
import os

class BinanceFuturesClient:
    def __init__(self, api_key, api_secret, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        
        self.client = Client(api_key, api_secret)
        
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
            logger.info("Client initialized for Binance Futures Testnet.")
        else:
            logger.info("Client initialized for Binance Futures Mainnet.")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        """Places order on Binance Futures."""
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            # Logic for LIMIT orders
            if order_type == "LIMIT":
                params["timeInForce"] = "GTC"
                params["price"] = price
            
            # Logic for STOP-LIMIT orders (The Fix)
            # The CLI passes type="STOP", so we check for that here.
            if order_type == "STOP":
                if not price or not stop_price:
                    raise ValueError("Price and Stop Price are required for STOP orders.")
                params["timeInForce"] = "GTC"
                params["price"] = price
                params["stopPrice"] = stop_price

            logger.info(f"Sending API Request: {params}")
            
            response = self.client.futures_create_order(**params)
            
            logger.info(f"API Response: {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.status_code} - {e.message}")
            raise
        except Exception as e:
            logger.error(f"Unexpected Error: {str(e)}")
            raise