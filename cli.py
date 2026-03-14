import argparse
import os
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import execute_order
from bot.validators import validate_input
from bot.logging_config import logger


load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "STOP_LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price for LIMIT or STOP_LIMIT orders")
    parser.add_argument("--stop-price", type=float, help="Trigger price for STOP_LIMIT orders")

    args = parser.parse_args()

    try:
        
        validated_data = validate_input(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
        symbol, side, order_type, quantity, price = validated_data

    
        if not API_KEY or not API_SECRET:
            raise ValueError("API_KEY and API_SECRET must be set in .env file")
            
        client = BinanceFuturesClient(API_KEY, API_SECRET, testnet=True)

        if order_type == "STOP_LIMIT":
            if not args.stop_price:
                raise ValueError("--stop-price is required for STOP_LIMIT orders.")
            logger.info(f"Placing STOP_LIMIT order. Stop: {args.stop_price}, Limit: {price}")
            
            
            execute_order(client, symbol, side, "STOP", quantity, price=price, stop_price=args.stop_price)
        else:
            execute_order(client, symbol, side, order_type, quantity, price)

    except ValueError as ve:
        logger.error(f"Validation Error: {ve}")
    except Exception as e:
        logger.error(f"Application Error: {e}")

if __name__ == "__main__":
    main()