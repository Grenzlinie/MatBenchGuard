#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.json ===
python3 /solution/write_formation.py > /app/outputs/formation_energies.json

# === solve block: migration_barriers.json ===
python3 /solution/write_migration.py > /app/outputs/migration_barriers.json
