#!/usr/bin/env python3
"""Simple HTTP endpoint health checker with retries (demo SRE tooling)."""
import argparse
import sys
import time
import urllib.request


def check(url: str, timeout: int = 5) -> tuple[bool, int | str]:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return (200 <= resp.status < 400), resp.status
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)


def main() -> int:
    p = argparse.ArgumentParser(description="Health check an endpoint.")
    p.add_argument("url")
    p.add_argument("--retries", type=int, default=3)
    p.add_argument("--delay", type=int, default=2)
    args = p.parse_args()

    for attempt in range(1, args.retries + 1):
        ok, detail = check(args.url)
        if ok:
            print(f"OK   {args.url} -> {detail}")
            return 0
        print(f"WARN attempt {attempt}/{args.retries} failed: {detail}")
        time.sleep(args.delay)

    print(f"FAIL {args.url} is unhealthy after {args.retries} attempts")
    return 1


if __name__ == "__main__":
    sys.exit(main())
