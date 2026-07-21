#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'EOF'
{
  "diffusion": {
    "291": { "shell": 2.08, "bulk": 2.09, "pure": 2.31 },
    "296": { "shell": 2.21, "bulk": 2.25, "pure": 2.31 },
    "311": { "shell": 3.00, "bulk": 3.30, "pure": 3.50 },
    "321": { "shell": 3.84, "bulk": 4.34, "pure": 4.50 },
    "348": { "shell": 5.24, "bulk": 5.61, "pure": null }
  },
  "hb_correlation": {
    "291": { "shell_decay_rank": -1, "bulk_decay_rank": 1 },
    "296": { "shell_decay_rank": -1, "bulk_decay_rank": 1 },
    "311": { "shell_decay_rank": -1, "bulk_decay_rank": 1 },
    "321": { "shell_decay_rank": -1, "bulk_decay_rank": 1 },
    "348": { "shell_decay_rank": -1, "bulk_decay_rank": 1 }
  },
  "density_first_shell": {
    "291": { "higher_than_bulk": true },
    "296": { "higher_than_bulk": true },
    "311": { "higher_than_bulk": false },
    "321": { "higher_than_bulk": false },
    "348": { "higher_than_bulk": false }
  },
  "charge_oscillation": ["+", "-", "+"],
  "hb_counts": {
    "291": { "shell": 3.615, "bulk": 3.625 },
    "296": { "shell": 3.575, "bulk": 3.604 },
    "311": { "shell": 3.518, "bulk": 3.548 },
    "321": { "shell": 3.463, "bulk": 3.490 },
    "348": { "shell": 3.367, "bulk": 3.463 }
  },
  "coordination_numbers": {
    "291": { "OW": 17.9, "HW": 36.1 },
    "296": { "OW": 17.8, "HW": 35.9 },
    "311": { "OW": 17.4, "HW": 35.2 },
    "321": { "OW": 17.2, "HW": 34.8 },
    "348": { "OW": 17.0, "HW": 34.3 }
  },
  "rotational_relaxation": {
    "291": { "shell": 6.08, "bulk": 5.50 },
    "296": { "shell": 5.41, "bulk": 4.55 },
    "311": { "shell": 3.61, "bulk": 3.63 },
    "321": { "shell": 3.40, "bulk": 3.27 },
    "348": { "shell": 2.47, "bulk": 2.12 }
  }
}
EOF
