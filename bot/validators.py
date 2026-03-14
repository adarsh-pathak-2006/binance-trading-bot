from bot.logging_config import logger

def validate_input(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """Validates user input before sending to API."""
    
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError(f"Invalid side: {side}. Must be 'BUY' or 'SELL'.")

    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError(f"Invalid order type: {order_type}. Must be 'MARKET', 'LIMIT', or 'STOP_LIMIT'.")

    if quantity <= 0:
        raise ValueError(f"Quantity must be positive. Got: {quantity}")

    if order_type in ["LIMIT", "STOP_LIMIT"] and (price is None or price <= 0):
        raise ValueError(f"Price is required and must be positive for {order_type} orders.")

    logger.info(f"Input validated: Symbol={symbol}, Side={side}, Type={order_type}, Qty={quantity}, Price={price}")
    return symbol, side, order_type, quantity, price