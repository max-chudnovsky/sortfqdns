#!/usr/bin/env python3
# sortfqdns.py
# Author: Max Chudnovsky (max@chudnovsky.ca)
# Date: 2025-07-14
#
# Description:
#   Read FQDNs from a file, extract zone and subdomain, and print sorted unique entries.
#   Usage:
#     python sortfqdns.py [input_file]
#   If no input_file is given, defaults to /tmp/fqdns.
# # Requirements:
#   - tldextract: Install with 'apt install python3-tldextract'
#   - Python 3.x

"""
sortfqdns.py: Read FQDNs from a file, extract zone and subdomain, and print sorted unique entries.
Usage:
  python sortfqdns.py [input_file]

If no input_file is given, defaults to /tmp/fqdns.
"""

import sys
import os
from collections import defaultdict

try:
    import tldextract
except ImportError:
    print("Error: tldextract module not found. Install with 'apt install python3-tldextract'", file=sys.stderr)
    sys.exit(1)

def parse_fqdns(lines):
    zones = defaultdict(set)
    for line in lines:
        orig_line = line.strip()
        fqdn = orig_line.lstrip("*.")  # Remove leading '*.' for parsing
        if not fqdn:
            continue
        ext = tldextract.extract(fqdn)
        zone = f"{ext.domain}.{ext.suffix}"
        subdomain = ext.subdomain
        # Restore '*' if original line started with '*.'
        if orig_line.startswith("*."):
            subdomain = f"*.{subdomain}" if subdomain else "*"
        zones[zone].add(subdomain)  # subdomain may be '' or start with '*.'
    return zones

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    fqdn_file = sys.argv[1] if len(sys.argv) > 1 else "/tmp/fqdns"
    if not os.path.isfile(fqdn_file):
        print(f"Error: File not found -> {fqdn_file}\n", file=sys.stderr)
        print(__doc__)
        print("\nYou may provide a file as a parameter.")
        sys.exit(1)
    with open(fqdn_file, "r") as f:
        lines = f.readlines()
    zones = parse_fqdns(lines)

    for zone in sorted(zones):
        for sub in sorted(zones[zone]):
            print(f"{zone}:{sub}")
        print()  # blank line between domains

if __name__ == "__main__":
    main()
