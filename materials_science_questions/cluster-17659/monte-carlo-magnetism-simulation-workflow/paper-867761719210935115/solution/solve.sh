#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lifetime_data.json ===
#!/bin/bash
python3 /solution/write_lifetime.py /app/outputs/lifetime_data.json

# === solve block: switching_field_data.json ===
#!/bin/bash
python3 /solution/write_switching.py /app/outputs/switching_field_data.json
