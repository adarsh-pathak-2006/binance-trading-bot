from bot.client import BinanceFuturesClient
from bot.logging_config import logger

def execute_order(client: BinanceFuturesClient, symbol, side, order_type, quantity, price=None, stop_price=None):
    """Orchestrates the order execution process."""
    
    logger.info(f"Attempting to place {order_type} order for {symbol}...")
    
    try:
        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )
        
      
        order_id = response.get('orderId')
        status = response.get('status')
        exec_qty = response.get('executedQty', '0')
        avg_price = response.get('avgPrice', 'N/A')

        success_msg = (
            f"\n--- Order Success ---\n"
            f"Order ID: {order_id}\n"
            f"Status: {status}\n"
            f"Executed Qty: {exec_qty}\n"
            f"Avg Price: {avg_price}\n"
            f"---------------------"
        )
        print(success_msg)
        return response

    except Exception as e:
        print(f"\n--- Order Failed ---\nError: {str(e)}\n--------------------")
        return None