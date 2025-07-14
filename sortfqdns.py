#!/usr/bin/env python3

import tldextract
import os
import sys

fqdn_file = "/tmp/fqdns"

# ✅ Check if file exists
if not os.path.isfile(fqdn_file):
    print(f"Error: File not found -> {fqdn_file}", file=sys.stderr)
    sys.exit(1)

# Use a set to avoid duplicates
output = set()

with open(fqdn_file, "r") as f:
    for line in f:
        fqdn = line.strip().lstrip("*.")  # Remove leading '*.'
        if not fqdn:
            continue
        ext = tldextract.extract(fqdn)
        zone = f"{ext.domain}.{ext.suffix}"
        subdomain = ext.subdomain
        output.add(f"{zone}:{subdomain}" if subdomain else f"{zone}:")

# ✅ Print sorted output
for entry in sorted(output):
    print(entry)
