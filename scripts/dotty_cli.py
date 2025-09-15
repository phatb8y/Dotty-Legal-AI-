#!/usr/bin/env python3
import sys
from dotty.core import Dotty

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/dotty_cli.py \"your text here\"")
        sys.exit(1)

    text = sys.argv[1]
    dotty = Dotty()
    result = dotty.analyze(text)
    print(dotty.format_response(result))

if __name__ == "__main__":
    main()
