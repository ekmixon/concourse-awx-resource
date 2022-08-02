#!/usr/bin/env python

import json
import sys
from awx import AWX


def main():
    _stdin = "".join(sys.stdin.readlines())
    _in = json.loads(_stdin)

    awx = AWX(_in)
    results = awx.launch()

    metadata = [
        {"name": k, "value": json.dumps(results[k])}
        for k in sorted(results.keys())
    ]

    _out = {"version": {}, "metadata": metadata}

    print(json.dumps(_out))
    if results.get("status", "failed") != "successful":
        sys.exit(1)


if __name__ == "__main__":
    main()
