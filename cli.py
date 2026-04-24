import argparse
import logging
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        print("\n📌 Order Request Summary")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")

        logging.info(f"Order Request: {vars(args)}")

        response = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        logging.info(f"Order Response: {response}")

        print("\n📊 Order Response")

        if "error" in response:
            print("❌ Failed:", response["error"])
        else:
            print(f"Order ID: {response.get('orderId')}")
            print(f"Status: {response.get('status')}")
            print(f"Executed Qty: {response.get('executedQty')}")
            print(f"Avg Price: {response.get('avgPrice')}")
            print("✅ Order placed successfully")

    except Exception as e:
        logging.error(str(e))
        print("❌ Error:", str(e))


if __name__ == "__main__":
    main()