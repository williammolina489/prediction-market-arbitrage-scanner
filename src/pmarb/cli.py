import argparse
import json
from decimal import Decimal

from .kalshi import Client
from .scanner import discover, scan_once


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only E001 structural scanner")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate-live")
    sub.add_parser("scan-once")
    args = parser.parse_args()
    client = Client()
    payload = discover(client) if args.cmd == "validate-live" else scan_once(client)
    print(json.dumps(payload, cls=Encoder, indent=2))

if __name__ == "__main__":
    main()
