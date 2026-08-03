#!/bin/bash
set -euo pipefail
mkdir -p /logs/verifier
python /tests/checker.py /app/outputs > /logs/verifier/reward.txt
