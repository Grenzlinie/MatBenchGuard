#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dd_zfs_results.json ===
cat > "$OUTDIR/dd_zfs_results.json" <<'FFEOF'
{
  "Dq_1350": {
    "dd_transitions": [13164, 18015, 24849, 26752, 28700],
    "zfs_1e3_3a": 34.4
  },
  "Dq_1400": {
    "dd_transitions": [12677, 17575, 24849, 26735, 28700],
    "zfs_1e3_3a": 41.0
  },
  "Dq_1500": {
    "dd_transitions": [11702, 16683, 24849, 26705, 28700],
    "zfs_1e3_3a": 60.2
  }
}
FFEOF

# === solve block: signed_zfs_results.json ===
cat > "$OUTDIR/signed_zfs_results.json" <<'FFEOF'
{
  "set1": {
    "Dq_pos": {
      "param": {
        "B": 730,
        "C": 3150,
        "alpha": 90,
        "zeta": 300,
        "Dq": 1350
      },
      "zfs": 8.5
    },
    "Dq_neg": {
      "param": {
        "B": 730,
        "C": 3150,
        "alpha": 90,
        "zeta": 300,
        "Dq": -1350
      },
      "zfs": 6.37
    }
  },
  "set2": {
    "Dq_pos": {
      "param": {
        "B": 730,
        "C": 3150,
        "alpha": 90,
        "zeta": 420,
        "Dq": 1350
      },
      "zfs": 34.4
    },
    "Dq_neg": {
      "param": {
        "B": 730,
        "C": 3150,
        "alpha": 90,
        "zeta": 420,
        "Dq": -1350
      },
      "zfs": 18.3
    }
  },
  "set3": {
    "Dq_pos": {
      "param": {
        "B": 1100,
        "C": 4000,
        "alpha": 90,
        "zeta": 440,
        "Dq": 2150
      },
      "zfs": 56.6
    },
    "Dq_neg": {
      "param": {
        "B": 1100,
        "C": 4000,
        "alpha": 90,
        "zeta": 440,
        "Dq": -2150
      },
      "zfs": 39.3
    }
  },
  "set4": {
    "Dq_pos": {
      "param": {
        "B": 1100,
        "C": 4000,
        "alpha": 0,
        "zeta": 440,
        "Dq": 2150
      },
      "zfs": 79.7
    },
    "Dq_neg": {
      "param": {
        "B": 1100,
        "C": 4000,
        "alpha": 0,
        "zeta": 440,
        "Dq": -2150
      },
      "zfs": 53.6
    }
  }
}
FFEOF
